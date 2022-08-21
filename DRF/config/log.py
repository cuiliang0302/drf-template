import os.path
from pathlib import Path
from loguru import logger

LOG_DIR = os.path.join(Path(__file__).resolve().parent.parent.parent, 'logs')
debug_log = os.path.join(LOG_DIR, "debug.log")
info_log = os.path.join(LOG_DIR, "info.log")
error_log = os.path.join(LOG_DIR, "error.log")
# logger配置
config = {
    "rotation": "00:00",  # 每天00点生成新文件
    "encoding": "utf-8",
    "retention": "7 days",  # 日志保留天数
    "backtrace": True,  # 错误堆栈日志
    "diagnose": True
}
# logger打印sql
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': debug_log
#         }
#     },
#     'loggers': {
#         # 'django.db.backends': {  # Django sql操作
#         #     'handlers': ['console', 'file'],
#         #     'propagate': True,
#         #     'level': 'DEBUG',
#         # },
#         "django.server": {  # 由RunServer命令调用的服务器所接收的请求的处理相关的日志消息
#             "handlers": ['file'],
#             "propagate": True,  # 向不向更高级别的logger传递
#             "level": "DEBUG",
#         },
#     }
# }
logger.add(info_log, level='INFO', **config)
logger.add(error_log, level='ERROR', **config)
