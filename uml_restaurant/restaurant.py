"""Module implements Restaurant class"""

import random

from abc import ABC, abstractmethod


class NoGoodError(Exception):
    """No Good found exception"""


class AlreadyAtWork(Exception):
    """Already at work exception"""


class AlreadyAtRestaurant(Exception):
    """Already at restaurant exception"""

class AlreadyAtHome(Exception):
    """Already at home exception"""


class Restaurant:
    """Restaurant class"""

    def __init__(self, title, menu):
        self._title = title
        self._waiters = []
        self._customers = []
        self._menu = menu

    def get_menu(self):
        """Returns menu"""
        return self._menu

    def get_waiters(self):
        """Returns waiters"""
        return self._waiters

    def get_title(self):
        """Returns title"""
        return self._title

    def waiter_in_event(self, waiter):
        """Call when waiter went to restaurant"""
        self._waiters.append(waiter)

    def waiter_out_event(self, waiter):
        """Call when waiter go out from restaurant"""
        self._waiters.remove(waiter)

    def customer_in_event(self, customer):
        """Call when customer went to restaurant"""
        self._customers.append(customer)

    def customer_out_event(self, customer):
        """Call when customer go out from restaurant"""
        self._customers.remove(customer)

    def __repr__(self):
        return f'Restaurant(title={self._title}, waiters={len(self._waiters)}, \
            customers={len(self._customers)})'


class Order:
    """Order class"""

    def __init__(self, customer, waiter, order_list):
        self._customer = customer
        self._waiter = waiter
        self._order_list = order_list

        self._price = self._count_price()

        self._is_payed = False

    def _count_price(self):
        """Counts order price depending on its order list"""
        price = 0

        for good in self._order_list:
            price += good.get_price()

        return price

    def get_waiter(self):
        """Returns order waiter"""
        return self._waiter

    def get_order_list(self):
        """Returns order list"""
        return self._order_list

    def get_price(self):
        """Returns order price"""
        return self._price

    def pay_event(self):
        """Pay event"""
        self._is_payed = True

    def __repr__(self):
        return f'Order(customer={self._customer}, waiter={self._waiter}, \
            goods={len(self._order_list)}, price={self.get_price()}, is_payed={self._is_payed})'


class Person(ABC): # pylint: disable=too-few-public-methods
    """Person class"""

    def __init__(self, name):
        self._name = name
        self._restaurant = None

    def get_name(self):
        """Returns person name"""
        return self._name

    @abstractmethod
    def __repr__(self):
        pass


class Waiter(Person): # pylint: disable=too-few-public-methods
    """Waiter class"""

    def go_work(self, restaurant):
        """Waiter goes work"""
        if self._restaurant is not None:
            raise AlreadyAtWork('You are already at work.')

        restaurant.waiter_in_event(self)
        self._restaurant = restaurant

    def go_home(self):
        """Waiter goes home"""
        if self._restaurant is None:
            raise AlreadyAtHome('You are already at home.')

        self._restaurant.waiter_out_event(self)
        self._restaurant = None

    def take_order(self, goods, customer):
        """Waiter takes order"""
        order_list = []
        menu = self._restaurant.get_menu()
        for good in goods:
            try:
                menu_item = next(filter(lambda x, g=good: x['title'] == g, menu.get_list()))
                order_list.append(menu_item['type'](good, menu_item['price'],
                                    menu_item['attribute']))
            except StopIteration as no_found_item:
                raise NoGoodError('No good with specified name found.') from no_found_item

        return Order(customer, self, order_list)

    def __repr__(self):
        return f'Waiter(name={self.get_name()})'


class Customer(Person):
    """Customer class"""

    def go_eat(self, restaurant):
        """Customer goes restaurant"""
        if self._restaurant is not None:
            raise AlreadyAtRestaurant('You are already at restaurant.')

        restaurant.customer_in_event(self)
        self._restaurant = restaurant

    def go_home(self):
        """Customer goes home"""
        if self._restaurant is None:
            raise AlreadyAtHome('You are already at home.')

        self._restaurant.customer_out_event(self)
        self._restaurant = None

    def call_waiter(self):
        """Returns random waiter"""
        return random.choice(self._restaurant.get_waiters())

    def give_order(self, waiter, goods):
        """Gives order"""
        return waiter.take_order(goods, self)

    # pylint: disable=R0201
    def pay_order(self, order):
        """Pays order"""
        order.pay_event()

    def __repr__(self):
        return f'Customer(name={self.get_name()})'


class Menu:
    """Menu class"""

    def __init__(self):
        self._list = []

    def get_list(self):
        """Returns menu goods list"""
        return self._list

    def add_good(self, good):
        """Adding good to menu"""
        self._list.append(good)

    def remove_good(self, good):
        """Removing good from menu"""
        self._list.remove(good)

    def __repr__(self):
        return f'Menu(items={len(self._list)})'

class Good(ABC):
    """Good abstract class"""

    def __init__(self, title, price):
        self._title = title
        self._price = price

    def get_title(self):
        """Returns good title"""
        return self._title

    def get_price(self):
        """Return good price"""
        return self._price

    @abstractmethod
    def __repr__(self):
        pass


class Drink(Good):
    """Drink class that extends from abstract class Good"""

    def __init__(self, title, price, volume):
        super().__init__(title, price)
        self._volume = volume

    def get_volume(self):
        """Returns drink volume"""
        return self._volume

    def __repr__(self):
        return f'Drink(title={self.get_title()}, price={self.get_price()}, \
            volume={self.get_volume()})'


class Food(Good):
    """Food class that extends from abstract class Good"""

    def __init__(self, title, price, weight):
        super().__init__(title, price)
        self._weight = weight

    def get_weight(self):
        """Returns food weight"""
        return self._weight

    def __repr__(self):
        return f'Food(title={self.get_title()}, price={self.get_price()}, \
            weight={self.get_weight()})'


def main():
    """Main func"""
    menu = Menu()
    menu.add_good({
        'title': 'Coca-cola',
        'type': Drink,
        'price': 10,
        'attribute': 1
    })

    print(menu.get_list())
    print(menu)

    bob = Waiter('Bob')
    john = Waiter('John')
    carl = Customer('Carl')

    rest = Restaurant('Krasti Crubs', menu)

    bob.go_work(rest)
    john.go_work(rest)
    carl.go_eat(rest)

    print(rest)

    waiter = carl.call_waiter()
    order = carl.give_order(waiter, ['Coca-cola', 'Coca-cola'])
    print(order)

    carl.pay_order(order)
    print(order)

    order_list = order.get_order_list()
    print(order_list[0])

    bob.go_home()
    carl.go_home()


if __name__ == '__main__':
    main()
