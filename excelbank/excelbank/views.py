from django.shortcuts import render, HttpResponse, redirect
import pandas as pd

def readcsv():
    try:
        filename='bank.csv'
        df=pd.read_csv(filename,index_col=0)
        # print(df)
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
        df=df.drop(accno)
        print(df)
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
    
def index(request):
    return render(request,'home.html')

def newaccno(request):
    accno=''
    name=''
    balance=''
    if request.GET:
        accno=int(request.GET['accno'])
        name=request.GET['name']
        balance=int(request.GET['balance'])
        NewAccount(accno,name,balance)
        return HttpResponse('created')
    # return render(request,'newaccno.html')
    return render(request,'newaccno.html',{'accno':accno,"name":name,"balance":balance}) 

def deposite(request):
    accno=''
    amount=''
    if request.GET:
        accno=int(request.GET['accno'])
        amount=int(request.GET['amount'])
        Deposite(accno,amount)
        return HttpResponse('f{{amount}} is Deposited')
    return render(request,'deposite.html')

def moneywithdraw(request):
    accno=''
    amount=''
    if request.GET:
        accno=int(request.GET['accno'])
        amount=int(request.GET['amount'])
        withdraw(accno,amount)
        return HttpResponse('Money Withdraw')
    return render(request,'withdraw.html')

def details(request):
    accno=''
    result=''
    if request.GET:
        accno=int(request.GET['accno'])
        result=searchAccount(accno)
        print(result)
    return render (request,'detail.html',{"result":result})

def delete(request):
    accno=''
    result=None
    if request.GET:
        accno=int(request.GET['accno'])
        result=CloseAccount(accno)
        print(result)
    return render (request,'delete.html',{"result":result})


