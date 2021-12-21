#https://adventofcode.com/2021/day/21
from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}day21.txt")
data = gd.separarPorLineas(data)


class Dice():
    value = 1
    times_rolled = 0
    def roll(self):
        res = self.value
        if self.value == 100:
            self.value = 1
        else:
            self.value += 1
        self.times_rolled += 1
        return res
    
    def __str__(self) -> str:
        return f'{self.value}, {self.times_rolled}'

    def __repr__(self) -> str:
        return f'{self.value}, {self.times_rolled}'

class Player():
    name = ''
    pos = 0
    score = 0
    has_won = False

    def __init__(self, name, initial_pos) -> None:
        self.name = name
        self.pos = initial_pos

    
    def move(self, positions):
        self.pos += positions
        if self.pos > 10:
            self.pos = self.pos%10
            if self.pos == 0:
                self.pos = 10
        self.score += self.pos
        if self.score >= 1000:
            self.has_won = True

    def __str__(self) -> str:
        return f'{self.name}: pos:{self.pos}, score:{self.score}'

    def __repr__(self) -> str:
        return f'{self.name}: pos:{self.pos}, score:{self.score}'

def problem1(p1_pos, p2_pos):
    p1 = Player('p1',p1_pos)
    p2 = Player('p2',p2_pos)
    dice = Dice()
    places = 0
    turn = p1
    while not p1.has_won and not p2.has_won:
        if dice.times_rolled == 122:
            print()
        places += dice.roll()
        if dice.times_rolled % 3 == 0:
            turn.move(places)
            if turn == p1:
                turn = p2
            else:
                turn = p1
            places = 0
    
    res = 0
    if p1.has_won:
        res = p2.score * dice.times_rolled
    else:
        res = p1.score * dice.times_rolled
    return res

player1 = int(data[0][-1])
player2 = int(data[1][-1])
print(problem1(player1, player2))