from .list import ListEntity

class RankList(ListEntity):

    def __init__(self, author):
        super().__init__(author)

    def load_premade_list(self):
        pass

    def sort_list_elements(self):
        pass