import requests

TOKEN = 'Jrb3iT6GH1JNwLIHindsyQ9PgBAKTFblfkvtk4p1hmD'
api_url = 'https://notify-api.line.me/api/notify'


send_contents = 'キノコード'

#情報を辞書型にする
TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN} 
send_dic = {'message': send_contents}
print(TOKEN_dic)
print(send_dic)

#LINE通知を送る（200: 成功時、400: リクエストが不正、401: アクセストークンが無効：公式より）
requests.post(api_url, headers=TOKEN_dic, data=send_dic)


#画像ファイルのパスを指定
image_file = './test.png'
#バイナリデータで読み込む
binary = open(image_file, mode='rb')
#指定の辞書型にする
image_dic = {'imageFile': binary}
#LINEに画像とメッセージを送る
requests.post(api_url, headers=TOKEN_dic, data=send_dic, files=image_dic)