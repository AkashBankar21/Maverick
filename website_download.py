import os
import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen

file1 = open('./worldometers_countrylist.txt', 'r')


def download(country):
    req = Request('https://www.worldometers.info/coronavirus/country/' + str(country),headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open('./countryhtml/' + str(country) + '.html','w',encoding="utf-8")
    f.write(mydata)
    f.close


countries = []
for line in file1:
    line = line.strip()
    if len(line) != 0 and line[-1] != '-' and line[-1] != ':':
        line = line.replace(' ', '-')
        download(line)

print("Websites are downloaded in countryhtml folder")