from django.urls import path
from . import views

urlpatterns = [    
    # path('', views.home, name="website_home"),
    # path('<int:year>/<str:month>/', views.home, name="website_home"),
    path('appts/', views.all_appts, name="website_appts"),
    path('add_appt/', views.add_appt, name="add_appt"),
    path('add_appt/<room>/<dt>/', views.add_appt, name="add_appt"),
    path('', views.CalendarView.as_view(), name='website_home'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('appt_dtls/<pk>', views.appt_dtls, name='appt_dtls'),
]
