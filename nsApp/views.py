from django.shortcuts import render
from .models import Author, Book
from nsApp.serializer import AuthorSerializer, BookSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class BookListPagination(PageNumberPagination):
    page_size = 2

class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookListPagination

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer