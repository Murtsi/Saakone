const api = {
    key:   "YOUR_API_KEY",
    base: "https://api.openweathermap.org/data/2.5/weather?"
};

const searchbox = document.querySelector('.search-box');
searchbox.addEventListener('keypress', function(evt) {
    if (evt.key === 'Enter') {
        getResults(searchbox.value);
    }
});

function getResults(query) {
    fetch(`${api.base}q=${query}&units=metric&appid=${api.key}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.cod !== 200) {
                throw new Error(data.message);
            }
            displayResults(data);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            displayError(error.message);
        });
}

function displayResults(weather) {
    if (!weather || !weather.sys || !weather.main || !weather.weather) {
        displayError("Invalid data received from the API");
        return;
    }

    let city = document.querySelector('.location .city');
    city.innerText = `${weather.name}, ${weather.sys.country}`;

    let now = new Date();
    let date = document.querySelector('.location .date');
    date.innerText = dateBuilder(now);

    let temp = document.querySelector('.current .temp');
    temp.innerHTML = `${Math.round(weather.main.temp)}<span>°c</span>`;

    let weather_el = document.querySelector('.current .weather');
    weather_el.innerText = weather.weather[0].main;

    let hilow = document.querySelector('.hi-low');
    hilow.innerText = `${Math.round(weather.main.temp_min)}°c / ${Math.round(weather.main.temp_max)}°c`;
}

function displayError(message) {
    let city = document.querySelector('.location .city');
    city.innerText = "Error";

    let date = document.querySelector('.location .date');
    date.innerText = "";

    let temp = document.querySelector('.current .temp');
    temp.innerHTML = "";

    let weather_el = document.querySelector('.current .weather');
    weather_el.innerText = message;

    let hilow = document.querySelector('.hi-low');
    hilow.innerText = "";
}

function dateBuilder(d) {
    let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    let day = days[d.getDay()];
    let date = d.getDate();
    let month = months[d.getMonth()];
    let year = d.getFullYear();

    return `${day} ${date} ${month} ${year}`;
}
