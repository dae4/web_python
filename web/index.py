#!/usr/bin/python3
print("content-type: text/html; charset=utf-8\n")
import cgi
import os 
import view
import html_sanitizer

sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if 'id' in form:
  pageId = form['id'].value
  description = open('data/'+pageId,'r').read()
  description = description.replace('<','&lt;').replace('>','&gt;')
  description = sanitizer.sanitize(description)
  update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
  delete_action ='''
        <form action="process_delete.py" method="post">
          <input type="hidden" name="pageId" value="{}">
          <input type="submit" value="delete">
        </form>
  '''.format(pageId)
else:
  pageId = "Welcome"
  description = "Hello, web"
  update_link =''
  delete_action=''


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
  {update_link}
  {delete_action}
  <h2> {title} </h2>
  <p> {docs} </p>
</body>
</html>
'''.format(title=pageId,
        docs=description,
        listStr=view.getList(),
        update_link=update_link,
        delete_action=delete_action))