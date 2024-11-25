from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about', views.about, name='about'),
    path('tim', views.tim, name='tim'),
    path('galeri', views.galeri, name='galeri'),
    path('kontak', views.kontak, name='kontak'),
    path('blog', views.blog_list, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/like/<int:pk>/', views.blog_like, name='blog_like'),
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.keluar, name='logout'),
    path('register/', views.register, name='register'),
    
    # Reset password
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    

]