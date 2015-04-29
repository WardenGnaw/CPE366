import hashlib

class Event:
   def __init__(self, email_id, event_type, event_date, fk_event_type_id, fk_campaign_name):
      self.email_id = email_id
      self.event_type = event_type
      self.event_date = event_date
      self.fk_event_type_id = fk_event_type_id
      elf.fk_campaign_name = fk_campaign_name

   def __eq__(self, other):
      if not isinstance(other, Event):
         return False
      
      return (self.email_id == other.email_id and
              self.event_type == other.event_type and
              self.event_date == other.event_date and
              self.fk_event_type_id == other.fk_event_type_id and
              self.fk_campaign_name == other.fk_campaign_name)

   def __str__(self):
      return   str(self.fk_email_id) + ', ' + str(self.event_type) + ', "' + str(event_date) + '", ' + str(fk_event_type_id) + ', ' + str(fk_campaign_name)

   def __hash__(self):
      return hash(self.email_id + fk_event_type_id)
