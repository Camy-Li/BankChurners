"""
Description: 將csv檔讀進來,可透過 新增,修改,刪除,儲存 產生新的csv檔
             並呼叫bank_churners_graph_analytics.py檔,產生圖表
Date:2022/05/18
Data: 'BankChurners-updated.csv'
      'BankChurners.csv'
      'bank_churners_graph_analytics.py'
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
import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv
import tkinter.messagebox as tkMessageBox

file_name = 'BankChurners-updated.csv'

win = tk.Tk()
win.wm_title("銀行客戶資料庫")
win.minsize(width=1050, height=550)  # 最小的視窗
win.maxsize(width=1200, height=700)  # 最大的視窗
win.resizable(1,1)   # 是否可以調整 0為False

#加入menu bar
menu_bar = tk.Menu(win)
file_menu = tk.Menu(menu_bar)            # 建立第一個下拉選單
file_menu.add_command(label="exit",command=exit)  # 建立 file_menu 裡有 'exit'
menu_bar.add_cascade(label="File", menu=file_menu)      # 把file_munu加進bar, 命名File
win.config(menu=menu_bar)                               # 要加這行 一整排bar才會顯示

# 建立labelframe1 客戶基本資料
labelframe1 = ttk.LabelFrame(win, text='客戶基本資料')   # 建立一個客戶資料的 label frame 物件
labelframe1.place(x=10,y=20,width=400,height=150)
label1 =tk.Label(labelframe1,text="編號：")       # 建立'編號'label
label1.place(x=0,y=0)
label2 =tk.Label(labelframe1,text="年齡：")       # 建立'年齡'label
label2.place(x=0,y=30)
label3 =tk.Label(labelframe1,text="性別：")       # 建立'性別'label
label3.place(x=0,y=60)
label4 =tk.Label(labelframe1,text="扶養人數：")    # 建立'扶養人數'label
label4.place(x=0,y=90)
label5 =tk.Label(labelframe1,text="教育程度：")    # 建立'教育程度'label
label5.place(x=180,y=0)
label6 =tk.Label(labelframe1,text="婚姻狀態：")    # 建立'婚姻狀態'label
label6.place(x=180,y=30)
label7 =tk.Label(labelframe1,text="年收入：")      # 建立'年收入'label
label7.place(x=180,y=60)
label8 =tk.Label(labelframe1,text="卡別：")        # 建立'卡別'label
label8.place(x=180,y=90)

# 建立 labelframe3 客戶往來數據
labelframe3 = ttk.LabelFrame(win, text='客戶往來數據')   # 建立一個labelframe: 客戶往來數據
labelframe3.place(x=580,y=20,width=200,height=150)
label9 =tk.Label(labelframe3,text="入籍期間 (月)：") # 建立'入籍期間(月)'label
label9.place(x=10,y=0)
label10 =tk.Label(labelframe3,text="持有商品數：")   # 建立'持有商品數'label
label10.place(x=10,y=30)
label11 =tk.Label(labelframe3,text="年交易量：")    # 建立'年交易量'label
label11.place(x=10,y=60)
label12 =tk.Label(labelframe3,text="年交易次數：")    # 建立'年交易次數'label
label12.place(x=10,y=90)

# 7個SpinBox:Client_no, age, dependent, months_on_book, relationship_Count,trans_amt, trans_ct
spinbox_value1 = tk.StringVar(value=0)       # 對應'編號'
spin_box1 = tk.Spinbox(labelframe1,from_=0,to=999999999,textvariable=spinbox_value1)
spin_box1.place(x=40,y=0,width=100)
spinbox_value2 = tk.StringVar(value=0)       # 對應'年齡'
spin_box2 = tk.Spinbox(labelframe1,from_=0,to=150,textvariable=spinbox_value2)
spin_box2.place(x=40,y=30,width=100)
spinbox_value3 = tk.StringVar(value=0)       # 對應'扶養人數'
spin_box3 = tk.Spinbox(labelframe1,from_=0,to=15,textvariable=spinbox_value3, state='readonly')
spin_box3.place(x=70,y=90,width=100)
spinbox_value4 = tk.StringVar(value=0)       # 對應'入籍期間(月)'
spin_box4 = tk.Spinbox(labelframe3,from_=0,to=100,textvariable=spinbox_value4)
spin_box4.place(x=130,y=0,width=60)
spinbox_value5 = tk.StringVar(value=0)       # 對應'持有商品數'
spin_box5 = tk.Spinbox(labelframe3,from_=0,to=6,textvariable=spinbox_value5)
spin_box5.place(x=130,y=30,width=60)
spinbox_value6 = tk.StringVar(value=0)       # 對應'年交易量'
spin_box6 = tk.Spinbox(labelframe3,from_=0,to=99999,textvariable=spinbox_value6)
spin_box6.place(x=130,y=60,width=60)
spinbox_value7 = tk.StringVar(value=0)       # 對應'年交易次數'
spin_box7 = tk.Spinbox(labelframe3,from_=0,to=200,textvariable=spinbox_value7)
spin_box7.place(x=130,y=90,width=60)

# 2個 radiobutton: gender, attrition(建立在labelframe2裡面)
rdbt1 = tk.StringVar(value='M')        # 設定初始值為'M'
rdbt_m = tk.Radiobutton(labelframe1, text='M',variable=rdbt1, value='M')
rdbt_f = tk.Radiobutton(labelframe1, text='F',variable=rdbt1, value='F')
rdbt_m.place(x=40,y=60)
rdbt_f.place(x=80,y=60)

labelframe2 = ttk.LabelFrame(win, text='客戶狀態:')   # 建立一個labelframe: 客戶狀態
labelframe2.place(x=420,y=20,width=150,height=150)
rdbt2 = tk.StringVar(value='Existing Customer')     # 多選一的元件 Radiobutton 的變數,初始值'Existing Customer'
rdbt_exist = tk.Radiobutton(labelframe2, text='Existing Customer',variable=rdbt2, value='Existing Customer')
rdbt_attrited = tk.Radiobutton(labelframe2, text='Attrited Customer',variable=rdbt2, value='Attrited Customer')
rdbt_exist.pack()
rdbt_attrited.pack()

# 4個 combobox下拉式選單: edu, marital, income, card
cbb1 = tk.StringVar()                           # 對應 教育程度
cbb_edu = ttk.Combobox(labelframe1, width=15, textvariable=cbb1, state='readonly')
cbb_edu['values'] = ('High School','College','Graduate','Post-Graduate','Doctorate','Uneducated','Unknown','Other') # Add drop down list
cbb_edu.place(x=250,y=0)
cbb2 = tk.StringVar()                           # 對應 婚姻狀態
cbb_marital = ttk.Combobox(labelframe1, width=15, textvariable=cbb2, state='readonly')
cbb_marital['values'] = ('Married','Single','Divorced','Unknown')  # Add drop down list
cbb_marital.place(x=250,y=30)
cbb3 = tk.StringVar()                           # 對應 年收入
cbb_income = ttk.Combobox(labelframe1, width=15, textvariable=cbb3, state='readonly')
cbb_income['values'] = ('Less than $40K','$40K - $60K','$60K - $80K','$80K - $120K','$120K +')  # Add drop down list
cbb_income.place(x=250,y=60)
cbb4 = tk.StringVar()                           # 對應 卡別
cbb_card = ttk.Combobox(labelframe1, width=15, textvariable=cbb4, state='readonly')
cbb_card['values'] = ('Blue','Silver','Gold','Platinum')  # Add drop down list
cbb_card.place(x=250,y=90)

# tree 列表
columns = ('編號','客戶狀態', '年齡','性別','扶養人數',"教育程度",'婚姻狀態','年收入','卡別',
           '入籍期間','持有商品數','年交易量','年交易次數','')    #最後一筆為空白column,為了scrollbar空間需要
tree = ttk.Treeview(win, columns=columns, show='headings',height=13)
tree.place(x=10,y=220)
tree.bind('<Motion>', 'break')      # tree heading not resizable
tree.heading('編號', text='編號')
tree.column("#1",width=80, anchor=CENTER)
tree.heading('客戶狀態', text='客戶狀態')
tree.column("#2",width=110, anchor=CENTER)
tree.heading('年齡', text='年齡')
tree.column("#3",width=40, anchor=CENTER)
tree.heading('性別', text='性別')
tree.column("#4",width=40, anchor=CENTER)
tree.heading('扶養人數', text='撫養人數')
tree.column("#5",width=60, anchor=CENTER)
tree.heading('教育程度', text='教育程度')
tree.column("#6",width=100, anchor=CENTER)
tree.heading('婚姻狀態', text='婚姻狀態')
tree.column("#7",width=100, anchor=CENTER)
tree.heading('年收入', text='年收入')
tree.column("#8",width=120, anchor=CENTER)
tree.heading('卡別', text='卡別')
tree.column("#9",width=60, anchor=CENTER)
tree.heading('入籍期間', text='入籍期間')
tree.column("#10",width=70, anchor=CENTER)
tree.heading('持有商品數', text='持有商品數')
tree.column("#11",width=70, anchor=CENTER)
tree.heading('年交易量', text='年交易量')
tree.column("#12",width=70, anchor=CENTER)
tree.heading('年交易次數', text='年交易次數')
tree.column("#13",width=70, anchor=CENTER)
tree.heading('', text='')
tree.column("#14",width=20, anchor=CENTER)

# scrollbars
vertical_scrollbar = Scrollbar(tree, orient="vertical", command=tree.yview)
vertical_scrollbar.place(relx=0.978, rely=0.01, relheight=0.98, relwidth=0.021)
tree.configure(yscrollcommand=vertical_scrollbar.set)

#讀進csv檔的資料
def getData(fileName):
    with open(fileName, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data

data=getData(file_name)[1:]
for value in data:
    tree.insert('',tk.END,values=value)

def item_selected(event):       # 把tree列表中的資料放入對應的輸入框中
    selected_items = tree.selection()
    if len(selected_items) == 0:
        return
    selected_item = selected_items[0]
    item = tree.item(selected_item)       # 選取的值 資料放在item['values']
    record = item['values']

    spinbox_value1.set(record[0])         # 將選取的record每個項目 放進對應的輸入框中
    rdbt2.set(record[1])
    spinbox_value2.set(record[2])
    rdbt1.set(record[3])
    spinbox_value3.set(record[4])
    cbb1.set(record[5])
    cbb2.set(record[6])
    cbb3.set(record[7])
    cbb4.set(record[8])
    spinbox_value4.set(record[9])
    spinbox_value5.set(record[10])
    spinbox_value6.set(record[11])
    spinbox_value7.set(record[12])

# 新增客戶資料
def addRecord():
    record = [spinbox_value1.get(),
                     rdbt2.get(),
                     spinbox_value2.get(),
                     rdbt1.get(),
                     spinbox_value3.get(),
                     cbb1.get(),
                     cbb2.get(),
                     cbb3.get(),
                     cbb4.get(),
                     spinbox_value4.get(),
                     spinbox_value5.get(),
                     spinbox_value6.get(),
                     spinbox_value7.get()]
    tree.insert('',tk.END,values=record)
    print("已添加此筆資料")
button_input = tk.Button(win, text="添加此筆資料",command=addRecord) # 建立 添加此筆資料的按鈕
button_input.place(x=850,y=20)

# 刪除客戶資料
def deleteRecord():
    if len(tree.selection()) == 0:                            # 若未選取資料
        tkMessageBox.showerror("操作錯誤", "請先選取要刪除的資料")  # 跳出錯誤視窗
    else:
        for selected_item in tree.selection():
            tree.delete(selected_item)
        print("已刪除資料")

button_del = tk.Button(win, text="刪除此筆資料",command=deleteRecord)  # 建立 刪除按鈕
button_del.place(x=850,y=50)

# 修改客戶資料
def modifyRecord():                                   # 定義修改所選資料的功能
    record = [spinbox_value1.get(),
                     rdbt2.get(),
                     spinbox_value2.get(),
                     rdbt1.get(),
                     spinbox_value3.get(),
                     cbb1.get(),
                     cbb2.get(),
                     cbb3.get(),
                     cbb4.get(),
                     spinbox_value4.get(),
                     spinbox_value5.get(),
                     spinbox_value6.get(),
                     spinbox_value7.get()]
    if len(tree.selection())==1:            # 選取的筆數為1筆,不能一次修改多筆
        selected_item = tree.selection()[0]
        tree.item(selected_item,values=record)
        print("已修改此筆資料")
    else:
        tkMessageBox.showerror("操作錯誤", "請選擇一筆要修改的資料")  # 錯誤視窗

button_modify = tk.Button(win, text="修改此筆資料",command=modifyRecord)  # 建立 修改按鈕
button_modify.place(x=850,y=85)

# 儲存檔案
def saveRecords():
    header = [
        "CLIENTNUM","Attrition_Flag","Customer_Age","Gender","Dependent_count",
        "Education_Level","Marital_Status","Income_Category","Card_Category","Months_on_book",
        "Total_Relationship_Count","Total_Trans_Amt","Total_Trans_Ct"
    ]

    item_ids = tree.get_children()          # get.children(): 取得每筆資料的id
    items=[]
    for child in item_ids:
        items.append(tree.item(child)["values"])     # 透過id,取得每筆資料的值

    with open(file_name, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(items)
    print("已儲存檔案")

button_save = tk.Button(win, text="儲存當前檔案",command=saveRecords)  # 建立 儲存按鈕
button_save.place(x=850,y=120)

# 產生圖表
import subprocess
def showPlots():
    t=subprocess.run(["python", "bank_churners_graph_analytics.py"]) # 呼叫另一個py檔
button_plot = tk.Button(win, text="產生統計圖表",command=showPlots)  # 建立 產生統計圖表 按鈕
button_plot.place(x=850,y=155)

# 設定 年齡 輸入限制
def validate(user_input):
    # check if the input is numeric
    while len(user_input)>1 and user_input[0]=="0":
        return False
    if user_input.isdigit():
        # Fetching minimum and maximum value of the spinbox
        minval = int(labelframe1.nametowidget(spin_box2).config('from')[4])
        maxval = int(labelframe1.nametowidget(spin_box2).config('to')[4])
        # check if the number is within the range
        if int(user_input) not in range(minval, maxval+1):
            print("Out of range")
            return False
        # Printing the user input to the console
        return True
    # if input is blank string
    elif user_input == "":
        print(user_input)
        return True
    # return false is input is not numeric
    else:
        print("Not numeric")
        return False

range_validation = labelframe1.register(validate)
spin_box2.config(validate="key",validatecommand=(range_validation, '%P'))

tree.bind('<<TreeviewSelect>>', item_selected)   # 連結到所選物件

win.geometry("1050x550+250+100")    # 設定視窗座標位置
win.mainloop()                      # 最後：程式做無限循環