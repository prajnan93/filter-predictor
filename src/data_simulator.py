import numpy as np
import constants


class DataSimulator():
    def __init__(self, random_seed=5170):
        self.random_seed = random_seed
        # Sets filter probability for each category
        self.filter_probs= {
            1: [0.1, 0.2, 0.3, 0.4],
            2: [0.4, 0.1, 0.2, 0.3],
            3: [0.3, 0.4, 0.1, 0.2],
            4: [0.2, 0.3, 0.4, 0.1],
            5: [0.2, 0.4, 0.1, 0.3]
        }
        self.config_probs = (0.4, 0.2, 0.1, 0.3)

    def generate_samples(self, n_samples=50):
        np.random.seed(self.random_seed)
        samples = []
        category_ids = np.random.choice(list(constants.CATEGORIES.keys()), size=n_samples)
        for id in category_ids:
            filter_id = np.random.choice(list(constants.FILTERS.keys()),
                                         p=self.filter_probs[id])
            config_id = np.random.choice(list(constants.FILTER_CONFIGS.keys()),
                                         p=self.config_probs)
            samples.append((id, filter_id, config_id))
        return samples
