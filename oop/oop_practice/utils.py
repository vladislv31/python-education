"""Модуль со вспомогательными функциями"""


def get_engine_power(obj):
    """Возвращает ноль, если нет двигателя"""
    return 0 if not hasattr(obj, 'engine_power') else obj.engine_power
