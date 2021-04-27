function sum(array) {
	var total = 0;
	for (let i = 0; i < array.length; i++) {
		var total = total + array[i];
	}
	return Number(total)
};
function range(start, stop) {
	var array = [];
	for (let i = start; i < stop; i++) {
		array.push(i);
	}
	return array;
};

var name, radius, hoogteAtmosfeer, zuurstof, koolstof, stikstof, conversiegraadO2, conversiegraadN2, groeifactorBomen, groeifactorKippen, dCO2;
function planeetinfo() {
	name = document.getElementById('name').value;
	radius = Number(document.getElementById('radius').value);
	hoogteAtmosfeer = Number(document.getElementById('hoogteAtmosfeer').value);
	zuurstof = Number(document.getElementById('zuurstof').value);
	koolstof = Number(document.getElementById('koolstof').value);
	stikstof = Number(document.getElementById('stikstof').value);
	conversiegraadO2 = Number(document.getElementById('conversiegraadO2').value);
	conversiegraadN2 = Number(document.getElementById('conversiegraadN2').value);
	groeifactorBomen = Number(document.getElementById('groeifactorBomen').value);
	groeifactorKippen = Number(document.getElementById('groeifactorKippen').value);
	dCO2 = Number(koolstofaarde - koolstof);
};

function inhouda() {
	planeetinfo();

	inhoudplaneet = 4/3 * Math.PI * (radius**3);
	inhoudatmosfeer = (4/3 * Math.PI * (radius + hoogteAtmosfeer)**3) - inhoudplaneet;
	// console.log(`Inhoud: ${inhoudatmosfeer} m3\nInhoudplaneet: ${inhoudplaneet}`)
};



var dichtheidC, dichtheidO, dichtheidN, zuurstofaarde, koolstofaarde, stikstofaarde;
dichtheidC = 1.986; 		//kg/m3
dichtheidO = 1.43; 			//kg/m3
dichtheidN = 1.25; 			//kg/m3
zuurstofaarde = 20.95;		//%
koolstofaarde = 0.038;
stikstofaarde = 78.08;


function boomjaren(jaar) {
	planeetinfo();
	inhouda();

	var bomen = Math.ceil(((inhoudatmosfeer * (Math.abs(dCO2))/100) * dichtheidC) / sum(range(0, jaar).map(x => groeifactorBomen**x * conversiegraadO2)));
	
	console.log(`Bomen: ${bomen}`)
	document.getElementById("bomenans").innerHTML = bomen;
	document.getElementById("jaarans").innerHTML = jaar;
	return bomen
};
function kipjaren(jaar) {
	planeetinfo();
	inhouda();

	var kippen = Math.ceil(((inhoudatmosfeer * (Math.abs(dCO2 - (zuurstof - zuurstofaarde)))/100) * dichtheidO) / sum(range(0, jaar).map(x => (groeifactorKippen**x * conversiegraadN2))));
	
	console.log(`Kippen: ${kippen}`);
	document.getElementById("kippenans").innerHTML = kippen
	document.getElementById("jaarans").innerHTML = jaar;
	return kippen
};


function wisseljaar() {
	planeetinfo();
	inhouda();
	var atleastboom = 1;
	var atleastkip = 1;

	var wisseljaren = document.getElementById('wisseljaren').value;
	var jaren = document.getElementById('jaren').value;

	document.getElementById("jaarans").innerHTML = jaren;
	document.getElementById("wisseljaarans").innerHTML = wisseljaren;
	
	if (jaren > wisseljaren) {
		atleastboom = 1;
		atleastkip = 1;

		if (boomjaren(wisseljaren)[0] === 0) {
			atleastboom = 1;

		} else if (kipjaren(jaren-wisseljaren)[1] === 0) {
			atleastkip = 1;

		} else {
			atleastboom = Math.ceil(boomjaren(wisseljaren));
			atleastkip = Math.ceil(kipjaren(jaren-wisseljaren));
		}

		// console.log(`Bomen: ${atleastboom}`);
		// console.log(`Kippen: ${atleastkip}`);
		
		document.getElementById("bomenans").innerHTML = atleastboom;
		document.getElementById("kippenans").innerHTML = atleastkip;
		
	} else {
		return 0;
	}
};
function n_bomenkippen() {
	planeetinfo();
	inhouda();
	var verschil = 0;
	var i = 0;
	var j = 0;
	var bomen = document.getElementById('bomen').value;
	var kippen = document.getElementById('kippen').value;

	//  Bomen
	while (verschil >= 0) {
		var verschil = ((inhoudatmosfeer * Math.abs(dCO2)/100) * dichtheidC) - sum(range(0, i).map(x => bomen * (groeifactorBomen**x) * conversiegraadO2));
		i++;
	};

	verschil = 0;

	// Kippen
	while (verschil >= 0) {
		verschil = ((inhoudatmosfeer * Math.abs(dCO2 - (zuurstof - zuurstofaarde))/100) * dichtheidN) - sum(range(0, j).map(x => kippen * (groeifactorKippen**x) * conversiegraadN2));
		j++;
	};

	verschil = 0;

	document.getElementById("bomenans").innerHTML = bomen;
	document.getElementById("kippenans").innerHTML = kippen;
	document.getElementById("jaarans").innerHTML = Number(i);
	document.getElementById("wisseljaarans").innerHTML = Number(j);

	var jaren = Number(i+j);
	console.log(`Jaren: ${jaren}`);
	return [i, j]
};


