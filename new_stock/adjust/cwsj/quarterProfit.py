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

  sys.path.append('D:\\stock_python\\stock\\new_stock')
##########################
import sys
print(sys.path)
import util
import util.utils
import const
import adjust.loop as loop



priorXQ = util.priorXQuarter
priorQ = util.priorQuarter
nextXQ = util.nextXQuarter

KN = const.CWSJ_KEYWORD.ADJUST_NAME
ID_NAME = const.CWSJ_KEYWORD.ID_NAME
KEY_NAME = const.CWSJ_KEYWORD.KEY_NAME
ADJUST_NAME = const.CWSJ_KEYWORD.ADJUST_NAME
MONGODB_ID = const.MONGODB_ID



class GenQuarterProfit(loop.AdjustOP):
  def columns(self):
    return [const.CWSJ_KEYWORD.ADJUST_NAME['QuarterProfit']]

  def op(self, data):
    for date, row in data.iterrows():
      try:
        profit = row[const.CWSJ_KEYWORD.KEY_NAME['jbmgsy']]
        if util.isSameQuarter(date, util.FirstQuarter):
          data.loc[date, const.CWSJ_KEYWORD.ADJUST_NAME['QuarterProfit']] = profit
        else:
          priorDate = priorQ(date)
          priorData = data.loc[priorDate]
          try:
            data.loc[date, const.CWSJ_KEYWORD.ADJUST_NAME['QuarterProfit']] = profit - priorData.loc[
              const.CWSJ_KEYWORD.KEY_NAME['jbmgsy']]
          except TypeError as e:
            print(e)
      except KeyError as e:
        print(e)




  def before(self, data):
    data.loc[:, ADJUST_NAME['QuarterProfit']] = np.nan
    pass

  def check(self, base, result):
    def innerCheck(x):
      if np.isnan(x):
        return True
      elif math.fabs(x) < 0.000001:
        return True

      return False

    base = base.loc[:, ADJUST_NAME['djmgsy_jy']]
    result = result.loc[:, ADJUST_NAME['QuarterProfit']]
    print(base)
    print(result)
    diff = base - result
    print(diff)
    re = diff.map(innerCheck)
    print(re)
    return re.all()