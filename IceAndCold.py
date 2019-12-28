import sys
import math
import numpy as np
import random

# MAP SIZE
WIDTH = 12
HEIGHT = 12

# OWNER
ME = 0
OPPONENT = 1

# BUILDING TYPE
HQ = 0


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x, self.y}'


class Unit:
    def __init__(self, owner, id, level, x, y):
        self.owner = owner
        self.id = id
        self.level = level
        self.pos = Position(x, y)

    def __str__(self):
        return f'Owner : {self.owner}, Id: {self.id}, level: {self.level}, pos: {self.pos}'


class Building:
    def __init__(self, owner, type, x, y):
        self.owner = owner
        self.type = type
        self.pos = Position(x, y)


class Game:
    def __init__(self):
        self.buildings = []
        self.units = []
        self.actions = []
        self.gold = 0
        self.income = 0
        self.opponent_gold = 0
        self.opponent_income = 0
        self.map = np.chararray([12, 12], itemsize=3)
        self.map[:] = '#'
        self.dir = ''

    def get_my_HQ(self):
        for b in self.buildings:
            if b.type == HQ and b.owner == ME:
                return b

    def get_opponent_HQ(self):
        for b in self.buildings:
            if b.type == HQ and b.owner == OPPONENT:
                return b

    def move_units(self):
        center = Position(11, 11)

        for unit in self.units:
            if unit.owner == ME:
                best_pos = self.best_position(unit)
                self.actions.append(
                    f'MOVE {unit.id} {best_pos.x} {best_pos.y}')

    def best_position(self, unit):
        # revisamos que sea mi unidad
        if unit.owner == ME:
            x = unit.pos.x
            y = unit.pos.y
            bp = [
                {'dir': 'down',
                 'pos': Position(x, y+1),
                 'value': self.map[y+1, x].decode('utf-8') if (y+1) < 12 else False,
                 'pond': 0
                 },
                {'dir': 'right',
                 'pos': Position(x+1, y),
                 'value': self.map[y, x+1].decode('utf-8') if (x+1) < 12 else False,
                 'pond': 0
                 },
                {'dir': 'up',
                 'pos': Position(x, y-1),
                 'value': self.map[y-1, x].decode('utf-8') if (y-1) >= 0 else False,
                 'pond': 0
                 },
                {'dir': 'left',
                 'pos': Position(x-1, y),
                 'value': self.map[y, x-1].decode('utf-8') if (x-1) >= 0 else False,
                 'pond': 0
                 }
            ]
            switchPond = {
                'E': 6,
                'X': 5,
                '.': 4,
                'x': 3,
                'o': 1,
                'O': 2,
                'P':0,
                '#': -1,
                False: -3
            }
            for alt in bp:
                alt['pond'] = switchPond.get(alt['value'], 0)
            best = max(bp, key=lambda x: x['pond'])
            # if(best['pond']== 0 or best['pond']== 1 ):
            #     for alt in sorted(bp, key=lambda x: x['pond'], reverse=True):
            #         if(alt['dir'] == 'down'  and self.dir == 'DOWN'):
            #             return alt['pos']
            #         if(alt['dir'] == 'up'  and self.dir == 'UP'):
            #             return alt['pos'] 
            # if(alt['pond'] < 3):
            #     hq = self.get_my_HQ()
            #     if hq.pos.x == 0:
            #         return Position(11, 11)
            #     return Position(0, 0)
            print(best, best['pos'], file=sys.stderr)
            self.map[best['pos'].y,best['pos'].x] = 'O'
            return best['pos']

    def get_train_position(self):
        hq = self.get_my_HQ()
        print(f'Esta es el hq: {hq.pos}, la long uni {len(self.units)} ', file=sys.stderr)
        if(len(self.units) != 0):
            if(len(self.units)== 1 and self.units[0].owner == OPPONENT):
                return Position(11, 10)
            best_pos = self.best_position(self.units[0])
            return best_pos
        if hq.pos.x == 0:
            return Position(0, 1)
        return Position(11, 10)

    def train_units(self):
        if self.gold > 20:
            train_pos = self.get_train_position()
            print(f'Esta es el train_pos: {train_pos}', file=sys.stderr)
            self.actions.append(f'TRAIN 1 {train_pos.x} {train_pos.y}')
            # if(len(self.units)<3):
            #     train_pos = self.get_train_position()
            #     self.actions.append(f'TRAIN 1 {train_pos.x} {train_pos.y}')
            # else:
            #     num = math.floor(random.random() * len(self.units))
            #     cant = 0
            #     while(True):
            #         cant = cant+1
            #         if(cant > 10 or len(self.units)< num): return
            #         if(self.units[num].level < 3 and self.units[num].owner == ME):
            #             self.actions.append(f'TRAIN {self.units[num].level+1} {self.units[num].pos.x} {self.units[num].pos.y}')
            #             return
            #         else:
            #             num = math.floor(random.random() * len(self.units))
            
            


        

    def init(self):
        # Unused in Wood 3
        number_mine_spots = int(input())
        for i in range(number_mine_spots):
            x, y = [int(j) for j in input().split()]

    def update(self):
        self.units.clear()
        self.buildings.clear()
        self.actions.clear()

        self.gold = int(input())
        self.income = int(input())
        self.opponent_gold = int(input())
        self.opponent_income = int(input())

        for idx, _ in enumerate(range(12)):
            line = input()
            self.map[idx:] = [char for char in line]

        #print(self.map, file=sys.stderr)
        if(self.map[0,0].decode('utf-8') == 'X'):
            self.dir = 'UP'
        else:
            self.dir = 'DOWN'


        building_count = int(input())
        for i in range(building_count):
            owner, building_type, x, y = [int(j) for j in input().split()]
            self.buildings.append(Building(owner, building_type, x, y))

        unit_count = int(input())
        for i in range(unit_count):
            owner, unit_id, level, x, y = [int(j) for j in input().split()]
            self.units.append(Unit(owner, unit_id, level, x, y))
            if(owner == ME):
                self.map[y,x] = 'P'
            if(owner == OPPONENT):
                self.map[y,x] = 'E'
        print([str(unit) for unit in self.units], file=sys.stderr)
        print(self.map, file=sys.stderr)

    def build_output(self):
        # TODO "core" of the AI
        self.train_units()
        self.move_units()

    def output(self):
        if self.actions:
            print(';'.join(self.actions))
        else:
            print('WAIT')


g = Game()

g.init()
while True:
    g.update()
    g.build_output()
    g.output()
