import pandas as pd


def readcsv():
    try:
        filename='bank.csv'
        df=pd.read_csv(filename,index_col=0)
        print(df)
        return df
    except:
        return None
df=readcsv()  

def writecsv(df):
    filename='bank.csv'
    df.to_csv(filename)

def getBalance(accno):
    try:
        df=readcsv()
        x=df['balance']   # extract all the balance from df
        return x.loc[accno]
    except:
        return None

def ChangeBalance(accno,newbalance):
    try:
        newdata={'accno':[accno],'balance':[newbalance]}
        newdata=pd.DataFrame(newdata,index=newdata['accno'])
        df=readcsv()
        print(newdata)
        df.update(newdata)
        writecsv(df) 
        return True
    except:
        return False
    
def withdraw(accno,amount):
    currentbalance=getBalance(accno)
    if currentbalance is None:
        return None
    if amount>currentbalance:
        return None
    newbalance=currentbalance-amount
    writecsv(df)
    ChangeBalance(accno,newbalance)

def Deposite(accno,amount):
    currentbalance=getBalance(accno)
    if currentbalance is None:
        return None
    newbalance=currentbalance+amount
    # writecsv(df)
    ChangeBalance(accno,newbalance)

def CloseAccount(accno):
    try:
        df=readcsv()
        x=df.drop(accno)
        print(x)
        writecsv(df)
        return True
    except:
        return False

def NewAccount(accno,name,balance):
    try:
        newdata={'accno':accno,'name':name,'balance':balance}
        df=readcsv()
        print(newdata)
        df.loc[accno]=newdata
        print(df)
        writecsv(df)
        return True
    except:
        return False
    
def searchAccount(accno):
    try:
       df=readcsv()
       x=df[['name']]
       name=x.loc[accno][0]
       balance=getBalance(accno)
       return  accno,name,balance
    
    except:
        return None
    
# while True:
#     print("0-Exit ,1-NewAccount , 2-Deposite , 3-Withdraw ,4-Search , 5-CloseAccount")
#     select=int(input('Please select your desire task = '))
#     if select==0:
#         break
#     elif select==1:
#             accno=int(input('Please enter account number = '))
#             name=(input('Please enter your name = '))
#             balance=int(input('Please enter an amount = '))
#             NewAccount(accno,name,balance)
#             continue
#     elif select==2:
#             accno=int(input('Please enter account number = '))
#             amount=int(input("Enter deposite Amount = "))
#             Deposite(accno,amount)
#             if Deposite:
#                  print(f'{amount} Amount deposited successfully')
#             else:
#                  print('Failed')
#             continue
#     elif select==3:
#             accno=int(input('Please enter account number = '))
#             amount=int(input("Enter deposite Amount = "))
#             withdraw(accno,amount)
#             if withdraw:
#                  print(f'{amount} Amount dedected')
#             else:
#                  print('Failed')
#             continue
#     elif select==4:
#             accno=int(input('Please enter account number = '))
#             accno,name,balance=searchAccount(accno)
#             print(accno,name,balance)
#             continue
#     elif select==5:
#             accno=int(input('Please enter account number = '))
#             CloseAccount(accno)
#             if CloseAccount:
#                  print(f'{accno} Your Account has been Closed.\n Thankyou.')
#             else:
#                  print('Failed')
#     else:
#          print('Invalid Selection')
    
    
    
# # search=searchAccount(44)
# # print(search)
# # print(type(search))

# # new=NewAccount(55,'Carolyn',5000)
# # if new:
# #     print('Account Created successfully')
# else:
#     print("Failed to create an account")

# amt=getBalance(44)
# print(amt)

# x=withdraw(22,300)
# print(x)

# y=Deposite(55,1200)
# if y:
#     print("Amount deposited successfully")
# else:
#     print('Failed to deposit an amount')
# # print(y)

drop=CloseAccount(33)
print(drop)


