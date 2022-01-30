son1 = 1
while son1<=5:
     print(son1,end=' ')
     son1 = son1+1
print('Kritilgan sonni kvadratga oshiruvchi dastur
')
savol = 'Istalgan sonni kiriting'
savol +='(To`xtatish uchun "exit" deb yozing): '
qiymat = ''
while qiymat !='exit':
    qiymat = input(savol)
    if qiymat !='exit':
        print(float(qiymat)**2)
print('Kritilgan sonni kvadratga oshiruvchi dastur')
savol = 'Istalgan sonni kiriting'
savol +='(To`xtatish uchun "exit" deb yozing): '
qiymat = ''
while qiymat !='exit':
    qiymat = input(savol)
    if qiymat !='exit':
        print(float(qiymat)**2)
print("Yoqritgan Kitobingiz nomini kiriting")
kitob ="Istalgan kitob \n"
kitob +="Dasturni to`xtatish uchun 'sotp'ni kiriting: "
Qiymat = ''
while Qiymat != 'stop':
    Qiymat = input(kitob)
    if Qiymat != 'stop':
        print(Qiymat)
print("Istalgan Kitobingiz nomini kiriting")
kitob = 'Kitob nomini kiriting>>>'
kitob += "(Dasturni to`xtatish uchun 'exit','quit' ni kiriting):"
qiymat = True
while qiymat:
    qiymat = str(input(kitob))
    if qiymat == 'exit' or qiymat == 'quit':
        qiymat = False
    else:
        qiymat =int(qiymat)
        if qiymat<=7:
            print("Assalomu Alaykum sizga muzayga kirish narxi 2000 so`m")
        elif (qiymat>7 and qiymat<18):
            print("Assalomu Alaykum sizga muzayga kirish narxi 3000 so`m")
        elif (qiymat>18 and qiymat<65):
            print("Assalomu Alaykum sizga muzayga kirish narxi 10000 so`m")
        elif (qiymat>65):
            print("Assalomu Alaykum sizga muzayga kirish narxi 10000 so`m")
        else:qiymat == False

savol = 'kiritilgan sonni ildizini qaytaruvchi dastur .\n'
savol += 'musbat son kiriting '
savol +="(Dasturni to`xtatish uchun 'exit' deb yozing '): "
while True:
    qiymat = input(savol)
    if qiymat<'0':
        continue
    elif str(qiymat)=='exit':
        break
    else:
        ildiz = float(int(qiymat)**0.5)
        print(f"{qiymat} - ni ildizi {ildiz}")
ismlar = []
print("Yaqin do`slarimizni  ro`yxatini tuzamiz.")
n = 1
while True:
    savol = f"{n} do`stingizni ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    javob = input(f"Yana ism qo`shasizmi ? (xa/yo`q)")
    if javob =='xa':
        n+=1
    else:
        break
print("Ro`yxat tuzildi .")
for ims in ismlar:
    print(ims)
print("Do`slaringiz yoshini saqlaymiz.")
doslar = {

}
ishoralar = True

while True:
    ism = input('Do`stingiz ismini kiriting: ')
    yosh = input(f"{ism.title()}ni Yoshini kiriting: ")
    doslar[ism]=int(yosh)
    javob = input("Yana qo`shasizmi?(ha/Yo`q):")
    if javob == "Yo`q":
        ishoralar = False
        break
for key,valu in doslar.items():
    print(key , valu)
cars = ['nexia','lacetti','nexia','toyota','malibu','nexia','tiko']
while 'nexia' in cars:
    cars.remove('nexia')
print(cars)
talabalar = ['hasan','husan','olim','nodira','shakarxon']
baxolar = {}
while talabalar:
    talaba = talabalar.pop()
    boho = input(f"{talaba.title()}ning baxosini kiriting: ")
    print(f"{talaba.title()} Baxolandi")
    baxolar[talaba] = boho
print("Talabalar kundaligi")
for key,qiymat in baxolar.items():
    print(f"{key} bohosi {qiymat}")
print(" e-bozorga xush kelibsiz ")
son = float(input('juft son kiriting :'))
if int(son)%2==0:
    print("raxmat")
else:print('xatolig')
yosh = int(input("yoshingiz nechida ?"))
if (yosh>4) and (yosh>60):
    narx = 0
elif yosh<18:
    narx = 1000
else:
    narx = 20000
print(f"chipa narxi {narx}")
yosh = int(input("yoshingizni kiriting: "))
try:
    yosh = int(yosh)
    print('')
except ValueError:
    print(yosh)
else:
#     print('siz adashdiz')
def salom_ber():
    """Salom Beruvchi funksiya"""
    print("Assalomu Alaykum !")

def tugulgan_yilni_xisoblash(Hozirgi_yil,yosh):
    """foydalanuvchi tug`ilgan yilini xioblovchi funksiya"""
    print(f"{Hozirgi_yil-yosh} siz shu yilda tug`ulgansiz")
