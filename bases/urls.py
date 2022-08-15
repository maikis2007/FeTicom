from django.urls import path
from bases.views import BlankView

app_name = "bases"
urlpatterns = [
    path('', BlankView.as_view(), name="blank")
]