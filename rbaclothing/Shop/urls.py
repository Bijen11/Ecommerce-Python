from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", views.index, name="index"),
    path('viewproduct/<int:pk>', views.view_product, name="view_product"),
    path("itemdetail/",views.itemdetail,name="itemdetail"),
    path("add-to-cart/<int:id>", views.add_to_cart, name="addtocart"),
    path("remove-from-cart/<int:id>", views.remove_from_cart, name="removefromcart"),
    path("increase/<int:id>", views.increase, name="increase"),
    path("decrease/<int:id>", views.decrease, name="decrease"),
    path("Checkout/",views.Checkout,name="Checkout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)