from .list import ListEntity

class TierList(ListEntity):

    def __init__(self, author):
        super().__init__(author)
        self.tiers = ["A", "B", "C", "D", "F"]

    def load_premade_list(self):
        pass

    def sort_list_elements(self):
        pass