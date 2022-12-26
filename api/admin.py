from django.contrib import admin
from api.models import UserDemo


# 用户测试信息
@admin.register(UserDemo)
class UserDemoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gender')
    # 文章列表里显示想要显示的字段
    list_display_links = ('name',)
    # 设置哪些字段可以点击进入编辑界面
    search_fields = ('name',)
    # 搜索字段
