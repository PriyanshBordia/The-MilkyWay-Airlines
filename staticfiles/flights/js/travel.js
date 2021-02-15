// document.addEventListener('DOMContentLoaded', () => {

// 	var today = new Date();

// 	var year = today.getFullYear();
// 	var month = parseInt(today.getMonth()) + 1;
// 	var date = today.getDate();

// 	today.setDate(date + 1);

// 	if (month < 10)
// 		month = '0' + month;

// 	if (date < 10)
// 		date = '0' + date;

// 	var hours = parseInt(today.getHours()) % 12;
// 	var minutes = today.getMinutes();
// 	var seconds = today.getSeconds();
// 	var mm_seconds = today.getMilliseconds();

// 	if (hours < 10)
// 		hours = '0' + hours;

// 	if (minutes < 10)
// 		minutes = '0' + minutes;

// 	if (seconds < 10)
// 		seconds = '0' + seconds;

// 	today = `${year}-${month}-${date}T${hours}:${minutes}:${seconds}.${mm_seconds}`;  

// 	document.getElementById('startDate').setAttribute('min', today);
// 	// document.getElementById('startDate').setAttribute('max', today);

// 	document.getElementById('endDate').setAttribute('min', today);
// 	// document.getElementById('endDate').setAttribute('max', today);

// 	document.querySelector('#startDate').onselect = () => {
// 		var start = document.getElementById('startDate').value;

// 		var end = document.getElementById('endDate');
//     	end.setAttribute('min', start);
// 	};

// 	document.querySelector('#endDate').onselect = () => {
// 		var end = document.getElementById('endDate').value;

// 		var start = document.getElementById('startDate');
// 		start.setAttribute('max', end);
// 	};
// });
