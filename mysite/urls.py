from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views # ログイン画面の準備に必要なモジュールのインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.login, name='login'), # ログインページの設定の追加
    path('accounts/logout/', views.logout, name='logout', kwargs={'next_page': '/'}), # ログアウトの設定の追加
    path('', include('demo_app.urls'))
]
