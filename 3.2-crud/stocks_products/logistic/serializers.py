from rest_framework import serializers

from logistic.models import *


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']


    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        for el in positions:
            StockProduct.objects.create(stock=stock,
                                        product=el['product'],
                                        quantity=el['quantity'],
                                        price=el['price']
                                        )
            # StockProduct.objects.create(el)
        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        for position in positions:
            StockProduct.objects.update_or_create(stock=stock, **position)
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        print(instance)
        print(validated_data)
        print(positions)
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        for position in positions:
            StockProduct.objects.update_or_create(stock=stock, **position)
        return stock
