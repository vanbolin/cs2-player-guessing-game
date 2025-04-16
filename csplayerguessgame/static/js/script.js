// CS2 Player Guess Game - Frontend Script

document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const playerSearchInput = document.getElementById('player-search');
    const submitGuessBtn = document.getElementById('submit-guess');
    const guessesContainer = document.getElementById('guesses-container');
    const gameStatusDiv = document.getElementById('game-status');
    const newGameBtn = document.getElementById('new-game');
    const modalNewGameBtn = document.getElementById('modal-new-game');
    const autocompleteContainer = document.getElementById('autocomplete-container');
    const resultModal = new bootstrap.Modal(document.getElementById('resultModal'));
    const resultContent = document.getElementById('result-content');
    
    // Game state
    let playerNames = [];
    let gameState = {};
    let selectedPlayer = '';
    
    // 跟踪当前选中的建议项
    let currentFocus = -1;
    
    // Initialize the game
    initGame();
    
    // Event Listeners
    playerSearchInput.addEventListener('input', handleInputChange);
    playerSearchInput.addEventListener('keydown', handleKeyDown);
    submitGuessBtn.addEventListener('click', submitGuess);
    newGameBtn.addEventListener('click', startNewGame);
    modalNewGameBtn.addEventListener('click', function() {
        resultModal.hide();
        startNewGame();
    });
    
    // Initialize Game
    function initGame() {
        // Fetch player names for autocomplete
        fetch('/api/players')
            .then(response => response.json())
            .then(data => {
                playerNames = data;
            })
            .catch(error => console.error('Error fetching player names:', error));
        
        // Get current game state
        fetchGameState();
    }
    
    // Fetch game state from server
    function fetchGameState() {
        fetch('/api/game_state')
            .then(response => response.json())
            .then(data => {
                gameState = data;
                renderGameState();
            })
            .catch(error => console.error('Error fetching game state:', error));
    }
    
    // Handle input change for autocomplete
    function handleInputChange() {
        const inputVal = playerSearchInput.value.trim();
        
        // 清除现有的自动完成项
        autocompleteContainer.innerHTML = '';
        autocompleteContainer.style.display = 'none';
        currentFocus = -1; // 重置选中索引
        
        if (!inputVal) {
            selectedPlayer = ''; // 只有输入为空时才清空selectedPlayer
            return;
        }
        
        // 过滤匹配的选手
        const matches = playerNames.filter(name => 
            name.toLowerCase().includes(inputVal.toLowerCase())
        );
        
        if (matches.length > 0) {
            autocompleteContainer.style.display = 'block';
            
            // 为每个匹配的选手创建一个div
            matches.forEach((match, index) => {
                const div = document.createElement('div');
                div.textContent = match;
                div.className = 'autocomplete-item';
                div.addEventListener('click', function() {
                    playerSearchInput.value = match;
                    selectedPlayer = match;
                    autocompleteContainer.style.display = 'none';
                    currentFocus = -1;
                });
                autocompleteContainer.appendChild(div);
            });
        }
    }

    // 添加键盘事件监听器
    function handleKeyDown(e) {
        const items = autocompleteContainer.getElementsByClassName('autocomplete-item');
        
        if (e.key === 'Enter') {
            e.preventDefault();
            
            // 如果有选中的建议项，使用它
            if (currentFocus > -1 && items.length > 0) {
                playerSearchInput.value = items[currentFocus].textContent;
            }
            
            // 总是提交输入框的当前值
            submitGuess();
            return;
        }
        
        // 只有在有建议项时才处理上下键
        if (items.length > 0) {
            switch (e.key) {
                case 'ArrowDown':
                    e.preventDefault();
                    currentFocus++;
                    if (currentFocus >= items.length) currentFocus = 0;
                    setActiveItem(items);
                    break;
                    
                case 'ArrowUp':
                    e.preventDefault();
                    currentFocus--;
                    if (currentFocus < 0) currentFocus = items.length - 1;
                    setActiveItem(items);
                    break;
                    
                case 'Escape':
                    e.preventDefault();
                    autocompleteContainer.style.display = 'none';
                    currentFocus = -1;
                    break;
            }
        }
    }

    // 设置活动项的样式
    function setActiveItem(items) {
        // 移除所有项的活动样式
        for (let i = 0; i < items.length; i++) {
            items[i].classList.remove('active');
        }
        
        // 为当前焦点项添加活动样式
        if (currentFocus > -1) {
            items[currentFocus].classList.add('active');
            // 确保选中项在视图中可见
            items[currentFocus].scrollIntoView({block: 'nearest'});
        }
    }
    
    // Submit a guess
    function submitGuess() {
        // 总是使用输入框的当前值，而不是selectedPlayer
        const playerName = playerSearchInput.value.trim();
        
        // 检查输入框是否为空
        if (!playerName) {
            showStatus('Please enter a player name', 'danger');
            return;
        }
        
        // Don't allow further guesses if game is over
        if (gameState.game_over) {
            showStatus('Game is over. Please start a new game.', 'warning');
            return;
        }
        
        // Send guess to server
        fetch('/api/make_guess', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ player_name: playerName }),
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(data => {
                    throw new Error(data.error || 'Failed to submit guess');
                });
            }
            return response.json();
        })
        .then(data => {
            gameState = data;
            renderGameState();
            playerSearchInput.value = ''; // 清空输入框
            selectedPlayer = '';  // 清空selectedPlayer
            autocompleteContainer.style.display = 'none';
            currentFocus = -1; // 重置焦点索引
            
            // Check if game is over
            if (gameState.game_over) {
                showGameResults();
            }
        })
        .catch(error => {
            showStatus(error.message, 'danger');
        });
    }

    
    // Start a new game
    function startNewGame() {
        fetch('/api/new_game', {
            method: 'POST',
        })
        .then(response => response.json())
        .then(() => {
            // Clear the UI
            guessesContainer.innerHTML = '';
            gameStatusDiv.innerHTML = '';
            playerSearchInput.value = '';
            selectedPlayer = '';
            
            // Fetch the new game state
            fetchGameState();
        })
        .catch(error => console.error('Error starting new game:', error));
    }
    
    // Render the current game state
    function renderGameState() {
        // Clear current guesses
        guessesContainer.innerHTML = '';
        
        // Add each guess to the table
        gameState.guesses.forEach(guess => {
            const row = document.createElement('tr');
            
            // Player Name
            const nameCell = document.createElement('td');
            nameCell.textContent = guess.name;
            nameCell.classList.add('player-name');
            nameCell.style.backgroundColor = '#0f3460'; // 确保名字栏有一个明确的背景色
            nameCell.style.color = '#ffffff'; // 确保名字是白色的
            row.appendChild(nameCell);
            
            // Team
            const teamCell = document.createElement('td');
            teamCell.textContent = guess.team.value;
            if (guess.team.correct) {
                teamCell.classList.add('correct');
            } else {
                teamCell.classList.add('incorrect');
            }
            row.appendChild(teamCell);
            
            // Nationality with flag
            const nationalityCell = document.createElement('td');
            
            // Fetch flag code for the country
            fetch(`/api/flag/${encodeURIComponent(guess.nationality.value)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.flag_code) {
                        const flagImg = document.createElement('img');
                        flagImg.src = `https://flagcdn.com/16x12/${data.flag_code}.png`;
                        flagImg.classList.add('flag-icon');
                        flagImg.alt = guess.nationality.value;
                        nationalityCell.prepend(flagImg);
                    }
                });
            
            nationalityCell.appendChild(document.createTextNode(guess.nationality.value));
            
            if (guess.nationality.correct) {
                nationalityCell.classList.add('correct');
            } else if (guess.nationality.partial) {
                nationalityCell.classList.add('partial');
            } else {
                nationalityCell.classList.add('incorrect');
            }
            row.appendChild(nationalityCell);
            
            // Age
            const ageCell = document.createElement('td');
            ageCell.textContent = guess.age.value;
            if (guess.age.correct) {
                ageCell.classList.add('correct');
            } else {
                ageCell.classList.add('incorrect');
                if (guess.age.direction === 'up') {
                    ageCell.classList.add('direction-up');
                } else if (guess.age.direction === 'down') {
                    ageCell.classList.add('direction-down');
                }
            }
            row.appendChild(ageCell);
            
            // Role
            const roleCell = document.createElement('td');
            roleCell.textContent = guess.role.value;
            if (guess.role.correct) {
                roleCell.classList.add('correct');
            } else {
                roleCell.classList.add('incorrect');
            }
            row.appendChild(roleCell);
            
            // HLTV Top20 Appearances
            const hltvCell = document.createElement('td');
            hltvCell.textContent = guess.hltv_top20_appearances.value;
            if (guess.hltv_top20_appearances.correct) {
                hltvCell.classList.add('correct');
            } else {
                hltvCell.classList.add('incorrect');
                if (guess.hltv_top20_appearances.direction === 'up') {
                    hltvCell.classList.add('direction-up');
                } else if (guess.hltv_top20_appearances.direction === 'down') {
                    hltvCell.classList.add('direction-down');
                }
            }
            row.appendChild(hltvCell);
            
            guessesContainer.appendChild(row);
        });
        
        // Update game status
        if (gameState.game_over) {
            if (gameState.won) {
                showStatus(`Congratulations! You guessed the player in ${gameState.guesses.length} tries!`, 'success');
            } else {
                showStatus('Game over! You ran out of guesses.', 'danger');
            }
        } else {
            showStatus(`Guesses left: ${gameState.guesses_left}`, 'info');
        }
    }
    
    // Show status message
    function showStatus(message, type) {
        gameStatusDiv.innerHTML = `<div class="alert alert-${type}">${message}</div>`;
    }
    
    // Show game results in modal
    function showGameResults() {
        const targetPlayer = gameState.target_player;
        
        if (!targetPlayer) return;
        
        let content = `<div class="player-profile">`;
        
        // Fetch flag code for the country
        fetch(`/api/flag/${encodeURIComponent(targetPlayer.nationality)}`)
            .then(response => response.json())
            .then(data => {
                if (data.flag_code) {
                    const flagHtml = `<img src="https://flagcdn.com/64x48/${data.flag_code}.png" alt="${targetPlayer.nationality}" class="mb-2"><br>`;
                    
                    // Continue building the content
                    content += `
                        <h2>${targetPlayer.name}</h2>
                        ${flagHtml}
                        <p><strong>Team:</strong> ${targetPlayer.team}</p>
                        <p><strong>Nationality:</strong> ${targetPlayer.nationality}</p>
                        <p><strong>Age:</strong> ${targetPlayer.age}</p>
                        <p><strong>Role:</strong> ${targetPlayer.role}</p>
                        <p><strong>HLTV Top20 Appearances:</strong> ${targetPlayer.hltv_top20_appearances}</p>
                    </div>`;
                    
                    if (gameState.won) {
                        content += `<div class="alert alert-success text-center">
                            You guessed correctly in ${gameState.guesses.length} tries!
                        </div>`;
                    } else {
                        content += `<div class="alert alert-danger text-center">
                            You ran out of guesses! The player was ${targetPlayer.name}.
                        </div>`;
                    }
                    
                    resultContent.innerHTML = content;
                    resultModal.show();
                }
            });
    }
    
    // 添加CSS样式
    const style = document.createElement('style');
    style.textContent = `
        .autocomplete-item {
            padding: 8px 12px;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        
        .autocomplete-item:hover,
        .autocomplete-item.active {
            background-color: #38598b;
            color: white;
        }
    `;
    document.head.appendChild(style);
}); 