var percentO2array = [];
var percentCO2array = [];
var percentN2array = [];
function ozonlaag() {
	planeetinfo();
	inhouda();
	boom_jaar = n_bomenkippen()[0];
	kip_jaar = n_bomenkippen()[1];

	var jaar = Number(document.getElementById('jaren').value);
	var bomen = document.getElementById('bomen').value;
	var kippen = document.getElementById('kippen').value;


	O2aardebereikt = 0;

	eerstebomen = bomen;
	tweedebomen = Math.ceil(eerstebomen * groeifactorBomen);
	bomenO = eerstebomen * conversiegraadO2;

	O2_massa1 = Number(inhoudatmosfeer * dichtheidO * (zuurstof/100));
	O2_massa2 = Number(O2_massa1 + bomenO);
	O2percent = (O2_massa1/inhoudatmosfeer) * 100;
	// O2array.push(O2_massa1)

	CO2_massa1 = Number(inhoudatmosfeer * dichtheidC * (koolstof/100));
	CO2_massa2 = Number(CO2_massa1 - bomenO);
	CO2percent = (CO2_massa1/inhoudatmosfeer) * 100;
	// CO2array.push(CO2_massa1)


	if (O2percent < 100 && O2percent > 0) {
		percentO2array.push(O2percent)
	}
	if (CO2percent < 100 && CO2percent > 0) {
		percentCO2array.push(CO2percent)
	}

	var i = 0;
	console.log(`${i}\t${Math.round(O2percent)}\t\t${Math.round(CO2percent)}\t\t${eerstebomen}`)
	
	for (let i = 0; i < range(0, jaar).length; i++) {
		if (O2aardebereikt = 0) {
			if (O2percent >= zuurstofaarde) {
				O2aardebereikt = i-1;
				console.log(`Zuurstof aarde bereik in jaar: ${O2aardebereikt}`);
			}
		}
		if (CO2percent <= 1 || O2percent > 100) {
			console.log(`CO2 bereikt: ${i}`);
			break;
		}

		eerstebomen = tweedebomen;
		bomenO = eerstebomen * conversiegraadO2;
		tweedebomen = Math.ceil(eerstebomen * groeifactorBomen);
		
		O2_massa1 = O2_massa2;
		O2_massa2 = O2_massa1 + bomenO;
		O2percent = (O2_massa1/(dichtheidO*inhoudatmosfeer)) * 100;
		// O2array.push(O2_massa1)

		CO2_massa1 = CO2_massa2;
		CO2_massa2 = CO2_massa1 - bomenO;
		CO2percent = (CO2_massa1/(dichtheidC*inhoudatmosfeer)) * 100;
		// CO2array.push(CO2_massa1)


		if (O2percent < 100 && O2percent > 0) {
			percentO2array.push(O2percent);
		}
		if (CO2percent < 100 && CO2percent > 0) {
			percentCO2array.push(CO2percent);
		}

		// console.log(`${i}\t${O2_massa1}\t\t${CO2_massa1}\t\t${N2_massa1}\t\t${eerstebomen}\t\t${O2_massa2 - O2_massa1}`)
		// console.log(`${i}\t${Math.round(O2percent)}\t\t${Math.round(CO2percent)}\t\t${Math.round(N2percent)}\t\t${eerstebomen}\t\t${O2_massa2 - O2_massa1}`)
		
		console.log(`${i}\t${Math.round(O2percent)}\t\t${Math.round(CO2percent)}\t\t${eerstebomen}`);
	}

	eerstekippen = kippen;
	tweedekippen = Math.ceil(eerstekippen * groeifactorKippen);
	kippenN = eerstekippen * conversiegraadN2;

	// O2_massa1 = O2_massa2;
	O2_massa2 = O2_massa1 - kippenN;
	O2percent = (O2_massa1/(dichtheidO*inhoudatmosfeer)) * 100;
	// O2array.push(O2_massa1)
	N2_massa1 = Number(inhoudatmosfeer * dichtheidN * (stikstof/100));
	N2_massa2 = Number(N2_massa1 + kippenN);
	N2percent = (N2_massa1/inhoudatmosfeer) * 100;
	// N2array.push(N2_massa1)


	if (O2percent < 100 && O2percent > 0) {
		percentO2array.push(O2percent);
	}
	if (N2percent < 100 && N2percent > 0) {
		percentN2array.push(N2percent);
	}

	// i = boom_jaar;
	console.log(`${i}\t${O2percent}\t\t${N2percent}\t\t${eerstekippen}`);
	beginjaar = O2aardebereikt;

	for (let k=0; k-1 < range(0, O2aardebereikt).length; k++) {
		percentN2array.push((inhoudatmosfeer * dichtheidN * (stikstof/100))/((dichtheidN*inhoudatmosfeer)*100))
	}

	for (let l=O2aardebereikt; l-1 < range(0, jaar).length; l++) {
		if (O2percent <= zuurstofaarde) {
			O2aardebereikt = i;
			console.log(`Zuurstof aarde bereik in jaar: ${boom_jaar + O2aardebereikt-1}`);
			console.log(`Zuurstof aarde bereik in jaar: ${O2aardebereikt}`);
			break
		}
		// console.log(i);
		
		eerstekippen = tweedekippen;
		kippenN = eerstekippen * conversiegraadN2;
		tweedekippen = Math.ceil(eerstekippen * groeifactorKippen);
		O2_massa1 = O2_massa2;
		O2_massa2 = O2_massa1 - kippenN;
		O2percent = (O2_massa1/(dichtheidO*inhoudatmosfeer)) * 100;
		// O2array.push(O2_massa1)

		N2_massa1 = N2_massa2;
		N2_massa2 = N2_massa1 + kippenN;
		N2percent = (N2_massa1/(dichtheidN*inhoudatmosfeer)) * 100;
		// N2array.push(N2_massa1)

		if (O2percent < 100 && O2percent > 0) {
		percentO2array.push(O2percent)
		}
		if (N2percent < 100 && N2percent > 0) {
			percentN2array.push(N2percent)
		}

		console.log(`${i}\t${O2percent}\t\t${N2percent}\t\t${eerstekippen}`);
	}
	// console.log(`O2 array: \n${O2array}`)
	// console.log(`CO2 array: \n${CO2array}`)
	// console.log(`N2 array: \n${N2array}`)
};
function showchart() {
	ozonlaag();
	var jaar = Number(document.getElementById('jaren').value);

	var ctx = document.getElementById('myChart');
	var chart = new Chart(ctx, {
		type: 'line',

		data: {
			labels: range(0, jaar),
			datasets: [{
				label: 'O2 [%]',
				// backgroundColor: 'rgb(255, 99, 132)',
				borderColor: 'rgb(0, 150, 250)',
				data: percentO2array
			}, {
				label: 'CO2 [%]',
				// backgroundColor: 'rgb(255, 99, 132)',
				borderColor: 'rgb(190, 190, 190)',
				data: percentCO2array
			}, {
				label: 'N2 [%]',
				// backgroundColor: 'rgb(255, 99, 132)',
				borderColor: 'rgb(0, 250, 100)',
				data: percentN2array
			}]
		},

		options: {}
	});

	percentO2array = [];
	percentCO2array = [];
	percentN2array = [];
	// This works
	// var chart = new Chart(ctx, {
	// 	// The type of chart we want to create
	// 	type: 'line',

	// 	// The data for our dataset
	// 	data: {
	// 		labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
	// 		datasets: [{
	// 			label: 'My First dataset',
	// 			// backgroundColor: 'rgb(255, 99, 132)',
	// 			borderColor: 'rgb(255, 99, 132)',
	// 			data: [0, 10, 5, 2, 20, 30, 45]
	// 		}]
	// 	},

	// 	// Configuration options go here
	// 	options: {}
	// });
};


