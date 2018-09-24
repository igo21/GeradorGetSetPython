def gerar(vetor):
    for i in range(len(vetor)):
        gete = ''
        sete = ''
        gete = "def " + vetor[i] + "(self):\n\treturn self.__" + vetor[i]
        print("@property")
        print(gete)
        sete = "def " + vetor[i] + "(self,valor):\n\tself.__" + vetor[i] + "=valor"
        print("@" + vetor[i] + ".setter")
        print(sete)


atr = []
n = int(input("Número de atributos..: "))
for i in range(n):
    nn = input()
    atr.append(nn)
gerar(atr)
