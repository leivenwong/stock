#!/usr/bin/env python
# -*- encoding: utf-8 -*-


def test():
  import pandas as pd
  d1 = [
    {'key': 'one', 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'same': 1},
    {'key': 'two', 'a': 2, 'b': 3, 'c': 4, 'd': 5, 'same': 1},
    {'key': 'three', 'a': 3, 'b': 4, 'c': 5, 'd': 6, 'same': 1},
    {'key': 'four', 'a': 11, 'b': 22, 'c': 33, 'd': 44, 'same': 1},
  ]
  d2 = [
    {'key': 'one', 'aa': 1, 'bb': 2, 'cc': 3, 'dd': 4, 'same': 22},
    {'key': 'three', 'aa': 11, 'bb': 22, 'cc': 33, 'dd': 44, 'same': 22},
    {'key': 'four', 'aa': 1111, 'bb': 222, 'cc': 333, 'dd': 444, 'same': 22},
  ]
  df1 = pd.DataFrame(d1)
  df2 = pd.DataFrame(d2)

  dfDiff = df1.diff
  print(dfDiff)


  df3 = pd.DataFrame.merge(df1, df2, on='key', how='left')
  df4 = df3.loc[:, ['key', 'a', 'c', 'dd']]
  print(df3)
  print(df4)


if __name__ == '__main__':
  test()
  # from fake_spider import cwsj
  # gpfh = cwsj.Handler()
  # gpfh.on_start()
  # gpfh.run()

  ###########################################
  from adjust import cwsj

  print(dir(cwsj))
  cwsj.test()
