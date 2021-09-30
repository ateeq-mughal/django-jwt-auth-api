from django.urls import path, include
from .views import RegisterView, LoginView, UserView, LogoutView, AllUserView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('logout', LogoutView.as_view()),
    # path('all-user', AllUserView.as_view()),




]
