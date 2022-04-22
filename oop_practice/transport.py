"""Модуль с реализованными классами для создания объектов транспортов"""

import time
import sys

from abc import ABC, abstractmethod

from exceptions import EngineTurnedOnError, EngineTurnedOffError, \
    PlayerIsPlayingError, PlayerIsNotPlayingError, \
    LightsIsLightningError, LightsIsNotLightningError

from utils import get_engine_power


class Transport(ABC):
    """Абстрактный класс - основа для всех транспортов"""

    __transports_count = 0

    def __init__(self, *args):
        name, brand, volume, wheels_count, color = args
        self.__name = name
        self.__brand = brand
        self.__volume = volume
        self.__wheels_count = wheels_count
        self.__color = color

        Transport.__transports_count += 1

    def print_type(self):
        """Выводит тип транспортного средства (двигатель/движитель :) )"""
        print(f"{self.__class__.__str__(self)} is working by mover.")

    @property
    def name(self):
        """Название транспорта"""
        return self.__name

    @property
    def brand(self):
        """Марка транспорта"""
        return self.__brand

    @property
    def volume(self):
        """Вместительность транспорта"""
        return self.__volume

    @property
    def wheels_count(self):
        """Количество колес у транспорта"""
        return self.__wheels_count

    @property
    def color(self):
        """Цвет транспорта"""
        return self.__color

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    def __eq__(self, another):
        if isinstance(another, Engine):
            return 0 == another.engine_power
        return self.__volume == another.volume

    def __ne__(self, another):
        if isinstance(another, Engine):
            return 0 != another.engine_power
        return self.__volume != another.volume

    def __lt__(self, another):
        if isinstance(another, Engine):
            return 0 < another.engine_power
        return self.__volume < another.volume

    def __gt__(self, another):
        if isinstance(another, Engine):
            return 0 > another.engine_power
        return self.__volume > another.volume

    def __le__(self, another):
        if isinstance(another, Engine):
            return 0 <= another.engine_power
        return self.__volume <= another.volume

    def __ge__(self, another):
        if isinstance(another, Engine):
            return 0 >= another.engine_power
        return self.__volume >= another.volume

    @staticmethod
    def get_transports_count():
        """Возвращает общее кол-во созданных транспортов"""
        return Transport.__transports_count

    def __del__(self):
        """При удалении транспорта кол-во транспортов снижается на единицу"""
        Transport.__transports_count -= 1


class Engine(ABC):
    """Абстрактный класс - двигатель"""

    def __init__(self, engine_power, engine_volume):
        self.__engine_power = engine_power
        self.__engine_volume = engine_volume
        self.__is_turned_on = False

    def print_type(self):
        """Выводит тип транспортного средства (двигатель/движитель :) )"""
        print(f"{self.__class__.__str__(self)} is working by engine.")

    @property
    def engine_power(self):
        """Мощность двигателя"""
        return self.__engine_power

    @property
    def engine_volume(self):
        """Объем двигателя"""
        return self.__engine_volume

    def __count_turning_time(self):
        """Возвращает кол-во секунд, требуемое на то, чтобы""" \
            """завести двигатель(зависит от мощности и кубатуры. Коряво, но интересно :) )"""
        return 1 / ((self.__engine_power / self.__engine_volume) % 10 **2) / 10 * 0.65

    def turn_on(self):
        """Включает двигатель, с time.sleep на то, чтобы его завести"""
        if self.__is_turned_on:
            raise EngineTurnedOnError
        print(f'{self.__class__.__str__(self)}: engine is turning on. Wait...')
        sys.stdout.flush()
        time.sleep(self.__count_turning_time())
        self.__is_turned_on = True
        print(f'{self.__class__.__str__(self)}: engine is turned on.')

    def turn_off(self):
        """Выключает двигатель"""
        if not self.__is_turned_on:
            raise EngineTurnedOffError
        self.__is_turned_on = False
        print(f'{self.__class__.__str__(self)}: engine is turned off.')

    def __eq__(self, another):
        return self.engine_power == get_engine_power(another)

    def __ne__(self, another):
        return self.engine_power != get_engine_power(another)

    def __lt__(self, another):
        return self.engine_power < get_engine_power(another)

    def __gt__(self, another):
        return self.engine_power > get_engine_power(another)

    def __le__(self, another):
        return self.engine_power <= get_engine_power(another)

    def __ge__(self, another):
        return self.engine_power >= get_engine_power(another)


