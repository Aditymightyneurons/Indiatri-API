from django.urls import path
from app.views import authentication

urlpatterns = [
    path("signup/",authentication.RegisterView.as_view(),name="signup"),
    path("signin/",authentication.SignInView.as_view(),name="signin"),
    path("send-otp/", authentication.SendOtpView.as_view(), name="send-otp"),
    path("signout/", authentication.Logout.as_view(), name="signout"),
    # for admin users only
    path("all-users/",authentication.AllUsers.as_view(),name="all-users"),
    path("retrive-or-delete-user/<int:pk>",authentication.RetriveOrDeleteUser.as_view(),name="retrive-or-delete-user"),
]
