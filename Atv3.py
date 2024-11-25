class Motor:
    def __init__(self, tipo, potencia):
        pass
        self.tipo = tipo
        self.potencia = potencia
        self.ligado = False
        
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return f"Motor {self.tipo}, de {self.potencia} cavalos ligado."
        return "O motor já está ligado."
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
            return f"Motor {self.tipo}, de {self.potencia} cavalos desligado."
        return "O motor já está desligado."

class Veiculo:
    def __init__(self, marca, modelo, ano):
        pass
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        self.movendo = False

    def imprimir(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

    def acelerar(self, incremento):
        self.velocidade += incremento
        self.movendo = True
        print(f"O veículo acelerou para {self.velocidade} km/h.")

    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade <= 0:
            self.velocidade = 0
            self.movendo = False
        print(f"O veículo freiou para {self.velocidade} km/h.")

    def mover(self):
        if not self.movendo:
            print("O veículo está parado. Acelere para movê-lo.")
        else:
            print("O veículo está em movimento.")

    def parar(self):
        self.velocidade = 0
        self.movendo = False
        print("O veículo parou.")

class Carro(Veiculo):
    def __init__(self, numero_de_portas, marca, modelo, ano, motor):
        super().__init__(marca, modelo, ano)
        self.numero_de_portas = numero_de_portas
        self.motor = motor

    def abrir_porta(self, porta):
        if 1 <= porta <= self.numero_de_portas:
            return f"Porta {porta}, do {self.marca} aberta."
        return "Número de portas inválido."
    def set_marca(self, marca):
        self.marca = marca 
    def get_marca(self):
        return self.marca
    
    def set_modelo(self, modelo):
        self.modelo = modelo
    def get_modelo(self):
        return self.modelo
    def set_ano(self, ano):
        
        self.ano = ano
    def get_ano(self):
        return self.ano
    
    def set_motor(self, motor):
        self.motor = motor
    def get_motor(self):
        return self.motor
    

# Exemplo
motor_v8 = Motor("V8", 488)
carro = Carro(4, "Ford", "Mustang", 2023, motor_v8)
carro.imprimir()
carro.acelerar(100)
carro.frear(40)
carro.mover()
carro.parar()
print(carro.motor.ligar())
print(carro.motor.desligar())
print(carro.abrir_porta(1))
carro.set_marca("Ferrari")
print("A nova marca é: " + carro.get_marca())
carro.set_modelo("Italia 458")
print("O modelo do carro é: " + carro.get_modelo())
carro.set_ano("2011")
print("O ano do carro é: " + carro.get_ano())
