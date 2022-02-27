from diceClass import Dice
from playerClass import Player
a=Dice(1)
tmk = Player(0)

(Dice.rollDice(a))
print(a.num)

abc=[1,1,1,5,4,4]
print(tmk.calculatePoint(abc))

print(tmk.throwDice(6))