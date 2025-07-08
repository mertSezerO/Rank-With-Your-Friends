from .list import ListEntity
from .tier_item import TierItem

class TierList(ListEntity):

    def __init__(self, author):
        super().__init__(author)
        self.__tiers = ["S","A", "B", "C", "D", "F"]

    @property
    def tiers(self):
        return self.__tiers
    
    def change_tier_name(self, index: int, new_name) -> None:
        self.__tiers[index] = new_name

    def add_tier(self, new_tier: str, tier_index: int) -> None:
        tiers = []
        for i in range(0, len(self.__tiers) + 1):
            if i == tier_index:
                tiers.append(new_tier)
                continue
            tiers.append(self.__tiers[i])
            
        self.__tiers = tiers
 
    def load_premade_list(self):
        pass

    def sort_list_elements(self) -> list[TierItem]:
        pass