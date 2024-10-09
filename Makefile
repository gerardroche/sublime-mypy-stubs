help:
	@echo "Usage:"
	@echo "	make <target>..."

stubgen:
	stubgen /opt/sublime_text/Lib/python38/
	cp /opt/sublime_text/Lib/python38/sublime_types.py ./sublime_types.pyi
