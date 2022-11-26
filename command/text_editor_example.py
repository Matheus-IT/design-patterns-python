from abc import ABC, abstractmethod
from editor import Editor


class Command(ABC):
	backup: str

	def __init__(self, editor: Editor):
		self.editor = editor

	@abstractmethod
	def execute(self):
		pass

	def backup(self):
		self.backup = self.editor.text_field.value

	def undo(self):
		self.editor.text_field.value = self.backup


class CopyAllEditorContentCommand(Command):
	def execute(self):
		self.editor.clipboard = self.editor.text_field.value


class PasteClipboardContentCommand(Command):
	def execute(self):
		if self.editor.clipboard != '':
			self.backup()
			self.editor.text_field.insert(self.editor.clipboard)


def main():
	e = Editor()
	e.text_field.value = 'hello'
	
	c = CopyAllEditorContentCommand(e)
	c.execute()

	p = PasteClipboardContentCommand(e)
	p.execute()

	print(e.text_field.value)      # -> hellohello

	p.undo()                       # -> hello

	print(e.text_field.value)


if __name__ == '__main__':
	main()
