def avto_info(make,model,karobka,rang,yil,narx=None):
    avto ={
        'kompaniya':make,
        'model':model,
        'karobka':karobka,
        'rang':rang,
        'yil':yil,
        'narx':narx
    }
    return avto
def kiritish():
    """Foydalanuvchiga avto-info functioni yordamida bir necha avtolar xaqida ma`lumotlarni bitta ro`yxatga joylash imkonini beruvchi function"""
    avtolar = []
    while True:
        print("\n Quyidagi ma`lumotlarni kiriting...",end='')
        kompaniya = input('Ishlab chiqaruvchi: ')
        model = input('Mashina modeli: ')
        karobka = input('Karobka: ')
        rang = input('Rangi: ')
        yil = int(input("Ishlab chiqarilgan yili: "))
        narx = input("Qiymati: ")
        avtolar.append(avto_info(make=kompaniya,model=model,karobka=karobka,rang=rang,yil=yil,narx=narx))
        javob=input("Yana avto qo`shasizmi (Yes/No)")
        if javob.lower()=='no':
            break
    return avtolar
def info_print(avto_info):
    """Avtolar xaqida ma`lumotlar konsolga chiqaruvchi function"""
    print(
        f"{avto_info['kompaniya'].upper()}, "
        f"{avto_info['model'].upper()}, "
        f"{avto_info['rang'].upper()}, "
        f"{avto_info['karobka'].upper()}, "
        f"{avto_info['yil']}-YIL,{avto_info['narx']}$"
    )
