import string

notaDaDis = 0
notaTotal = 0
media = ""
mediaTotal = ""
qAluno =  int(input("Coloque a quantidadxe de alunos que estão cursando o 3º semestre: "))
for i in range(qAluno):
    media = 0
    notaTotal = 0
    qDis = int(input("Coloque a quantidade de disciplinas cusradas no 2º semestr: "))
    for x in range(qDis):
            notaDaDis = float(input("Coloque a nota da disciplina: "))
            notaTotal += notaDaDis
            media =notaTotal / qDis
     
  
   
    mediaTotal += "Aluno" + str(i + 1) + " " + str(media) + "\n"   
print(mediaTotal) 
   