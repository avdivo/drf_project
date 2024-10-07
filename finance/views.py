from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer

# Вьюха для работы с категориями (доходы/расходы)
class CategoryListCreateView(APIView):

    def get(self, request, pk=None):
        if pk is not None:  # Проверяем, передан ли pk
            category = get_object_or_404(Category, pk=pk)  # Получаем категорию по ID
            serializer = CategorySerializer(category)  # Сериализуем категорию
            return Response(serializer.data)  # Возвращаем данные категории
        else:
            categories = Category.objects.all()  # Получаем все категории
            serializer = CategorySerializer(categories, many=True)  # Преобразуем их в JSON
            return Response(serializer.data)  # Возвращаем список категорий

    def post(self, request):
        serializer = CategorySerializer(data=request.data)  # Получаем данные от клиента
        if serializer.is_valid():  # Проверяем валидность данных
            serializer.save()  # Сохраняем новую категорию
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Возвращаем ошибки, если данные неверные

    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)  # Получаем категорию по ID
        serializer = CategorySerializer(category, data=request.data)  # Передаем данные для обновления
        if serializer.is_valid():  # Проверяем валидность данных
            serializer.save()  # Сохраняем обновленную категорию
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Возвращаем ошибки

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)  # Получаем категорию по ID
        category.delete()  # Удаляем категорию
        return Response(status=status.HTTP_204_NO_CONTENT)  # Возвращаем статус успешного удаления


# Вьюха для работы с транзакциями
class TransactionListCreateView(APIView):

    def get(self, request, pk=None):
        if pk is not None:  # Проверяем, передан ли pk
            transaction = get_object_or_404(Transaction, pk=pk)  # Получаем транзакцию по ID
            serializer = TransactionSerializer(transaction)  # Сериализуем транзакцию
            return Response(serializer.data)  # Возвращаем данные транзакции
        else:
            transactions = Transaction.objects.all()  # Получаем все транзакции
            serializer = TransactionSerializer(transactions, many=True)  # Преобразуем их в JSON
            return Response(serializer.data)  # Возвращаем список транзакций

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)  # Получаем данные от клиента
        if serializer.is_valid():  # Проверяем валидность данных
            serializer.save()  # Сохраняем транзакцию
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Возвращаем ошибки, если данные неверные

    def put(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)  # Получаем транзакцию по ID
        serializer = TransactionSerializer(transaction, data=request.data)  # Передаем данные для обновления
        if serializer.is_valid():  # Проверяем валидность данных
            serializer.save()  # Сохраняем обновленную транзакцию
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Возвращаем ошибки

    def delete(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)  # Получаем транзакцию по ID
        transaction.delete()  # Удаляем транзакцию
        return Response(status=status.HTTP_204_NO_CONTENT)  # Возвращаем статус успешного удаления