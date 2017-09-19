import sys
import pandas
import seaborn
import matplotlib.pyplot as plt
import collections
import datetime
from dateutil.relativedelta import relativedelta

__version__ = "0.2.2"

DAYS_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
MONTH_LABELS = (
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    )
Col = collections.namedtuple('col', ['name', 'start', 'end', 'misc'])


def project_start(df):
    col = Col(*df.columns[:4])
    return min(df[col.start])

def project_end(df):
    col = Col(*df.columns[:4])
    return max(df[col.end])

def _start_tasks(df):
    col = Col(*df.columns[:4])
    days = [d.toordinal() for d in df[col.start]]
    return days

def _end_tasks(df):
    col = Col(*df.columns[:4])
    days = [d.toordinal() for d in df[col.end]]
    return days

def get_labels(ds):
    import datetime
    stimes = [datetime.date.fromordinal(d).ctime().split() for d in ds]
    monyear = [s[1] + s[-1][-2:] for s in stimes]
    return monyear

def plot(df):
    col = Col(*df.columns[:4])
    df['idays'] = _start_tasks(df)
    df['fdays'] = _end_tasks(df)
    seaborn.barplot(x='fdays', y=col.name, data=df)
    seaborn.barplot(x='idays', y=col.name, data=df, color="#FFFFFF")

    start = start_yearmonth(df)
    end = end_yearmonth(df)

    xstart = start.toordinal()
    xend = end.toordinal()
    plt.xlim(xstart, xend)
    
    tick_dates = get_tick_dates(start, end, months=3)
    tick_labels = get_labels(tick_dates)
    plt.xticks(tick_dates, tick_labels)

    plt.xlabel('')
    plt.show()
    
def start_yearmonth(df):
    ps = project_start(df)
    return datetime.date(ps.year, ps.month, 1)

def end_yearmonth(df):
    ps = project_end(df)
    return datetime.date(ps.year, ps.month, 1) + relativedelta(months=1)

def main():
    try:
        csv = sys.argv[1]
    except IndexError:
        print("Usage: {} csvfile".format(sys.argv[0]))
        sys.exit(1)

    df = pandas.read_csv(csv, parse_dates=[1, 2])
    col = Col(*df.columns[:4])
    df = df.sort_values(col.start)
    print(df)

    plot(df)

def get_tick_dates(start, stop, months=3):

    dates = [start]
    while dates[-1] < stop:
        step = dates[-1] + relativedelta(months=months)
        print(step)
        dates.append(step)
    return [d.toordinal() for d in dates]

if __name__ == "__main__": #pragma: nocover
    main()
