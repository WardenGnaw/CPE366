class CustomerEmail:
   def __init__(self, email_id, email_domain=None, audience=None):
      self.email_id = email_id
      self.email_domain = email_domain
      self.audience = audience

   def __eq__(self, other):
      if not isinstance(other, CustomerEmail):
         return False

      return (self.email_id == other.email_id and 
              self.email_domain == other.email_domain and 
              self.audience == other.audience)

   def __str__(self):
      return str(self.email_id)
