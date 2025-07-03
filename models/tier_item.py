from list_element import ListElement
from builder_register import register_constructor

@register_constructor("tier")
class TierItem(ListElement):

    def __init__(self, name, rank, category):
        super().__init__(name, rank, category)