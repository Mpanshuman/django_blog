from django.contrib import admin
from django.urls import path, include
from user import views as user_views

userurlpatterns = [
    path("logintest/", user_views.login, name="user-login"),
    path("registertest/", user_views.register, name="user-register"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("login/",user_views.login,name="user-login"),
    path("register/",user_views.register,name="user-register"),
    path("user/", include(userurlpatterns)),
]
