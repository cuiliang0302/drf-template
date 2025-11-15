from rest_framework import serializers
from api.models import UserDemo
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    自定义jwt认证序列化器
    """

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['token'] = str(refresh.access_token)
        data['username'] = self.user.username
        data['id'] = self.user.id
        data.pop('refresh')
        data.pop('access')
        return data


class UserDemoSerializer(serializers.ModelSerializer):
    """
    用户信息序列化器
    """
    # 枚举类型字段显示（性别显示文字）
    sex_name = serializers.ReadOnlyField(source='get_sex_display')

    # 模型关联外键字段显示（获取外键文章分类id和name）
    # category = serializers.CharField(read_only=True)
    # category_id = serializers.IntegerField()
    # 多对多序列化器方法（获取资源类型多对多信息）
    # kinds_list = KindSerializer(many=True, source='kinds')
    # 自定义序列化器方法（计算使用年限）
    # tags = serializers.SerializerMethodField(）
    # 附加额外只读字段（用户名只读）
    # username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserDemo
        fields = "__all__"

    # 自定义序列化器（计算使用年限）
    # def get_age(self, obj):
    #     return round((now().date() - obj.date).days / 365.25, 1)

    # 自定义校验方法
    # def validate(self, attrs):
    #     phone = attrs.get('phone')
    #     if re.match('^1[0-9]\d{9}$', phone):
    #         # 手机号正则
    #         return attrs
    #     else:
    #         raise serializers.ValidationError('手机号格式错误')

    # 自定义创建方法
    # def create(self, validated_data):
    #     user = UserInfo(**validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user
