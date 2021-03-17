from Asset import Save,Map,Plot,Chicken_System
import threading,os,time,random

First_Open = 0
#-----------------------------Load()
Day = 0
Time = 0

Player_Place="Home"
if os.path.exists(os.getcwd()+os.sep+"save.txt") == True:
    with open(os.getcwd()+os.sep+"save.txt","rt",encoding="utf-8") as save:
        data = save.readlines()
        for i in data:
            a = i.rsplit("\n")
            a = a[0]
            a = exec(a)
if First_Open == 0:
    Day = 0
    Time = 0
    Chicken = Chicken_System.Chicken(0,0,0,0,0,0,0,0,0,0,0,0,0)
    
#-----------------------------Updata()
def Updata():
    while(1):
        time.sleep(0.1)
        p = random.randint(1,10)


updata = threading.Thread(target = Updata, name = 'Updata')
updata.start()

#-----------------------------Save()
def Save_Date(Chicken,p):
    Save.save(Chicken,p,p,p,p)

Save_Date(Chicken,1)
#----------------------------------------------------------Day()
Chicken._EXP(51)
Chicken._KFC()
    
while 1:
#-----------------------------Plot()
    if Day == 0:
        Plot.Main_Plot(0)
    if Day == 1:
        Plot.Main_Plot(2)
    if Day == 2:
        Plot.Main_Plot(3) 
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
        elif Chicken.Map[0] == "Bathhouse":
            while Chicken.Map[0] == "Bathhouse":
                op ="po"
     #-----------------------------Store()
        elif Chicken.Map[0] == "Store":
            while Chicken.Map[0] == "Store":
                op ="po"
    #-----------------------------School()
        elif Chicken.Map[0] == "School":
            while Chicken.Map[0] == "School":
                op ="po"
    #-----------------------------Search()
        elif Chicken.Map[0] == "Search":
            while Chicken.Map[0] == "Search":
                op ="po"
    print("Loop ok!")
