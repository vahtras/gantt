import pytest
import unittest.mock
import pandas as pd
import pandas.util.testing as pdt
import io
import datetime

import gantt

csv = """\
Proj,From,To,Comment
A,2018-01-01,2018-03-31,aaa
B,2018-04-01,2018-06-30,bbb
C,2018-07-01,2018-12-31,ccc
"""

csv2 = """\
Proj,From,To,Comment
A,2018-02-01,2018-03-31,aaa
B,2018-05-01,2018-06-30,bbb
C,2018-08-01,2018-12-31,ccc
"""

@pytest.fixture
def df():
    csv_stream = io.StringIO(csv)
    return pd.read_csv(
        csv_stream,
        parse_dates=['From', 'To']
        )

@pytest.fixture
def df2():
    csv_stream = io.StringIO(csv2)
    return pd.read_csv(
        csv_stream,
        parse_dates=['From', 'To']
        )

def test_project_start(df):
    assert gantt.project_start(df) == pd.Timestamp('2018-01-01')

def test_project_start2(df2):
    assert gantt.project_start(df2) == pd.Timestamp('2018-02-01')

def test_project_end(df):
    assert gantt.project_end(df) == pd.Timestamp('2018-12-31')

def test_start_tasks(df):
    days = [d for d in gantt.start_tasks(df)]
    assert days == [0, 90, 181]

def test_start_days(df):
    days = gantt._start_tasks(df)
    assert days == [736695, 736785, 736876]

def test_start_tasks2(df2):
    days = gantt._start_tasks(df2)
    assert days == [736726, 736815, 736907]

def test_end_tasks(df):
    days = [int(d) for d in gantt._end_tasks(df)]
    assert days == [736784, 736875, 737059]

def test_end_tasks2(df2):
    days = [int(d) for d in gantt._end_tasks(df2)]
    assert days == [736784, 736875, 737059]

def test_labels():
    assert gantt.get_labels([1]) == ['Jan01']

@unittest.mock.patch('gantt.plt.show')
@unittest.mock.patch('gantt.seaborn.barplot')
@pytest.mark.skip()
def test_plot(mock_plot, mock_show, df):

    gantt.plot(df)

    calls = [
        unittest.mock.call(
            x=pd.Series([89., 180., 364.]),
            y=pd.Series(['A', 'B', 'C']),
            ),
        unittest.mock.call(
            x=[0, 90, 181],
            y=['A', 'B', 'C'],
            color="#FFFFFF"
            ),
        ]
    mock_plot.assert_called
    mock_show.assert_called
    mock_plot.assert_has_calls(calls)


def test_set_ticks(df):
    tick_dates = [736695, 736785, 736876, 736968, 737060]
    assert gantt.get_tick_dates(
        datetime.date(2018,1,1), datetime.date(2018,12,31), months=3
        ) == tick_dates
        
