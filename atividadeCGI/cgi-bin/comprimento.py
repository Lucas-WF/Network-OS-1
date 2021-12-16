# -*- coding: UTF-8 -*- 

from models.comprimento_model import Comprimento
import cgitb
import cgi

cgitb.enable()

form = cgi.FieldStorage()

pin = form.getvalue("comprimento_p1")
pout = form.getvalue("comprimento_p2")
valor = form.getvalue("comprimento")

comp = Comprimento(valor, pin, pout)
resultado = comp.calcular()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print('<meta charset="utf-8">')
print("</head>")
print("""<body> <style>
h1{
    margin-top: 20%;
    text-align: center;
}

body{
    background-color: #808080;
}
</style>
""")
print(f"<h1>O seu resultado foi: {resultado} {pout}</h1>")
print("</body>")
print("</html>")