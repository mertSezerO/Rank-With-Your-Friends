from .list_element import ListElement
from domain import register_constructor


@register_constructor("tier")
class TierItem(ListElement):

    def __init__(self, name, rank, category):
        super().__init__(name, rank, category)
