import socket
import time
import random


class StatsClient(object):
  """docstring for StatsClient"""
  def __init__(self, address, port):
    super(StatsClient, self).__init__()    
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.connect((address, port))
    
  def __call__(self, i):
    data = str(i) + chr(10)
    self.sock.send(data)
    return i

  def close(self):
    self.sock.close()