from abc import ABC, abstractmethod

class ListElement(ABC):

    def __init__(self, name, rank, category):
        super().__init__()
        self._name = ""
        self._rank = rank
        self._category = category
