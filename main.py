from diceClass import Dice
from playerClass import Player
a=Dice()
tmk = Player(0)



throwedDice=tmk.throwDice(6)
print(throwedDice)
if tmk.calculatePoint(throwedDice)==0:
    print("BUSTED")
else:
    inp= input("Write indexes 1-6 with , AND LAST go or save")
    listInp=inp.split(",")
    listInpIndex=[int(i) for i in listInp[:-1]]
    print(listInpIndex)
    selectedDices=[]
    for i in listInpIndex:
        selectedDices.append(throwedDice[i-1])
    if not tmk.calculatePoint(selectedDices)==0:
        if listInp[-1]=="save":
            tmk.point=tmk.point+ tmk.calculatePoint(selectedDices)
            print(tmk.point)
    else:
        print("you selected 0 points")



"""
oyuncu 6 adet zar atacak
atılan zarlar 0 puansa busted yazacak
0 değilse seçim yapılacak
yapılan seçim sonucu taşlar ıstakaya alınacak iki seçenek var:
    1 ıstakadaki puanları işle
    2 zar atmaya devam et

"""