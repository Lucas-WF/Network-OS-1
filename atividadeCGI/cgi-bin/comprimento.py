import cgitb
import cgi

cgitb.enable()

form = cgi.FieldStorage()

metro = form.getvalue("metro")
centimetro = form.getvalue("centimetro")

print("Content-Type: text/html")
print("<html>")
print("<body>")
print(f"<h1> {metro} e {centimetro}</h1>")
print("</body>")
print("</html>")
