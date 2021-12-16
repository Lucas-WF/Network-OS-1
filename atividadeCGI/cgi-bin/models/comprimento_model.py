class Comprimento:
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
            medidas = {"mm":0.001, "cm":0.01, "dm":0.1, 'm':1, "dam": 10, "hm": 100, "km":1000}
            return valor*medidas[self.medidain]/medidas[self.medidaout]