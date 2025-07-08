import threading
import copy
from functools import singledispatchmethod

from models import TierList, RankList

class SharedListGenerator:

    def __init__(self, user_lists: list[TierList | RankList]):
        self.__user_lists = user_lists

    @property
    def shared_list(self):
        return copy.deepcopy(self.__shared_list)

    # Create threads according to list types
    def prepare(self):
        self.__threads = []
        for list in self.__user_lists:
            thread = threading.Thread(target=self.__calculate, args=(list, ))
            self.__threads.append(thread)
        
    def generate(self):
        for thread in self.__threads:
            thread.start()
        
        for thread in self.__threads:
            thread.join()
        
        print("All threads finished!")
        final_dict = self.__finalize()
    
    # Overloaded calculate method to calculate each list in parallel 
    @singledispatchmethod
    def __calculate(self, obj):
        raise TypeError("This object type is not valid!")
        
    @__calculate.register
    def _(self, list: TierList):
        tier_scores = {}
        tiers = list.tiers
        list_elements = list.get_elements_list()

        for i, tier in enumerate(tiers):
            tier_scores[tier] = (1 + (1/len(list_elements))) ** (len(tiers) - i)
        
        score_dict = {}
        for element in list_elements:
            score_dict[element.name] = tier_scores[element.tier]
        
        list.score_dict = score_dict

        
    @__calculate.register
    def _(self, list: RankList):
        print("Rank List calculation for: "+ list.author)

    def __finalize(self) -> dict[str, float]:
        final_score_dict = {} 
        for list in self.__user_lists:
            if len(final_score_dict) == 0:
                final_score_dict = {**(list.score_dict)}
                continue
            
            for key in list.score_dict.keys():
                final_score_dict[key] += list.score_dict[key]

        return final_score_dict
    
    def __reorder(self, dict: dict[str, float]) -> None:
        pass

