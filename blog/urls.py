
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# from .views import redirect_blog
from chatapp.views import register


urlpatterns = [

    # path('', redirect_blog),

    # path('grappelli/', include('grappelli.urls')),

    path('admin/', admin.site.urls),

    path('', include('chatapp.urls')),

    path('blog/', include('firstapp.urls')),

    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('signin/', register, name='signin'),
     
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout')

]