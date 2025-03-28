import socket
import time

def high_frequency_loop(cb, target_frequency=10):
  target_interval = 1.0 / target_frequency
  loop_count = 0
  last_time = time.perf_counter()

  try:
    while True:
      start_time = time.perf_counter()
      loop_count += 1
      elapsed = time.perf_counter() - start_time
      sleep_time = target_interval - elapsed
      if sleep_time > 0:
        time.sleep(sleep_time)
      if time.perf_counter() - last_time >= 1.0:
        actual_frequency = loop_count / (time.perf_counter() - last_time)
        print(f"目标频率：{target_frequency} Hz，实际频率：{actual_frequency:.2f} Hz")
        loop_count = 0
        last_time = time.perf_counter()
      cb()
  except KeyboardInterrupt:
    print("循环已停止")


def send_udp_message(message, host='127.0.0.1', port=1024):
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # def a():
    #   s.sendto(message.encode('utf-8'), (host, port))

    # high_frequency_loop(a, 1000)
    high_frequency_loop(lambda : s.sendto(message.encode('utf-8'), (host, port)), 1)


if __name__ == "__main__":
  send_udp_message("Hello, UDP Server.")
