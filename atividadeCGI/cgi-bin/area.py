from models.area_model import Area
import cgitb
import cgi

cgitb.enable()

form = cgi.FieldStorage()

pin = form.getvalue("area_p1")
pout = form.getvalue("area_p2")
valor = form.getvalue("area")

comp = Area(valor, pin, pout)
resultado = comp.calcular()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print('<meta charset="utf-8">')
print("</head>")
print("<body>")
print(f"<h1>{resultado}</h1>")
print("</body>")
print("</html>")
