from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from snippets.permission import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions


@api_view(["GET"])
def api_root(request, format=None):
    return Response({"users": reverse("user-list", request=request, format=format)})


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """「list」アクションと「retrieve」アクションを自動的に提供"""

    queryset = User.objects.all()
    rerializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """`list`、`create`、`retrieve`、 「更新」アクションと「破棄」アクション。 さらに、追加の「ハイライト」アクションも提供"""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
