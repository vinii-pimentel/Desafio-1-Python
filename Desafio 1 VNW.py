#
#---- PARA EVITAR RODAR TUDO DE UMA VEZ (pode dar erro em variáveis duplicadas) SÓ IR RETIRANDO O COMENTÁRIO DA QUESTÃO QUE DESEJA RODAR! ----
#

#------------ MISSÃO 1 ------------#
# nota = int(input("Inserir nota do aluno: "))
# if nota >= 6:
#  print("Aluno aprovado")
# else:
#  print ("Aluno Reprovado")

#------------ MISSÃO 2 ------------#

# idade = int(input("Digite a sua idade: "))

# if idade >= 16:
#  print ("Pode votar")

# else:
#  print ("Ainda não é hora amiguinho")

#------------ MISSÃO 3 ------------#
# nota = int(input("Inserir nota do aluno: "))
# if nota >= 101 or nota <0:
#  print ("Nota inválida")
# elif nota >= 90 and nota <= 100:
#  print ("Parabéns, você tirou A!")
# elif nota >= 80 and nota <= 89:
#  print ("Muito bem, você tirou B.")
# elif nota >= 70 and nota <= 79:
#  print ("Bom trabalho, você tirou C.")
# elif nota >= 60 and nota <= 69:
#  print ("Fique atento, você tirou D.")
# elif nota <= 59:
#  print ("Estude um pouco mais, você tirou F.")
# else:
#  print ("Nota inválida")

#------------ MISSÃO 4 ------------#
# n1 = int(input("Digite o primeiro número para a soma: "))
# n2 = int(input("Digite o segundo número para a soma: "))
# soma = n1 + n2
# print(soma)

#------------ MISSÃO 5 ------------#
# senha = input("Digite sua senha: ")
# if senha == "Python123":
#  print("Senha Correta")
# else:
#  print("Senha Incorreta")
 ##### sério que a 5 é mais fácil que a 1, Vini? hehe

 #------------ MISSÃO 6 ------------#
# num = 1
# while num <= 10:
#  print(num)
#  num += 1

#------------ MISSÃO 7 ------------#
# lista = [8,3,10,1,5]
# lista.sort()
# print(lista)

#------------ MISSÃO 8 ------------#
# mytuple = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
# print(mytuple[0],mytuple[-1])

#------------ MISSÃO 9 ------------#
# def double(n):
#     dobro = n * 2
#     print("O dobro de", n, "é:", dobro)

# num = double(int(input("Inserir número que deseja dobrar: ")))

#------------ MISSÃO 10 ------------#
def contador(n):
 num = len(n)
 print("O nome", n ,"tem", num, "letras!")

nome = contador(input("Insira o nome que deseja saber o número de letras que ele contém: "))
