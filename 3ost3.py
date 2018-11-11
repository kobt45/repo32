import pyautogui
import time
import clipboard
import pycountry
import xmlrpc.client
import os
import json
import struct
import urllib.request
#import urllib.urlretrieve
#import urllib2
#import zipfile
import gzip
import shutil
import requests
#import StringIO


ext = ['.mp4','.mkv','.mpeg','.mpg','.wmv','.x264','.xvid','.avi','.3gp']




server_name = "https://api.opensubtitles.org/xml-rpc"
server = xmlrpc.client.ServerProxy(server_name)
info = server.ServerInfo()
login = server.LogIn("","",'en',"TemporaryUserAgent")
token = login["token"]
#searchq = server.SearchSubtitles(token,[{'query':'22.Jump.Street.2014.720p.BluRay.x264.YIFY.mp4', 'sublanguageid':'eng'}],[{'limit':1}])
#searchq = server.SearchSubtitles(token,[{'query':'south park', 'season':1, 'episode':1, 'sublanguageid':'eng'}],[{'limit':1}])
#url = searchq["data"][0]["SubDownloadLink"]

#print (json.dumps(searchq, indent=2))



for dirpath, dirs, filenames in os.walk(r"c:\Users\Tetro\Downloads\utorrent\getsubs\\"):
    print(dirpath)
    #print(type(dirpath))
    print(filenames)
    for i in range(0,len(filenames)):
        #print(os.path.splitext(filenames[i])[1])
        checksrt = os.path.splitext(filenames[i])[0] + ".srt"
        checksrt = os.path.join(dirpath, checksrt)
        print (checksrt)
        #print (os.path.splitext(filenames[i])[1] in  ext)
        #print (os.path.exists(checksrt))
        
        if os.path.splitext(filenames[i])[1] in  ext and not os.path.exists(checksrt):
            print (filenames[i] + '\n\nGetting Subtitles...\n\n')
            print (os.path.join(dirpath, filenames[i]))
            path = os.path.join(dirpath, os.path.splitext(filenames[i])[0])
            path += '.srt'
            searchq = server.SearchSubtitles(token,[{'query':filenames[i], 'sublanguageid':'eng'}],[{'limit':1}])
            url = searchq["data"][0]["SubDownloadLink"]
            response = urllib.request.urlopen(url)
            with open(path, 'wb') as outfile:
                outfile.write(gzip.decompress(response.read()))

            
            

        
    
time.sleep(100)







