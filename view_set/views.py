from rest_framework import viewsets
from rest_framework import serializers

from genericapiview.models import Book


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


# class BookPureViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Book.objects.all()
#         serializer = BookModelSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         book = get_object_or_404(Book.objects.all(), pk=pk)
#         serializer = BookModelSerializer(book)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = BookModelSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def update(self, request, pk=None):
#         book = get_object_or_404(Book.objects.all(), pk=pk)
#         serializer = BookModelSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def partial_update(self, request, pk=None):
#         book = get_object_or_404(Book.objects.all(), pk=pk)
#         serializer = BookModelSerializer(book, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def destroy(self, request, pk=None):
#         book = get_object_or_404(Book.objects.all(), pk=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)