# finance/serializers.py

from rest_framework import serializers
from .models import Category, Transaction

# Сериализатор для модели Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Включаем все поля модели

# Сериализатор для модели Transaction
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'  # Включаем все поля модели