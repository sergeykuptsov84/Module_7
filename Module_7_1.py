class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')


class Shop(Product):
    def __init__(self, name, weight, category):
        super().__init__(name, weight, category)

    def get_products(self):
        __file_name = 'products.txt'
        file = open(__file_name, 'r')
        text_ = file.read()
        file.close()
        return text_

    def add(self, *products):
        __file_name = 'products.txt'
        for i in products:
            line_ = (str(i))
            file = open(__file_name, 'r')
            txt_ = file.read()
            file.close()
            if line_ in txt_:
                print(f'Продукт {line_} уже есть в магазине')
            else:
                file = open(__file_name, 'a')
                file.write(f'\n{line_}')
                file.close()


s1 = Shop('', 0, '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
s1.get_products()
