def Buy(Money,_id = 0):
    if _id == 0:
        print("已購滿brbr")
        return(Money-10)
    if _id == 1:
        print("已購滿brbr")
        return(Money-30)
    
def Sell(Money,_id = 0):
    if _id == 0:
        print("已賣出brbr")
        return(Money+5)
    if _id == 1:
        print("已購滿brbr")
        return(Money+15)
