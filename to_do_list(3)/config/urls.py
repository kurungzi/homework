from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('accounts/login/', user_views.login_view, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', user_views.sign_up, name='signup'),
]