# minimal-gantt

A script that takes a CSV file as input and produces
a Gantt chart in as a bar plots using the Seaborn library

It assumes that the CSV file has the first three columns as
task name, starting date and end date in ISO format.

## Install

```
pip install minimal-gantt
```

Examples


```
$ cat test.csv
Tasks,From,To,Misc
Prepare,2018-01-01,2018-03-31,comment
Action,2018-04-01,2018-06-30,comment
Postprocess,2018-07-01,2018-12-31,comment
```

```
$ python -m gantt test.csv
         Tasks       From         To     Misc
0      Prepare 2018-01-01 2018-03-31  comment
1       Action 2018-04-01 2018-06-30  comment
2  Postprocess 2018-07-01 2018-12-31  comment
```

![gantt chartt]("img/Figure_1.png")


