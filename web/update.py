#!/usr/bin/python3
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
  <form action="process_update.py" method="post">
    <p><input type="hidden" name="pageId" placeholder="pageId" value="{form_defalut_title}"</p>
    <p><input type="text" name="title" placeholder="title" value="{form_defalut_title}"</p>
    <p><textarea rows="4" name="description"placeholder="description" >{form_defalut_description}</textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
</html>'''.format(title=pageId,docs=description,listStr=listStr,form_defalut_title=pageId, form_defalut_description=description))