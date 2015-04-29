import hashlib

class DeviceRegistration:
   def __init__(self, registration_id, registration_date, fk_device_model, fk_purchase_store_id, fk_serial_number, fk_registration_source_id):
     self.registration_id = registration_id
     self.registration_date = registration_date
     self.fk_device_model = fk_device_model
     self.fk_purchase_store_id = fk_purchase_store_id
     self.fk_serial_number = fk_serial_number
     self.fk_registration_source_id = fk_registration_source_id

   def __eq__(self, other)
      if not isinstance(other, DeviceRegistration):
         return False

      return (self.registration_id == other.registration_id and
              self.registration_date == other.registration_date and
	      self.fk_device_model = other.fk_device_model and
	      self.fk_purchase_store_id = other.fk_purchase_store_id and
	      self.fk_serial_number = other.fk_serial_number and
	      self.fk_registration_source_id = other.fk_registration_sourcr_id)

   def __str__(self):
      return '"' + str(self.registration_id) + '", "' + str(self.registration_date) + '", "' + str(self.fk_device_model) + '", "' + str(self.fk_purchase_store_id) + '", "' + str(self.fk_serial_number) + '", "' + str(self.fk_registration_source_id) + '"' 
   
   def __hash__(self):
      return hash(self.registration_id)