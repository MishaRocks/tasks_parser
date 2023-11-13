import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from app.src.queries.core import sync_get

if __name__ == '__main__':
    sync_get()
