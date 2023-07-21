# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#
import urllib.request
import json


def main():
    weburl = urllib.request.urlopen("http://www.google.com")
    print("result code: " + str(weburl.getcode()))
    data = weburl.read()
    print(data)
    

if __name__ == "__main__":
    main()
