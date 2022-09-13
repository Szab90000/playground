#!/usr/bin/env python
# coding: utf8


def atvalt(val, typ):
		
	if typ == "inch":
		num = float(val) * 2.54
		result = f"{num} cm"
	elif typ == "cm":
		num = float(val) / 2.54
		result = f"{num} inch"
	else :
		result = False

	return result
		
def testifnumber(val):
	isnum = True
	
	try:
		int(val)
	except ValueError:
		try: 
			float(val)
		except ValueError:
			isnum = False

	return isnum		
	

print("Adj meg egy értéket, és a mértékegységét (inch vagy cm)")
val = input("érték: " )
while testifnumber(val) == False:
	val = input("Kérlek számot adj meg ")	

typ = input("Mértékegység(inch/cm): ")
while atvalt(val, typ) == False:
	typ = input("Kérlek megfelelő mértékegységet adj meg ")

print(atvalt(val, typ))	






	


