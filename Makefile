all: a b

a:
	python3 Query1.py > output.txt

b:
	python3 website_download.py