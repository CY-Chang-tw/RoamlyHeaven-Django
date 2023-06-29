from django.urls import include, path
from .views import Home, Login, Logout, Signup, About, Faqs, Reservation, Payment

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('about/', About.as_view()),
    path('faqs/', Faqs.as_view()),
    path('search/', Home.as_view, name='search'),
    path('home/', Logout.as_view(), name='logout'),
    path('reservation/', Reservation.as_view(), name='reservation'),
    path('complete/', Payment.as_view(), name='complete'),
]