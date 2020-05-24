# """
# Daire Alan: πr^2
# Daire Çevre: 2πr
# Yari capi verilen bir dairenin alan ve cevresini heaplayiniz
# r:3.14"""

# pi=3.14
# r=float(input("yaricapi yaziniz:"))       #input str bilgi verir str to float conv
# alan=pi*(r**2)
# cevre=2*pi*r
# print("alan: ",alan)
# print("Cevre: ",cevre)
# print("cevre:",str(cevre)+" alan:",str(alan))


website="http://www.google.com"
course="Python Kursu : 40 saatlik bir bootcamp eğitimi"
#Q2 'course' karakter dizisinde kaç karakter vardir

len(course)
print(len(course))

#Q3 'website' icinden www karakterini alin

print(website[7:10])

w=len(website)
w=website[7:10]
print(w)


#Q3 com karakterlerini alin
print(website[18:21])


#Q4 ilk 15 ve son 15 karakteri alin
print(website[0:15])
print(website[:15])

#Q5 course ifadesindeki karakterleri tersten yazin
print(course[::-1]) #:: tüm elemanları al   -1:tersten git ve birer birer al
print(course[::2])

# s='12345'*5
# print(s[::5]) #beş kere yaz ama beş karakterde bir al 5. karakterden sonra 1 var*5

#Q6 Asagidaki degiskenlerle 
#'Benim adim Fatma Elik, Yasim 26 ve meslegim mühendis.' yazdirin
name, surname, age, job='Fatma','Elik', 26, 'mühendis'

ifade="Benim adim "+name+" "+surname+" yasim "+str(age)+" ve meslegim "+job

ifade='Benim adim {} {}, Yasim {} ve meslegim {}.'.format(name,surname,age,job)
ifade=f"Benim adim {name} {surname}, Yasim {age} ve meslegim {job}"
print(ifade)

#Q7 'Hello world' ifadesindeki w harfini 'W' ile degistirin.

s='Hello world'
s= s[0:6]+'W'+s[-4:]
print(s)

s.replace('w','W')  #replace metodu

#Q8 abc ifadesini 3 kez yan yana yazdir
s='abc\n'*3
print(s)

####s   string uygulamalari

website="http://www.google.com"
course="Python Kursu : 40 saatlik bir bootcamp eğitimi"


#Q9 ' Hello World '  karakter dizisindeki bas ve sondaki bosluklari silin
word=' Hello World '
word=' Hello World '.strip()
word=' Hello World '.lstrip()     #soldan bosluk siler
word=' Hello World '.rstrip()       #sagdan bosluk siler
web=website.lstrip('/:pth')    #saoldan yazilan karakterlerin hepsini siler

print(word)
print(web)

#Q10 "http://www.google.com"  google haricindeki bilgiyi silin

q= 'http://www.google.com'.strip('w.moc')
print('q:', q)

#Q11 course karakter dizisindeki tum hafleri kucuk yapin

course=course.lower()
course=course.upper()   #hepsi buyuk
course=course.title()   #ilk har buyuk
print(course)

#Q12 'website' icinde kac tane a karakteri vardır
# website=website.count('a')
# website=website.count('www',0,10)  #0-10 index arasinda ara
# print(website)

#Q13 'website' ww ile baslayip com ile bitiyor mu
isFound=str(website).startswith('ww')
isFound=str(website).endswith('com')
print(isFound)

#Q14 'website' icinde com ifadesi var mi
index=str(website).find('com')   
index=str(website).find('com',0,10)     
index=(website).find('Python') 
index=str(website).rfind('com')     #sagdan saymaya baslar
index=str(website).index('com') 
index=str(website).rindex('com') 
print(index)                        #yoksa=> find:<0 index:hata verir

#Q15 'course' icindeki karakterlerin hepsi alfabetik mi
result=course.isalpha()     #alfabetik mi
print(result)           #false :sayilar da var
result2=course.isdigit()    #alfanumerik mi
print(result2)          #false: harfler var

#Q16 'contents' ifadesini 50 karaktere yerlestirin ve  icine * koyun

a='contents'
#a=a.center(50,'*')
a=a.ljust(50,'*')       #contents sola yasladi
a='contents'.rjust(50,'*')     #saga yasladi
print(a)

