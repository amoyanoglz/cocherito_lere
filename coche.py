# - Coche
#     - marca : str
#     - modelo : str
#     - matricula : str
#     - motor: { tipo | combustible | kw_bat }
#     - __str__()

class Coche:
    def __init__(self, marca, modelo, matricula):

        TIPO_MOTOR = (
            "cambustion",
            "hibrido",
            "electrico"
        )

        TIPO_COMBUSTIBLE = (
            "gasolina",
            "gasoil",
            "gas"
        )

        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula


    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} - [{self.matricula}]"