tugulgan_yilni_xisoblash(Hozirgi_yil=2022,yosh=90)
def xningNchidarjasi(x,n):
    """x ni n chi darajasini aniqlovchi funksiya"""
    print(f"{x**n }- x ning n chi darajasi")
xningNchidarjasi(x=2,n=1)
def bolinish(n):
    for i in range(2,10+1):

        if n % i == 0:
            print(f"2-dan 10-gacha bo`lgan sonlar ichida siz kiritgan songa qoldiqsiz bo`linadigan solar {i} ")
bolinish(n=4)
def avto_info(make,model,rangi,korobka,yili,narxi=None):
    avto={
        'kampaniya':make,
        'model':model,
        'rangi':rangi,
        'karobka':korobka,
        'yil':yili,
        'narxi':narxi
    }
    return avto

avto1=avto_info('Gm','Malibu','Qora','Avtomat',2018,20000)

avto2=avto_info('Gm','Nexi','Oq','Mexanik',2013,5000)

avtolar = [avto1,avto2]
print("online bozordagi mavjud mashinalar:")

for avto in avtolar:
    if avto['narxi']:
        print(f"{avto['rangi']}{avto['model']}.Narxi:{avto['narxi']}")
    else:
        print(f"{avto['rangi']}{avto['model']}.Narxi:Noma`lum")


def oraiq(min,max,qadam):
    sonlar=[]
    while min<max:
        sonlar.append(min)
        min +=qadam
    return sonlar
print(oraiq(1,21,2))
def avto_info(make,model,rangi,korobka,yili,narxi=None):
    avto={
        'kampaniya':make,
        'model':model,
        'rangi':rangi,
        'karobka':korobka,
        'yil':yili,
        'narxi':narxi
    }
    return avto
print("Saytimizdagi avtolar ro`yxatini shakllantiramiz,")
avtolar = []
while True:
    print("\nQuyidagi ma`lumotlarni kiriting" , end=' ')
    kompaniya=input('Ishlab chiqaruvchi: ')
    model = input('Modeli: ')
    rangi = input('Rangi: ')
    korobka = input('Korobka: ')
    yili = input('Yili: ')
    narxi = input('Narxi: ')
    avtolar.append(avto_info(make=kompaniya,model=model,rangi=rangi,korobka=korobka,yili=yili,narxi=narxi))
    javob = input("Yana qo`shmoqchimisiz (yes/no)")
    if javob=='no':
        break
    else:
        continue
def registratsiya(ism,familya,yil,manzil,email,tel,kasbi,malumoti):
    register ={
        'ism':ism,
        'fam':familya,
        'yil':yil,
        'manzil':manzil,
        'email':email,
        'tel':tel,
        'kasbi':kasbi,
        'malumoti':malumoti
    }
    return register
print("Assalomu Alaykum  Iltimos ro`yxatdan o`ting")
register = []
while True:
    print("\nQuyidagi Malumotlarni to`ldirihingizni So`raymiz")
    ism = input('Ismni kiriting: ')
    fam = input('Famni kiriting: ')
    yil = input('Qachon tug`ulgansiz: ')
    manzil =input('Manzilni kiritin: ')
    email = input('Elektron manzilni kirting: ')
    tel = input('Telefon raqam: ')
    kasbi = input('Kasbingiz nima?:')
    malumot = input('Malumotingiz qanday?:')
    javob = input('Malumotlar to`g`ri yozilgan bo`lsa (yuborish/bekorqilish): ')
    register.append(registratsiya(ism,fam,yil,manzil,email,tel,kasbi,malumot))
    for  shaxs in register:
        if shaxs['tel']:
            shaxs['tel']=tel
        else:
            shaxs['tel'] = 'Noma`lum'
        print(f"{shaxs['ism']}\n{shaxs['fam']}\n{shaxs['yil']}\n{shaxs['manzil']}\n{shaxs['email']}\n{shaxs['tel']}\n{shaxs['kasbi']}\n{shaxs['malumoti']}")
    if javob =='yuborish':
        continue
    else:

        break
son =[]
def nush(a,b,c):
    son.append(a)
    son.append(b)
    son.append(c)
    print(max(son))
    return son
nush(5,8,9)
def tubsonlar(a,b):
    if a>1:
        for i in range(a,b):
            birinchi = i%2
def tubsonlar(a):
    for l in range ( 2, 7 ):
        if l != 4 and l !=6:
            print ( l )
    for i in range(2,a+1):
        if i%2!=0:
            if i%3!=0:
                if i%5!=0:
                    if i%7!=0:
                        print(i)
tubsonlar(30)
def fibonachi(nterms):
    n1,n2 =0,1
    count = 0
    if nterms <=0:
        print('eror')
    elif nterms==1:
        print(n1)
    else:
        print('fibonachi sonlar')
        while count<nterms:
            print(n1)
            nth = n1+n2
            n1=n2
            n2=nth
            count +=1
