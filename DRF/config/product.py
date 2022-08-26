# 生产环境配置
import os
from DRF.settings import BASE_DIR, env

# 设置redis作为django的缓存设置
CACHES = {
    'default': env.cache(),
}
# 设置redis存储django的session信息
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
# DRF缓存扩展配置
REST_FRAMEWORK_EXTENSIONS = {
    # 默认缓存时间
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 3600,
    # 缓存存储
    'DEFAULT_USE_CACHE': 'default'
}
# 指定样式收集目录
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
