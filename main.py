from colorama import Fore, Back, Style, init
import pyfiglet
Titre = "BiteDeadCalc"
ASCII_art_1 = pyfiglet.figlet_format(Titre)
print(ASCII_art_1)
init()



print(Fore.GREEN+("calculateur de mort"))



def calc():
	print("choix d'age de depart")
	nombre = int(input())
	print("a quel age vous comptez mourir ?")
	fin = int(input())
	nav = 0
	x = 0
	if nombre > fin :
		print("inverse")
	else :
		pass
	while nav == 0:
		if nombre < fin :
			x+=1
			nombre += 1
			print(nombre)
		else :
			nav += 1
	print("vous allez mourir dans", x, "ans")



calc()
input()
	
