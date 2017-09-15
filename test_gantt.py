import pytest
import pandas as pd
import io

import gantt

csv = """\
Proj,From,To
A,2018-01-01,2018-03-31
B,2018-04-01,2018-06-30
C,2018-07-01,2018-12-31
"""

@pytest.fixture
def df():
    csv_stream = io.StringIO(csv)
    return pd.read_csv(
        csv_stream,
        parse_dates=['From', 'To']
        )

def test_project_start(df):
    assert gantt.project_start(df) == pd.Timestamp('2018-01-01')

def test_project_end(df):
    assert gantt.project_end(df) == pd.Timestamp('2018-12-31')

def test_start_taskx(df):
    days = [int(d) for d in gantt.start_tasks(df)]
    assert days == [0, 90, 181]

def test_end_tasks(df):
    days = [int(d) for d in gantt.end_tasks(df)]
    assert days == [89, 180, 364]

