from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book
from rest_framework.generics import GenericAPIView, get_object_or_404

# Create your views here.

class BookGenericApiView(GenericAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_object(self, pk):
        return get_object_or_404(Book, pk=pk)

    def get(self, request, pk=None):
        if pk:
            return Response({
                "status": status.HTTP_200_OK,
                "data": self.get_serializer(self.get_object(pk)).data
            })
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "count": self.get_queryset().count(),
            "data": serializer.data
        })

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = Book.objects.create(**serializer.validated_data)

        return Response({
            "status": status.HTTP_201_CREATED,
            "data": self.get_serializer(book).data
        }, status=status.HTTP_201_CREATED)

    def delete(self, request, pk=None):
        self.get_object(pk).delete()
        return Response({
            "status": status.HTTP_204_NO_CONTENT,
            'message': 'Book deleted successfully'
        })

    def put(self, request, pk=None):
        book = self.get_object(pk)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        for field, value in serializer.validated_data.items():
            setattr(book, field, value)
        book.save()

        return Response({
            "status": status.HTTP_200_OK,
            "data": self.get_serializer(self.get_object(pk)).data
        })

    def patch(self, request, pk=None):
        book = self.get_object(pk)
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        for field, value in serializer.validated_data.items():
            setattr(book, field, value)
        book.save()

        return Response({
            "status": status.HTTP_200_OK,
            "data": self.get_serializer(self.get_object(pk)).data
        })