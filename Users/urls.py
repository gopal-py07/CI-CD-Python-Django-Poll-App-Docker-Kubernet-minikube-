from django.urls import path
from Users.views import (
            home,
            login_view,
            logout_view,
            registration_view,
        )
        
app_name = 'users'       
urlpatterns  = [
    path('home/',home, name="home"),
    path('register/',registration_view, name="register" ),
    path('logout/',logout_view, name="logout" ),
    path('login/',login_view, name="login" )
]