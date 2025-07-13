import copy
from abc import ABC, abstractmethod

from .list_element import ListElement


# Abstract Base Class for lists
class ListEntity(ABC):

    def __init__(self, author: str):
        super().__init__()
        self._elements = []
        self._author = author

    # Elements property as tuple for limit code access
    @property
    def elements(self) -> tuple:
        return tuple(self._elements)

    @property
    def author(self) -> str:
        return self._author

    def get_elements_list(self) -> list[ListElement]:
        return copy.deepcopy(self._elements)

    # Find the element in the list by its id
    def get_element_by_id(self, element_id: str) -> ListElement:
        try:
            return next(
                element for element in self._elements if element.id == element_id
            )
        except StopIteration:
            raise AttributeError(f"No element found with id: {element_id}")

    # Add new element to the list
    def add_element(self, new_element: ListElement) -> None:
        self._elements.append(new_element)

    # Parse and set the elements from an external source
    @abstractmethod
    def load_premade_list(self, premade_list):
        pass

    # Will be implemented by subclasses according to their own type & logic
    @abstractmethod
    def sort_list_elements(self):
        pass
