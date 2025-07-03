from list_element import ListElement

class RankItem(ListElement):

    def __init__(self, name, rank: int, category):
        super().__init__(name, rank, category)