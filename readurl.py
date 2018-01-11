import urllib
import sys
import json
datasource= urllib.urlopen("https://dashboard.motionloft.com/api/v1/stream?api_key=01cecfc22e99fee8a46e92f1bcd61fd3");

while (1):
	line=datasource.readline();
	if  line.find("uid")>0 : print line,
