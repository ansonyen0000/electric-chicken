from Asset import Save,Money_System,Map,Plot
import threading,os,time,random


#-----------------------------Load()
First_Open = False
Player_Place="Home"
if os.path.exists(os.getcwd()+os.sep+"save.txt") == False:
    monry = 0
else:
    with open(os.getcwd()+os.sep+"save.txt","rt",encoding="utf-8") as save:
        data = save.readlines()
        for i in data:
            a = i.rsplit("\n",1)
            a = a[0]
            a = exec(a)
#-----------------------------Updata()
def Updata():
    while(1):
        time.sleep(0.1)
        p = random.randint(1,10)


updata = threading.Thread(target = Updata, name = 'Updata')
updata.start()

#-----------------------------Save()
def Save_Date():
    Save.save("df",100)
#----------------------------------------------------------Day()

Plot.Main_Plot(0)
Plot.Main_Plot(1)
Plot.Main_Plot(2)
Plot.Main_Plot(3)
Plot.Main_Plot(4)
Plot.Main_Plot(5)
Plot.Main_Plot(6)
Plot.Main_Plot(7)
Plot.Main_Plot(8)
Plot.Main_Plot(9)

qw = 84
map = Map.Map_Load(0)
while(1):
    pp = input(":")
    qw = Map.Player_Move(map[0],map[1],map[2],qw,pp)
    Map.Map_Print(map[0],map[1],map[2],qw)

while 1:
#-----------------------------Plot()
#-----------------------------Home()
    while 1:
        ppw = input()
        if ppw == "ok":
            break
        print("wre")
        if Player_Place == "Hme":
            while 1:
                op ="po"
     #-----------------------------Bathhouse()
        elif Player_Place == "Bathhouse":
            while 1:
                op ="po"
     #-----------------------------Store()
        elif Player_Place == "Store":
            while 1:
                money = Money_System.Buy(money,0)
                print(money)
                money = Money_System.Sell(money,0)
                print(money)
    #-----------------------------School()
        elif Player_Place == "School":
            while 1:
                op ="po"
    #-----------------------------Search()
        elif Player_Place == "Search":
            while 1:
                op ="po"
    print("Loop ok!")
