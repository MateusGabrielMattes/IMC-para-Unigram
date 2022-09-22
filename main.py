peso = float(input("Informar Peso: "))

altura = float(input("Informar Altura: "))

imc = peso / altura ** 2

print("Seu IMC é:", imc)

if(imc < 18.5):
  print("Baixo peso!")

elif(imc >= 18.5 and imc < 25):
  print("Peso adequado!")

elif(imc >= 25 and imc < 30):
  print("Sobrepeso!")

else:
  print("Obesidade!")
