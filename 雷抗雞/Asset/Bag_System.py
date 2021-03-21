import time
#-----------------------------------倉庫----------------------------------------

class Bag():        #####倉庫類別#####
    def __init__(self,Money,Diamond,Food,Cake,Cookies,Hamburger):
        self.Money = Money           #金幣
        self.Diamond = Diamond       #鑽石
        self.Food = Food             #雞飼料
        self.Cake = Cake             #蛋糕
        self.Cookies = Cookies       #餅乾
        self.Hamburger = Hamburger   #特大麥香雞
    
    def show(self):     #列出資源
        print("目前身上的物品: ")
        print('金幣:    ',self.Money,'鑽石:    ',self.Diamond,
              '\n有機雞飼料:    ',self.Food,'生乳酪蛋糕:    ',self.Cake,'餅乾:    ',
              self.Cookies,'特大麥香雞    ',self.Hamburger)
        print("")
#-------------------------------##增減##函式--------------------------------------
    def add_money(self,add):
        self.Money += add
    
    def add_diamond(self,add):
        self.Diamond += add

    def add_food(self,add):
        self.Food += add

    def add_cake(self,add):
        self.Cake += add

    def add_cookies(self,add):
        self.Cookies += add

    def add_hamburger(self,add):
        self.Hamburger += add
#--------------------------------##進食##函式---------------------------------------
    def Eat(self,Chicken):
        while 1:
            Chicken._State(1)
            print('0.不吃了',
                  '\n1.有機雞飼料:    ',self.Food,
                  '\n2.生乳酪蛋糕:    ',self.Cake,
                  '\n3.餅乾:    ',self.Cookies,
                  '\n4.特大麥香雞:    ',self.Hamburger)
            print("")
            eat = input('請輸入想吃的物品編號: ')
            if eat == "0":
                break
            if eat == "1" and self.Food > 0:
                Chicken._MP(1)      #能力值增加
                Chicken._Hunger(5)
                self.add_food(-1)    #食物減少
                print(Chicken.Name,' 吃了有機雞飼料 ! ! ')
                time.sleep(0.5)
                print(Chicken.Name,' 的行動值增加 1 ,飽食度增加 5 ')
                time.sleep(0.5)
            elif eat == "1":
                print("食物不足")
            if eat == "2" and self.Cake > 0:
                Chicken._MP(3)
                Chicken._Hunger(15)
                Chicken._Emotion(15)
                self.add_cake(-1)
                print(Chicken.Name,' 一臉滿足的吃下了生乳酪蛋糕 ')
                time.sleep(0.5)
                print(Chicken.Name,' 的行動值增加 3 ,飽食度增加 15 ,心情增加 15 ')
                time.sleep(0.5)
            elif eat == "2":
                print("食物不足")
            if eat == "3" and self.Cookies > 0:
                Chicken._MP(8)
                Chicken._Hunger(15)
                self.add_cookies(-1)
                print('喀滋喀滋... ',Chicken.Name,' 優雅的吃完餅乾了 ')
                time.sleep(0.5)
                print(Chicken.Name,' 的行動值增加 8 ,飽食度增加 15 ')
                time.sleep(0.5)
            elif eat == "3":
                print("食物不足")
            if eat == "4" and self.Hamburger > 0:
                Chicken._MP(20)
                Chicken._Hunger(20)
                Chicken._Emotion(30)
                self.add_hamburger(-1)
                print('吧唧吧唧... ',Chicken.Name,' 含著眼淚吃完了特大麥香雞... ')
                time.sleep(0.5)
                print(Chicken.Name,' 的行動值增加 20 ,飽食度增加 20 \n但是心情減少 30 ')
                time.sleep(0.5)
            elif eat == "4":
                print("食物不足")
