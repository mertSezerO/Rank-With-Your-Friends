from .list_element import ListElement
from domain import register_constructor


@register_constructor("rank")
class RankItem(ListElement):

    def __init__(self, name, rank: int, category):
        super().__init__(name, rank, category)
