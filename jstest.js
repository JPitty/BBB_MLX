"use strict";

const mraa = require('mraa');
let i2c = new mraa.I2c(1);
i2c.address(0x68);
//i2c.write("R,56.26");
console.log("Reading I2C..");
function readMLX() {
	    var d = i2c.read(7);
	        console.log(">> " + d);
}
setTimeout(function (e) { readMLX(); }, 500);
