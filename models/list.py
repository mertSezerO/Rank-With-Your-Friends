from abc import ABC, abstractmethod

from models.list_element import ListElement

# Abstract Base Class for lists
class List(ABC):
    
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
    
    # Find the element in the list by its rank
    def get_element_by_rank(self, rank: int) -> ListElement:
        try:
            return next(element for element in self._elements if element.rank == rank)
        except StopIteration:
            raise AttributeError(f"No element found with rank: {rank}")
    
    # Find the element in the list by its id
    def get_element_by_id(self, element_id: str) -> ListElement:
        try:
            return next(element for element in self._elements if element.id == element_id)
        except StopIteration:
            raise AttributeError(f"No element found with id: {element_id}")
    
    # Add new element to the list
    def add_element(self, new_element: ListElement) -> None:
        self._elements.append(new_element)

    # Change the rank of the element by given id
    def change_element_rank(self, new_rank: int, element_id: str) -> None:
        try:
            element = self.get_element_by_id(element_id)
            element.rank = new_rank
        except (AttributeError, ValueError) as e:
            print(str(e))
    
    # Parse and set the elements from an external source
    @abstractmethod
    def load_premade_list(self):
        pass

    # Will be implemented by subclasses according to their own type & logic
    @abstractmethod
    def _sort_list_elements(self):
        pass
