from django.urls import path
from .views import CustomerListView, CustomerListCreateView

urlpatterns = [
    path('list/', CustomerListView.as_view(), name='customer_list'),
    path('customers/', CustomerListCreateView.as_view(), name='order-list-create'),
]
