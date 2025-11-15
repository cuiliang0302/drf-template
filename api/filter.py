from django_filters import FilterSet, CharFilter
from api.models import UserDemo


class UserDemoFilter(FilterSet):
    """
    数据源名称，模糊查询
    """
    name = CharFilter(field_name='name', lookup_expr='icontains')  # icontains，包含且忽略大小写

    class Meta:
        # 指定模型
        models = UserDemo
        # 指定需要模糊查询的字段
        fields = ['name']
