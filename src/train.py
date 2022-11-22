import json

filters = {
    1: "Vivid",
    2: "Monochrome",
    3: "Sepia",
    4: "Vignette"
}

filter_configs = {
    1: ((12, 12, 12), (11, 10, 1)),
    2: (5, 10, 2, 4)
}


class DataStore():
    def __init__(self, verbose=False, reward=1) -> None:
        self.datastore = None
        self.verbose = verbose
        self.reward = reward
        # Add initialization for datastore

    def load_store(self, fname):
        with open(fname) as f:
            self.datastore = json.load(f)
        if self.verbose:
            print("Data store loaded:\n", self.datastore)

    def save_store(self, fname='store.json'):
        json_store = json.dumps(self.datastore)
        with open(fname, 'w') as f:
            f.write(json_store)
        if self.verbose:
            print("Store saved:\n", self.datastore)

    def reward(self, category_id, filter_id, config_id):
        self.datastore[category_id][]
