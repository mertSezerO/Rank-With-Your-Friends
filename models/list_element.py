import uuid
from abc import ABC

from util.common.category_type import CategoryType

class ListElement(ABC):

    def __init__(self, name, rank, category: CategoryType):
        super().__init__()
        self._id = str(uuid.uuid4())
        self.name = name
        self._rank = rank
        self._category = category

    @property
    def rank(self) -> int: 
        return self._rank
    
    @property.setter
    def rank(self, rank) -> None:
        if(rank <= 0):
            raise ValueError("Rank cannot be less than 0!")
        else:
            self._rank = rank
    
    @property
    def category(self) -> str:
        return self._category
    
    @property.setter
    def category(self, category: CategoryType) -> None:
        self._category = category

    @property
    def id(self) -> str:
        return self._id
