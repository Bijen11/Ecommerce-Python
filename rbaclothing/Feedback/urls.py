from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("Feedback/", views.Feedback, name="Feedback"),
    path("feedback/", views.feedback, name="feedback"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
