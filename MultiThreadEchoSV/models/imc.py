class IMC:
    def __init__(self, weight, height, age):
        self.__weight = weight
        self.__height = height
        self.__age = age

    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    def calc(self) -> str:
        try:
            result = float(self.__weight) / (float(self.__height) ** 2)
            self.__age = float(self.__age)
            if 18.5 > result > 0:
                return "O resultado foi de {:.2f} - Abaixo do Peso".format(result)
            elif 18.5 <= result <= 24.9:
                return "O resultado foi de {:.2f} - Peso normal".format(result)
            elif 25 <= result <= 29.9:
                return "O resultado foi de {:.2f} - Sobrepeso".format(result)
            elif 30 <= result <= 34.9:
                return "O resultado foi de {:.2f} - Obesidade grau 1".format(result)
            elif 35 <= result <= 39.9:
                return "O resultado foi de {:.2f} - Obesidade grau 2".format(result)
            elif result <= 0:
                return "Dados inválidos"
            else:
                return "O resultado foi de {:.2f} - Obesidade grau 3".format(result)
        except ValueError:
            return "Dados inválidos"


if __name__ == "__main__":
    print("Classe IMC")
