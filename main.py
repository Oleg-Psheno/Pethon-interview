class ItemDiscount:

    def __init__(self):
        self._name = 'name'
        self._price = 123

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price


class ItemDiscountReport(ItemDiscount):

    def __init__(self, discount=0.9, *args, **kwargs):
        super(ItemDiscountReport, self).__init__(*args, **kwargs)
        self.discount = discount

    def __str__(self):
        return f'Товар - {self.get_name()}, цена со скидкой: {self.discount * self.get_price()}'

    def get_parent_data(self):
        return f'Наименование:{self.get_name()}, цена: {self.get_price()}'


class Daughter1(ItemDiscountReport):
    def get_info(self):
        return self.get_name()


class Daughter2(ItemDiscountReport):
    def get_info(self):
        return self.get_price()


good2 = ItemDiscountReport()
print(good2.get_parent_data())
good2.set_price(1000)
print(good2.get_parent_data())
print(good2)
d1 = Daughter1()
d2 = Daughter2()
print(d1.get_info())
print(d2.get_info())

'''
        Результаты:
    Наименование:name, цена: 123
    Наименование:name, цена: 1000
    Товар - name, цена со скидкой: 900.0
    name
    123
'''

