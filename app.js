console.log("Weather App is connected Successfully")
const apikey = "9fde7798706edf680cb709b5eedd87b2";
document.querySelector("button").addEventListener("click", function () {
    const city = document.querySelector("textarea").value;
    const baseUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apikey}&units=metric`;
    alert("You searched for: " + city);
    fetch(baseUrl)
    .then(response => response.json())
    .then(data => {
        document.getElementById('location').textContent = `Location: ${data.name}, ${data.sys.country}`;
        document.getElementById('temperature').textContent = `Temperature: ${data.main.temp}°C`;
        document.getElementById('condition').textContent = `Condition: ${data.weather[0].description}`;
        document.getElementById('humidity').textContent = `Humidity: ${data.main.humidity}%`;
        document.getElementById('wind').textContent = `Wind Speed: ${data.wind.speed} km/h`;
    })
    .catch(error => {
        alert("could not fetch weather data. Please try again");
        console.error(error);
    })
})
