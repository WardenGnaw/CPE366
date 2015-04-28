import sys
import csv

def main():
   with open('CP_Device_Model.csv', 'rb') as csvfile:
      deviceReader = csv.reader(csvfile, delimiter=',')
      for row in deviceReader:
         print row
   return 0

if __name__ == "__main__":
   sys.exit(main())
