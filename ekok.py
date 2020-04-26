x = int(input("birinci sayiyi giriniz"))
y = int(input("ikinci sayiyi giriniz"))
liste = []
liste2 = [2,3,5,7,11]
liste3 =[]
for i in liste2:
	while x % i == 0:
		liste.append(i)
		x = (x/i)
for i in liste2:
	while y % i == 0:
		y = (y/i)
		liste3.append(i)						
print(liste)
print(liste3)

	