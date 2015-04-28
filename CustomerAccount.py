class CustomerAccount:
   def __init__(self, customer_id, permission, customer_tier, gender, zip, state, income_level, num_registrations):
      self.customer_id = customer_id
      self.permission = permission
      self.customer_tier = customer_tier
      self.gender = gender
      self.zip = zip
      self.state = state
      self.income_level = income_level
      self.num_registrations = num_registrations

   def __eq__(self, other):
      if not isinstance(other, CustomerAccount):
         return False

      return True

   def __str__(self):
      return "" 
