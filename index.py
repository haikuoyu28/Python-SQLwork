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
    if conn is not None:
        cursor = conn.cursor()
        username = e1.get()
        password = e2.get()

        try:
            query = "SELECT * FROM sn_id WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("登录成功", "欢迎回来！")
            else:
                messagebox.showerror("登录失败", "用户名或密码错误")
        except mysql.connector.Error as err:
            messagebox.showerror("数据库查询错误", f"发生错误：{err}")
        finally:
            cursor.close()
            conn.close()


# 注册功能
def sign_up():
    def register_user():
        conn = connect_db()
        if conn is not None:
            cursor = conn.cursor()
            username = e1.get()
            password = e2.get()

            try:
                query = "INSERT INTO sn_id (username, password) VALUES (%s, %s)"
                cursor.execute(query, (username, password))
                conn.commit()
                messagebox.showinfo("注册成功", "用户已注册！")
                swindow.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("注册失败", f"发生错误：{err}")
            finally:
                cursor.close()
                conn.close()

    swindow = Toplevel(root)
    swindow.title("注册界面")
    swindow.geometry("300x150")
    swindow.resizable(False, False)

    f3 = Frame(swindow)
    f3.pack(pady=20)
    f4 = Frame(swindow)
    f4.pack()

    # 输入框
    l3 = Label(f3,text="username")
    l3.pack(side=LEFT)
    l4 = Label(f4,text="password")
    l4.pack(side=LEFT)

    e3 = Entry(f3)
    e3.pack(side=TOP)
    e4 = Entry(f4, show="*")
    e4.pack(side=TOP)

    b = Button(swindow, text="注册", command=register_user,width=10)
    b.pack(pady=10)
    

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
