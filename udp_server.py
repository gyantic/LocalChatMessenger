import socket
import os
from faker import Faker
#Faker:ダミーデータの生成

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = './udp_socket_file' #現在のディレクトリにソケットファイルのパス設定

fake = Faker('ja-JP') #Facker()のインスタンス、日本語対応させた。

print('starting up on {}'.format(server_address))

sock.bind(server_address)

try:
  while True:
    print('\nwaiting to receive message')

    data, address = sock.recvfrom(4096) #4096バイトまでのデータを受信
    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
      response_text = fake.name()
      #バイト列にメッセージを変換
      response_text = response_text.encode('utf-8')
      sent = sock.sendto(response_text, address)
      # 送信したバイト数と送信先のアドレスを表示
      print('sent {} bytes back to {}'.format(sent, address))

except KeyboardInterrupt:
  print('\nServer is shutting down.')

finally:
  # ソケットを閉じてソケットファイルを削除
  print('closing socket')
  sock.close()
  #サーバーソケットファイルを削除
  try:
    os.unlink(address)
  except FileNotFoundError:
    pass
