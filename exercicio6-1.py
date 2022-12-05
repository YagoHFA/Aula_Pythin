aMulher = 0
qMulher = 0
qHomem = 0
menorAltura = 9999999
maiorAltura = 0
for num in range(3):
    s = int(input("Digite 1 para homem " 
                  "Digite 2 para mulher "))
    a = float(input("Digite a altura "))
    if(a < menorAltura):
     menorAltura = a
    if(s == 2):
        aMulher += a 
        qMulher += 1
    if(s==1):
        qHomem += 1
    if(maiorAltura < a):
        maiorAltura = a  
        if(s==1):
            sexo = "Homem"
        else:sexo = "mulher" 
        
mediaMulher = aMulher / qMulher     
  
print(menorAltura)
print(mediaMulher)
print(qHomem)  
print(sexo)