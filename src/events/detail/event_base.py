from abc import ABCMeta, abstractmethod


class AbstractEventBase(metaclass=ABCMeta):
    @property
    @abstractmethod
    def on_event(self):
        pass
