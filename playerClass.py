from diceClass import Dice
class Player:
    point = 0
    processedDices = []
    selectedDices = []

    def __init__(self, point):
        self.point = point

    def throwDice(self, count):
        throwedDice=[]
        a= Dice(1)
        for i in range(count):
            (Dice.rollDice(a))
            throwedDice.append(a.num)
        return throwedDice

    def selectDice(self, diceNum):
        self.selectedDices.append(diceNum)

    def calculatePoint(self, selectedDices):
        point = 0
        tempPoint = 0
        count = 0

        # 1
        count = selectedDices.count(1)
        if count == 0:
            tempPoint = 0
        elif count == 1:
            tempPoint = 100
        elif count == 2:
            tempPoint = 200
        elif count == 3:
            tempPoint = 1000
        elif count == 4:
            tempPoint = 2000
        elif count == 5:
            tempPoint = 4000
        elif count == 6:
            tempPoint = 8000
        point=point+tempPoint

        # 2
        count = selectedDices.count(2)
        if count == 0 or count == 1 or count == 2:
            tempPoint=0
        elif count==3:
            tempPoint=200
        elif count == 4:
            tempPoint=400
        elif count == 5:
            tempPoint=800
        elif count == 6:
            tempPoint=1600
        point=point+tempPoint

        # 3
        count = selectedDices.count(3)
        if count == 0 or count == 1 or count == 2:
            tempPoint = 0
        elif count == 3:
            tempPoint = 300
        elif count == 4:
            tempPoint = 600
        elif count == 5:
            tempPoint = 1200
        elif count == 6:
            tempPoint = 2400
        point = point + tempPoint

        # 4
        count = selectedDices.count(4)
        if count == 0 or count == 1 or count == 2:
            tempPoint = 0
        elif count == 3:
            tempPoint = 400
        elif count == 4:
            tempPoint = 800
        elif count == 5:
            tempPoint = 1600
        elif count == 6:
            tempPoint = 3200
        point = point + tempPoint

        # 5
        count = selectedDices.count(5)
        if count == 0:
            tempPoint = 0
        elif count == 1:
            tempPoint = 50
        elif count == 2:
            tempPoint = 100
        elif count == 3:
            tempPoint = 500
        elif count == 4:
            tempPoint = 1000
        elif count == 5:
            tempPoint = 2000
        elif count == 6:
            tempPoint = 4000
        point = point + tempPoint


        # 6
        count = selectedDices.count(6)
        if count == 0 or count == 1 or count == 2:
            tempPoint = 0
        elif count == 3:
            tempPoint = 600
        elif count == 4:
            tempPoint = 1200
        elif count == 5:
            tempPoint = 2400
        elif count == 6:
            tempPoint = 4800
        point = point + tempPoint

        return point