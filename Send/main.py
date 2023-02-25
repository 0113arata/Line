#インポート
from tkinter import filedialog
from tkinter import messagebox
import requests, json
import sys
import tkinter
import tkinter.ttk as ttk
from linebot import LineBotApi
from linebot.models import TextSendMessage

#Tikinterの基本設定
root = tkinter.Tk()
root.title(u"LINE送信パネル")
root.geometry("310x150")
root.resizable(0,0)

#ファンクションプログラム
def main(event):
    value = EditBox1.get()
    #作者のUserIDは"U3f694234eb3d4a5feba203c28284f1bf"です。
    user_id = EditBox2.get()
    #作者のトークンは"V8mKR62V0YtYk1ESTzFlmNGdAVkNo+EQEBQgmhyscrOYS5PNd4ai/yXP6E7zcAgVS3vZ+cF+TyfrpwZWduL6hudy+vSrhq8qadl1Nm8OAaxNZoTOA6vUrSHxIy0EeZqr+wNx1FxEBHurgSXTCtB84wdB04t89/1O/w1cDnyilFU="です。
    YOUR_CHANNEL_ACCESS_TOKEN = EditBox3.get()
    line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
    #送信設定
    messages = TextSendMessage(text=value)
    line_bot_api.push_message(user_id, messages=messages)
    EditBox1.delete(0, tkinter.END)
    messagebox.showinfo('LINE送信パネル','送信しました。')

def File(event):
    #ファイル参照
    FileType = [('Jsonファイル','*.json')] 
    Dir = 'C:/'
    File = filedialog.askopenfilename(filetypes = FileType, initialdir = Dir) 
    json_open = open(File,'r')
    json_load = json.load(json_open)
    UserID = json_load['UserID']['key']
    Token = json_load['Token']['key']
    print("UserID: " + UserID)
    print("Token: " + Token)

#UI
EditBox1 = tkinter.Entry(width=50)
EditBox1.pack()

border1=ttk.Separator(root,orient="horizontal")
border1.pack(fill="both")

EditBox2 = tkinter.Entry(width=50)
EditBox2.pack()

border2=ttk.Separator(root,orient="horizontal")
border2.pack(fill="both")

EditBox3 = tkinter.Entry(width=50)
EditBox3.pack()

border3=ttk.Separator(root,orient="horizontal")
border3.pack(fill="both")

Button = tkinter.Button(text=u'送信（上からメッセージ、ユーザーID、トークンの順に入れる。）',width=50)
Button.bind("<Button-1>",main) 
Button.pack()

Button2 = tkinter.Button(text=u'保存しているファイルを開く',width=50)
Button2.bind("<Button-1>",File) 
Button2.pack()

root.mainloop()