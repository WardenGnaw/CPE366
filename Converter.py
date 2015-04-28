import sys
import csv

import DeviceModel
import RegistrationLocation
import CustomerAccount
import CustomerEmail

def main():
   device_models = {}
   registration_location = {}
   customer_email = {}
   customer_account = {}
   device_counter = 0
  
   # Read and parse Device Model csv
   with open('CP_Device_Model.csv', 'rb') as csvfile:
      deviceReader = csv.reader(csvfile, delimiter=',')
      
      deviceReader.next()                         #Skip Header Row
      
      for row in deviceReader:
         try:
            device_models[row[0]]                 # Try to index into the map with key
         except KeyError:                         # If it dosen't exist, put into map
            temp = DeviceModel.DeviceModel(row[1], row[3], row[0], row[2]) 
            device_models[temp] = device_counter
            device_counter = device_counter + 1
   
   # Read and parse Device csv
   with open('CP_Device.csv', 'rb') as csvfile:
      deviceReader = csv.reader(csvfile, delimiter=',')
      
      deviceReader.next()                         #Skip Header Row
      # Continue making Device Models
      for row in deviceReader:
         try:
            print device_models[row[3]]
         except KeyError:
            temp = DeviceModel.DeviceModel(row[3], 'NULL', 'NULL', 'NULL') 
            device_models[temp] = device_counter
            device_counter = device_counter + 1
  
   with open('CP_Account.csv', 'rb') as csvfile:
      deviceReader = csv.reader(csvfile, delimiter=',')
      
      deviceReader.next()
      for row in deviceReader:
         try:
            registration_location[row[2]]
         except KeyError:
            temp = RegistrationLocation.RegistrationLocation(row[2], row[3])
            registration_location[row[2]] = temp

         try:
            customer_account[row[0]] 
         except KeyError:
            temp = CustomerAccount.CustomerAccount(row[0], 'TRUE' if row[8] == '0' else 'FALSE', row[12], row[6], row[4], row[5], row[7], 0)
            customer_account[row[0]] = temp

   for key, value in device_models.iteritems():
      print 'INSERT INTO DeviceInformation(' + str(value) + ', ' + str(key) + ');'
   
   for key, value in registration_location.iteritems():
      print 'INSERT INTO RegistrationLocation(' + str(value) + ');'
   
   for key, value in customer_account.iteritems():
      print 'INSERT INTO CustomerAccount(' + str(value) + ');'

   return 0

if __name__ == "__main__":
   sys.exit(main())
