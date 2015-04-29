# CREATE TABLE DeviceInformation (
#    serial_number VARCHAR(50),
#    device_model VARCHAR(100),
#    purchase_date DATE,
#    UNIQUE(device_model),
#    PRIMARY KEY(serial_number)
# );

class DeviceInformation:

	def __init__(self, serial_number, device_model, purchase_date):
		self.serial_number = serial_number
		self.device_model = device_model
		self.purchase_date = purchase_date

	def __eq__(self, other):
		if not isinstance(other, DeviceInformation):
			return False

		return (self.serial_number == other.serial_number and
				self.device_model == other.device_model and
				self.purchase_date == purchase_date)

	def __str__(self):
		return '"' + self.serial_number + '","' + self.device_model + '","' + self.purchase_date

	def __hash__(self):
		return hash(self.serial_number)