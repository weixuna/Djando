from django.contrib import admin
from django.urls import include, path
from myapp import views  # 确保导入了 views 模块

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('', views.index, name='index'),  # 为根URL添加视图
]
