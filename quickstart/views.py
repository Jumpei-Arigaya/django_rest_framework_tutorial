from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ユーザーを表示または編集できるようにするAPIエンドポイント"""

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """グループの表示または編集を可能にするAPIエンドポイント"""

    queryset = Group.objects.al()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
