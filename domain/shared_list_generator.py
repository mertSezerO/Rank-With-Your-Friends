import threading
import copy
from functools import singledispatchmethod
from sklearn.cluster import KMeans
import numpy as np

from models import TierList, RankList
from .list_item_builder import ListItemBuilder


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
            thread = threading.Thread(target=self.__calculate, args=(list,))
            self.__threads.append(thread)

    def generate(self):
        for thread in self.__threads:
            thread.start()

        for thread in self.__threads:
            thread.join()

        print("All threads finished!")
        self.__finalize(self.__user_lists)
        self.__reorder_and_cluster()
        self.__construct_list()

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
            tier_scores[tier] = (1 + (1 / len(tiers))) ** (len(tiers) - i)

        score_dict = {}
        for element in list_elements:
            score_dict[element.name] = tier_scores[element.tier]

        list.score_dict = score_dict

    @__calculate.register
    def _(self, list: RankList):
        print("Rank List calculation for: " + list.author)

    @singledispatchmethod
    def __finalize(self, obj):
        raise TypeError("This object type is not valid!")

    @__finalize.register
    def _(self, user_lists: list[TierList]) -> None:
        final_score_dict = {}

        for list in user_lists:
            if len(final_score_dict) == 0:
                final_score_dict = {**(list.score_dict)}
                continue

            for key in list.score_dict.keys():
                final_score_dict[key] *= list.score_dict[key]

        self.final_score_dict = final_score_dict

    @__finalize.register
    def _(self, user_lists: list[RankList]) -> None:
        pass

    # Reorder and create tiers using k-means algorithm
    def __reorder_and_cluster(self) -> None:
        sorted_dict = dict(
            sorted(self.final_score_dict.items(), key=lambda item: item[1])
        )
        keys = list(sorted_dict.keys())
        values = list(sorted_dict.values())

        kmeans = KMeans(n_clusters=self.number_of_tiers, random_state=0)
        kmeans.fit(np.array(values).reshape(-1, 1))

        labels = kmeans.labels_

        clustered_data = {key: label for key, label in zip(keys, labels)}

        # Initialize builders for constructing list

    # Type agnostic construction method
    def __construct_list(self) -> None:
        pass
