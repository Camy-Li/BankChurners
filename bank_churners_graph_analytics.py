"""
HW: 利用OpenDate 讀取CSV檔,印出資料的最大值,最小值,中位數,平均值, 並以資料繪圖
Date: 2022/04/13
Data:'BankChurners.csv'
"""
"""
資料說明：
CLIENTNUM(客戶編號) - Client number. Unique identifier for the customer holding the account
Attrition_Flag(是否為流失客戶) - Internal event (customer activity) variable - if the account is closed then 1 else 0
Customer_Age - Customer's Age in Years
Gender - M=Male, F=Female
Dependent_count(要扶養的人數) - Number of dependents
Education_Level - example: high school, college graduate, etc.
Marital_Status - Married, Single, Divorced, Unknown
Income_Category - Annual Income (< $40K, $40K - 60K, $60K - $80K, $80K-$120K, > $120K, Unknown)
Card_Category - Type of Card (Blue, Silver, Gold, Platinum)
Months_on_book(在名冊上的持續期間)- Period of relationship with bank
Total_Relationship_Count(持有商品數) - Total no. of products held by the customer
Total_Trans_Amt(過去一年交易量) - Total Transaction Amount (Last 12 months)
Total_Trans_Ct(過去一年交易次數) - Total Transaction Count (Last 12 months)
共10127筆資料
"""

import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

def getCol(fileName,n):                     # 取得每個column的值
    dataset = pd.read_csv(fileName)
    return dataset.iloc[:, n].values

attrition = getCol('BankChurners.csv',1)
age = getCol('BankChurners.csv',2)
gender = getCol('BankChurners.csv',3)
depend_ct = getCol('BankChurners.csv',4)
edu = getCol('BankChurners.csv',5)
marital = getCol('BankChurners.csv',6)
income = getCol('BankChurners.csv',7)
card_ctgr = getCol('BankChurners.csv',8)
months_on_books = getCol('BankChurners.csv',9)
relationship_count = getCol('BankChurners.csv',10)
trans_amt = getCol('BankChurners.csv',11)
trans_ct = getCol('BankChurners.csv',12)


