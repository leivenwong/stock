# -*- coding: utf-8 -*-

# sys
import json
import math
# thirdpart
import pandas as pd
import numpy as np

# this project
if __name__ == '__main__':
  import sys

  sys.path.append('D:\stock_python\stock/new_stock')
##########################
import sys
print(sys.path)
import util
import util.utils
import const
import query.query_stock_list as query
import adjust.loop as loop



priorXQ = util.priorXQuarter
priorQ = util.priorQuarter
nextXQ = util.nextXQuarter

KN = const.CWSJ_KEYWORD.ADJUST_NAME
ID_NAME = const.CWSJ_KEYWORD.ID_NAME
KEY_NAME = const.CWSJ_KEYWORD.KEY_NAME
ADJUST_NAME = const.CWSJ_KEYWORD.ADJUST_NAME
MONGODB_ID = const.MONGODB_ID


class GenForecastPE(loop.AdjustOPSimpleColumnCheck):

  @property
  def key(self):
    return ADJUST_NAME['ForcastPE']

  def columns(self):
    return [self.key]

  def baseColumns(self):
    return []

  def op(self, data):
    for date, row in data.iterrows():
      try:
        data.loc[date, self.key] = self.stock.lastPrice / row[ADJUST_NAME['ForecastPerShareProfit']]
      except KeyError as e:
        print(e)
      except TypeError as e:
        print(e)
