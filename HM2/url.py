import urllib.request

html_res = urllib.request.urlopen('http://www.python.org/')
html_content = html_res.read()
file = open("server/www.python.org.html", 'w')
file.write(html_content.decode())
file.close()    