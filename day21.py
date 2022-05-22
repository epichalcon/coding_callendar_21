#https://adventofcode.com/2021/day/21
from typing import SupportsComplex, overload
from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
from random import randint
import functools
data = gd.getdata(f"{DIRECTORY}day21.txt")
data = gd.separarPorLineas(data)

class Dice():
    value = 1
    faces:int
    times_rolled = 0
    
    def __init__(self, faces) -> None:
        self.faces = faces

    def roll(self):
        res = self.value
        if self.value == self.faces:
            self.value = 1
        else:
            self.value += 1
        self.times_rolled += 1
        return res

    def __str__(self) -> str:
        return f'{self.faces}, {self.value}, {self.times_rolled}'

    def __repr__(self) -> str:
        return self.__str__()

class Player():
    name = ''
    pos = 0
    score = 0
    has_won = False
    winning_amount = 0

    def __init__(self, name, initial_pos, winnig_amount, score = 0) -> None:
        self.name = name
        self.pos = initial_pos
        self.winning_amount = winnig_amount
        self.score = score

    
    def move(self, positions):
        self.pos = ( self.pos + positions - 1) % 10 + 1
        self.score += self.pos
        if self.score >= self.winning_amount:
            self.has_won = True

    def undo_move(self, positions):
        self.score -= self.pos
        self.pos = ( self.pos - positions - 1) % 10 + 1
        if self.score < self.winning_amount:
            self.has_won = False



    def won(self):
        return self.has_won or self.score >= self.winning_amount

    def __str__(self) -> str:
        return f'{self.name}: pos:{self.pos}, score:{self.score}'

    def __repr__(self) -> str:
        return f'{self.name}: pos:{self.pos}, score:{self.score}'

def problem1(p1_pos, p2_pos):
    p1 = Player('p1',p1_pos, 1000)
    p2 = Player('p2',p2_pos, 1000)
    dice = Dice(100)
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
    players = [Player('p1', p1, 21, s1),Player('p2', p2, 21, s2)]
    if players[0].won():
        return [1,0]
    if players[1].won():
        return [0,1]
    
    play = turn%2

    comb = [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]   

    win_times = [0,0]

    for positions, ways in comb:
        players[play].move(positions)
        res = problem2(turn+1,players[0].pos, players[1].pos, players[0].score, players[1].score)
        win_times[0] += res[0]*ways
        win_times[1] += res[1]*ways
        players[play].undo_move(positions)

    return win_times

player1 = int(data[0][-1])
player2 = int(data[1][-1])
print(problem1(player1, player2))
print(max(problem2(0, player1,player2,0,0)))
