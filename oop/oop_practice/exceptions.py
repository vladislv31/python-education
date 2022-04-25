

class EngineTurnedOnError(Exception):
    """Двигатель уже включен"""


class EngineTurnedOffError(Exception):
    """Двигатель уже выключен"""


class PlayerIsPlayingError(Exception):
    """Плеер уже играет музыку"""


class PlayerIsNotPlayingError(Exception):
    """Плеер уже не играет музыку"""


class LightsIsLightningError(Exception):
    """Фары уже включены"""


class LightsIsNotLightningError(Exception):
    """Фары уже выключены"""
