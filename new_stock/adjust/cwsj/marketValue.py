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
import adjust.loop as loop



priorXQ = util.priorXQuarter
priorQ = util.priorQuarter
nextXQ = util.nextXQuarter

KN = const.CWSJ_KEYWORD.ADJUST_NAME
ID_NAME = const.CWSJ_KEYWORD.ID_NAME
KEY_NAME = const.CWSJ_KEYWORD.KEY_NAME
ADJUST_NAME = const.CWSJ_KEYWORD.ADJUST_NAME
MONGODB_ID = const.MONGODB_ID



class GenMarketValue(loop.AdjustOPSimpleColumnCheck):
  @property
  def key(self):
    return ADJUST_NAME['MarketValue']

  def columns(self):
    return [self.key]

  def baseColumns(self):
    return []

  def op(self, data):
    try:
      data.loc[:, self.key] = self.stock.lastPrice * self.stock.zgb
    except TypeError as e:
      print(e)
    except KeyError as e:
      print(e)



class GenZGB(loop.AdjustOPSimpleColumnCheck):
  @property
  def key(self):
    return ADJUST_NAME['zgb']

  def columns(self):
    return [self.key]

  def baseColumns(self):
    return []

  def op(self, data):
    try:
      data.loc[:, self.key] = self.stock.zgb
    except TypeError as e:
      print(e)
    except KeyError as e:
      print(e)


class GenIndustry(loop.AdjustOPSimpleColumnCheck):
  @property
  def key(self):
    return ADJUST_NAME['industry']

  def columns(self):
    return [self.key]

  def baseColumns(self):
    return []

  def op(self, data):
    try:
      data.loc[:, self.key] = self.stock.industry
    except TypeError as e:
      print(e)
    except KeyError as e:
      print(e)



class GenLastPrice(loop.AdjustOPSimpleColumnCheck):
  @property
  def key(self):
    return ADJUST_NAME['lastPrice']

  def columns(self):
    return [self.key]

  def baseColumns(self):
    return []

  def op(self, data):
    try:
      data.loc[:, self.key] = self.stock.lastPrice
    except TypeError as e:
      print(e)
    except KeyError as e:
      print(e)


class GenCodeAndName(loop.AdjustOPSimpleColumnCheck):
  @property
  def keyC(self):
    return ADJUST_NAME['code']

  @property
  def keyN(self):
    return ADJUST_NAME['name']

  def columns(self):
    return [self.keyC, self.keyN]

  def baseColumns(self):
    return []

  def op(self, data):
    try:
      data.loc[:, self.keyC] = self.stock.code
      data.loc[:, self.keyN] = self.stock.name
    except TypeError as e:
      print(e)
    except KeyError as e:
      print(e)