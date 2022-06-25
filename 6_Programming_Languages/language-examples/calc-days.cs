function calculateDays(int month, int year) {
    var days = 0;
    switch (month) {
        case 1:
            days = 31;
            break;
        case 2:
            if (year % 4 == 0) {
                days = 29;
            } else {
                days = 28;
            }
            break;
        case 3:
            days = 31;
            break;
        case 4:
            days = 30;
            break;
        case 5:
            days = 31;
            break;
        case 6:
            days = 30;
            break;
        case 7:
            days = 31;
            break;
        case 8:
            days = 31;
            break;
        case 9:
            days = 30;
            break;
        case 10:
            days = 31;
            break;
        case 11:
            days = 30;
            break;
        case 12:
            days = 31;
            break;
    }
    return days;
}
function calculateHours(int days) => days * 24;
function calculateMinutes(int hours) => hours * 60;
function calculateTime(int days, int hours, int minutes) => days + " days " + hours + " hours " + minutes + " minutes";

