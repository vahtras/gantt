import sys
import pandas
import seaborn
import matplotlib.pyplot as plt
import collections


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

def end_tasks(df):
    col = Col(*df.columns[:4])
    delta = (df[col.end] - project_start(df))
    days = delta.astype('timedelta64[D]')
    return days

def plot(df):
    col = Col(*df.columns[:4])
    idays = start_tasks(df)
    fdays = end_tasks(df)
    seaborn.barplot(x=fdays, y=df[col.name])
    seaborn.barplot(x=idays, y=df[col.name], color="#FFFFFF")
    days_accumulated = [sum(DAYS_MONTH[:i]) for i in range(12)]
    start_month = project_start(df).month - 1
    end_month = project_end(df).month + 1
    plt.xlim((days_accumulated[start_month], days_accumulated[end_month-start_month]))
    plt.xticks(days_accumulated[:end_month-start_month:], MONTH_LABELS[start_month:end_month:])
    plt.xlabel('')
    plt.show()
    

def main():
    try:
        csv = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} csvfile")

    df = pandas.read_csv(csv, parse_dates=[1, 2])
    col = Col(*df.columns[:4])
    df = df.sort_values(col.start)
    print(df)

    plot(df)

if __name__ == "__main__":
    main()
