function calculateDaysBetweenDates(begin, end) {    
    var oneDay = 24*60*60*1000; // hours*minutes*seconds*milliseconds
    var firstDate = new Date(begin);
    var secondDate = new Date(end);
    var diffDays = Math.round(Math.abs((firstDate.getTime() - secondDate.getTime())/(oneDay)));
    return diffDays;
}
function testCalculateDaysBetweenDates() {
    var begin = "2017-01-01";
    var end = "2017-01-03";
    var expected = 2;
    var actual = calculateDaysBetweenDates(begin, end);
    if (expected === actual) {
        console.log("PASSED");
    } else {
        console.log("FAILED");
        console.log("Expected: " + expected);
        console.log("Actual: " + actual);
    }
}
testCalculateDaysBetweenDates();

function calculateHoursBetweenDates(begin, end){    
    var oneDay = 24*60*60*1000; // hours*minutes*seconds*milliseconds
    var firstDate = new Date(begin);
    var secondDate = new Date(end);
    var diffDays = Math.round(Math.abs((firstDate.getTime() - secondDate.getTime())/(oneDay)));
    var diffHours = diffDays * 24;
    return diffHours;
}
function testCalculateHoursBetweenDates() {
    var begin = "2017-01-01";
    var end = "2017-01-03";
    var expected = 48;
    var actual = calculateHoursBetweenDates(begin, end);
    if (expected === actual) {
        console.log("PASSED");
    } else {
        console.log("FAILED");
        console.log("Expected: " + expected);
        console.log("Actual: " + actual);
    }
}       
testCalculateHoursBetweenDates();