from requests import get
from bs4 import BeautifulSoup
import requests


def main():
 r=get("http://sslproxies.org")
 html = BeautifulSoup( r.text, "html5lib")
 for item in html.select("table.table tr"):
  if "yes" in item.text:
   print ":".join([item.select_one("td").text,item.select_one("td:nth-of-type(2)").text])


if __name__ == "__main__":
 try:
  main()
 except requests.exceptions.ConnectionError:
  print("(*) Internet Connection Error")
  exit()
