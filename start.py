import threading,os,time,random

#-----------------------------Start()
First_Open = False
if os.getcwd()+os.sep+"save.txt" == False:
    pass
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
        print('\n隨機事件' + str(p))

updata = threading.Thread(target = Updata, name = 'Updata')
updata.start()

#-----------------------------
