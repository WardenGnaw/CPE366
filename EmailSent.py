# CREATE TABLE EmailSent(
#    campaign_name VARCHAR(100),
#    version VARCHAR(50),
#    subject_line VARCHAR(100),
#    audience VARCHAR(100),
#    fk_link_name VARCHAR(30),
#    PRIMARY KEY(campaign_name),
#    FOREIGN KEY(fk_link_name) REFERENCES Link(link_name)
# );

import hashlib

class EmailSent:
	def __init__(self, campaign_name, version, subject_line, audience, fk_link_name):
		self.campaign_name = campaign_name
		self.version = version
		self.subject_line = subject_line
		self.audience = audience
		self.fk_link_name = fk_link_name

	def __eq__(self, other):
		if not isinstance(self, other):
			return False

		return (self.campaign_name == other.campaign_name and
				self.version == version and
				self.subject_line == subject_line and
				self.audience == audience and
				self.fk_link_name = fk_link_name)

	def __str__(self):
		return '"' + self.campaign_name + '", "' + self.version + "', '" + self.subject_line + "', '" + self.audience
			+ "', '" + self.fk_link_name

	def __hash__(self):
		return hash(self.campaign_name)
	