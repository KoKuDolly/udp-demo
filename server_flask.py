from flask import Flask
import socket
import threading
from datetime import datetime

app = Flask(__name__)

# 存储接收到的日志
syslog_messages = []

def udp_server():
    # 创建 UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 绑定到所有接口的 514 端口（标准 Syslog 端口）
    server_address = ('0.0.0.0', 514)
    sock.bind(server_address)
    
    print(f"Starting UDP syslog server on {server_address}")
    
    while True:
        data, address = sock.recvfrom(4096)
        message = data.decode('utf-8', errors='replace')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        syslog_messages.append({
            'timestamp': timestamp,
            'source': address[0],
            'message': message
        })
        print(f"Received syslog from {address}: {message}")

@app.route('/logs')
def show_logs():
    # 显示接收到的日志
    return {
        'logs': syslog_messages,
        'count': len(syslog_messages)
    }

if __name__ == '__main__':
    # 启动 UDP 服务器线程
    udp_thread = threading.Thread(target=udp_server)
    udp_thread.daemon = True  # 设置为守护线程，主程序退出时自动结束
    udp_thread.start()
    
    # 启动 Flask 应用
    app.run(host='0.0.0.0', port=5000, debug=True)
