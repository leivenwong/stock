# -*- coding: utf-8 -*-


# sys
import datetime

# thirdpart
import pandas as pd
import pymongo
from pymongo import MongoClient

# this project
if __name__ == '__main__':
  import sys

  sys.path.append('D:\\stock_python\\stock\\new_stock')
##########################
import util
import util.utils
import const
import query
import query.query_cwsj
import query.query_yjyg
import query.query_stock_list
import query.query_kdata

class Stock:
  def __init__(self, code):
    self._code = code
    self._df = None
    self._bdf = None

  @property
  def code(self):
    return self._code

  @property
  def data(self):
    return self._df

  @property
  def benchmark_data(self):
    return self._bdf

  @property
  def zgb(self):
    return self._basicInfo[const.TS.BASICS.KEY_NAME['zgb']]

  @property
  def name(self):
    return self._basicInfo[const.TS.BASICS.KEY_NAME['name']]

  @property
  def industry(self):
    return self._basicInfo[const.TS.BASICS.KEY_NAME['industry']]

  @property
  def gdp_speed(self):
    return self._gdp_speed

  @property
  def lastPrice(self):
    return self._lastPrice

  @property
  def zsz(self):
    return self._zsz

  def loadFile(file):
    def string2Datetime(x):
      return x.to_pydatetime()

    df = pd.read_excel(file)
    df.loc[:, const.CWSJ_KEYWORD.KEY_NAME['date']] = df.loc[:, const.CWSJ_KEYWORD.KEY_NAME['date']].map(string2Datetime)
    df.set_index(const.CWSJ_KEYWORD.KEY_NAME['date'], inplace=True)
    return df

  def load(self, **kwargs):
    if 'mock' in kwargs:
      self._df = Stock.loadFile(kwargs['mock']['file'])
      # return

    if 'cwsj' in kwargs and kwargs['cwsj']:
      self._df = query.query_cwsj.QueryTop(-1, self.code)

    if 'yjyg' in kwargs:
      dates = kwargs['yjyg']
      df = query.query_yjyg.Query(dates, self.code)
      #drop
      if len(df.index):
        df.drop(const.YJYG_KEYWORD.KEY_NAME['scode'], axis=1, inplace=True)
        df.drop(const.YJYG_KEYWORD.KEY_NAME['sname'], axis=1, inplace=True)
        self._df = self._df.join(df, how='outer')

    #sort
    self._df.sort_index(inplace=True, ascending=False)
    #fill na
    # try:
    #   self._df.loc[:, const.CWSJ_KEYWORD.KEY_NAME['zgb']].fillna(method='ffill', inplace=True)
    # except KeyError as e:
    #   print(e)
    #drop
    #c = self._df.columns



    #scala data
    self._basicInfo = query.query_stock_list.queryOne(self.code)
    self._gdp_speed = 0.067
    self._lastPrice = query.query_kdata.queryLastClosePrice(self.code)
    self._zsz = self.zgb * self.lastPrice


    # mock
    if 'mock' in kwargs:
      self._basicInfo[const.TS.BASICS.KEY_NAME['zgb']] = kwargs['mock']['zgb']




  def loadBenchmark(self, **kwargs):
    if 'file' in kwargs:
      self._bdf = Stock.loadFile(kwargs['file'])
      return

    if 'cwsj' in kwargs and kwargs['cwsj']:
      self._bdf = query.query_cwsj.QueryTop(-1, self.code)

    if 'yjyg' in kwargs:
      dates = kwargs['yjyg']
      df = query.query_yjyg.Query(dates, self.code)
      self._bdf = self._bdf.join(df)


if __name__ == '__main__':
  s = Stock('002415')
  s.load(cwsj=True, yjyg=['2018-09-30', '2018-06-30', '2018-03-31'])
  df = s.data
  print(df)
  df.to_excel('/home/ken/workspace/tmp/new-002415.xls')
  pass
