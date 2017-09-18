import sys
import pandas
import seaborn
import matplotlib.pyplot as plt
import collections
import datetime
import dateutil


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

def start_tasks(df):
    col = Col(*df.columns[:4])
    delta = (df[col.start] - project_start(df))
    days = delta.astype('timedelta64[D]')
    return days

def _start_tasks(df):
    col = Col(*df.columns[:4])
    days = [d.toordinal() for d in df[col.start]]
    return days

def end_tasks(df):
    col = Col(*df.columns[:4])
    delta = (df[col.end] - project_start(df))
    days = delta.astype('timedelta64[D]')
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
    idays = _start_tasks(df)
    fdays = _end_tasks(df)
    seaborn.barplot(x=fdays, y=df[col.name])
    seaborn.barplot(x=idays, y=df[col.name], color="#FFFFFF")
    xlim = min(idays), max(fdays)
    plt.xlim(xlim)
    
    tick_dates = get_tick_dates(project_start(df), project_end(df), 3)
    tick_labels = get_labels(tick_dates)
    plt.xticks(tick_dates, tick_labels)
    plt.xlabel('')
    plt.show()
    

def main():
    try:
        csv = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} csvfile")
        raise SystemExit

    df = pandas.read_csv(csv, parse_dates=[1, 2])
    col = Col(*df.columns[:4])
    df = df.sort_values(col.start)
    print(df)

    plot(df)

def get_tick_dates(start, stop, months=3):

    from dateutil.relativedelta import relativedelta
    dates = [start]
    while dates[-1] < stop:
        step = dates[-1] + relativedelta(months=months)
        print(step)
        dates.append(step)
    return [d.toordinal() for d in dates]

if __name__ == "__main__":
    main()
