calculateDays = lambda x: x * 365
calculateHours = lambda x: x * 365 * 24
calculateMinutes = lambda x: x * 365 * 24 * 60
calculateSeconds = lambda x: x * 365 * 24 * 60 * 60

calculateTime = lambda x, y: calculateDays(x) + calculateHours(y)