import math

class Planeet:

	dichtheidC = 1.986 #kg/m3
	dichtheidO = 1.43 #kg/m3
	dichtheidN = 1.25 #kg/m3
	zuurstofaarde = 20.95
	koolstofaarde = 0.038
	stikstofaarde = 78.08

	def __init__(self, name, radiusplaneet, hoogteatmosfeer, zuurstof, koolstof, stikstof, conversiegraadO, conversiegraadN, boomgroei, kfcgroei):
		self.name = name
		self.rp = radiusplaneet
		self.ha = hoogteatmosfeer
		self.zuurstof = zuurstof
		self.koolstof = koolstof
		self.stikstof = stikstof
		self.cgO = conversiegraadO
		self.cgN = conversiegraadN
		self.boomgroei = boomgroei
		self.kfcgroei = kfcgroei
		self.dCO2 = self.koolstofaarde - self.koolstof

		self.eerstemassaO2 = 0
		self.tweedemassaO2 = 0

		self.eerstemassaCO2 = 0
		self.tweedemassaCO2 = 0

		self.eerstemassaN2 = 0
		self.tweedemassaN2 = 0
	
	def inhouda(self):
		self.inhoudplaneet = (4/3) * math.pi * self.rp**3
		self.inhoudatmosfeer = (4/3) * math.pi * (self.rp + self.ha)**3 - self.inhoudplaneet

	def ozonlaag(self, jaren, **kwargs):
		self.inhouda()
		bomen = 0
		kippen = 0
		wisseljaar = 0

		if len(kwargs) > 0:
			try:
				bomen = kwargs['bomen']
				kippen = kwargs['kippen']
				wisseljaar = kwargs['wisseljaar']
			except KeyError as ke:
				lskwarg = ['bomen', 'kippen', 'wisseljaar']
				for i in lskwarg:
					try:
						kwargs[i]
					except KeyError:
						print(f'{i} isn\'t defined')

		print(f"\nJaar\tMassa Zuurstof\t\t\tMassa Koolstofdioxide\t\tAantal Bomen\tDelta massa")
		
		eerstebomen = bomen
		tweedebomen = math.floor(eerstebomen * self.boomgroei)
		bomencg = eerstebomen * self.cgO

		eerstekippen = kippen
		tweedekippen = math.floor(eerstekippen * self.kfcgroei)
		kippencg = eerstekippen * self.cgN
		
		self.eerstemassaO2 = int(self.inhoudatmosfeer * (self.zuurstof/100) * self.dichtheidO) # int uses the full long number and wont round it
		tweedemassaO2 = int(self.eerstemassaO2 + bomencg)

		self.eerstemassaCO2 = int(self.inhoudatmosfeer * (self.koolstof/100) * self.dichtheidC)
		tweedemassaCO2 = int(self.eerstemassaCO2 - bomencg)

		self.eerstemassaN2 = int(self.inhoudatmosfeer * (self.stikstof/100) * self.dichtheidN)
		tweedemassaN2 = int(self.eerstemassaN2 + kippencg)

		i = 0
		print(f"{i}\t{float(self.eerstemassaO2)}\t\t{float(self.eerstemassaCO2)}\t\t{eerstebomen}\t\t{tweedemassaO2-self.eerstemassaO2}\t\t{tweedemassaCO2-self.eerstemassaCO2}")

		for i in range(1, jaren):
		
			eerstebomen = tweedebomen
			tweedebomen = math.floor(eerstebomen * self.boomgroei)
			bomencg = eerstebomen * self.cgO

			self.eerstemassaO2 = tweedemassaO2
			tweedemassaO2 = self.eerstemassaO2 + bomencg

			self.eerstemassaCO2 = tweedemassaCO2
			tweedemassaCO2 = self.eerstemassaCO2 - bomencg

			print(f"{i}\t{float(self.eerstemassaO2)}\t\t{float(self.eerstemassaCO2)}\t\t{eerstebomen}\t\t{tweedemassaO2-self.eerstemassaO2}\t\t{tweedemassaCO2-self.eerstemassaCO2}")
		
		print()

	# Hoeveel bomen er nodig zijn als we het in zoveel jaren recht getrokken willen hebben
	def boomjaren(self, jaren):
		self.inhouda()
		jaren = int(jaren)

		bomen = int(math.ceil(((self.inhoudatmosfeer * abs(self.dCO2)/100) * self.dichtheidC) / sum((self.boomgroei**x) * self.cgO for x in range(0, jaren))))
		return bomen

	def kipjaren(self, jaren):
		self.inhouda()
		jaren = int(jaren)
		
		kippen = int(math.ceil(((self.inhoudatmosfeer * abs(self.dCO2 - (self.zuurstof - self.zuurstofaarde))/100) * self.dichtheidO) / sum((self.kfcgroei**x) * self.cgN for x in range(0, jaren))))
		return kippen



	def wisseljaar(self, jaren, wisseljaar):
		if jaren > wisseljaar:
			atleastboom = 1
			atleastkip = 1

			if self.boomjaren(wisseljaar) == 0:
				atleastboom = 1
			elif self.kipjaren(jaren-wisseljaar) == 0:
				atleastkip = 1
			else:
				atleastboom = math.ceil(self.boomjaren(wisseljaar))
				atleastkip = math.ceil(self.kipjaren(jaren-wisseljaar))
			return [atleastboom, atleastkip]
		else:
			return 0
			# return '\nHet wisseljaar is groter dan het aantal opgegeven jaren en dat werkt niet.\nPorbeer een kleiner getal voor wisseljaar dan het aantal jaren te nemen.\n'
	
	# Hoe veel jaar er nodig is als ik begin met zoveel bomen of kippen
	def n_bomen(self, bomen):
		self.inhouda()
		verschil = 1

		jaar = 0
		while verschil >= 0:
			verschil = int(((self.inhoudatmosfeer * abs(self.dCO2)/100) * self.dichtheidC) - sum(bomen * (self.boomgroei**x) * self.cgO for x in range(0, jaar)))
			jaar += 1

		verschil = 1
		return jaar

	def n_kippen(self, kippen):
		self.inhouda()
		verschil = 1
		
		jaar = 0
		while verschil >= 0:
			verschil = int(((self.inhoudatmosfeer * abs(self.dCO2 - (self.zuurstof - self.zuurstofaarde))/100) * self.dichtheidN) - sum(int(kippen * (self.kfcgroei**x) * self.cgN) for x in range(0, jaar)))
			jaar += 1
			
		verschil = 1
		return jaar


