from rest_framework import serializers
from .models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    model = StockProduct
    fields = ['id', 'stock', 'product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        print(validated_data)
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        print(positions)

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные
        for i in positions:
            stock = serializers.IntegerField('stock')
            product = serializers.IntegerField('product')
            quantity = serializers.IntegerField('quantity')
            price = serializers.FloatField('price')
            print(i)
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock
