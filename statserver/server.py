import socket
import argparse

from stats import SimpleMovingAverage


def handle(address, port, period=10):
  """Starts stats server and waits for incoming connection."""
  
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind((address, port))
  sock.listen(5)
  
  sma = SimpleMovingAverage(period)
  
  print 'Stats server is running at %s:%s' % (address, port)
  print 'Quit the server with CONTROL-C.'
  
  try:
    while 1:
      csock, address = sock.accept()
      print 'Connection from', address
      while 1:
        data = csock.recv(512)
        print 'received:', data
        for i in data.strip().split(chr(10)):
          try:
            sma(float(i))
          except ValueError:
            print 'ignored value: %s' % (i.strip(),)
          else:
            print unicode(sma)
  except KeyboardInterrupt:
    print 'Closing connection...'
    sock.close()


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Simple Stats Server')
  parser.add_argument('address', 
    metavar='address:port', 
    type=str, 
    help='address and port for server'
  )
  parser.add_argument('--period', '-p', 
    dest='period', 
    action='store', 
    default=10, 
    help='window for simple moving average'
  )
  args = parser.parse_args()
  
  handle(
    address=args.address.split(':')[0], 
    port=int(args.address.split(':')[1]), 
    period=int(args.period)
  )