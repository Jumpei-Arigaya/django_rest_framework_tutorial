from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """オブジェクトの所有者のみにオブジェクトの編集を許可するカスタム権限"""

    def has_object_permission(self, request, view, obj):
        # 読み取り権限はあらゆるリクエストに許可され、GET HEAD または OPTIONS リクエストは常に許可される
        if request.method in permissions.SAFE_METHODS:
            return True

        # 書き込み権限は、スニペットの所有者にのみ許可
        return obj.owner == request.user
