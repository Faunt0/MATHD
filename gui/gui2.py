import tkinter as tk
# from tkinter import ttk
import math
import planeet2

# method test
def clicky():
	print("JEL")

name = ''
radius = 0
hoogteatmosfeer = 0
zuurstof = 0
koolstof = 0
stikstof = 0
conversiegraadO = 0
conversiegraadN = 0
boomgroei = 0
kfcgroei = 0
p = None

def getinfo():
	global name
	global radius
	global hoogteatmosfeer
	global zuurstof
	global koolstof
	global stikstof
	global conversiegraadO
	global conversiegraadN
	global boomgroei
	global kfcgroei
	global p

	name = str(name2.get())
	radius = int(radius2.get())
	hoogteatmosfeer = int(hoogteatmosfeer2.get())
	zuurstof = float(zuurstof2.get())
	koolstof = float(koolstof2.get())
	stikstof = float(stikstof2.get())
	conversiegraadO = float(conversiegraadO2.get())
	conversiegraadN = float(conversiegraadN2.get())
	boomgroei = float(boomgroei2.get())
	kfcgroei = float(kfcgroei2.get())

	print(f"Name: \t\t\t{name}")
	print(f"Radius: \t\t{radius} m")
	print(f"Hoogte Atmosfeer: \t{hoogteatmosfeer} m")
	print(f"Zuurstof: \t\t{zuurstof} %")
	print(f"Koolstof: \t\t{koolstof} %")
	print(f"Stikstof: \t\t{stikstof} %")
	print(f"Conversie graad O2: \t{conversiegraadO} kgco2/boom")
	print(f"Conversie graad N2: \t{conversiegraadN} kgN2/kip")
	print(f"Boomgroei: \t\t{boomgroei} bomen/jaar")
	print(f"Kippen groei: \t\t{kfcgroei} kippen/jaar")
	print()
	
	p = planeet2.Planeet(name, radius, hoogteatmosfeer, zuurstof, koolstof, stikstof, conversiegraadO, conversiegraadN, boomgroei, kfcgroei)
	p.inhouda()

	# print(p.inhoudatmosfeer)
	# print(p.n_bomen(100))

def jaren():

	try:
		jaren = int(jaarentry.get())
		atleastboom = 1
		atleastkip = 1

		p = planeet2.Planeet(name, radius, hoogteatmosfeer, zuurstof, koolstof, stikstof, conversiegraadO, conversiegraadN, boomgroei, kfcgroei)
		p.inhouda()

		if p.boomjaren(jaren) == 0:
			atleastboom = 1
		elif p.kipjaren(jaren) == 0:
			atleastkip = 1
		else:
			atleastboom = math.ceil(p.boomjaren(jaren))
			atleastkip = math.ceil(p.kipjaren(jaren))

		jaar3['text'] = f'{atleastboom} Bomen'
		wisseljaar3['text'] = f'{atleastkip} Kippen'

		atleastboom = 1
		atleastkip = 1
		errormessage['text'] = '-'

	except ValueError:
		errormessage['text'] = 'Invalid input'
	except OverflowError:
		errormessage['text'] = 'Input too big'
	except ZeroDivisionError:
		errormessage['text'] = 'Submit first'


def wisseljaar():
	p = planeet2.Planeet(name, radius, hoogteatmosfeer, zuurstof, koolstof, stikstof, conversiegraadO, conversiegraadN, boomgroei, kfcgroei)
	p.inhouda()
	# if int(wisseljaarentry.get()) > 1:
	# 	wisseljaar = int(wisseljaarentry.get())
	# else:
	# 	wisseljaar3['text'] = "Make it bigger"
	jaren = int(jaarentry.get())
	wisseljaar = int(wisseljaarentry.get())
	# jaar3['text'] = f'- Bomen'
	# wisseljaar3['text'] = f'- Kippen'
	# if int(jaren[0]) == 0:

	jaren = p.wisseljaar(math.ceil(jaren), math.ceil(wisseljaar))

	jaar3['text'] = f'{str(int(jaren[0]))} Bomen'
	wisseljaar3['text'] = f'{str(int(jaren[1]))} Kippen'
	errormessage['text'] = '-'

	# print(f'Bomen:\t{float(jaren[0])}')
	# print(f'Kippen:\t{float(jaren[1])}')

	# Not the value we want.
	# print(f"Aantal bomen: \t\t{atleastboom}")
	# print(f"Aantal kippen: \t\t{atleastkip}")


	# kippen = str(int(str(jaren[1]).strip()))
	# print(f'met wisseljaar')
	# print(f'Bomen: \t\t{bomen}')
	# print(f'Kippen: \t\t{kippen}')
	# print(round(p.n_bomen(jaren), 5))
	# jaren = [math.ceil(p.boomjaren(jaren)), math.ceil(p.kipjaren(jaren))]
	# bomen = float()

