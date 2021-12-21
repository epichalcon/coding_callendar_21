#https://adventofcode.com/2021/day/21
from typing import overload
from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
from random import randint
import functools
data = gd.getdata(f"{DIRECTORY}day21.txt")
data = gd.separarPorLineas(data)

class Dice():
    value = 1
    faces:int
    
    def __init__(self, faces) -> None:
        self.faces = faces

    def roll(self):
        res = randint(range(self.faces))
        return res

    def __str__(self) -> str:
        return f'{self.faces}, {self.value}'

    def __repr__(self) -> str:
        return self.__str__()

class Deterministic_dice(Dice):
    value = 1
    times_rolled = 0

    def __init__(self, faces) -> None:
        super().__init__(faces)

    def roll(self):
        res = self.value
        if self.value == self.faces:
            self.value = 1
        else:
            self.value += 1
        self.times_rolled += 1
        return res
    def __str__(self) -> str:
        return super().__str__() + f', {self.times_rolled}'

    def __repr__(self) -> str:
        return self.__str__()

class Player():
    name = ''
    pos = 0
    score = 0
    has_won = False
    winning_amount = 0

    def __init__(self, name, initial_pos, winnig_amount) -> None:
        self.name = name
        self.pos = initial_pos
        self.winning_amount = winnig_amount

    
    def move(self, positions):
        self.pos += positions
        if self.pos > 10:
            self.pos = self.pos%10
            if self.pos == 0:
                self.pos = 10
        self.score += self.pos
        if self.score >= self.winning_amount:
            self.has_won = True

    def __str__(self) -> str:
        return f'{self.name}: pos:{self.pos}, score:{self.score}'

    def __repr__(self) -> str:
        return f'{self.name}: pos:{self.pos}, score:{self.score}'

def problem1(p1_pos, p2_pos):
    p1 = Player('p1',p1_pos, 1000)
    p2 = Player('p2',p2_pos, 1000)
    dice = Deterministic_dice(100)
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

@functools.lru_cache(maxsize=None)
def problem2(turn,p1, p2, s1, s2):
    players = [p1, p2]
    scores = [s1, s2]
    if s1 >= 21:
        return [1,0]
    if s2 >= 21:
        return [0,1]
    
    play = turn%2

    comb = [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]   

    win_times = [0,0]

    for combination in comb:
        players[play] = (players[play] + combination[0] - 1)%10 + 1
        scores[play] += players[play]
        res = problem2(turn+1,players[0], players[1], scores[0], scores[1])
        win_times[0] += res[0]*combination[1]
        win_times[1] += res[1]*combination[1]
        scores[play] -= players[play]
        players[play] = (players[play] - combination[0] - 1)%10 + 1

    return win_times

player1 = int(data[0][-1])
player2 = int(data[1][-1])
p1 = Player('p1', player1, 21)
p2 = Player('p2', player2, 21)
print(max(problem2(0, player1,player2,0,0)))
