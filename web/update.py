#!C:\Users\jihye\AppData\Local\Programs\Python\Python310\python.exe
print("content-type: text/html; charset=utf-8\n")
import cgi
import os 

form = cgi.FieldStorage()
if 'id' in form:
  pageId = form['id'].value
  description = open('data/'+pageId,'r').read()
else:
  pageId = "Welcome"
  description = "Hello, web"
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
  <form action="process_create.py" method="post">
    <p><input type="text" name="title" placeholder="title"</p>
    <p><textarea rows="4" name="description"placeholder="description"></textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
</html>'''.format(title=pageId,docs=description,listStr=listStr))