def bomenkippen():
	bomenkippen = [int(bomenentry.get()), int(kippenentry.get())]

	try:
		p = planeet2.Planeet(name, radius, hoogteatmosfeer, zuurstof, koolstof, stikstof, conversiegraadO, conversiegraadN, boomgroei, kfcgroei)
		p.inhouda()
		print()
		print(math.ceil(p.n_bomen(bomenkippen[0])))
		print(p.n_kippen(bomenkippen[1]))
		bomen3['text'] = f'{math.ceil(p.n_bomen(bomenkippen[0]) + p.n_kippen(bomenkippen[1]))} Jaren'
		# print(f"Jaren: \t\t{p.n_bomen(bomenkippen[0]) + p.n_kippen(bomenkippen[1])}")
		
	except ZeroDivisionError as e:
		print(e)
		bomen3['text'] = 'SUBMIT FIRST'
		# break



window = tk.Tk()
window.minsize(450, 620)
window.title("Planet model")

# window.maxsize(450, 620)
# window.maxsize(0, 0)
# window.minsize(450, 620)
# window.columnconfigure([0,1], weight=1, minsize=75)
# window.rowconfigure([0,1,2], weight=1, minsize=50)
# window.minsize(200)
# inputfrm = tk.Frame(window, relief=tk.RAISED, border=3, pady=15)
# inputfrm.pack()



# Input Frame
inputfrm = tk.LabelFrame(window, text="Planeet gegevens", pady=15, width=450, height=620)
inputfrm.pack(padx=10, pady=10)

name1 = tk.Label(inputfrm, text="Name: ").grid(row=0, column=0, pady=1, sticky="e")
name2 = tk.Entry(inputfrm, width=20)
name2.grid(row=0, column=1, pady=1)

radius1 = tk.Label(inputfrm, text="Radius: ").grid(row=1, column=0, pady=1, sticky="e")
radius2 = tk.Entry(inputfrm, width=20)
radius2.grid(row=1, column=1, pady=1)
radius3 = tk.Label(inputfrm, text="m").grid(row=1, column=2, pady=1, sticky="w")

hoogteatmosfeer1 = tk.Label(inputfrm, text="Hoogte Atmosfeer: ").grid(row=2, column=0, pady=1, sticky="e")
hoogteatmosfeer2 = tk.Entry(inputfrm, width=20)
hoogteatmosfeer2.grid(row=2, column=1, pady=1)
hoogteatmosfeer3 = tk.Label(inputfrm, text="m").grid(row=2, column=2, pady=1, sticky="w")

zuurstof1 = tk.Label(inputfrm, text="Zuurstof: ").grid(row=3, column=0, pady=1, sticky="e")
zuurstof2 = tk.Entry(inputfrm, width=20)
zuurstof2.grid(row=3, column=1, pady=1)
zuurstof3 = tk.Label(inputfrm, text="%").grid(row=3, column=2, pady=1, sticky="w")

koolstof1 = tk.Label(inputfrm, text="Koolstof: ").grid(row=4, column=0, pady=1, sticky="e")
koolstof2 = tk.Entry(inputfrm, width=20)
koolstof2.grid(row=4, column=1, pady=1)
koolstof3 = tk.Label(inputfrm, text="%").grid(row=4, column=2, pady=1, sticky="w")

