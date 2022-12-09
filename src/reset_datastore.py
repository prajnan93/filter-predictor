from auto_filter import AutoFilter
import os

os.remove('store.json')
af = AutoFilter(verbose=True)
af.simulate()