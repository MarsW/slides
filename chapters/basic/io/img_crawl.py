import requests
img_src = "https://tw.pyladies.com/images/header.jpg"
img_response = requests.get(img_src)
img = img_response.content
fo = open("photo.jpg","wb")
fo.write(img)
fo.close()