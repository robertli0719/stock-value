# -*- coding: utf-8 -*-
"""
假设未来的净资产收益率以及杠杆率不变，计算股票以当前价格买入后多久可收回成本

@author: robert
"""
import math
import data


def p2f(x):
    return float(x.strip('%'))/100


ticker_arr = ["AAPL", "FB", "DIS", "GOOG", "NVDA", "AMZN",
              "MSFT", "IBM", "BABA", "TCEHY", "BIDU", "V", "NKE", "LULU"]
title_arr = ["Trailing P/E", "Forward P/E",
             "Price/Book", "Return on Assets", "Return on Equity"]

data_set = data.pick_data(ticker_arr, title_arr)

print("\nInstrments", "\tTrailing PE", "\tForward PE",
      "\tP/B", "\tRoA", "\tRoE", "\tCost Years")

for ticker in data_set:
    vals = data_set[ticker]
    t_pe = vals["Trailing P/E"]
    f_pe = vals["Forward P/E"]
    roe_str = vals["Return on Equity"]
    roa_str = vals["Return on Assets"]
    roe = p2f(roe_str)
    roa = p2f(roa_str)
    pb = float(vals["Price/Book"])
    cost_year = round(math.log(pb)/math.log(1+roe), 2)

    row_format = "{:<10}\t{:<7}\t\t{:<7}\t\t{:<7}\t{:<7}\t{:>7}\t{:>7}"

    teams_list = [ticker, t_pe, f_pe, pb, roa_str, roe_str, cost_year]
    print(row_format.format(*teams_list))
