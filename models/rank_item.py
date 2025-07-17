from .list_element import ListElement
from util import register_constructor
from util.common import CategoryType


@register_constructor("rank")
class RankItem(ListElement):

    def __init__(self, name, rank: int, category: CategoryType):
        super().__init__(name, category)
