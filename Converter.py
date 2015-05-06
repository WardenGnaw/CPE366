import sys
import csv
import datetime

import DeviceModel
import RegistrationLocation
import CustomerAccount
import CustomerEmail
import PurchaseInformation
import DeviceRegistration
import DeviceSerial
import DevicePurchaseDate
import Link
import Deployment


def main():
   device_models = {}
   registration_location = {}
   customer_email = {}
   customer_account = {}
   purchase_information = {}
   device_registration = {}
   purchase_date = {}
   serial_number = {}
   purchase_information[""] = "NULL"
   device_counter = 0
   store_counter = 0
   purchase_date_counter = 0
   serial_counter = 0

   # Read and parse Device Model csv
   with open('CP_Device_Model.csv', 'rb') as csvfile:
      deviceReader = csv.reader(csvfile, delimiter=',')
      
      deviceReader.next()                         #Skip Header Row
      
      for row in deviceReader:
         try:
            device_models[row[0]]                 # Try to index into the map with key
         except KeyError:                         # If it dosen't exist, put into map
            temp = DeviceModel.DeviceModel(row[1], row[0], row[2], row[3]) 
            device_models[row[0]] = temp #device_counter
            device_counter = device_counter + 1
   
   # Read and parse Device csv
   with open('CP_Device.csv', 'rb') as csvfile:
      deviceReader = csv.reader(csvfile, delimiter=',')
      
      deviceReader.next()                         #Skip Header Row
      # Continue making Device Models
      for row in deviceReader:
         try:
            device_models[row[3]]
         except KeyError:
            temp = DeviceModel.DeviceModel('', row[3], '', '') 
            device_models[row[3]] = device_counter
            device_counter = device_counter + 1
   
         try:
            if row[4]:
               serial_number[row[4]]
         except KeyError:
            temp = DeviceSerial.DeviceSerial(row[4])
            serial_number[row[4]] = serial_counter
            serial_counter = serial_counter + 1
         
         try:
            if row[5]:
               purchase_date[row[5]]
         except KeyError:
            temp = DevicePurchaseDate.DevicePurchaseDate(row[5])
            purchase_date[row[5]] = purchase_date_counter
            purchase_date_counter = purchase_date_counter + 1

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
        
         try:
            customer_email[row[1]]
         except KeyError:
            temp = CustomerEmail.CustomerEmail(row[1], row[11])

   with open('CP_Device.csv', 'rb') as csvfile:
      deviceReader = csv.reader(csvfile, delimiter=',')
      
      deviceReader.next()                         #Skip Header Row
      # Continue making Device Models
      for row in deviceReader:
         try:
            device_models[row[3]]
         except KeyError:
            temp = DeviceModel.DeviceModel('NULL', row[3], 'NULL', 'NULL') 
            device_models[row[3]] = device_counter
            device_counter = device_counter + 1
         
         try:
            cust = customer_account[row[0]]
            if row[11] > cust.num_registrations:
               cust.num_registrations = row[11]
         except KeyError:
            pass 
        
         found_purchase_info = None
         try:
            purchase_information[row[6] + row[7] + row[8]]
         except KeyError:
            temp = PurchaseInformation.PurchaseInformation(store_counter, row[6], row[7], row[8], row[9])
            purchase_information[row[6] + row[7] + row[8]] = store_counter 
            store_counter = store_counter + 1
         
         try:
            registration_location[row[1]]
         except KeyError:
            temp = RegistrationLocation.RegistrationLocation(row[1], row[2])
            registration_location[row[1]] = temp
        
         try:
            device_registration[row[12]]
         except KeyError:
            temp = DeviceRegistration.DeviceRegistration(row[12], datetime.datetime.strptime(row[10], "%m/%d/%Y").strftime("%Y/%m/%d"), device_models[row[3]], purchase_information[row[6] + row[7] + row[8]], serial_number[row[4]] if row[4] else "NULL", row[1], purchase_date[row[5]] if row[5] else "NULL") 
            device_registration[row[12]] = temp
   
   deployment = {}
   link = {}

   with open('CP_Email.csv', 'rb') as csvfile:
      deviceReader = csv.reader(csvfile, delimiter=',')
      
      deviceReader.next()                         #Skip Header Row
      
      for row in deviceReader:
         try:
            link[row[10]]
         except KeyError:
            temp = Link.Link(row[10], row[11])
            link[row[10]] = temp

         try:
            deployment[row[6]]
         except KeyError:
            temp = Deployment.Deployment(row[6], row[5], 0)
            deployment[row[6]] = temp

   for key, value in link.iteritems():
      print 'INSERT INTO Link(' + str(value) + ');'
   
   return 0

"""
   for key, value in device_registration.iteritems():
      print 'INSERT DeviceRegistration(' + str(value) + ');'
   for key, value in purchase_information.iteritems():
      print 'INSERT INTO PurchaseInformation(' + str(value) + ');'
   for key, value in customer_account.iteritems():
      print 'INSERT INTO CustomerAccount(' + str(value) + ');'
   for key, value in registration_location.iteritems():
      print 'INSERT INTO RegistrationLocation(' + str(value) + ');'
   for key, value in device_models.iteritems():
      print 'INSERT INTO DeviceInformation(' + str(value) + ');'
   for key, value in purchase_date.iteritems():
      print 'INSERT DevicePurchaseDate(' + str(value) + ', "' + datetime.datetime.strptime(key, "%m/%d/%Y").strftime("%Y/%m/%d") + '");'
   
   
   
"""

if __name__ == "__main__":
   sys.exit(main())
