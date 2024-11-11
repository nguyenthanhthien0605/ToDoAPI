from rest_framework import viewsets


class BaseViewSet(viewsets.ModelViewSet):
    read_serializer_class = None
    detail_serializer_class = None
    create_serializer_class = None
    update_serializer_class = None

    def get_serializer_class(self):
        if self.action == "list":
            return self.read_serializer_class
        if self.action == "retrieve":
            return self.detail_serializer_class
        if self.action == "create":
            return self.create_serializer_class
        return self.update_serializer_class
