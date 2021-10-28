import urllib.request
import os.path

print("\nSeyed Hadi Ranjbar :)\n")

links = [
    "https://stackoverflow.com/"
    "https://github.com/" ,
    "http://www.python.org/" ,
    "https://www.educba.com/" ,
    "https://extensions.gnome.org/" ,
    "https://wordpress.org/" ,
    "https://cpanel.net/" ,
    "https://cafebazaar.ir/" ,
    "https://myket.ir",
    "https://basalam.com/"
]

url = links[0]

html_res = urllib.request.urlopen(url)
html_content = html_res.read()
url = url.replace("https://", "")
url = url.replace("http://", "")
url = url.replace("/", "")
path = os.path.dirname(__file__)
file = open(os.path.join(path, "server/" + url + ".html"),"w", encoding='utf-8')
file.write(html_content.decode())
file.close()    