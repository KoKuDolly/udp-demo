import logging
from logging.handlers import SysLogHandler

# QRadar服务器配置
QRadar_IP = '192.168.52.22'  # 替换为实际IP
QRadar_PORT = 514            # 替换为实际端口

# 配置Logger
logger = logging.getLogger('QRadarLogger')
logger.setLevel(logging.INFO)

# 配置Syslog Handler（默认使用UDP）
handler = SysLogHandler(address=(QRadar_IP, QRadar_PORT))
logger.addHandler(handler)

# 发送日志
logger.info('This is a test log message from WSL Python.')