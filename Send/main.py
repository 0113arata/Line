#インポート
from linebot.models import TextSendMessage
from linebot import LineBotApi
from tkinter import filedialog
from tkinter import messagebox
import tkinter.ttk as ttk
import requests
import tkinter
import json
import sys
import os

#Tikinterの基本設定
root = tkinter.Tk()
root.title(u"LINE送信パネル")
root.geometry("310x210")
root.resizable(0,0)

#ファンクションプログラム
def main():
    accesstoken = LineBotApi(EditBox3.get())
    user_id = EditBox2.get()
    messages = TextSendMessage(text=EditBox1.get())
    accesstoken.push_message(user_id, messages)

def File(event):
    json_open = open('Deta.json', 'r')
    json_load = json.load(json_open)
    Token = json_load['Token']['key']
    UserID =  json_load['UserID']['key']
    EditBox2.delete(0)
    EditBox3.delete(0)
    EditBox2.insert(0,UserID)
    EditBox3.insert(0,Token)
    messagebox.showinfo("LINE送信パネル","ユーザーID、アクセストークンを読み込みました。")

def Save(event):
    Token = EditBox3.get()
    UserID = EditBox2.get()
    with open('Deta.json', 'w') as SaveFile:
        print('', file=SaveFile)
        print('{"Token":{"key":"' + Token + '"},"UserID":{"key":"' + UserID + '"}}', file=SaveFile)
    messagebox.showinfo("LINE送信パネル","ユーザーID、アクセストークンを保存しました。")

#UI
Static1 = tkinter.Label(text=u'メッセージ内容')
Static1.pack()

EditBox1 = tkinter.Entry(width=50)
EditBox1.pack()

border1=ttk.Separator(root,orient="horizontal")
border1.pack(fill="both")

Static2 = tkinter.Label(text=u'宛先（ユーザーID経由）')
Static2.pack()

EditBox2 = tkinter.Entry(width=50)
EditBox2.pack()

border2=ttk.Separator(root,orient="horizontal")
border2.pack(fill="both")

Static1 = tkinter.Label(text=u'チャネルアクセストークン')
Static1.pack()

EditBox3 = tkinter.Entry(width=50)
EditBox3.pack()

border3=ttk.Separator(root,orient="horizontal")
border3.pack(fill="both")

Button = tkinter.Button(text=u'LINEを送る。',width=40)
Button.bind("<Button-1>",main) 
Button.pack()

Button2 = tkinter.Button(text=u'ファイルを開く',width=40)
Button2.bind("<Button-1>",File) 
Button2.pack()

Button2 = tkinter.Button(text=u'保存する',width=40)
Button2.bind("<Button-1>",Save) 
Button2.pack()

root.mainloop()