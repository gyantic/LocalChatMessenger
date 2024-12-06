import socket
import os

#UNIXドメインソケットトデータグラムソケット
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

#サーバーアドレス
server_address = './udp_socket_file'

#クライアントアドレス
address = './udp_client_socket_file'

#サーバーに送信するメッセージ(バイト列)
#ユーザーが入力したものをメッセージとする
message = input('Please input your message.\n')
message = message.encode('utf-8')

# このクライアントのアドレスをソケットに紐付けます。
# これはUNIXドメインソケットの場合に限ります。
# このアドレスは、サーバによって送信元アドレスとして受け取られます
sock.bind(address)

try:
  #サーバーにメッセージ送る
  print('sending {!r}'.format(message))
  sent = sock.sendto(message, server_address)

  #サーバーからの応答を待つ
  print('waiting to receive')

  data, server = sock.recvfrom(4096)
  print('received {!r}'.format(data.decode('utf-8')))

finally:
  #最後にソケット閉じて、リソースを解法
  print('closing socket')
  sock.close()
  # クライアントソケットファイルの削除
  try:
    os.unlink(address)
  except FileNotFoundError:
    pass
