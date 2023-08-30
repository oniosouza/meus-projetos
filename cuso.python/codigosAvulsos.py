#TOMADA DE DECIOSOES

nomeAluno = str(input("digite o nome do aluno \n"))
sexoAluno = str(input("digite o sexo do aluno \n"))
cidadeAluno = str(input("digite a cidade do aluno \n"))

nota1 = float(input("digite a primeira nota:"))
print("a primeira nota é:", nota1, "\n")

nota2 = float(input("digite a segunda nota:"))
print("a segunda nota é:", nota2, "\n")

nota3 = float(input("digite a terceira nota:"))
print("a terceira nota é:", nota3, "\n")

soma = nota1 + nota2 + nota3


media = (nota1 + nota2 + nota3)/3

if(media >= 6):
    print("aluno:",nomeAluno,"\n","sexo:",sexoAluno,"\n","cidade:",cidadeAluno,"\n","esta aprovado")
else:
    print("aluno:",nomeAluno,"\n","sexo:",sexoAluno,"\n""cidade:",cidadeAluno,"\n","esta reprovado")
