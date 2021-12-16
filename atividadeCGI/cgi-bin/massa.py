from models.massa_model import Massa
import cgitb
import cgi

cgitb.enable()

form = cgi.FieldStorage()

pin = form.getvalue("massa_p1")
pout = form.getvalue("massa_p2")
valor = form.getvalue("massa")

comp = Massa(valor, pin, pout)
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
