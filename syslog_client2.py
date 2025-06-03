import socket
import time

print("syslog client2 send start.")
# QRadar服务器配置
QRadar_IP = '192.168.137.22'
QRadar_PORT = 514

# 构造Syslog消息（RFC5424格式）
# message = '<14>1 %(timestamp)s %(hostname)s %(appname)s - - - This is a raw test log' % {
#     'timestamp': datetime.datetime.utcnow().isoformat() + 'Z',
#     'hostname': socket.gethostname(),
#     'appname': 'MyPythonApp'
# }

message = '<188>Jun 1 2022 02:24:16 HUAWEI %%01IPS/4/DETECT(l):CID=0x814f041e;An intrusion was detected. (SyslogId=1, Vsys="public", Policy="test", SrcIp=6.0.0.2, DstIp=7.0.0.2, SrcPort=5678, DstPort=1025, SrcZone=trust, DstZone=untrust, User="unknown", Protocol=TCP, Application="HTTP", Profile="hwips", SignName="Sun SDK and JRE Applet Sandbox Security Bypass", SignId=19740, EventNum=1, Target=client, Severity=high, Os=all, Category=Other, Reference=CVE-2004-1029, Action=Alert)'

message2 = '<188>Jun 1 2022 02:24:16 HUAWEI %%01IPS/4/DETECT(l):CID=0x814f041e;An intrusion was detected. (SyslogId=1, Vsys="public", Policy="test", SrcIp=6.0.0.3, DstIp=7.0.0.3, SrcPort=5678, DstPort=1025, SrcZone=trust, DstZone=untrust, User="unknown", Protocol=TCP, Application="HTTP", Profile="hwips", SignName="Sun SDK and JRE Applet Sandbox Security Bypass", SignId=19740, EventNum=1, Target=client, Severity=high, Os=all, Category=Other, Reference=CVE-2004-1029, Action=Alert)'

# 发送UDP报文
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
  while True:
    sock.sendto(message.encode('utf-8'), (QRadar_IP, QRadar_PORT))
    sock.sendto(message2.encode('utf-8'), (QRadar_IP, QRadar_PORT))
    print(f"sendto QRadar_IP: {QRadar_IP}, QRadar_PORT: {QRadar_PORT}")
    time.sleep(1)   # 暂停1秒
except KeyboardInterrupt:
  print("定时器已停止")


print("syslog client2 send ok.")
