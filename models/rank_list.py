from .list import ListEntity
from .rank_item import RankItem

class RankList(ListEntity):

    def __init__(self, author):
        super().__init__(author)

    # Find the element in the list by its rank
    def get_element_by_rank(self, rank: int) -> RankItem:
        try:
            return next(element for element in self._elements if element.rank == rank)
        except StopIteration:
            raise AttributeError(f"No element found with rank: {rank}")

    # Change the rank of the element by given id
    def change_element_rank(self, new_rank: int, element_id: str) -> None:
        try:
            element = self.get_element_by_id(element_id)
            element.rank = new_rank
        except (AttributeError, ValueError) as e:
            print(str(e))

    def load_premade_list(self):
        pass

    def sort_list_elements(self) -> list[RankItem]:
        pass