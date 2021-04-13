from random import randint
from time import sleep

computador = randint(0,5)
usuario = int(input("Adivinhe o número: "))

print("Hummm... verificando se voce acertou...")
sleep(3)

if computador == usuario:
    print("PARABENS, VOCE GANHOU")
else:
    print("QUE PENA, VOCE PERDEU!")
    
print(f"""
    O computador escoleu: {computador}
    E voce escolheu: {usuario}
""")
