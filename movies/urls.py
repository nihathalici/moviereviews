from django.urls import path
from . import views

urlpatterns = [
    path("<int:movies_id>", views.detail, name="detail"),
    path("<int:movies_id>/create", views.createreview, name="createreview"),
    path("review/<int:review_id>", views.updatereview, name="updatereview"),
    path("review/<int:review_id>/delete", views.deletereview, name="deletereview"),
]