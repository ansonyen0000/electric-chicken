import random

def Attack(My_Name, My_ATK, My_HP, My_DF, Mon_Name, Mon_ATK, Mon_HP, Mon_DF):
    My_Name = Name #雞的數值
    My_ATK = ATK
    My_HP = HP
    MY_DF = DF
    Mon_Name = MonName #怪物的數值
    Mon_ATK = MonATK
    Mon_HP = MonHP
    Mon_DF = MonDF
    
    MyAttack = My_ATK - Mon_DF #雞的攻擊
    MonAttack = Mon_ATK - My_DF #怪物的攻擊
    if MyAttack <= 0:
        MyAttack = 1
    if MonAttack <= 0:
        MonAttack = 1
    while 1:
        if My_HP > 0:
            if random.randint(1,11) == 4:
                MyFinalAttack = 2*MyAttack
            else:
                MyFinalAttack = MyAttack
            if random.randint(1,11) == 5:
                MonFinalAttack = 2*MonAttack
            else:
                MonFinalAttack = MonAttack
            Mon_HP -= MyFinalAttack
            My_HP -= MonFinalAttack
            print('%s 對 %s 造成', MyFinalAttack, '點傷害'%(My_Name,Mon_Name))
            print('%s 對 %s 造成', MonFinalAttack, '點傷害'%(Mon_Name,My_Name))
        elif My_HP <= 0:
            print('%s 被 %s 擊殺了'%(My_Name,Mon_Name))
            print('你死了!')
            return 0
            break
        elif Mon_HP <= 0:
            print('%s 被 %s 擊殺了'%(Mon_Name,My_Name))
            return 1
            break
