from builder_register import REGISTERED_CONSTRUCTORS
from util.common.category_type import CategoryType

class ListItemBuilder:

    def __init__(self, type: str, category: CategoryType):
        if type not in REGISTERED_CONSTRUCTORS:
            raise ValueError(f"Unknown item type: {type}")
        self._type = type
        self._category = category
        self._name = ""
        self._rank = None

    def set_name(self, name):
        self._name = name
        return self
    
    def set_rank(self, rank):
        self._rank = rank
        return self
    
    def build(self):
        if self._rank is None:
            raise ValueError("Item doesn't have ranking!")
        item_type = REGISTERED_CONSTRUCTORS[self._type]
        return item_type(self._name, self._rank, self._category)
