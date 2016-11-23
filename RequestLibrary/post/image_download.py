import requests

url = "https://www.gxsoftware.com/upload/a9739508-f5ae-4973-90c2-f1da6ba55e42_image7012640870507305629.jpg"
response = requests.get(url)
if response.status_code == 200:
    with open("/home/asif/Downloads/04e17a17-d0bc-4f02-90a5-362719eab5f0_Implementaties-1024.jpg", 'wb') as f:
        f.write(response.content)
