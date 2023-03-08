from django.urls import path

from .views import AuthenticatedView

urlpatterns=[
    path('user_details/',AuthenticatedView.as_view()),
]