from django.db import models


# 性别枚举类型
class Gender(models.IntegerChoices):
    man = 1, '男'
    woman = 2, '女'
    secrecy = 0, '保密'


# 用户测试
class UserDemo(models.Model):
    name = models.CharField('姓名', max_length=25)
    age = models.IntegerField('年龄')
    gender = models.IntegerField(verbose_name='性别', choices=Gender.choices, default=Gender.secrecy)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户测试'
        verbose_name_plural = '用户测试'
