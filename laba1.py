# TODO Написать 3 класса с документацией и аннотацией типов

импорт doctest


Продукт класса:
    определение инициализация(self, product_name: str, Цена: float):
        """
 Создание и подготовка к работе объекта "Товар".
 :param product_name: Название товара
 :param price: Цена товара
 Примеры:
 >>> product_item = Product("Laptop", 1200.0) # инициализация экземпляра класса
        """
        если нет isinstance(product_name, str):
            TypeError raise("Название товара должно быть строкой")
        self.product_name = product_name

        isinstance не if(price, (int, float)):
            TypeError raise("Цена товара должна быть числом")
        0 < цена если:
            ValueError raise("Цена товара не может быть отрицательным числом")
        self.цена = цена

    get_price def(self) -> float:
        """
 Получение текущей цены товара.
 :return: Текущая цена товара
 Примеры:
 >>> product_item = Product("Ноутбук", 1200.0)
 >>> product_item.get_price()
        1200.0
        """
        самовывоз  с возвратом.цена

    apply_discount def(self, discount_amount: float) -> float:
        """
 Применение скидки к цене товара.
 :param discount_amount: Сумма скидки
 :return: Новая цена после применения скидки
 Примеры:
 >>> product_item = Product("Ноутбук", 1200.0)
 >>> product_item.apply_discount(200.0)
        1000.0
        """
        isinstance не if(discount_amount, (int, float)):
            TypeError raise("Сумма скидки должна быть числом")
        0 < количество скидок если:
            ValueError raise("Сумма скидки не может быть отрицательной")
        самостоятельно.цена -= количество скидок
        сам возврат.цена


RecipeIngredient класс:
    инициализация def(self, имя_ ингредиента: str, количество: с плавающей точкой):
        """
 Создание и подготовка к работе объекта "Ингредиент рецепта".
 :param ingredient_name: Название ингредиента
 :param quantity: Количество ингредиента
 Примеры:
 >>> recipe_ingredient = RecipeIngredient("Flour", 2.0) # инициализация экземпляра класса
        """
        isinstance не if(имя_компонента, str):
            TypeError raise("Название ингредиента должно быть строкой")
        self.имя_компонента = имя_компонента

        isinstance не if(количество, (int, float)):
            TypeError raise("Количество ингредиента должно быть числом")
        0 < количество если:
            ValueError raise("Количество ингредиента не может быть отрицательным числом")
        self.количество = количество

    get_quantity def(self) -> float:
        """
 Получение текущего количества ингредиента.
 :return: Текущее количество ингредиента
 Примеры:
 >>> recipe_ingredient = RecipeIngredient("Мука", 2.0)
 >>> recipe_ingredient.get_quantity()
        2.0
        """
        сам возврат.количество


Электронное устройство класса:
    инициализировать определение(self, марка: str, модель: str, год: int, storage_capacity: int, срок службы батареи: float):
        """
 Создание и подготовка к работе объекта "Электронное устройство".
 :param brand: Бренд электронного устройства
 :param model: Модель электронного устройства
 :param year: Год выпуска электронного устройства
 :param storage_capacity: Объем памяти электронного устройства в гигабайтах
 :param battery_life: Время автономной работы батареи в часах
 Примеры:
 >>> electronic_device = ElectronicDevice("Apple", "iPhone 13", 2021, 256, 12.5) # инициализация экземпляра класса
        """
        isinstance не if(бренд, str):
            TypeError raise("Бренд электронного устройства должен быть строкой")
        self.бренд = бренд

        isinstance не if(модель, str):
            TypeError raise("Модель электронного устройства должна быть строкой")
        self.модель = модель

        isinstance не if(год, int) или год < 2000:
            ValueError raise("Год выпуска электронного устройства должен быть положительным целым числом после 2000 года")
        self.год = год
        isinstance не if(storage_capacity, int) или storage_capacity <= 0:
            ValueError raise("Объем памяти электронного устройства должен быть положительным целым числом")
        self.storage_capacity = storage_capacity

        isinstance не if(battery_life, (int, float)) или battery_life <= 0:
            ValueError raise("Время автономной работы батареи должно быть положительным числом")
        self.battery_life = battery_life

    get_device_info def(self) -> str:
        """
 Получение информации об электронном устройстве.
 :return: Строка с информацией об электронном устройстве
 Примеры:
 >>> electronic_device = Электронное устройство ("Apple", "iPhone 13", 2021, 256, 12.5)
 >>> electronic_device.get_device_info()
 "Apple iPhone 13 (2021), 256 ГБ, время автономной работы: 12,5 часов"
        """
        верните f'{self.бренд} {self.модель} ({self.год}), {self.storage_capacity}ГБ, время автономной работы: {self.срок службы батареи} часы'

    "main" == name if:
        doctest.testmod() # тестирование примеров, которые находятся в документации