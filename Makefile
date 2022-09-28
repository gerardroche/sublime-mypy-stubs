help:
	@echo "Usage:"
	@echo "	make <target>..."

stubgen:
	stubgen ~/sublime_text_4/Lib/python38/
	cp ~/sublime_text_4/Lib/python38/sublime_types.py ./sublime_types.pyi
