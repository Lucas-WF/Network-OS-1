# -*- coding: UTF-8 -*- 

class Massa:
    def __init__(self, entrada, medidain, medidaout) -> None:
        self.entrada = entrada
        self.medidain = medidain
        self.medidaout = medidaout

    
    def calcular(self) -> int:
        try:
            valor = float(self.entrada)
        except:
            return "Valor Inválido"

        if self.medidain == self.medidaout:
            return valor
        else:
            medidas = {"mg":0.001, "cg":0.01, "dg":0.1, 'g':1, "dag": 10, "hg": 100, "kg":1000}
            return valor*medidas[self.medidain]/medidas[self.medidaout]