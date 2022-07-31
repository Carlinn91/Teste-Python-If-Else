# Desafio If, Else

# Criar um programa que dependendo da temperatura (em celsius) do Steak 
# ele retorna o ponto de cozimento em portugues. O usuario deverá fornecer a temperatura

# # Temperaturas - Cozimento
# 120ºF ou 48ºC - Selada
# 130ºF ou 54ºC - Ao ponto para o mal
# 140ºF ou 60ºC - Ao ponto
# 150ºF ou 65ºC - Ao ponto para o bem
# 160ºF ou 71ºC - bem passada


temp_cel = int(input('Qual é a temperatura da carne? ')) #Tranformou em integer

if temp_cel < 48:
    print('Cozinhar por mais tempo')
elif temp_cel in range(48,53):
    print('Selada')
elif temp_cel in range(54,59):
    print('Ao ponto para o mal')
elif temp_cel in range(60,64):
    print('Ao Ponto')
elif temp_cel in range(65,70):
    print('Ao ponto para o bem')
else:
    temp_cel >= 71
    print('Bem passada!')
