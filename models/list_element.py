import uuid
from abc import ABC

from util.common import CategoryType


class ListElement(ABC):

    def __init__(self, name, category: CategoryType):
        super().__init__()
        self._id = str(uuid.uuid4())
        self.name = name
        self._category = category

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, category: CategoryType) -> None:
        self._category = category

    @property
    def id(self) -> str:
        return self._id
