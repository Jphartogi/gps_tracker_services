import requests
import json
import time

yucom_uri = 'http://yucomtrack.co.id/track-api/unit/read.php?po=qlue'
traccar_uri = 'http://traccar.qlue.id:5055'
device_id = 313484


def getData():
    r = requests.get(url = yucom_uri) 
  
    # extracting data in json format 
    data = r.json() 
    content = data["content"][0]
    lat = content['latitude']
    lon = content['longitude']
    speed = content['speed']

    return lat,lon,speed
    

def postData(lat,lon,speed):
    #

    url = 'https://www.w3schools.com/python/demopage.php'
    myobj = {
            'id': device_id,
            'lat': lat,
            'lon': lon,
            'timestamp': getTime(),
            'speed':speed
            }


    x = requests.post(traccar_uri, params=myobj)

    
    print("latnya %s longnya %s speednya %s" % (lat,lon,speed))



def getTime():
  
    waktu = time.time()
    return int(waktu)

if __name__ == "__main__":
    while True:
        lat,lon,speed = getData()
        postData(lat,lon,speed)
        time.sleep(10)
    # postData()