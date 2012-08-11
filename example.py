import random
from statserver import StatsClient


# First, start the server:
# $ python statserver/server.py localhost:5050


if __name__ == '__main__':
  sc = StatsClient('localhost', 5050)

  try:
    while 1:
      print sc(random.random() * 10000)
  except KeyboardInterrupt:
    sc.close()
