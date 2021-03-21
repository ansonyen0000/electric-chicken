class Mons():
    def __init__(self,Name,HP,ATK,DF,EXP,Coin,Map):
        self.Name = Name
        self.HP = HP
        self.ATK = ATK
        self.DF = DF
        self.EXP = EXP
        self.Coin = Coin
        self.Map = Map
    def _HP(self,HP):
        self.HP += HP
    def attribute(self):
        print (self.Name,'\n','等級:',self.Level,' ','生命值:',self.HP,' ',
               '攻擊:',self.ATK ,' ','防禦:',self.DF,' ','擊殺經驗:',self.EXP,
               '錢:',self.Coin)
        
#-------------新增野怪區--------------------------------------------------------
def Mon(_id):
    if _id == 0:
        return Mons('雞骨頭',25,25,0,5,5,[0,0])
    elif _id == 1:
        return Mons('史萊姆',45,18,5,5,5,[0,0])
    elif _id == 2:
        return Mons('期中霉運吉娃娃',60,25,12,5,5,[1,0])
    elif _id == 3:
        return Mons('不重要的路人甲',100,20,10,5,5,[1,0])
    elif _id == 4:
        return Mons('不重要的路人乙',55,40,7,5,5,[2,0])
    elif _id == 5:
        return Mons('重修怨魂',50,25,40,5,5,[2,0])
    elif _id == 6:
        return Mons('鳥人幫成員',65,20,25,5,5,[3,0])
    elif _id == 7:
        return Mons('學分守門員',70,30,20,5,5,[3,0])
    elif _id == 8:
        return Mons('嬰靈雞',35,50,10,5,5,[4,0])
    elif _id == 9:
        return Mons('星爆連流雞',40,60,15,5,5,[4,0])
    elif _id == 10:
        return Mons('渾元形意太雞門徒',85,40,20,5,5,[5,0])
    elif _id == 11:
        return Mons('',85,40,20,5,5,[5,0])
    elif _id == 12:
        return Mons('',85,40,20,5,5,[6,0])
    elif _id == 13:
        return Mons('',85,40,20,5,5,[6,0])
    elif _id == 14:
        return Mons('',85,40,20,5,5,[7,0])
    elif _id == 15:
        return Mons('',85,40,20,5,5,[7,0])
    elif _id == 16:
        return Mons('',85,40,20,5,5,[8,0])
    elif _id == 17:
        return Mons('',85,40,20,5,5,[8,0])
#-------------新增boss區--------------------------------------------------------
    elif _id == 18:
        return Mons('阿雞米德',210,40,20,5,5,[0,0])
    elif _id == 19:
        return Mons('青眼白斬雞',305,53,32,5,5,[1,0])
    elif _id == 20:
        return Mons('拿著野太刀的雞頭人',455,108,25,5,5,[2,0])
    elif _id == 21:
        return Mons('究極青眼白斬雞',625,137,50,5,5,[3,0])
    elif _id == 22:
        return Mons('青眼九頭古巨雞',1150,96,35,5,5,[4,0])
    elif _id == 23:
        return Mons('重甲雞神.雞動號',875,145,83,5,5,[5,0])
    elif _id == 24:
        return  Mons('鳥人幫幫主.助教',1020,163,45,5,5,[6,0])
    elif _id == 25:
        return Mons('拿著期中預警通知對你微笑.啟彬.吳.',910,225,15,5,5,[7,0])
    elif _id == 26:
        return Mons('真.學分掌控.啟彬.吳.The Boss',1545,180,55,5,5,[8,0])
#-------------------------------------------------------------------------------

def Drop(Bag,Mons,Chicken):
    Chicken.EXP += Mons.EXP
    Bag.Money += Mons.EXP
    if random.randint(1,101) == 7:
        Bag.Diamond += 1
