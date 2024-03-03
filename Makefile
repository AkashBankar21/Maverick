all: a b c

a:
	python3 Query1.py > output.txt

b:
	python3 website_download.py

c:
	python3 Query2.py