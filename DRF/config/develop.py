# 开发环境配置
import os
from DRF.settings import BASE_DIR
# 静态资源目录
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static")
# ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')