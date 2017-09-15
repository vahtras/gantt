DAYS_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
MONTH_LABELS = (
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    )

def project_start(df):
    return min(df.From)

def project_end(df):
    return max(df.To)

def start_tasks(df):
    delta = (df.From - project_start(df))
    days = delta.astype('timedelta64[D]')
    return days

def end_tasks(df):
    delta = (df.To - project_start(df))
    days = delta.astype('timedelta64[D]')
    return days



