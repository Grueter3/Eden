
class Hello:
    def __init__(self,world,universe,galaxy,cosmos):
        self.world = world
        self.universe = universe
        self.galaxy = galaxy
        self.cosmos = cosmos

    def sun(self):
        return '{self.world} is floating with the sun'

hellomikeworld =  'Earth'
hellomikeuniverse = ' The One'
hellomikegalaxy = ' The Milky Way'
hellomikecosmos = ' Isnt that the same as Galaxy?'

hellomike = Hello(hellomikeworld,hellomikeuniverse,hellomikegalaxy,hellomikecosmos)

print('Hello what planet are you from: {}'.format(hellomike.world))
print('What Universe?{}'.format(hellomike.universe))
print('What Galaxy?{}'.format(hellomike.galaxy))
print('How about cosmos?{}'.format(hellomike.cosmos))

#-------------
bullets = ['50cal','.22','.45','9mm']

for bullet in bullets:
    if bullet == '50cal':
        print( bullet +' Nice gun Schwartzanager')
        continue
    else:
        print (bullet + ' Nice gun Bond')



#----------
weight = int(input('Enter your weight (lbs):'))

if weight <160:
    print('keep up the good work')
elif weight < 200:
    print ('Your on your way')
else:
    print('find a treadmill')

#----------
### not working 
weight = 20
numb = 0

while weight < numb:
    print (numb)
    numb += 1

    if numb < 10:
        break


#----------
num1 = 345.6789
num2 = 222.2222

print(f'num1 is {num1:.2f} and num2 is {num2:.2f}')

#------

age = input ('how old are you? (young/middleage/old):')
intellegence= input ('how smart are you?(wicked smart/stupid/sharp):')
print('You are',  age, 'and', intellegence)

answer = input('want to know the hypotanoose of your triangle? (y/n)')

if answer == 'y': 

    base = int(input('enter base'))
    height = int(input('enter height'))
    hypotanoose = (base**2 + height**2)
    print('the hypotanoose of your triangle is', hypotanoose)

else:
    print('fine then')

#--------------- split method not working 
greeting = 'hello kind lady what is your name'
greeting.split(' ')

print(greeting)

#-------------
people = ['sam', 'max', 'peter']
people.append('tom')
print(people)
#---------------
people = ['sam', 'max', 'peter']
del(people[2])
print(people)
#--------------------
people = ['sam', 'max', 'peter']
people.pop(0)
print(people)