def statPrint(list):              # 尋找 最大值, 最小值, 中位數, 平均值
    list.sort()
    n= len(list)
    max = "最大值:"+ str(list[-1])
    min = "最小值:"+ str(list[0])
    med = "中位數:" + str((list[(n-1)//2]+list[n//2])/2)
    avg = "平均值:"+ 0 if len(list) == 0 \
        else "平均值:"+str(round(sum(list/len(list)),2))
    return max, min, med, avg

# 印出 最大值, 最小值, 中位數, 平均值
print("註冊期間:", statPrint(months_on_books))
print("持有產品數:", statPrint(relationship_count))
print("過去一年交易量:", statPrint(trans_amt))
print("過去一年交易次數:", statPrint(trans_ct))


# 換成中文的字體
# plt.rcParams['font.新細明體'] = ['SimSun'] # 步驟一（替換sans-serif字型）
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）

figure, axes = plt.subplots(3, 3, figsize=(18, 8), num="銀行信用卡用戶資料統計圖")  # figsize:預設視窗大小(w,h)
plt.subplots_adjust(left=0.1, bottom=0.065, right=0.92, top=0.95, wspace=0.25, hspace=0.45) # 預設subplots位置和大小
ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9 = axes.flatten()

def getDataByGender(fileName, gender):              # 將資料以 性別 分類
    dataset = pd.read_csv(fileName)
    result=[]
    for data in dataset.values:
        d = list(data)
        if d[3] == gender:
            result.append(d)
    return result

def getDataByMaritalStatus(fileName, marital_status):  # 將資料以 婚姻狀態 分類
    dataset = pd.read_csv(fileName)
    result=[]
    for data in dataset.values:
        d = list(data)
        if d[6] == marital_status:
            result.append(d)
    return result

def getDataByAttrit(fileName, attrit):              # 將資料分類 現存客戶, 流失客戶
    dataset = pd.read_csv(fileName)
    result=[]
    for data in dataset.values:
        d = list(data)
        if d[1] == attrit:
            result.append(d)
    return result
existing=getDataByAttrit('BankChurners.csv', 'Existing Customer')
attrited=getDataByAttrit('BankChurners.csv', 'Attrited Customer')

def getDataByIncome(fileName, income):              # 將資料以 所得區間 分類
    dataset = pd.read_csv(fileName)
    result=[]
    for data in dataset.values:
        d = list(data)
        if d[7] == income:
            result.append(d)
    return result
below40=getDataByIncome('BankChurners.csv', 'Less than $40K')
btw40and60=getDataByIncome('BankChurners.csv', '$40K - $60K')
btw60and80=getDataByIncome('BankChurners.csv', '$60K - $80K')
btw80and120=getDataByIncome('BankChurners.csv', '$80K - $120K')
higher120=getDataByIncome('BankChurners.csv', '$120K +')
unknown=getDataByIncome('BankChurners.csv', 'Unknown')

def getDataByCard(fileName, card):              # 將資料以 信用卡等級 分類
    dataset = pd.read_csv(fileName)
    result=[]
    for data in dataset.values:
        d = list(data)
        if d[8] == card:
            result.append(d)
    return result

# 1
m=getDataByGender('BankChurners.csv', 'M')  # 呼叫性別為'M'的資料
f=getDataByGender('BankChurners.csv', 'F')  # 呼叫性別為'F'的資料
width = 0.35
males_count=[0]*7           # 每個x軸起始值設為0, males_count = [0, 0, 0, 0, 0, 0, 0]
females_count=[0]*7
for value in m:
    males_count[value[-3]]+=1     # 找Total_Relationship_Count的資料,找到就在對應的軸+1
for value in f:
    females_count[value[-3]]+=1

males_count=males_count[1:]       #去掉第一個值(因為是0)後, males_count = [425, 596, 1084, 892, 862, 910]
females_count=females_count[1:]   # females_count = [485, 647, 1221, 1020, 1029, 956]
x1=np.arange(6)+1
ax1.bar(x1 - width/2, males_count, width, label="男性",color='seagreen',edgecolor='gray')
ax1.bar(x1 + width/2, females_count, width, label="女性",color='coral',edgecolor='gray')
ax1.legend()
ax1.set_title("不同性別客戶持有銀行金融商品數量", loc='center', size=10)    # 設定標題
ax1.set_xlabel('商品數量', loc='right', size=9)  # x軸命名
ax1.set_ylabel('客戶人數')  # y軸命名

# 2
males_transaction_count=[0]*10     # males_transaction_count= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
females_transaction_count=[0]*10

for value in m:
    males_transaction_count[value[-1]//14]+=1       # 找Total_Trans_Ct的資料,找到就在對應的組+1
for value in f:
    females_transaction_count[value[-1]//14]+=1     # 因為Total_Trans_Ct最大值為139,故//14 讓xticks為10組

x2=np.arange(10)+1  # x2= [ 1  2  3  4  5  6  7  8  9 10]
ax2.bar(x2 - width/2, males_transaction_count, width, label="男性",color='seagreen',edgecolor='gray')
ax2.bar(x2 + width/2, females_transaction_count, width, label="女性",color='coral',edgecolor='gray')
ax2.legend()
ax2.set_title("不同性別客戶過去一年總交易次數", loc='center', size=10)     # 設定標題
ax2.set_xlabel('交易次數', loc='right', size=9)  # x軸命名
ax2.set_ylabel('客戶人數')  # y軸命名
ax2.set_xticks(x2)
labels=[]
for i in range(10):
    labels.append(str(i*14)+"~"+str(i*14+13))       # 設定xtick範圍: 0~13, 14~27...
ax2.set_xticklabels(labels)
ax2.tick_params(axis='both', which='major', labelsize=6)

# 3
males_transaction_amount=[0]*5      # males_transaction_amount=[0, 0, 0, 0, 0]
females_transaction_amount=[0]*5
for value in m:
    males_transaction_amount[value[-2]//4000]+=1    # 找Total_Trans_Amt, 找到就在對應的組+1
for value in f:
    females_transaction_amount[value[-2]//4000]+=1  # 因為Total_Trans_Amt最大值為18484,故//4000 讓xticks為5組

x3=np.arange(5)+1       # x3 = [1 2 3 4 5]
ax3.bar(x3 - width/2, males_transaction_amount, width, label="男性",color='seagreen',edgecolor='gray')
ax3.bar(x3 + width/2, females_transaction_amount, width, label="女性",color='coral',edgecolor='gray')
ax3.legend()
ax3.set_title("不同性別客戶過去一年總交易金額", loc='center', size=10)     # 設定標題
ax3.set_xlabel('交易金額(美元)', loc='right', size=9)  # x軸命名
ax3.set_ylabel('客戶人數')  # y軸命名
ax3.set_xticks(x3)
labels=[]
for i in range(5):
    labels.append(str(i*4000)+"~"+str(i*4000+3999))       # 設定xtick範圍: 0~3999, 4000~7999...
ax3.set_xticklabels(labels)
ax3.tick_params(axis='both', which='major', labelsize=7)

# 4
ax4.pie([len(existing), len(attrited)],labels=['現存客戶','流失客戶'],
        colors=['dodgerblue', 'salmon'],
        autopct='%.2f%%', shadow=True, startangle=90)             # autopct:小數點後幾位, startangle:起始角度(逆時針)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax4.set_title("現存客戶及流失客戶比例圓餅圖", loc='center', size=10)

# 5
ax5.pie([len(below40), len(btw40and60),len(btw60and80), len(btw80and120), len(higher120), len(unknown)],
        labels=['$40K以下', '$40K - $60K', '$60K - $80K', '$80K - $120K', '$120K以上', '未知'],
        autopct='%.2f%%', startangle=90,textprops={'fontsize':8}) # autopct:小數點後幾位, startangle:起始角度(逆時針)
ax5.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circl1e.
ax5.set_title("客戶所得區間圓餅圖", loc='center', size=10)

# 6
Blue=getDataByCard('BankChurners.csv', 'Blue')
Silver=getDataByCard('BankChurners.csv', 'Silver')
Gold=getDataByCard('BankChurners.csv', 'Gold')
Platinum=getDataByCard('BankChurners.csv', 'Platinum')
ax6.pie([len(Blue), len(Silver),len(Gold)+len(Platinum)],
        labels=['藍色級','銀色級','金色級和白金級'],
        colors=['skyblue', 'silver','goldenrod'],
        autopct='%.2f%%', startangle=0,textprops={'fontsize':8},
        explode = (0, 0.2, 0.3))             # autopct:小數點後幾位, startangle:起始角度(逆時針)
ax6.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax6.set_title("客戶信用卡等級比例圓餅圖", loc='center', size=10)

# 7
width = 0.2
married_count=[0]*7
single_count=[0]*7
divorced_count=[0]*7
unknown_count=[0]*7
m=getDataByMaritalStatus('BankChurners.csv', 'Married')
s=getDataByMaritalStatus('BankChurners.csv', 'Single')
d=getDataByMaritalStatus('BankChurners.csv', 'Divorced')
u=getDataByMaritalStatus('BankChurners.csv', 'Unknown')
for value in m:
    married_count[value[-3]]+=1
for value in s:
    single_count[value[-3]]+=1
for value in d:
    divorced_count[value[-3]]+=1
for value in u:
    unknown_count[value[-3]]+=1
married_count=married_count[1:]
single_count=single_count[1:]
divorced_count=divorced_count[1:]
unknown_count=unknown_count[1:]
x1=np.arange(6)+1
ax7.bar(x1 - 3*width/2, married_count, width, label="已婚", color='pink', edgecolor='black')
ax7.bar(x1 - width/2, single_count, width, label="單身", color='lightgreen', edgecolor='black')
ax7.bar(x1 + width/2, divorced_count, width, label="離婚", color='powderblue', edgecolor='black')
ax7.bar(x1 + 3*width/2, unknown_count, width, label="未知", color='gray', edgecolor='black')
ax7.legend(prop={'size': 9})
ax7.set_title("不同婚姻狀態之客戶持有銀行金融商品數量", loc='center', size=10)
ax7.set_xlabel('商品數量', loc='right', size=9)  # x軸命名
ax7.set_ylabel('客戶人數')  # y軸命名

#8
married_count=[0]*10
single_count=[0]*10
divorced_count=[0]*10
unknown_count=[0]*10
for value in m:
    married_count[value[-1]//14]+=1     # 找Total_Trans_Ct的資料,找到就在對應的組+1
for value in s:
    single_count[value[-1]//14]+=1      # 因為Total_Trans_Ct最大值為139,故//14 讓xticks為10組
for value in d:
    divorced_count[value[-1]//14]+=1
for value in u:
    unknown_count[value[-1]//14]+=1
x8=np.arange(10)+1
ax8.bar(x8 - 3*width/2, married_count, width, label="已婚", color='pink', edgecolor='black')
ax8.bar(x8 - width/2, single_count, width, label="單身", color='lightgreen', edgecolor='black')
ax8.bar(x8 + width/2, divorced_count, width, label="離婚", color='powderblue', edgecolor='black')
ax8.bar(x8 + 3*width/2, unknown_count, width, label="未知", color='gray', edgecolor='black')
ax8.legend()
ax8.set_title("不同婚姻狀態之客戶過去一年總交易次數", loc='center', size=10)
ax8.set_xticks(x8)
labels=[]
for i in range(10):
    labels.append(str(i*14)+"~"+str(i*14+13))       # 設定xtick範圍: 0~13, 14~27...
ax8.set_xticklabels(labels)
ax8.tick_params(axis='both', which='major', labelsize=6)
ax8.set_xlabel('交易次數', loc='right', size=9)  # x軸命名
ax8.set_ylabel('客戶人數')  # y軸命名

#9
married_count=[0]*5
single_count=[0]*5
divorced_count=[0]*5
unknown_count=[0]*5
for value in m:
    married_count[value[-2]//4000]+=1        # 找Total_Trans_Amt, 找到就在對應的組+1
for value in s:
    single_count[value[-2]//4000]+=1        # 因為Total_Trans_Amt最大值為18484,故//4000 讓xticks為5組
for value in d:
    divorced_count[value[-2]//4000]+=1
for value in u:
    unknown_count[value[-2]//4000]+=1

x9=np.arange(5)+1
ax9.bar(x9 - 3*width/2, married_count, width, label="已婚", color='pink', edgecolor='black')
ax9.bar(x9 - width/2, single_count, width, label="單身", color='lightgreen', edgecolor='black')
ax9.bar(x9 + width/2, divorced_count, width, label="離婚", color='powderblue', edgecolor='black')
ax9.bar(x9 + 3*width/2, unknown_count, width, label="未知", color='gray', edgecolor='black')
ax9.legend()
ax9.set_title("不同婚姻狀態之客戶過去一年總交易金額", loc='center', size=10)
ax9.set_xticks(x9)
labels=[]
for i in range(5):
    labels.append(str(i*4000)+"~"+str(i*4000+3999))       # 設定xtick範圍: 0~13, 14~27...
ax9.set_xticklabels(labels)
ax9.tick_params(axis='both', which='major', labelsize=7)
ax9.set_xlabel('交易金額(美元)', loc='right', size=9)  # x軸命名
ax9.set_ylabel('客戶人數')  # y軸命名

plt.get_current_fig_manager().window.wm_geometry("+0+0")  # 設定視窗座標位置
plt.show()  # 繪製

