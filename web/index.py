#!/usr/bin/python3
print("content-type: text/html; charset=utf-8\n")
import cgi
import os 

form = cgi.FieldStorage()
if 'id' in form:
  pageId = form['id'].value
  description = open('data/'+pageId,'r').read()
  update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
else:
  pageId = "Welcome"
  description = "Hello, web"
  update_link =''
files = os.listdir('data/')
listStr =''
for item in files:
  listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

print('''<html>
<head>
  <title>WEB1 - Welcom</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="create.py">create</a>
  <a {update_link} </a>
  <h2> {title} </h2>
  <p> {docs} </p>
</body>
</html>'''.format(title=pageId,docs=description,listStr=listStr,update_link=update_link))