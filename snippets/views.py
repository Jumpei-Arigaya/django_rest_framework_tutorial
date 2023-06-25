from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from snippets.permission import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers


@api_view(["GET"])
def api_root(request, format=None):
    return Response({"users": reverse("user-list", request=request, format=format)})


class SnippetList(generics.ListCreateAPIView):
    """すべてのスニペットをリストするか、新しいスニペットを作成する"""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """新しいスニペットを作成する"""
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """スニペットの詳細を取得、更新、削除する"""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    """ユーザーのリストを表示する"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """ユーザーの詳細を表示する"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
