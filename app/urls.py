from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html")),
    path("accounts/", include("allauth.urls")),
    path("store/", views.cars, name="cars"),
    path("order/<int:order_id>", views.order, name="order"),
    path("update_car/<int:car_id>", views.update_car, name="update_car"),
    path(
        "order_is_processed/<int:order_id>",
        views.order_is_processed,
        name="order_is_processed",
    ),
]
