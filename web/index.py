#!C:\Users\jihye\AppData\Local\Programs\Python\Python310\python.exe
print("content-type: text/html; charset=utf-8\n")
import cgi 
form = cgi.FieldStorage()
pageId = form['id'].value
print('''<html>
<head>
  <title>WEB1 - Welcom</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    <li><a href="index.py?id=HTML">HTML</a></li>
    <li><a href="index.py?id=CSS">CSS</a></li>
    <li><a href="index.py?id=JavaScript">JavaScript</a></li>
  </ol>
  <h2>{title}</h2>
  <p>
  <img src="woojoo.jpg" width="100%">
  </p>
</body>
</html>'''.format(title=pageId))