stikstof1 = tk.Label(inputfrm, text="Stikstof: ").grid(row=5, column=0, pady=1, sticky="e")
stikstof2 = tk.Entry(inputfrm, width=20)
stikstof2.grid(row=5, column=1, pady=1)
stikstof3 = tk.Label(inputfrm, text="%").grid(row=5, column=2, pady=1, sticky="w")

conversiegraadO1 = tk.Label(master=inputfrm, text="Conversiegraad O2: ").grid(row=6, column=0, pady=1, sticky="e")
conversiegraadO2 = tk.Entry(inputfrm, width=20)
conversiegraadO2.grid(row=6, column=1, pady=1)
conversiegraadO3 = tk.Label(inputfrm, text="kg/m3").grid(row=6, column=2, pady=1, sticky="w")

conversiegraadN1 = tk.Label(inputfrm, text="Conversiegraad N2: ").grid(row=7, column=0, pady=1, sticky="e")
conversiegraadN2 = tk.Entry(inputfrm, width=20)
conversiegraadN2.grid(row=7, column=1, pady=1)
conversiegraadN3 = tk.Label(inputfrm, text="kg/m3").grid(row=7, column=2, pady=1, sticky="w")

boomgroei1 = tk.Label(inputfrm, text="Groeifactor Bomen: ").grid(row=8, column=0, pady=1, sticky="e")
boomgroei2 = tk.Entry(inputfrm, width=20)
boomgroei2.grid(row=8, column=1, pady=1)
boomgroei3 = tk.Label(inputfrm, text="bomen/jaar").grid(row=8, column=2, pady=1, sticky="w")

kfcgroei1 = tk.Label(inputfrm, text="Groeifactor Kippen: ").grid(row=9, column=0, pady=1, sticky="e")
kfcgroei2 = tk.Entry(inputfrm, width=20)
kfcgroei2.grid(row=9, column=1, pady=1)
kfcgroei3 = tk.Label(inputfrm, text="kippen/jaar").grid(row=9, column=2, pady=1, sticky="w")

# Submit
submit = tk.Button(inputfrm, text="Submit", command=getinfo, padx=7, pady=7)
submit.grid(row=10, column=1)



# Answer frame
answerfrm = tk.LabelFrame(window, text="Functies toepassen op planeet", pady=15, width=450, height=620)
answerfrm.pack(padx=10, pady=10)


# trying to make the grid easier.
row = 0
column = 0
error = tk.Label(answerfrm, text="Error: ").grid(row=row, column=column, pady=1, sticky="e")
column += 1
errormessage = tk.Label(answerfrm, text=" - ")
errormessage.grid(row=row, column=column)


# Row 1
row += 1
column = 0
jaar1 = tk.Label(answerfrm, text="Jaren: ").grid(row=row, column=column, pady=1, sticky="e")
column += 1
jaarentry = tk.Entry(answerfrm, width=15)
jaarentry.grid(row=row, column=column, pady=1)
column += 1
jaar2 = tk.Button(answerfrm, text="Jaren", command=jaren).grid(row=row, column=column)
column += 1
jaar3 = tk.Label(answerfrm, text="- Bomen")
jaar3.grid(row=row, column=column, pady=1, sticky="w")
# jaaruitleg = tk.Label(answerfrm, text="Het moet recht getrokken zijn in x jaar").grid(row=1, column=0, columnspan=30)


# Row 2
row += 1
column = 0
wisseljaar1 = tk.Label(answerfrm, text="Wisseljaar: ").grid(row=row, column=column, pady=1, sticky="e")
column += 1
wisseljaarentry = tk.Entry(answerfrm, width=15)
wisseljaarentry.grid(row=row, column=column, pady=1)
column += 1
column += 1
wisseljaar3 = tk.Label(answerfrm, text="- Kippen")
wisseljaar3.grid(row=row, column=column, pady=1, sticky="w")


# Row 3
row += 1
column = 1
wisseljaar2 = tk.Button(answerfrm, text="Wisseljaar", command=wisseljaar).grid(row=row, column=column)
# info = "De atmosfeer moet \ngelijk worden in \nx jaar Als je niet \nop hetzelfde moment \nde kippen en bomen \n\'aanzet\' kun je "
# jareninfo = tk.Label(answerfrm, text=info).grid(row=row, column=column, sticky='w')



