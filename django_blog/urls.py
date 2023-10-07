from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
# userurlpatterns = [
#     path("logintest/", user_views.login, name="user-login"),
#     path("registertest/", user_views.register, name="user-register"),
# ]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("profile/",user_views.profile,name="user-profile"),
    path("login/",LoginView.as_view(template_name="user/login.html"),name="user-login"),
    path("logout/",LogoutView.as_view(template_name="user/logout.html"),name="user-logout"),
    path("register/",user_views.register,name="user-register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)