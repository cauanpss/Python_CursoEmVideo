frase = 'Esta é uma frase de 33 caracteres ase ase'
frase[1:10:2]
print(len(frase))
print(frase.find('ase'))
print('curso' in frase)
print('frase' in frase)
print(frase.find('ase'))
print(frase.replace('ase','cauan'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase2 = 'Curso em vídeo Python'
frase3 = frase2.split()
print(' '.join(frase3))

