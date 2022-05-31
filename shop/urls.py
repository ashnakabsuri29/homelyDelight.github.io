from unicodedata import name
from django.urls import path
from shop import views
urlpatterns = [
     path('',views.index,name='index'),
     path('about/',views.about,name='about'),
     path('contact/',views.contact,name='contact'),
     path('thanks/',views.thanks,name='thanks'),
     path('foodzone/',views.foodzone,name='foodzone'),
     path('dish-view/<int:dishId>/', views.dishView,name='dish-view'),
     path('filter/',views.filter,name='filter'),
     path('reset/',views.reset,name='reset'),
     path('clear/',views.clear,name='clear'),
     path('login/',views.loginn,name='login'),
     path('authenticate/',views.authenti,name='authenticate'),
     path('signup/',views.signup,name='signup'),
     path('register/',views.register,name='register'),
     path('logout/',views.Logout,name='logout'),
     path('my-dish/',views.myDish,name='my-dish'),
     path('delete-dish/<int:dishID>',views.deleteDish,name='delete-dish'),
     path('add-item/',views.addDish,name='add-item'),
     path('add-to-cart/<int:dishID>',views.AddToCart,name='add-to=cart'),
     path('view-cart/',views.getCart,name='view-cart'),
     path('payment/', views.payment,name='payment'),
     path('checkout/', views.checkout, name='checkout'),
     path('delete-cart-item/<int:disID>',views.DeleteCartItem,name='delete-cart-item')
]
