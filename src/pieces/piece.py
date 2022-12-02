from abc import ABC, abstractmethod
from coordinate import Coordinate

class piece(ABC):
    @abstractmethod
    def move(self):
        pass