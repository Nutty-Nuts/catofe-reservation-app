source_dir = src
assets_dir = assets

run:
	./venv/bin/python3 $(source_dir)/main.py

install:
	./venv/bin/pip install -r requirements.txt

clearn:
	rm -rf __pycache__
