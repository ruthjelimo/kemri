# from knox import views as knox_views
# from .views import LoginAPI
# from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token  



# urlpatterns = [
#     path('api/login/kemri/', LoginAPI.as_view(), name='login'),
#     path('api/login/moringa/', LoginAPI.as_view(), name='login'),
#     path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
#     path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
#     # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
# ] 

from django.contrib import admin
from django.urls import path, include, re_path
from kemri.views import SellerRegistrationView, BuyerRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('core.urls', namespace='api')),
    path('registration/seller/', SellerRegistrationView.as_view(), name='register-seller'),
    path('registration/buyer/', BuyerRegistrationView.as_view(), name='register-buyer'),
]

   