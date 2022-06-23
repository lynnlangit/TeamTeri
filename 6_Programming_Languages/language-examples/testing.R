calculateDays() {
  echo "days($1, $2, $3)" | R --no-save
}
calculateHours() {
  echo "hours($1, $2, $3)" | R --no-save
}
calculateMinutes() {
  echo "minutes($1, $2, $3)" | R --no-save
}
calculateSeconds() {
  echo "seconds($1, $2, $3)" | R --no-save
}
calculateTime() {
  echo "time($1, $2, $3)" | R --no-save
}
calculateTimeFromDays() {
  echo "timeFromDays($1, $2, $3)" | R --no-save
}