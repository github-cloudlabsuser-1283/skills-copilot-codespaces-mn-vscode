// function to convert Celcius to Fahrenheit
function celciusToFahrenheit(celcius) {
  return (celcius * 9/5) + 32;
}
// function to convert Fahrenheit to Celcius
function fahrenheitToCelcius(fahrenheit) {
  return (fahrenheit - 32) * 5/9;
}


// Driver code
const celcius = 25;
const fahrenheit = 77;
console.log(`${fahrenheit}°F is equal to ${fahrenheitToCelcius(fahrenheit)}°C`);
console.log(`${celcius}°C is equal to ${celciusToFahrenheit(celcius)}°F`);
