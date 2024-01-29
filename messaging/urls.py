from django.urls import path
from messaging.views import MessagesListCreateView, MessagesDetailView

urlpatterns = [
    path('api/messages/', MessagesListCreateView.as_view(), name='messages-list'),
    path('api/messages/<int:pk>/', MessagesDetailView.as_view(), name='messages-detail'),
]
