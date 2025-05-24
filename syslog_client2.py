import socket

# QRadar服务器配置
QRadar_IP = '192.168.52.22'
QRadar_PORT = 514

# 构造Syslog消息（RFC5424格式）
# message = '<14>1 %(timestamp)s %(hostname)s %(appname)s - - - This is a raw test log' % {
#     'timestamp': datetime.datetime.utcnow().isoformat() + 'Z',
#     'hostname': socket.gethostname(),
#     'appname': 'MyPythonApp'
# }

message = '<188>Jun 1 2022 02:24:16 HUAWEI %%01IPS/4/DETECT(l):CID=0x814f041e;An intrusion was detected. (SyslogId=1, Vsys="public", Policy="test", SrcIp=6.0.0.3, DstIp=7.0.0.3, SrcPort=5678, DstPort=1025, SrcZone=trust, DstZone=untrust, User="unknown", Protocol=TCP, Application="HTTP", Profile="hwips", SignName="Sun SDK and JRE Applet Sandbox Security Bypass", SignId=19740, EventNum=1, Target=client, Severity=high, Os=all, Category=Other, Reference=CVE-2004-1029, Action=Alert)'

# 发送UDP报文
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(message.encode('utf-8'), (QRadar_IP, QRadar_PORT))
