# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject2
import pandas as pd
# Import from our lib
from mlproject2.tools import haversine
import pytest


def test_haversine():
    out = haversine(48.865070, 2.380009, 48.235070, 2.393409)
    assert out == 70.00789153218594
