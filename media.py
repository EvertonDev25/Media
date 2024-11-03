Nota1 = float(input('Digite a 1°Nota: '))
print(Nota1)

Nota2 = float(input('Digite a 2°Nota: '))
print(Nota2)

Media = (Nota1 + Nota2) / 2
print('Media final: \n{}'.format(Media))

if Media >= 6:
    print('Aluno Aprovado!')
else:
    print('Aluno Reprovado!')
