import random
VI = ['Covaxin','Covisheild','Sputnik']
v1 = random.choice(VI)

VU = ['Pfizer','Moderna','Johnson & Johnson',]
v2 = random.choice(VU)

VB = ['Pfizer','Astrazeneca-Oxford','Moderna','Johnson & Johnson']
v3 = random.choice(VB)

name = input("What's your name: ")
country = input('Which country you resides: ').upper()

if country == 'BRITAIN':
    print(f'Hi {name} the vaccine which is suitable for you is {v3}')
elif country == 'INDIA':
    print(f'Hi {name} the vaccine which is suitable for you is {v1}')
else:
    print(f'Hi {name} the vaccine which is suitable for you is {v2}')

print(('Stay safe!! Stay happy'))