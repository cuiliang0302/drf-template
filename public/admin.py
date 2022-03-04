from django.contrib import admin
from public.models import UserDemo


# 用户测试信息
class UserDemoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex')
    # 文章列表里显示想要显示的字段
    list_display_links = ('name',)
    # 设置哪些字段可以点击进入编辑界面
    search_fields = ('name',)
    # 搜索字段


admin.site.register(UserDemo, UserDemoAdmin)
