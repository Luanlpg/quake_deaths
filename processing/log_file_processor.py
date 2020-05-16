import re
from pprint import pprint

TYPES_OF_DEATH = ['MOD_UNKNOWN', 'MOD_SHOTGUN', 'MOD_GAUNTLET', 'MOD_MACHINEGUN',
        'MOD_GRENADE', 'MOD_GRENADE_SPLASH', 'MOD_ROCKET', 'MOD_ROCKET_SPLASH',
        'MOD_PLASMA', 'MOD_PLASMA_SPLASH', 'MOD_RAILGUN', 'MOD_LIGHTNING',
        'MOD_BFG', 'MOD_BFG_SPLASH', 'MOD_WATER', 'MOD_SLIME', 'MOD_LAVA',
        'MOD_CRUSH', 'MOD_TELEFRAG', 'MOD_FALLING', 'MOD_SUICIDE',
        'MOD_TARGET_LASER', 'MOD_TRIGGER_HURT', 'MOD_NAIL', 'MOD_CHAINGUN',
        'MOD_PROXIMITY_MINE', 'MOD_KAMIKAZE', 'MOD_JUICED', 'MOD_GRAPPLE'
]

class LogFileProcessor:
    def __init__(self):
        self.file_name = 'games.log'
        self.game = 0
        self.player_keys = {}
        self.response = {}

    def start(self):
        log = open(self.file_name,"r")
        for line in log:
            if 'InitGame' in line:
                self.create_game()
            if 'ClientUserinfoChanged' in line:
                self.register_player(line)
            if 'Kill' in line:
                self.register_kill(line)
        log.close()
        return self.response

    def create_game(self):
        self.game += 1
        self.response[f'game_{self.game}'] = {
            'total_kills': 0,
            'players': [],
            'kills': {},
            'kills_by_means': {},
            'world_kills': 0
        }

    def register_player(self, line):
        id = int(re.findall("( [0-9] )", line)[0].strip())
        name = line.split("\\")[1]
        self.player_keys[id] = name
        self.response[f'game_{self.game}']['players'].append(name)
        self.response[f'game_{self.game}']['players'] = sorted(set(self.response[f'game_{self.game}']['players']))

    def register_kill(self, line):
        kill = re.findall("([0-9][0-9]* [0-9]* [0-9][0-9]*)", line)[0].strip().split(' ')
        murderer = self.player_keys[int(kill[0])] if kill[0] != '1022' else '<world>'
        dead = self.player_keys[int(kill[1])]
        death = TYPES_OF_DEATH[int(kill[2])]

        self.response[f'game_{self.game}']['total_kills'] += 1

        if murderer =='<world>':
            self.response[f'game_{self.game}']['world_kills'] += 1
            if dead not in self.response[f'game_{self.game}']['kills']:
                self.response[f'game_{self.game}']['kills'][dead] = -1
            else:
                self.response[f'game_{self.game}']['kills'][dead] -= 1

        elif murderer not in self.response[f'game_{self.game}']['kills']:
            self.response[f'game_{self.game}']['kills'][murderer] = 1
        else:
            self.response[f'game_{self.game}']['kills'][murderer] += 1

        if death not in self.response[f'game_{self.game}']['kills_by_means']:
            self.response[f'game_{self.game}']['kills_by_means'][death] = 1
        else:
            self.response[f'game_{self.game}']['kills_by_means'][death] += 1
