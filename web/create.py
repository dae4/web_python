#!/usr/bin/python3
print("content-type: text/html; charset=utf-8\n")
import cgi
import os 
import view

form = cgi.FieldStorage()
if 'id' in form:
  pageId = form['id'].value
  decription = open('data/'+pageId,'r').read()
else:
  pageId = "Welcome"
  decription = "Hello, web"


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
  <form action="process_create.py" method="post">
    <p><input type="text" name="title" placeholder="title"</p>
    <p><textarea rows="4" name="description"placeholder="description"></textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
</html>'''.format(title=pageId,docs=decription,listStr=view.getList()))
