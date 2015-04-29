class IsSentTo:
   def __init__(self, fk_campaign_name, fk_email_id):
      self.fk_campaign_name = fk_campaign_name
      self.fk_email_id = fk_email_id

   def __eq__(self, other):
      if not isinstance(other, IsSentTo):
         return False
      
      return (self.fk_campaign_name == other.fk_campaign_name and
              self.fk_email_id == other.fk_email_id)

   def __str__(self):
      return '"' + self.fk_campaign_name + '", "' + str(self.fk_email_id) + '"'

   def __hash__(self):
      return hash(fk_campaign_name) + hash(fk_email_id)
	
