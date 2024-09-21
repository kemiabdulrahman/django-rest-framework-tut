from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShopViewSet, ItemViewSet
# from .views import item_list, item_detail

router = DefaultRouter()
router.register(r'shops', ShopViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('items/', item_list),
    # path('items/<int:pk>/', item_detail),
]
