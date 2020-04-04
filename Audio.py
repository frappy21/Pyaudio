import os
from mutagen.easyid3 import EasyID3
from os import listdir
import requests
import subprocess
import json
i = 0

#___________________________________________________________________________________________________________________________#
apikey = '3c0a2184581d6ae1fd3bc77134956666'; # generate and place here your unique API access key, the key must be 'active'
#############################################################################################################################



ffmpeg = 'ffmpeg.exe'
key1 = '-i'
key2 = "-ar 8000 -ac 1 -vn"
os.chdir('.')


#payload = {'action': 'stat', 'apikey': apikey}
#r = requests.post('https://audiotag.info/api',data=payload)
#j = json.loads(r.text)
print("-----------------------------------------")
print('seconds remaind:')
#print(j["identification_free_sec_remainder"])
print("-----------------------------------------")
print()
print()
files = listdir("./input")


numbers = next(os.walk("./input"))
file_count = len(numbers)
print("----------------------------------")
print("files in queue:")
print(file_count)
print("----------------------------------")
print()
print()

while i < file_count:
    tmp1 = files[i]
    song = './input/'+tmp1#.replace(' ','%20')
    print (files[i])
    tmp = "./temp/"+files[i]+".wav"

    outtext = 'ffmpeg -i ' '"' +song+ '"' ' -ss 00:00:20 -t 00:00:15 -ar 8000 -ac 1 -vn ' '"' +tmp + '"'
    

    os.system(outtext)
    #subprocess.call(['ffmpeg.exe -i' +song, ' -ar 8000 -ac 1 -vn' +tmp])
    i+=1
# ffmpeg -i input_file.ext -ar 8000 -ac 1 -vn coverted.wav
