class DeviceModel:
   def __init__(self, device_name, device_model, device_type, carrier):
      self.device_name = device_name

   def __eq__(self, other):
      return False

   def __str__(self):
      return ""
