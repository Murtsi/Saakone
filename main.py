import tkinter as tk
import requests



def get_weather():
    city = city_entry.get().strip()

    api_key = "bb9d5d8b5a86b29e2d80e6cd44f0c861"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    print(f"Fetching weather for: {city}")
    print(f"URL: {url}")


    try:




        response = requests.get(url)
        response.raise_for_status()  # Ilmoittaa jos tulee virhe
        weather_data = response.json()

        if weather_data.get("cod") != 200:
            city_label.config(text="Error")
            temp_label.config(text="")
            desc_label.config(text=weather_data.get("message", "City not found"))
        else:

            city_name = weather_data['name']
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']

            city_label.config(text=city_name)
            temp_label.config(text=f"{temperature}°C")
            desc_label.config(text=description.capitalize())

    except requests.exceptions.RequestException as e:
            city_label.config(text="Error")
            temp_label.config(text="")
            desc_label.config(text=f"Request failed: {e}")



# Luodaan ikkuna
window = tk.Tk()
window.title("Weather App")

# Luo kentän kaupungin nimen syöttämiseen
city_entry = tk.Entry(window, font=('Arial', 18))
city_entry.pack(pady=10)


# Fontit tiedon näyttämiseen
city_label = tk.Label(window, font=('Arial', 24))
city_label.pack()

temp_label = tk.Label(window, font=('Arial', 48))
temp_label.pack()

desc_label = tk.Label(window, font=('Arial', 18))
desc_label.pack()

# Nappi joka hakee säätiedot
button = tk.Button(window, text="Get Weather", command=get_weather)
button.pack(pady=10)

window.mainloop()