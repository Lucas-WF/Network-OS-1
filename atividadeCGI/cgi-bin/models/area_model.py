# -*- coding: UTF-8 -*- 

class Area:
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
            medidas = {"mm²": 0.000001, "cm²": 0.0001, "dm²": 0.01, "m²":1, "are": 100, "ha": 10000, "km²": 1000000}
            return valor*medidas[self.medidain]/medidas[self.medidaout]