"""
Database of CS2 professional players.
Each player has the following attributes:
- name: Player's in-game name
- team: Current team
- nationality: Country of origin
- continent: Continent for region-based hints
- age: Player's age
- role: 'Rifler' or 'AWPer'
- hltv_top20_appearances: Number of HLTV Top 20 appearances
"""

PLAYERS = [
    # 根据最新数据修改的现有选手
    {
        "name": "s1mple",
        "team": "NAVI",
        "nationality": "Ukraine",
        "continent": "Europe",
        "age": 27,
        "role": "AWPer",
        "hltv_top20_appearances": 8
    },
    {
        "name": "ZywOo",
        "team": "Vitality",
        "nationality": "France",
        "continent": "Europe",
        "age": 24,
        "role": "AWPer",
        "hltv_top20_appearances": 6
    },
    {
        "name": "NiKo",
        "team": "Falcons",
        "nationality": "Bosnia and Herzegovina",
        "continent": "Europe",
        "age": 28,
        "role": "Rifler",
        "hltv_top20_appearances": 9
    },
    {
        "name": "device",
        "team": "Astralis",
        "nationality": "Denmark",
        "continent": "Europe",
        "age": 29,
        "role": "AWPer",
        "hltv_top20_appearances": 9
    },
    {
        "name": "sh1ro",
        "team": "Spirit",
        "nationality": "Russia",
        "continent": "Europe",
        "age": 23,
        "role": "AWPer",
        "hltv_top20_appearances": 4
    },
    {
        "name": "Ax1Le",
        "team": "BetBoom",
        "nationality": "Russia",
        "continent": "Europe",
        "age": 22,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "blameF",
        "team": "Fnatic",
        "nationality": "Denmark",
        "continent": "Europe",
        "age": 27,
        "role": "Rifler",
        "hltv_top20_appearances": 4
    },
    {
        "name": "electronic",
        "team": "Virtus.pro",
        "nationality": "Russia",
        "continent": "Europe",
        "age": 26,
        "role": "Rifler",
        "hltv_top20_appearances": 4
    },
    {
        "name": "m0NESY",
        "team": "G2 Esports",
        "nationality": "Russia",
        "continent": "Europe",
        "age": 19,
        "role": "AWPer",
        "hltv_top20_appearances": 3
    },
    {
        "name": "Jame",
        "team": "PARIVISION",
        "nationality": "Russia", 
        "continent": "Europe",
        "age": 26,
        "role": "AWPer",
        "hltv_top20_appearances": 2
    },
    {
        "name": "huNter-",
        "team": "G2 Esports",
        "nationality": "Bosnia and Herzegovina",
        "continent": "Europe",
        "age": 29,
        "role": "Rifler",
        "hltv_top20_appearances": 4
    },
    {
        "name": "ropz",
        "team": "Vitality",
        "nationality": "Estonia",
        "continent": "Europe",
        "age": 25,
        "role": "Rifler",
        "hltv_top20_appearances": 7
    },
    {
        "name": "Spinx",
        "team": "MOUZ",
        "nationality": "Israel",
        "continent": "Asia",
        "age": 24,
        "role": "Rifler",
        "hltv_top20_appearances": 3
    },
    {
        "name": "frozen",
        "team": "FaZe Clan",
        "nationality": "Slovakia",
        "continent": "Europe",
        "age": 22,
        "role": "Rifler",
        "hltv_top20_appearances": 3
    },
    {
        "name": "broky",
        "team": "FaZe Clan",
        "nationality": "Latvia",
        "continent": "Europe",
        "age": 24,
        "role": "AWPer",
        "hltv_top20_appearances": 4
    },
    {
        "name": "Magisk",
        "team": "Falcons",
        "nationality": "Denmark",
        "continent": "Europe",
        "age": 27,
        "role": "Rifler",
        "hltv_top20_appearances": 5
    },
    {
        "name": "stavn",
        "team": "Astralis",
        "nationality": "Denmark",
        "continent": "Europe",
        "age": 23,
        "role": "Rifler",
        "hltv_top20_appearances": 4
    },
    {
        "name": "YEKINDAR",
        "team": "Team Liquid",
        "nationality": "Latvia",
        "continent": "Europe",
        "age": 25,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "Twistzz",
        "team": "Team Liquid",
        "nationality": "Canada",
        "continent": "North America",
        "age": 25,
        "role": "Rifler",
        "hltv_top20_appearances": 5
    },
    {
        "name": "cadiaN",
        "team": "Astralis",
        "nationality": "Denmark",
        "continent": "Europe",
        "age": 29,
        "role": "AWPer",
        "hltv_top20_appearances": 1
    },
    {
        "name": "rain",
        "team": "FaZe Clan",
        "nationality": "Norway",
        "continent": "Europe",
        "age": 30,
        "role": "Rifler",
        "hltv_top20_appearances": 3
    },
    {
        "name": "KSCERATO",
        "team": "FURIA",
        "nationality": "Brazil",
        "continent": "South America",
        "age": 25,
        "role": "Rifler",
        "hltv_top20_appearances": 4
    },
    {
        "name": "Brollan",
        "team": "MOUZ",
        "nationality": "Sweden",
        "continent": "Europe",
        "age": 22,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "kennyS",
        "team": "retired",
        "nationality": "France",
        "continent": "Europe",
        "age": 29,
        "role": "AWPer",
        "hltv_top20_appearances": 5
    },
    {
        "name": "coldzera",
        "team": "RED Canids",
        "nationality": "Brazil",
        "continent": "South America",
        "age": 30,
        "role": "Rifler",
        "hltv_top20_appearances": 3
    },
    {
        "name": "dupreeh",
        "team": "Falcons",
        "nationality": "Denmark",
        "continent": "Europe",
        "age": 32,
        "role": "Rifler",
        "hltv_top20_appearances": 7
    },
    {
        "name": "FalleN",
        "team": "FURIA",
        "nationality": "Brazil",
        "continent": "South America",
        "age": 33,
        "role": "AWPer",
        "hltv_top20_appearances": 2
    },
    {
        "name": "gla1ve",
        "team": "ENCE",
        "nationality": "Denmark",
        "continent": "Europe",
        "age": 29,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "NAF",
        "team": "Team Liquid",
        "nationality": "Canada",
        "continent": "North America",
        "age": 27,
        "role": "Rifler",
        "hltv_top20_appearances": 3
    },
    
    # 添加缺失的知名选手
    {
        "name": "EliGE",
        "team": "FaZe Clan",
        "nationality": "United States",
        "continent": "North America",
        "age": 27,
        "role": "Rifler",
        "hltv_top20_appearances": 6
    },
    {
        "name": "GuardiaN",
        "team": "Retired",
        "nationality": "Slovakia",
        "continent": "Europe",
        "age": 33,
        "role": "AWPer",
        "hltv_top20_appearances": 6
    },
    {
        "name": "GeT_RiGhT",
        "team": "No Team",
        "nationality": "Sweden",
        "continent": "Europe",
        "age": 34,
        "role": "Rifler",
        "hltv_top20_appearances": 4
    },
    {
        "name": "f0rest",
        "team": "Retired",
        "nationality": "Sweden",
        "continent": "Europe",
        "age": 36,
        "role": "Rifler",
        "hltv_top20_appearances": 4
    },
    {
        "name": "shox",
        "team": "No Team",
        "nationality": "France",
        "continent": "Europe",
        "age": 32,
        "role": "Rifler",
        "hltv_top20_appearances": 4
    },
    {
        "name": "flusha",
        "team": "Retired",
        "nationality": "Sweden",
        "continent": "Europe",
        "age": 31,
        "role": "Rifler",
        "hltv_top20_appearances": 4
    },
    {
        "name": "Xyp9x",
        "team": "No Team",
        "nationality": "Denmark",
        "continent": "Europe",
        "age": 29,
        "role": "Rifler",
        "hltv_top20_appearances": 4
    },
    {
        "name": "Snax",
        "team": "G2 Esports",
        "nationality": "Poland",
        "continent": "Europe",
        "age": 31,
        "role": "Rifler",
        "hltv_top20_appearances": 4
    },
    {
        "name": "olofmeister",
        "team": "Faze Clan",
        "nationality": "Sweden",
        "continent": "Europe",
        "age": 33,
        "role": "Rifler",
        "hltv_top20_appearances": 4
    },
    {
        "name": "KRIMZ",
        "team": "Fnatic",
        "nationality": "Sweden",
        "continent": "Europe",
        "age": 30,
        "role": "Rifler",
        "hltv_top20_appearances": 5
    },
    {
        "name": "b1t",
        "team": "NAVI",
        "nationality": "Ukraine",
        "continent": "Europe",
        "age": 22,
        "role": "Rifler",
        "hltv_top20_appearances": 3
    },
    {
        "name": "HObbit",
        "team": "1win",
        "nationality": "Kazakhstan",
        "continent": "Asia",
        "age": 30,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "apEX",
        "team": "Vitality",
        "nationality": "France",
        "continent": "Europe",
        "age": 32,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "flamie",
        "team": "Retired",
        "nationality": "Russia",
        "continent": "Europe",
        "age": 27,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "fer",
        "team": "No Team",
        "nationality": "Brazil",
        "continent": "South America",
        "age": 33,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "flameZ",
        "team": "Vitality",
        "nationality": "Israel",
        "continent": "Asia",
        "age": 21,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "oskar",
        "team": "Inner Circle",
        "nationality": "Czech Republic",
        "continent": "Europe",
        "age": 33,
        "role": "AWPer",
        "hltv_top20_appearances": 2
    },
    {
        "name": "Kjaerbye",
        "team": "JiJieHao",
        "nationality": "Denmark",
        "continent": "Europe",
        "age": 26,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "yuurih",
        "team": "FURIA",
        "nationality": "Brazil",
        "continent": "South America", 
        "age": 25,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "w0nderful",
        "team": "NAVI",
        "nationality": "Ukraine",
        "continent": "Europe",
        "age": 20,
        "role": "AWPer",
        "hltv_top20_appearances": 1
    },
    {
        "name": "donk",
        "team": "Spirit",
        "nationality": "Russia",
        "continent": "Europe",
        "age": 18,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "jL",
        "team": "NAVI",
        "nationality": "Lithuania",
        "continent": "Europe",
        "age": 25,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "xertioN",
        "team": "MOUZ",
        "nationality": "Israel",
        "continent": "Asia",
        "age": 20,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "pashaBiceps",
        "team": "No Team",
        "nationality": "Poland",
        "continent": "Europe",
        "age": 36,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "Dosia",
        "team": "Retired",
        "nationality": "Russia",
        "continent": "Europe",
        "age": 36,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "ScreaM",
        "team": "Retired",
        "nationality": "Belgium",
        "continent": "Europe",
        "age": 30,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "NBK-",
        "team": "Mercenaires",
        "nationality": "France",
        "continent": "Europe",
        "age": 30,
        "role": "Rifler",
        "hltv_top20_appearances": 3
    },
    {
        "name": "JW",
        "team": "EYEBALLERS",
        "nationality": "Sweden",
        "continent": "Europe",
        "age": 30,
        "role": "AWPer",
        "hltv_top20_appearances": 3
    },
    # 添加遗漏的选手
    {
        "name": "friberg",
        "team": "No Team",
        "nationality": "Sweden",
        "continent": "Europe",
        "age": 33,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "Happy",
        "team": "No Team",
        "nationality": "France",
        "continent": "Europe",
        "age": 33,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "Brehze",
        "team": "No Team",
        "nationality": "United States",
        "continent": "North America",
        "age": 26,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "jks",
        "team": "Team Liquid",
        "nationality": "Australia",
        "continent": "Oceania",
        "age": 29,
        "role": "Rifler",
        "hltv_top20_appearances": 2
    },
    {
        "name": "Xizt",
        "team": "NIP",
        "nationality": "Sweden",
        "continent": "Europe",
        "age": 34,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "Hiko",
        "team": "Retired",
        "nationality": "United States",
        "continent": "North America",
        "age": 35,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "Nico",
        "team": "No Team",
        "nationality": "Denmark",
        "continent": "Europe",
        "age": 33,
        "role": "AWPer",
        "hltv_top20_appearances": 1
    },
    {
        "name": "markeloff",
        "team": "No Team",
        "nationality": "Ukraine",
        "continent": "Europe",
        "age": 37,
        "role": "AWPer",
        "hltv_top20_appearances": 1
    },
    {
        "name": "Edward",
        "team": "Retired",
        "nationality": "Ukraine",
        "continent": "Europe",
        "age": 37,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "SmithZz",
        "team": "Retired",
        "nationality": "France",
        "continent": "Europe",
        "age": 36,
        "role": "AWPer",
        "hltv_top20_appearances": 1
    },
    {
        "name": "byali",
        "team": "No Team",
        "nationality": "Poland",
        "continent": "Europe",
        "age": 30,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "swag",
        "team": "Retired",
        "nationality": "United States",
        "continent": "North America",
        "age": 28,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "kioShiMa",
        "team": "No Team",
        "nationality": "France",
        "continent": "Europe",
        "age": 30,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "cajunb",
        "team": "No Team",
        "nationality": "Denmark",
        "continent": "Europe",
        "age": 35,
        "role": "AWPer",
        "hltv_top20_appearances": 1
    },
    {
        "name": "NEO",
        "team": "Faze Clan",
        "nationality": "Poland",
        "continent": "Europe",
        "age": 37,
        "role": "Coach",
        "hltv_top20_appearances": 1
    },
    {
        "name": "allu",
        "team": "JANO",
        "nationality": "Finland",
        "continent": "Europe",
        "age": 32,
        "role": "AWPer",
        "hltv_top20_appearances": 1
    },
    {
        "name": "Skadoodle",
        "team": "Retired",
        "nationality": "United States",
        "continent": "North America",
        "age": 31,
        "role": "AWPer",
        "hltv_top20_appearances": 1
    },
    {
        "name": "fnx",
        "team": "No Team",
        "nationality": "Brazil",
        "continent": "South America",
        "age": 35,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "dennis",
        "team": "No Team",
        "nationality": "Sweden",
        "continent": "Europe",
        "age": 34,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "k0nfig",
        "team": "No Team",
        "nationality": "Denmark",
        "continent": "Europe",
        "age": 27,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "AdreN",
        "team": "Novaq",
        "nationality": "Kazakhstan",
        "continent": "Asia",
        "age": 35,
        "role": "Coach",
        "hltv_top20_appearances": 1
    },
    {
        "name": "boltz",
        "team": "No Team",
        "nationality": "Brazil",
        "continent": "South America",
        "age": 27,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "suNny",
        "team": "Ambush",
        "nationality": "Finland",
        "continent": "Europe",
        "age": 30,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "autimatic",
        "team": "No Team",
        "nationality": "United States",
        "continent": "North America",
        "age": 28,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "valde",
        "team": "Tricked",
        "nationality": "Denmark",
        "continent": "Europe",
        "age": 29,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "woxic",
        "team": "Eternal Fire",
        "nationality": "Turkey",
        "continent": "Europe",
        "age": 26,
        "role": "AWPer",
        "hltv_top20_appearances": 1
    },
    {
        "name": "sergej",
        "team": "No Team",
        "nationality": "Finland",
        "continent": "Europe",
        "age": 23,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "CeRq",
        "team": "500",
        "nationality": "Bulgaria",
        "continent": "Europe",
        "age": 25,
        "role": "AWPer",
        "hltv_top20_appearances": 1
    },
    {
        "name": "Ethan",
        "team": "Retired",
        "nationality": "United States",
        "continent": "North America",
        "age": 25,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "syrsoN",
        "team": "No Team",
        "nationality": "Germany",
        "continent": "Europe",
        "age": 28,
        "role": "AWPer",
        "hltv_top20_appearances": 1
    },
    {
        "name": "HEN1",
        "team": "RED Canids",
        "nationality": "Brazil",
        "continent": "South America",
        "age": 29,
        "role": "AWPer",
        "hltv_top20_appearances": 1
    },
    {
        "name": "SunPayus",
        "team": "HEROIC",
        "nationality": "Spain",
        "continent": "Europe",
        "age": 26,
        "role": "AWPer",
        "hltv_top20_appearances": 1
    },
    {
        "name": "NertZ",
        "team": "Team Liquid",
        "nationality": "Israel",
        "continent": "Asia",
        "age": 25,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "jabbi",
        "team": "Astralis",
        "nationality": "Denmark",
        "continent": "Europe",
        "age": 21,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "malbsMd",
        "team": "G2 Esports",
        "nationality": "Bosnia and Herzegovina",
        "continent": "Europe",
        "age": 22,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "XANTARES",
        "team": "Eternal Fire",
        "nationality": "Turkey",
        "continent": "Europe",
        "age": 29,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "iM",
        "team": "NAVI",
        "nationality": "Romania",
        "continent": "Europe",
        "age": 25,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "Jimpphat",
        "team": "MOUZ",
        "nationality": "Finland",
        "continent": "Europe",
        "age": 18,
        "role": "Rifler",
        "hltv_top20_appearances": 1
    },
    {
        "name": "torzsi",
        "team": "MOUZ",
        "nationality": "Hungary",
        "continent": "Europe",
        "age": 22,
        "role": "AWPer",
        "hltv_top20_appearances": 1
    }
]

def get_all_players():
    """Returns all players from the database."""
    return PLAYERS

def get_player_by_name(name):
    """Returns a player by their in-game name (case insensitive)."""
    name_lower = name.lower()
    for player in PLAYERS:
        if player["name"].lower() == name_lower:
            return player
    return None

def add_player(player_data):
    """Add a new player to the database."""
    PLAYERS.append(player_data)
    return True

def get_random_player():
    """Returns a random player from the database."""
    import random
    return random.choice(PLAYERS) 