if __name__ == "__main__":

	stikstofperjaar = ((900*0.1 *365)/1000) * 0.015 # = 0.49275 kg/jaar

	mars = Planeet(
		"Mars", 			#name
		6752000, 			#radius
		10000, 				#hoogteatmosfeer
		0.34, 				#zuurstof
		95, 				#koolstof
		2.7, 				#stikstof
		20, 				#conversiegraadO
		stikstofperjaar, 	#conversiegraadN
		1.2, 				#Groeifactorbomen
		3					#Groeifactorkippen
	)

	mars.ozonlaag(10, bomen=200)


	# print(mars.n_bomen(1))
	# print(mars.boomjaren(100))
	# print(mars.n_kippen(600))
	# print(mars.kipjaren(100))
	# print(mars.wisseljaar(200, 100))



	# aarde = Planeet("Aarde", 6371000, 6000, 21, 0.013, 20, 1.2)
	# saturn = Planeet("Saturn", 6371000, 10000, 0.035, 35, 20, 1.002)
	# print(aarde.zuurstof)
	# aarde.zuurstof = 31
	# print(aarde.zuurstof)
	# print(aarde.inhoudatmosfeer)
	# print(f"Inhoud Atmosfeer: {aarde.inhouda()}")
	# print(aarde.ozonlaag(200, 100).eerstemassaO2)

		# self.zuurstof = self.zuurstof + (self.koolstofaarde - self.koolstof)
		# kippen = ((self.inhoudatmosfeer * abs((self.stikstofaarde - self.stikstof))/100) * self.dichtheidN) / ((self.kfcgroei**jaren) * self.cgN)
		# return kippen
		# kippen = ((self.inhoudatmosfeer * abs((self.zuurstofaarde - self.zuurstof))/100) * self.dichtheidO) / ((self.kfcgroei**jaren) * self.cgN)
		# return kippen
		# kippen = round(((self.inhoudatmosfeer * abs(self.zuurstofaarde - self.zuurstof)/100) * self.dichtheidO) / sum((self.boomgroei**x) * self.cgN for x in range(0, jaren)))
		# return kippen

		# jaren = math.log(((self.inhoudatmosfeer * abs(self.zuurstof + self.dCO2)/100) * self.dichtheidO) / (bomen * self.cgO), self.boomgroei)
		# return jaren
		# print(jaren)
		# print(i)

		# print(f'Verschil: {verschil}')
		# time.sleep(0.05)
		# print(i)

		# jaren = math.log(((self.inhoudatmosfeer * abs(self.dCO2 - self.zuurstofaarde)/100) * self.dichtheidO) / (kippen * self.cgN), self.boomgroei)
		# return jaren
		# print(jaren)
		# print(i)
		# print(f'Verschil: {verschil}')
		# time.sleep(0.05)
		# print(i)

		# bomen = ((self.inhoudatmosfeer * abs(self.zuurstofaarde - self.zuurstof)/100) * self.dichtheidO) / ((self.boomgroei**jaren) * self.cgO)
		# return bomen
		# bomen = ((self.inhoudatmosfeer * abs((self.koolstofaarde - self.koolstof))/100) * self.dichtheidC) / ((self.boomgroei**jaren) * self.cgO)
		# return bomen
		# bomen = ((self.inhoudatmosfeer * abs(self.koolstofaarde - self.koolstof)/100) * self.dichtheidC) / sum((self.boomgroei**x) * self.cgO for x in range(0, jaren))
		# return [bomen, self.inhoudatmosfeer * (abs(self.koolstofaarde - self.koolstof)/100) * self.dichtheidC]
