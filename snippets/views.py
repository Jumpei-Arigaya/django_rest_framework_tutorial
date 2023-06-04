from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User


class SnippetList(generics.ListCreateAPIView):
    """すべてのスニペットをリストするか、新しいスニペットを作成する"""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadonly]

    def perform_create(self, serializer):
        """新しいスニペットを作成する"""
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """スニペットの詳細を取得、更新、削除する"""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadonly]


class UserList(generics.ListAPIView):
    """ユーザーのリストを表示する"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetriveAPIView):
    """ユーザーの詳細を表示する"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
