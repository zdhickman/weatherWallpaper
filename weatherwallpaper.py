import pycurl, string, time, ctypes

tornado = ['Tornado']
hurricane = ['Tropical Storm', 'Hurricane']
thunder = ['Severe Thunderstorms', 'Thunderstorms', 'Isolated Thunderstorms', 'Scattered Thunderstorms']
rain = ['Freezing Drizzle', 'Drizzle', 'Freezing Rain', 'Showers', 'Scattered Showers', 'Light Drizzle']
snow = ['Scattered Snow Showers', 'Mixed Rain and Hail', 'Heavy Snow', 'Mixed Rain and Snow', 'Mixed Rain and Sleet', 'Mixed Snow and Sleet', 'Snow Flurries', 'Light Snow Showers', 'Blowing Snow', 'Snow', 'Hail', 'Sleet']
cloudy = ['Cloudy', 'Mostly Cloudy (Night)', 'Mostly Cloudy (Day)', 'Partly Cloudy (Night)', 'Partly Cloudy (Day)', 'Partly Cloudy']
fog = ['Fog', 'Foggy', 'Dust', 'Haze', 'Smoky']
wind = ['Windy', 'Wind', 'Blustery']
clear = ['Clear', 'Clear (Night)', 'Clear (Day)', 'Fair (Night)', 'Fair (Day)', 'Hot', 'Cold']



# get_weather takes a yahoo weather ID and returns a weather struct
def get_weather(n):
	c = pycurl.Curl()
	c.setopt(pycurl.URL, "http://weather.yahooapis.com/forecastrss?w=" + str(n))
	c.setopt(pycurl.HTTPHEADER, ["Accept:"])
	import StringIO
	b = StringIO.StringIO()
	c.setopt(pycurl.WRITEFUNCTION, b.write)
	c.setopt(pycurl.FOLLOWLOCATION, 1)
	c.setopt(pycurl.MAXREDIRS, 5)
	c.perform()
	b.getvalue()

	n = 0

	b.seek(0)
	for line in b:
		if n == 2:
			m = line
			n = 0
		if n == 1:
			l = line
			n = 0
		if line == "<b>Current Conditions:</b><br />\n":
			n = 1

	l = l.replace("<BR />\n", "")
	c_1 = (l.split(',', 1))[0]
	c_2 = (l.split(',', 1))[1]
	t = time.localtime()
	t = t.tm_hour
	weather = {'hour' : t, 'conditions' : c_1, 'temp' : c_2}

	return weather
	
def get_time_string(n):
	if n < 5 or n >= 20:
		time = "night"
	elif n >= 5 and n < 9:
		time = "morning"
	elif n >=9 and n < 17:
		time = "day"
	else:
		time = "evening"
		
	return time

def get_condition_filter(c):
	if any(c in s for s in snow):
		return "snow"
	elif any(c in s for s in tornado):
		return "tornado"
	elif any(c in s for s in hurricane):
		return "hurricane"
	elif any(c in s for s in rain):
		return "rain"
	elif any(c in s for s in thunder):
		return "thunder"
	elif any(c in s for s in clear):
		return "clear"
	elif any(c in s for s in cloudy):
		return "cloudy"
	elif any(c in s for s in fog):
		return "fog"
	elif any(c in s for s in wind):
		return "wind"
	else:
		return "clear"
		
def read_location_code(config_file):
	line = config_file.readline()
	line = line[:-2]
	line = line[9:]
	if line == "":
		return 2354302  # Boston, MA default
	return int(line)
	
def weather_desktop(w_struct):
	time = get_time_string(w_struct['hour'])
	condition = get_condition_filter(w_struct['conditions'])
	path = "./wallpapers/" + condition  + "/" + time + "/wallpaper.jpg"
	return path
	
def do_paper_change(path):
	ctypes.windll.user32.SystemParametersInfoA(20, 0, path , 0)
	print path + "    ."

f = open('./config.sys', 'r')
location_code = read_location_code(f)	
do_paper_change(weather_desktop(get_weather(location_code)))