#Q17 'course' tum bosluklari '-' ile degistir
result=course.replace(' ','-')
result=course.replace(' ','')   #bosluklari siler!
print(result)
#Q18 'Hello Worl' karakter dizisinde 'World' yerine 'There' koyun
word=word.replace('World','There' )
word=word.replace('World','There',5 )   #ilk 5 karaktere yapar

print(word)

#Q19 'course karakter dizisini bosluk karakterlerinden ayirin
course=course.split(' ')
course=course[2]        #ayrilan(dizi) karakterin 2. elemani
print(course)

###Liste Uygulamalari

#Q20 "BMW,Mercedes,Opel,Mazda" elemanlarina sahip bir liste olusturun
list=['BMW','Mercedes','opel','Mazda']

#Liste kac elemanlidir
print(len(list))

#Listenin ilk ve son elemani nedir
print(list[0])
print(list[-1])

#Mazda ile Toyota degerini degistirin
list[-1]='Toyota'
print(list)

#Mercedes listenin bir elemani midir
x='Mercedes' in list
print(x)

#Listenin -2 indeksindeki degeri nedir
print(list[-2])

#Listenin ilk uc elemanini alin
print(list[0:3])
print(list[:3])
print(list[-2:])

#Listenin son iki elemani yerine 'Toyota' ve 'Renault' ekleyin
list[-2:]=['Toyota','Renault']
print(list)

#Listeye 'Audi' ve 'Nissan' ekleyin

list1=['Audi','Nissan']
lists=list+list1
print(lists)

# #Listenin son elemanini silin

del list[-1]
print(list)

 #Liste elemanlarni tersten yazdirin

x=list[::-1]
print(x)

#Asagidaki verileri bir liste icinde saklayiniz

    #student1: Yigit Bilgi 2010, (70,60,70)
    #student2: Sena Turan 1999, (80,80,70)
    #student3: Ahmet Turan 1998, (80,70,90)

s1=['Yigit ','Bilgi ',2010,[70,60,70]]
s2=['Sena ','Turan ','1999, ','(80,80,70)']
s3=['Ahmet ','Turan ', '1998, ',[80,80,70]]

#Liste elemanlarini yazdirin
print(s1, s2, s3)
x=s1[1]
y=s3[3][1]
print(x,y)
result= f"{s1[0]} {s1[1]} {2020-s1[2]} yasina ve ortlamasi {(s1[3][0]+s1[3][1]+s1[3][1])/3}"
print(result)
ort=(s1[3][0]+s1[3][1]+s1[3][1])/3
ort=round(ort,3)
print(ort)



#####Liste Metodlari

#Q21
names=['Ali','Yagmur','Hakan','Deniz']
years=[1998,2000,1998,1987]

#cenk ismini listenin sonuna ekleyin
names.append('Cenk')
print(names)
#serra listenin basina ekleyin
names.insert(0,'Serra')
names.insert(len(names),'Mehmet')   #en sondaki indexten önce: en sona koyar
print(names)
#Deniz ismini listeden siliniz
names.remove('Deniz')
names.pop() # en sonu siler
names.pop(1)   #1.indexi sil
index=names.index('Deniz')
names.pop(index) #Denizin old imdexi sil
print(names)
#Ali listenin bir elemani mi
result='Ali' in names  #T/F
 print(result)
#Liste elemanlarini ters cevir
names.reverse()
print(names)
#Liste elemanlarini alfabetik olarak siralayin
names.sort()
print(names)
#years listesini siralayain
years.sort()
print(years)
#str='chevrolet,Dacia' karakterlerini listeye ekleyin
str='chevrolet','Dacia'
result=str.split(',')   #liste oldu virgulden ayrildi
print(result)
#names.append('Dacia')
print(names)
#years dizisinin min max elemani
time1=min(years)
time2=max(years)
print(time1,time2)
#years dizisinde kac tane 1988 vardir
print(years.count(1998))
#years dizisinin tum elemanlarini siliniz
years.clear()
#kullanicidan alacaginiz 1 tane marka bilgisini bir listede saklayin
print('marka adi giriniz')
markalar=[]
marka=input("marka: ")   #kullanicinin girdigi deger
markalar.append(marka)  #girilen degeri ekle
print(markalar)