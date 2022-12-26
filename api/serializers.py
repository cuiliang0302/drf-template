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
    # 性别显示文字
    sex_name = serializers.ReadOnlyField(source='get_sex_display')

    class Meta:
        model = UserDemo
        fields = "__all__"