class Lights(ABC):
    """Абстрактный класс - фары"""

    def __init__(self, lights_count):
        self.__lights_count = lights_count
        self.__is_lightning = False

    @property
    def lights_count(self):
        """Кол-во фар"""
        return self.__lights_count

    def lights_on(self):
        """Включает фары"""
        if self.__is_lightning:
            raise LightsIsLightningError
        self.__is_lightning = True
        print(f'{self.__class__.__str__(self)}: lights is lightning.')

    def lights_off(self):
        """Выключает фары"""
        if not self.__is_lightning:
            raise LightsIsNotLightningError
        self.__is_lightning = False
        print(f'{self.__class__.__str__(self)}: lights is not lightning.')


class MusicPlayer(ABC):
    """Музыкальный плеер"""

    def __init__(self):
        self.__is_playing = False

    def play_music(self):
        """Включает музыку"""
        if self.__is_playing:
            raise PlayerIsPlayingError
        self.__is_playing = True
        print(f'{self.__class__.__str__(self)}: player is playing music.')

    def stop_music(self):
        """Выключает музыку"""
        if not self.__is_playing:
            raise PlayerIsNotPlayingError
        self.__is_playing = False
        print(f'{self.__class__.__str__(self)}: player is not playing music.')


class Car(Engine, Lights, MusicPlayer, Transport):
    """Класс - автомобиль"""

    def __init__(self, name, brand, engine_power, engine_volume, color): # pylint: disable=too-many-arguments
        Engine.__init__(self, engine_power, engine_volume)
        Lights.__init__(self, 2)
        MusicPlayer.__init__(self)
        Transport.__init__(self, name, brand, 5, 4, color)

    @classmethod
    def black(cls, name, brand, engine_power, engine_volume):
        """Создает автомобиль черного цвета"""
        return cls(name, brand, engine_power, engine_volume, 'black')

    def __str__(self):
        return f'Car {self.name}'

    def __repr__(self):
        return f'Car(name={self.name}, brand={self.brand},' \
            'lights={self.lights_count}, color={self.color})'


class QuadBike(Engine, Lights, Transport):
    """Класс - квадроцикл"""

    def __init__(self, name, brand, engine_power, engine_volume, color): # pylint: disable=too-many-arguments
        Engine.__init__(self, engine_power, engine_volume)
        Lights.__init__(self, 2)
        Transport.__init__(self, name, brand, 2, 4, color)

    def __str__(self):
        return f'QuadBike {self.name}'

    def __repr__(self):
        return f'QuadBike(name={self.name}, brand={self.brand},' \
            'lights={self.lights_count}, color={self.color})'


class Motorcycle(Engine, Lights, Transport):
    """Класс - мотоцикл"""

    def __init__(self, name, brand, engine_power, engine_volume, color): # pylint: disable=too-many-arguments
        Engine.__init__(self, engine_power, engine_volume)
        Lights.__init__(self, 1)
        Transport.__init__(self, name, brand, 2, 2, color)

    def __str__(self):
        return f'Motorcycle {self.name}'

    def __repr__(self):
        return f'Motorcycle(name={self.name}, brand={self.brand},' \
            'lights={self.lights_count}, color={self.color})'


class Bicycle(Lights, Transport):
    """Класс - велосипед"""

    def __init__(self, name, brand, color):
        Lights.__init__(self, 1)
        Transport.__init__(self, name, brand, 2, 2, color)

    def __str__(self):
        return f'Bicycle {self.name}'

    def __repr__(self):
        return f'Bicycle(name={self.name}, brand={self.brand},' \
            'lights={self.lights_count}, color={self.color})'
