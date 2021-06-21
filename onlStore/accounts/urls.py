from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.indexView,name="home_url"),
    path('',views.loginView,name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',views.logoutUser,name="logout_url"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('payment/',views.payment, name="payment"),
    path('update_item/',views.updateItem, name="update_item"),
    path('process_order/',views.processOrder, name="process_order"),

]