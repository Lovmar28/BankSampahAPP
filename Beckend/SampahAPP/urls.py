from django.urls import  path, include
from rest_framework.routers import DefaultRouter
from .views import SampahViewSet, SetorViewSet, TabunganViewSet, TarikViewSet, UserViewSet, TitikPoinViewSet, Contact_UsViewSet, AdminViewSet

router = DefaultRouter()

router.register(r'Sampah', SampahViewSet)
router.register(r'Setor', SetorViewSet)
router.register(r'TitikPoin', TitikPoinViewSet)
router.register(r'Tabungan', TabunganViewSet)
router.register(r'Tarik', TarikViewSet)
router.register(r'User', UserViewSet)
router.register(r'Admin', AdminViewSet)
router.register(r'Contact_Us', Contact_UsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
# from .views import get_ContactUs, create_ContactUs
# urlpatterns = [
#     path('ContactUs/', get_ContactUs, name='get_ContactUs'),
#     path('ContactUs/create/', create_ContactUs, name='create_ContactUs'),
# ] 