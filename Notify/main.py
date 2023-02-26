#インポート
from tkinter import messagebox
from tkinter import filedialog
import tkinter.ttk as ttk
import requests
import tkinter
import json
import sys
import os

#必要な情報を変数に代入
url = 'https://notify-api.line.me/api/notify'

MyToken = 'Jrb3iT6GH1JNwLIHindsyQ9PgBAKTFblfkvtk4p1hmD'
Osyaberikai = 'T01hlGkUjXSB3xmMwm4KB9h4Wmg5tf1wVaOStInbW5q'

#Tikinterの基本設定
root = tkinter.Tk()
root.title(u"LINE送信パネル(Notify)")
root.geometry("310x115")
root.resizable(0,0)

#ファンクションプログラム
def main(event):
    if EditBox1.get() == "自分":
        TOKEN = 'Jrb3iT6GH1JNwLIHindsyQ9PgBAKTFblfkvtk4p1hmD'
    elif EditBox1.get() == "おしゃべり会":
        TOKEN = 'T01hlGkUjXSB3xmMwm4KB9h4Wmg5tf1wVaOStInbW5q'
    elif EditBox1.get() == "電話グループ":
        TOKEN = "AYB8PfeQ7Qw895MmTPL59wv4egSJlFFaNF1po0BHz5k"
    
    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    send_dic = {'message': EditBox2.get()}
    requests.post(url, headers=TOKEN_dic, data=send_dic)
    EditBox2.delete(0,tkinter.END)

#UI
Static1 = tkinter.Label(text=u'誰に送信しますか？')
Static1.pack()

EditBox1 = tkinter.Entry(width=50)
EditBox1.pack()

border1=ttk.Separator(root,orient="horizontal")
border1.pack(fill="both")

Static2 = tkinter.Label(text=u'内容')
Static2.pack()

EditBox2 = tkinter.Entry(width=50)
EditBox2.pack()

border2=ttk.Separator(root,orient="horizontal")
border2.pack(fill="both")

Button = tkinter.Button(text=u'文字を送る。',width=40)
Button.bind("<Button-1>",main) 
Button.pack()

root.mainloop()