fibonachi(10)
def bahola(ismlar):
    baholar ={}
    while ismlar:
       ism = ismlar.pop()
       baho = int(input(f'{ism.title()} ga baho qo`ying : '))
       baholar[ism] = baho
    print(baholar)
    return bahola
try:
    talabalar = {'ali','vali','hasan','husan'}
    bahola(talabalar)
except:
    print(bahola(talabalar).)
def matin(royxat):
    dialoglar = {}
    while royxat:
        ro = royxat.pop()
        dialoglar[ro]=''
        lisat=list(dialoglar)
        for n in lisat:
            print(n.title())
matin('vali')
def matin (royxat):
    lista = []
    while royxat:
        roy = royxat.pop()
        lista.append(roy)
        for a in  lista:
            print(a.title())
royxat = [
    'alisher',
    'g`anisher',
    'egamberdi',
    'lazizbek'
]
matin(royxat)
def summa(*sonlar):
    """Kiritilgan soni Yig`indisini qaytaruvchi function."""
    yigindi = 0
    for i in sonlar:
        yigindi+=i
    return yigindi
print(summa(10,12))

def san(x,y,*sonlar):
    """Kiritilgan sonni qoshib beradigan dastur"""
    return x+y+sum(sonlar)
print(san(1,2,10,12))
def avto_info(kompaniya,model,**malumotlar):
    """Avto haqida ma`lumotlarni lug`at kerinishida qaytaruvchi function"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar
print(avto_info(kompaniya='Gm',model='malibu'))
def kopaytma(*sonlar):

def multiply(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma

print(multiply(4,5,6))
def mull(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma*=son
    return kopaytma
print(mull(1,2,3,4,5,6))
def talaba(ism,fam,**malumotlar):
    malumotlar['ism']=ism
    malumotlar['fam']=fam
    return malumotlar
print(talaba(ism='Javohir',fam='Oltmishev',Kurs=4,))

import avto_info_mod
avto1 = avto_info_mod.avto_info(make='GM',model='Malibu',karobka='Avtomat',rang='Oq',yil=2002,narx=23000)
avto_info_mod.info_print(avto1)
import math,random as r
from math import pi
print(pi)
print(math.log2(100))

ismlar = [ 'Anvar','g`ulom','Umidjon','Ahadjon']
ism =r.choice(ismlar)
print(ism)
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
print(all(ismlar))
from struct import *
pack('hhl', 1, 2, 3)
unpack('hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03')
calcsize('hhl')
import math
uzunlik = lambda pi,r:2*pi*r
print(uzunlik(math.pi,10))
kavadirat = lambda x: x**2
print(kavadirat(20))
def daraja(n,x):
    return lambda x: x**n
kvadiirat = daraja(2)
kub = daraja(3)
print(f"2ni kvadirato{kvadiirat} teng \n 2 nigng kubi {kub}ga teng ")

from math import sqrt
sonlar = list(range(1,10))
ildizlar = list(map(sqrt,sonlar))
print(ildizlar)

berilgan sonlarning kvadiratini qaytaruvchi funksiya yozmiz
sonlar = list(range(1,11))
def aq(x):
    return x*x
print(list(map(aq,sonlar)))
kvdaratlar = list(map(lambda x: x*x,sonlar))
print(kvdaratlar)
a = [1,3,2,]
b = [4,5,8]
a_plus_b = list(map(lambda x,y: x+y,a,b))
print(a_plus_b)
ismlar = ['hasan','husan','umar','abubakir']
print(list(map(lambda x:x.upper(),ismlar)))

import random as r
sonlar = r.sample(range(100),10)
def juftmi (x):
    return x%2==0
juftsonlar  = list(filter(juftmi,sonlar))
print(sonlar)
print(juftsonlar)
import random as r
sonlar = r.sample(range(100),10)
juftlar = list(filter(lambda x: x%2==0,sonlar))
print(juftlar)
mevalar = ['olma','anor','behi','banan','mandarin','ab']
tekshir = list(filter(lambda meva:meva.startswith('b'),mevalar))
print(tekshir)
mevalaar = list(filter(lambda meva:len(meva)>=4,mevalar))
st = list(filter(lambda mevali:mevali.startswith('a') and mevali.endswith('r'),mevalaar))
print(mevalaar,st)
sonlar = list(range(1,100))

kop = list(map(lambda  x: x*10,sonlar))
print(kop
a = 8
b = 3
xisonla = lambda x ,y : x+y
print(xisonla(a,b))
import  random as r
sonlar  = r.sample(range(1000),10)
kavdirart = list(map(lambda x : x**2,sonlar))
print(kavdirart)
toqsonlar = list(filter(lambda s:s%2!=0,sonlar))
print(f"toqsonlar{toqsonlar}")
