import os

__version__ = '1.0.2'

# set Python env variable to keep track of example data dir
orbitize_dir = os.path.dirname(__file__)
DATADIR = os.path.join(orbitize_dir, 'gc_data/')
