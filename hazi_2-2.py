
def convert(val, typ):
		
	result = False
	
	while result == False:
		result = True
		typ = typ.lower()
		
		if typ == "inch":
			num = (float(val) / 2.54).__round__(2)
			print(f"{num} cm")
		elif typ == "cm":
			num = (float(val) * 2.54).__round__(2)
			print(f"{num} inches")
		else :
			result = False
			typ = input("Not correct unit\n")
			
#loopba van rakva a convert hogy ne álljon le az egész	egy incorrect unitnál, és lehessen újat beütni		


if __name__ == "__main__":
	print("Adjon meg egy számot és egy mértékegységet")
	number = input()
	unit = input()
	convert(number, unit)
	






	



