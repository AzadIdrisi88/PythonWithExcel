import pandas as pd
# from demo2 import SaveToExcel

'''
1-read csv and return df.
2-write csv __ (a) csv name (b) data frame.
3-get colunm , get row and colunm.
4-get row.

'''


def readcsv():
    try:
        filename = "accno.csv"
        df = pd.read_csv(filename,index_col=0)
        # accno=df["accno"]
        # customer=df["customer"]
        # balance=df["balance"]
        df['customer'].fillna(value=pd.NA, inplace=True)
        df['balance'].fillna(value=pd.NA, inplace=True)
        print(df)
        return df
    except:
        return None
readcsv()


def getBalance(accno):
    try:
        df = readcsv()
        x = df['balance']
        return x.loc[accno]
    except:
        return None


# def Withdraw(accno, amount):
#     currentbalance = getBalance(accno)
#     if currentbalance is None:
#         return None
#     if amount > currentbalance:
#         return None
#     newbalance = currentbalance-amount
#     ChangeBalance(accno, newbalance)


# def Deposit(accno, amount):
#     currentbalance = getBalance(accno)
#     if currentbalance is None:
#         return None
#     newbalance = currentbalance+amount
#     ChangeBalance(accno, newbalance)


def ChangeBalance(accno, newbalance):
    try:
        newdata = {'accno': [accno],'balance': [newbalance]}
        newdata = pd.DataFrame(newdata, index=newdata["accno"])
        print(newdata)
        df = readcsv()
        df.update(newdata)
        writecsv(df)
        return True
    except:
        return False


# def CloseAccount(accno):
#     try:
#         df = readcsv()
#         df = df.drop(accno)
#         print(df)
#         writecsv(df)
#         return True
#     except:
#         return False


def NewAccount(accno, name, balance):
    try:
        newdata = {'accno': accno,
                   'name': name,
                   'balance': balance
                   }
        df = readcsv()
        print('dfff', newdata)
        df=df.append(newdata,ignore_index=True)
        writecsv(df)
        return True
    except:
        return False


def writecsv(df):
    filename = "accno.csv"
    df.to_csv(filename)


# '''
# 0-Exit,1-New Account,2-Deposit,3-Withdraw,4-Check Balance, 5-Close Account

# '''
# df = readcsv()
# print(df)
# amt = getBalance(44)
# print(amt)
# Deposit(44, 1000)

# amt = getBalance(44)
# print(amt)

# drop=CloseAccount(11)
# print('drop',drop)

new = NewAccount(89, 'Raju', 500)
if new:
    print("Account created successfully")
else:
    print("Failed to create an account")
