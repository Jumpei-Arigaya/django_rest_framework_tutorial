from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    """すべてのスニペットをリストするか、新しいスニペットを作成する"""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """スニペットの詳細を取得、更新、削除する"""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
