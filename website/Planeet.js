var dichtheidC = 1.986;
var dichtheidO = 1.43;
var dichtheidN = 1.25;
var zuurstofaarde = 20.95;
var koolstofaarde = 0.038;
var stikstofaarde = 78.08;

class Planeet {
	constructor(name, radiusplaneet, hoogteatmosfeer, zuurstof, koolstof, stikstof, conversiegraadO2, conversiegraadN2, boomgroei, kipgroei) {
		this.name = name;
		this.rp = radiusplaneet;
		this.ha = hoogteatmosfeer;
		this.zuurstof = zuurstof;
		this.koolstof = koolstof;
		this.stikstof = stikstof;
		this.cgO = conversiegraadO2;
		this.cgN = conversiegraadN2;
		this.boomgroei = boomgroei;
		this.kipgroei = kipgroei;
		this.O2eerstemassa = 0;
		this.O2tweedemassa = 0;
		this.CO2eerstemassa = 0;
		this.CO2tweedemassa = 0;
		this.N2eerstemassa = 0;
		this.N2tweedemassa = 0;
	}
	static inhouda() {
		this.inhoudplaneet = (4 / 3) * Math.PI * this.rp ** 3;
		this.inhoudatmosfeer = (4 / 3) * Math.PI * (this.rp + this.ha) ** 3 - this.inhoudplaneet;
	}
}
