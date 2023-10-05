"""
URL configuration for devsearchlive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# for email reset 
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', include('users.urls')),

    # in this page we write our email to reset the password 
    # here we tell to render which template 
    path('reset_password/', auth_view.PasswordResetView.as_view(template_name="reset_password.html"),
        name="reset_password"),
    # this link tell that the reset link password is sent 
    path('reset_password_sent/', auth_view.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
        name="password_reset_done"),
    # uidb64 = user id with the base 64 encryption 
    # in this page we can reset our password by writing down in the fields 
    path('reset/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name="reset.html"),
        name="password_reset_confirm"),
    # this page tell that the password is successfully changed or not 
    path('reset_password_complete/', auth_view.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), 
        name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC, document_root=settings.MEDIA_ROOT) for the collect static
