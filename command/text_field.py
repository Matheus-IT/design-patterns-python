class TextField:
	def __init__(self):
		self.value = ''

	def insert(self, editor_clipboard: str):
		self.value += editor_clipboard
