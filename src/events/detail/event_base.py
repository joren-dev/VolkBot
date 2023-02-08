from abc import ABCMeta, abstractmethod


class OnReadyEvent(metaclass=ABCMeta):
    @property
    @abstractmethod
    def on_ready(self):
        pass


class OnMessageEvent(metaclass=ABCMeta):
    @property
    @abstractmethod
    def on_message(self, message):
        pass
