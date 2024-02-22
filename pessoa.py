# Crie uma classe que modele uma Pessoa, tendo como atributos nome, idade, peso e altura, e tendo como métodos envelhecer (idade recebe mais um a cada ano) e crescer (altura recebe 0,5 cm por ano até idade de 21 anos).

class pessoa:
    def __init__(self, nome, idade, altura, peso, anos):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.anos = anos
    
    def envelhecer(self, anos):
        self.idade += anos
       
    def crescer(self, anos):
        if self.idade < 21:
            self.altura += 0.005*anos
            
    def dados(self):
        print(self.nome, self.idade, self.altura, self.peso)

humano = pessoa(nome = input("Digite seu nome: "), idade = int(input("Informe sua idade: ")), altura = float(input("Informe sua altura: ")), peso = float(input("Informe seu peso: ")), anos = int(input("Informe quantos anos que vc queira saber: ")))
humano.envelhecer(humano.anos)
humano.crescer(humano.anos)
humano.dados()
