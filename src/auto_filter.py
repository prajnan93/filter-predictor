import json
from filter_bank import FILTER_NAMES, _FILTERS, CATEGORIES
from data_simulator import DataSimulator
from pprint import pprint
import os
import numpy as np

class DataStore:
    def __init__(self, verbose=False) -> None:
        self.verbose = verbose
        self.datastore = None

    def load_store(self, fname="store.json"):

        def jsonKV2int(x):
            if isinstance(x, dict):
                return {int(k):v for k,v in x.items()}
            return x

        if not os.path.exists(fname):
            self.datastore = {
                1: {
                    1: [0, 0, 0],
                    2: [0, 0, 0],
                    3: [0, 0, 0],
                    4: [0, 0, 0]
                },
                2: {
                    1: [0, 0, 0],
                    2: [0, 0, 0],
                    3: [0, 0, 0],
                    4: [0, 0, 0]
                },
                3: {
                    1: [0, 0, 0],
                    2: [0, 0, 0],
                    3: [0, 0, 0],
                    4: [0, 0, 0]
                },
                4: {
                    1: [0, 0, 0],
                    2: [0, 0, 0],
                    3: [0, 0, 0],
                    4: [0, 0, 0]
                },
                5: {
                    1: [0, 0, 0],
                    2: [0, 0, 0],
                    3: [0, 0, 0],
                    4: [0, 0, 0]
                }
            }
        else:
            with open(fname, 'r') as f:
                self.datastore = json.load(f, object_hook=jsonKV2int)
        if self.verbose:
            print("Data store loaded:\n")
            pprint(self.datastore)

    def save_store(self, fname="store.json"):
        json_store = json.dumps(self.datastore)
        with open(fname, "w") as f:
            f.write(json_store)
        if self.verbose:
            print("Store saved:\n")
            pprint(self.datastore)

    def reward(self, category_id, filter_id, config_id, reward_amt=1, save=False):
        if self.verbose:
            print("Updating:", category_id, filter_id, config_id, reward_amt)
        self.datastore[category_id][filter_id][config_id] += reward_amt
        if save:
            self.save_store()

    def display_store(self):
        pprint(self.datastore)

    def query_category(self, category_id):
        return self.datastore[category_id]


class AutoFilter:
    def __init__(self, verbose=False) -> None:
        self.datastore = DataStore(verbose=verbose)
        self.datastore.load_store()
        self.verbose = verbose

    def simulate(self, n_samples=5000):
        data_sim = DataSimulator()
        samples = data_sim.generate_samples(n_samples=n_samples)
        for sample in samples:
            self.datastore.reward(category_id=sample[0], filter_id=sample[1], config_id=sample[2])
        self.datastore.save_store()
        if self.verbose:
            self.datastore.display_store()

    # Return schema: [(4, array([1, 0, 2], dtype=int64)), (3, array([1, 0, 2], dtype=int64)), (2, array([1, 0, 2], dtype=int64)), (1, array([1, 0, 2], dtype=int64))]
    def get_filter_ranking(self, category_id):
        if self.verbose:
            print("Get filters for category:", category_id, CATEGORIES[category_id])
        filters = self.datastore.query_category(category_id)
        filter_scores = [sum(i) for i in list(filters.values())]
        sorted_filter_idx = np.argsort(filter_scores)[::-1]
        filter_ids = np.array(list(filters.keys()))
        sorted_filter_ids = filter_ids[sorted_filter_idx]
        ret_filters = []
        for filter_id in sorted_filter_ids:
            sorted_config_idx = np.argsort(filters[filter_id])[::-1]
            ret_filters.append((filter_id, sorted_config_idx))
        return ret_filters

    def reward(self, category_id, filter_id, config_id, reward_amt=1):
        self.datastore.reward(category_id=category_id, 
        filter_id=filter_id, 
        config_id=config_id, 
        reward_amt=reward_amt,
        save=True)