from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Messages
from .permissions import IsOwnerOrReceiver
from .serializers import MessagesSerializer


class MessagesListCreateView(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReceiver]

    def get_queryset(self):
        user = self.request.user
        is_read = self.request.query_params.get('is_read')

        # queryset = Messages.objects.filter(Q(receiver=user) | Q(sender=user))
        queryset = Messages.objects.filter(receiver=user)
        if is_read and is_read.lower() == 'false':
            queryset = queryset.filter(is_read=False)

        return queryset


class MessagesDetailView(generics.RetrieveDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReceiver]
