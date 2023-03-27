import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open() as f:
    _data_sql = f.read().decode('utf8')
