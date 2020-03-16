import requests
import json
import time

yucom_uri = 'http://yucomtrack.co.id/track-api/unit/read.php?po=qlue'
traccar_uri = 'http://traccar.qlue.id:5055'
device_id = 313484


def getData():
 
	try:
		r = requests.get(url = yucom_uri,timeout=5)
	except requests.exceptions.Timeout:
		print('timeout error')
		
		# Maybe set up for a retry, or continue in a retry loop
	except requests.exceptions.TooManyRedirects:
		print('too many redrect timeout')
		
		# Tell the user their URL was bad and try a different one
	except requests.exceptions.RequestException as e:
		# catastrophic error. bail.
		print('errornya :',e)
			
     
  
    # extracting data in json format 
	data = r.json() 
	content = data["content"][0]
	lat = content['latitude']
	lon = content['longitude']
	speed = content['speed']
	
	return lat,lon,speed
    

def postData(lat,lon,speed):
    #

	myobj = {
		'id': device_id,
		'lat': lat,
		'lon': lon,
		'timestamp': getTime(),
		'speed':speed
	}

	try:
		x = requests.post(traccar_uri, params=myobj,timeout=5)
	except requests.exceptions.Timeout:
		print('timeout error')
		
		# Maybe set up for a retry, or continue in a retry loop
	except requests.exceptions.TooManyRedirects:
		print('too many redrect timeout')
		
		# Tell the user their URL was bad and try a different one
	except requests.exceptions.RequestException as e:
		# catastrophic error. bail.
		print('errornya :',e)
	

    
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