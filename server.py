import socket

def start_udp_server(host='0.0.0.0', port=1024):
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
      s.bind((host, port))
      print(f"UDP Server listening on {host}:{port}")

      while True:
        data, addr = s.recvfrom(1024)
        message = data.decode('utf-8')
        print(f"Received from {addr}: {message}")
        s.sendto(b"UDP Message received!", addr)
  except KeyboardInterrupt:
    print(" Server stopped.")


if __name__ == "__main__":
  start_udp_server()

