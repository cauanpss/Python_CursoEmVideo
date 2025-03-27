#Contagem regressiva de 10, 0, pausa de 1s (estouro de fogos de artifício).
import emoji
import time
print('Os fogos vão estourar em:')
for count in range (10, 0, -1):
    print(count)
    time.sleep(1) #Aguardar tempo na contagem.
for p in range (0,4):
    print(emoji.emojize(':fireworks:'':fireworks:'':fireworks:'':fireworks:'))