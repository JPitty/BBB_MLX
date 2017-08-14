var i2c = require('i2c');
var addr = 0x68;
var wire = new i2c(address)

//wire.scan (function(err, data) {
	//result
//});

wire.on('data', function(data) {
	  // result for continuous stream contains data buffer, address, length, timestamp
});
