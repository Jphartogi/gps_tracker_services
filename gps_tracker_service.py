import requests
import json
import time

yucom_uri = 'http://yucomtrack.co.id/track-api/unit/read.php?po=qlue'
traccar_uri = 'http://traccar.qlue.id:5055'
device_id = 313484
delay = 5


def getData():
 
	try:
		r = requests.get(url = yucom_uri,timeout=5)
	except requests.exceptions.Timeout:
		print('timeout error')
		return 0,0,0
		
		# Maybe set up for a retry, or continue in a retry loop
	except requests.exceptions.TooManyRedirects:
		print('too many redrect timeout')
		return 0,0,0
		
		# Tell the user their URL was bad and try a different one
	except requests.exceptions.RequestException as e:
		# catastrophic error. bail.
		print('errornya :',e)
		return 0,0,0
			
     
	
    # extracting data in json format 
	data = r.json() 
	content = data["content"][0]
	lat = content['latitude']
	lon = content['longitude']
	speed = content['speed']
	heading = content['direction']
	
	return lat,lon,speed,heading
    

def postData(lat,lon,speed,heading):
    #

	myobj = {
		'id': device_id,
		'lat': lat,
		'lon': lon,
		'timestamp': getTime(),
		'speed':speed,
		'heading':heading
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
	

    
	print("latnya %s longnya %s speednya %s headingnya  %s"  % (lat,lon,speed,heading))
	print(x.text)

def getTime():
  
    waktu = time.time()
    return int(waktu)

if __name__ == "__main__":
	while True:
		lat,lon,speed,heading = getData()
		if lat == 0 and lon == 0 and speed == 0 :
			print('data failed to retrieve')
		else:
			postData(lat,lon,speed,heading)
			time.sleep(delay)
		time.sleep(1)
        
    