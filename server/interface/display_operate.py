import abc


class IDisplayOperate(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def state(self) -> bool:
        pass

    def turn_on(self):
        pass

    def turn_off(self):
        pass
