from .list_element import ListElement
from util import register_constructor
from util.common import CategoryType


@register_constructor("tier")
class TierItem(ListElement):

    def __init__(self, name, tier_index: int, category: CategoryType):
        super().__init__(name, category)
        self.__tier = tier_index

    @property
    def tier(self) -> int:
        return self.__tier
    
    def set_tier(self, new_tier: int) -> None:
        if new_tier < 0:
            raise ValueError("New tier index cannot be less than 0!")
        else:
            self.__tier = new_tier

