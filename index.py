from tkinter import *
from tkinter import messagebox
import mysql.connector

# 链接数据库
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",      # 数据库主机地址
            user="root",           # 数据库用户名
            password="asdfghjkl", # 数据库密码
            database="sn_mysql" # 使用的数据库名
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("数据库连接错误", f"无法连接到数据库：{err}")
        return None

# 登入功能
def login():
    conn = connect_db()


# 注册功能
def sign_up():
    swindow = Toplevel(root)
    swindow.title("注册界面")
    swindow.geometry("300x150")
    swindow.resizable(False, False)

    f3 = Frame(swindow)
    f3.pack(pady=30)
    f4 = Frame(swindow)
    f4.pack()

    # 输入框
    l1 = Label(f3,text="username")
    l1.pack(side=LEFT)
    l2 = Label(f4,text="password")
    l2.pack(side=LEFT)

    e1 = Entry(f3)
    e1.pack(side=TOP)
    e2 = Entry(f4, show="*")
    e2.pack(side=TOP)


# 创建主窗口
root = Tk()

root.title('登入界面')
root.geometry('315x415')
root.resizable(False, False)#不能自由拉伸界面，我不想:)

# 容器
f1 = Frame(root)
f1.pack(pady=40)
f2 = Frame(root)
f2.pack()

# 输入框
l1 = Label(f1,text="用户名")
l1.pack(side=LEFT)
l2 = Label(f2,text="密码")
l2.pack(side=LEFT)

e1 = Entry(f1)
e1.pack(side=TOP)
e2 = Entry(f2, show="*")
e2.pack(side=TOP)

#创建按钮
b1 = Button(root, text="log in", width=18,)
b1.place(x=100, y=225)


b2 = Button(root, text="sign up",command=sign_up, width=18,)
b2.place(x=100, y=275)

mainloop()# 也可以使用while True:root.upadte()
