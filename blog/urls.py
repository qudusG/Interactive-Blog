from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:post_id>/', views.detail, name = 'detail'),
	path('profile', views.profile, name = 'profile'),
	path('signup', views.signup, name = 'signup'),
	path('login', views.login_view, name = 'login'),
	path('logout', views.logout_view, name= 'logout')
]