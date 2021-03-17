import random

class Chicken(): #雞
    def __init__(self,State,Name,EXP,Level,HP,ATK,DF,Hunger,Emotion,MP,Luck,Map,Point):
        self.State = State
        self.Name = Name
        self.EXP = EXP
        self.Level = Level
        self.HP = HP
        self.ATK = ATK
        self.DF = DF
        self.Hunger = Hunger
        self.Emotion = Emotion
        self.MP = MP
        self.Luck = Luck
        self.Map = Map
        self.Point = Point
    def _State(self,Hp):
        p=np
    def _Name(self,Name):
        self.Name = Name
    def _EXP(self,exp):
        if self.Level <= 10:
            self.EXP += exp
            if self.EXP >= 50:
                self.Level += 1
                self.Point += 3
                self.EXP -= 50

        elif 10 < self.Level <= 20:
            if self.EXP >= 100:
                self.Level += 1
                self.Point += 3
                self.EXP -= 100
        elif 20 < self.Level <= 30:
            if self.EXP >= 150:
                self.Level += 1
                self.Point += 4
                self.EXP -= 150
        elif 30 < self.Level <= 40:
            if self.EXP >= 200:
                self.Level += 1
                self.Point += 5
                self.EXP -= 200
        elif 40 < self.Level < 50:
            if self.EXP >= 250:
                self.Level += 1
                self.Point += 5
                self.EXP -= 250
        elif self.Level == 50:
            self.EXP = 0
    def _Hp(self,Hp):
        self.Hp = Hp
    def _ATK(self,ATK):
        self.ATK = ATK
    def _DF(self,DF):
        self.DF = DF
    def _Hunger(self,Hunger):
        self.Hunger = Hunger
    def _Emotion(self,Emotion):
        self.Emotion = Emotion
    def _MP(self,MP):
        self.MP = MP
    def _Luck(self,Luck):
        self.Luck = Luck
    def _Map(self,Map):
        self.Map = Map
    def _KFC(self):
        if self.Level <= 10:
            MaxEXP = 50
        elif 10 < self.Level <= 20:
            MaxEXP = 100
        elif 20 < self.Level <= 30:
            MaxEXP = 150
        elif 30 < self.Level <= 40:
            MaxEXP = 200
        elif 40 < self.Level <= 50:
            MaxEXP = 250
        print(self.Name,'   ','Level ',self.Level,'(',self.EXP,'/',MaxEXP,')'
              ,'\n','HP: ',self.HP,'   ','ATK: ',self.ATK,'   ','DF: ',self.DF,'   '
              ,'\n','飽食度: ',self.Hunger,'/100','   ','心情值: ',self.Emotion,'/100'
              ,'   ','行動值: ',self.MP,'/100','\n','當前狀態: ',self.State,'   '
              ,'幸運值: ',self.Luck,end="")
    def LevelUp(self,Level,ATK,HP,DF,Luck):
        if self.Level == 10:
            self.ATK += 5
            self.HP += 50
            self.DF += 5
            self.Luck += 2
        elif Level == 20:
            self.ATK += 7
            self.HP += 75
            self.DF += 5
            self.Luck += 2
        elif Level == 30:
            self.ATK += 9
            self.HP += 100
            self.DF += 7
            self.Luck += 2
        elif Level == 40:
            self.ATK += 12
            self.HP += 150
            self.DF += 8
            self.Luck += 2
        elif Level == 50:
            self.ATK += 15
            self.HP += 200
            self.DF += 10
            self.Luck += 2