function marspreload() {
	document.getElementById('name').value = 'Mars';
	document.getElementById('radius').value = 6752000;
	document.getElementById('hoogteAtmosfeer').value = 10000;
	document.getElementById('zuurstof').value = 0.34;
	document.getElementById('koolstof').value = 95;
	document.getElementById('stikstof').value = 2.7;
	document.getElementById('conversiegraadO2').value = 20;
	document.getElementById('conversiegraadN2').value = 0.49275;
	document.getElementById('groeifactorBomen').value = 1.2;
	document.getElementById('groeifactorKippen').value = 3;
};	

function jaren() {
	planeetinfo();

	var jaren = document.getElementById('jaren').value;
	console.log(jaren);

	var bomen = Math.ceil(((inhoudatmosfeer * (Math.abs(dCO2))/100) * dichtheidC) / sum(range(0, jaren).map(x => groeifactorBomen**x * conversiegraadO2)));
	var kippen = Math.ceil(((inhoudatmosfeer * (Math.abs(dCO2 - (zuurstof - zuurstofaarde)))/100) * dichtheidO) / sum(range(0, jaren).map(x => (groeifactorKippen**x * conversiegraadN2))));
	
	console.log(`Bomen: ${bomen}`);
	console.log(`Kippen: ${kippen}`);
	
	document.getElementById("kippenans").innerHTML = kippen;
	document.getElementById("bomenans").innerHTML = bomen;
	document.getElementById("jaarans").innerHTML = jaren;
	return [bomen, kippen]
};