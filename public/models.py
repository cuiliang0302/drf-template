from django.db import models


# 性别枚举类型
class Sex(models.TextChoices):
    men = '1', '男'
    women = '2', '女'


# 友情链接
class UserDemo(models.Model):
    name = models.CharField('名称', max_length=25)
    sex = models.CharField(verbose_name='性别', max_length=1, choices=Sex.choices, default=Sex.men)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户测试'
        verbose_name_plural = '用户测试'
