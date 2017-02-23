import logging

# 1. logging.DEBUG
# 2. logging.info
# 3. logging.warning
# 4. logging.critical
# 5. logging.exception

logging.basicConfig(filename = 'logfile.txt', level = logging.DEBUG)

def main():

  x = input("please enter the integer value")
  try:
    if type(x) == int:
      print "x is integer"

  except Exception as e:
    logging.critical(str(e))

# run the main function
main()
