import os

def save(Name,Money):
    with open(os.getcwd()+os.sep+"save.txt","wt",encoding="utf-8") as save:
        save.write('pp='+"'"+str(Name)+"'"+"\n")
        save.write('money='+str(Money)+"\n")
