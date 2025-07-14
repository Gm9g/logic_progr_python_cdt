###MVC

#model
###armazenar os numeros e calculos

#View
###realiza operações matematicas

#Controller
###validar entradas 


def mostrar_menu():
 print("\n---calculadora---")
print("1.adição")
print("2.subtração")
print("Sair")
print("------------")

def obter_numeros():
 while True:
  num1= float(input("digite o primeiro numero"))
  num2=float(input("digite o segundo numero"))
  return num1, num2
 except ValueError
print("Entrada Invalida. Por favor,"\
      "digite numeros válidos.")