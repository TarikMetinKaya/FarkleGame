import random
class Dice:

    num=0
    def __init__(self,num):
        self.num=num

    def rollDice(self):
        self.num=random.randint(1,6)
