class Token:
	def __init__(self, type_, value=None):
		self.type = type_
		self.value = value
	def __repr__(self):
		if self.value: return "{}:{}".format(self.type, self.value)
		return '{}'.format(self.type)