# for row in range(0, 5):
# 	for column in range(0,3):
# 		jaar1 = tk.Label(answerfrm, text="Jaren: ").grid(row=0, column=column, pady=1, sticky="e")
# 		jaarentry.grid(row=0, column=1, pady=1)
# 		jaar2 = tk.Button(answerfrm, text=" = ", command=jaren).grid(row=0, column=2)
# 		jaar3.grid(row=0, column=3, pady=1, sticky="w")

# working version
# jaar1 = tk.Label(answerfrm, text="Jaren: ").grid(row=0, column=0, pady=1, sticky="e")
# jaarentry = tk.Entry(answerfrm, width=15)
# jaarentry.grid(row=0, column=1, pady=1)
# jaar2 = tk.Button(answerfrm, text=" = ", command=jaren).grid(row=0, column=2)
# jaar3 = tk.Label(answerfrm, text="- Bomen\n- Kippen")
# jaar3.grid(row=0, column=3, pady=1, sticky="w")
# jaaruitleg = tk.Label(answerfrm, text="Het moet recht getrokken zijn in x jaar").grid(row=1, column=0, columnspan=30)


# Row 4
row += 1
bomen1 = tk.Label(answerfrm, text="Bomen: ").grid(row=row, column=0, pady=1, sticky="e")
bomenentry = tk.Entry(answerfrm, width=15)
bomenentry.grid(row=row, column=1, pady=1)
bomen2 = tk.Button(answerfrm, text=" = ", command=bomenkippen).grid(row=row, column=2)
bomen3 = tk.Label(answerfrm, text="- Jaren")
bomen3.grid(row=row, column=3, pady=1, sticky="w")


# Row 5
row += 1
kippen1 = tk.Label(answerfrm, text="Kippen: ").grid(row=row, column=0, pady=1, sticky="e")
kippenentry = tk.Entry(answerfrm, width=15)
kippenentry.grid(row=row, column=1, pady=1)


# Row 6
row += 1
boomkipuitleg = tk.Label(answerfrm, text="Hoe lang duurt het als ik x bomen en kippen heb").grid(row=row, column=0, columnspan=30)


# Deze hebben ook jaren nodig
# bomen1 = tk.Label(answerfrm, text="Bomen: ").grid(row=1, column=0, pady=1, sticky="e")
# boomentry = tk.Entry(answerfrm, width=10)
# boomentry.grid(row=1, column=1, pady=1)
# boom2 = tk.Button(answerfrm, text=" = ", command=clicky).grid(row=1, column=2)
	# boom3 = tk.Label(answerfrm, text="-").grid(row=1, column=3, pady=1, sticky="e")

# kippen1 = tk.Label(answerfrm, text="Kippen: ").grid(row=1, column=0, pady=1, sticky="e")
# bomen2.grid(row=0, column=1, pady=1)

# Preloads
def marspreload():
	name2.insert(0, "Mars")
	radius2.insert(0, "6752000")
	hoogteatmosfeer2.insert(0, "10000")
	zuurstof2.insert(0, "0.13")
	koolstof2.insert(0, "95.32")
	stikstof2.insert(0, "2.7")
	conversiegraadO2.insert(0, "20")
	conversiegraadN2.insert(0, "0.49275")
	boomgroei2.insert(0, "1.2")
	kfcgroei2.insert(0, "3")

def aardepreload():
	name2.insert(0, "Aarde")
	radius2.insert(0, "6371000")
	hoogteatmosfeer2.insert(0, "6000")
	zuurstof2.insert(0, "20.95")
	koolstof2.insert(0, "0.013")
	stikstof2.insert(0, "78.08")
	conversiegraadO2.insert(0, "20")
	conversiegraadN2.insert(0, "0.49275")
	boomgroei2.insert(0, "1.2")
	kfcgroei2.insert(0, "3")

marspreload()
# aardepreload()

window.mainloop()	