# CREATE TABLE Link(
#    link_name VARCHAR(30),
#    url VARCHAR(50),
#    PRIMARY KEY(link_name)
# );


import hashlib

class Link:
	def __init__(self, link_name, url):
		self.link_name = link_name
		self.url = url

	def __eq__(self, other):
		if not isinstance(other, EventType):
			return False

		return (self.link_name == other.link_name and
				self.url == other.url)

	def __str__(self):
		return '"' + self.link_name + '", "' + self.url

	def __hash__(self):
		return hash(self.link_name)