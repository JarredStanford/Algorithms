#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_max_profit = 0
  current_min_price = 0
  for i in range(len(prices)):
    for j in range(len(prices)):
      if (j > i and prices[j]-prices[i] > current_max_profit) or current_max_profit == 0:
        current_max_profit = prices[j] - prices[i]
  return current_max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))