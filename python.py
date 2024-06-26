import tkinter as tk
import requests
import io
from PIL import Image, ImageTk
from tkinter import ttk


def get_weather():
    city = city_entry.get().strip()

    api_key = "bb9d5d8b5a86b29e2d80e6cd44f0c861"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    print(f"Fetching weather for: {city}")
    print(f"URL: {url}")


    try:




        response = requests.get(url)
        response.raise_for_status()  # Ilmoittaa HTTP-vastauksen virheestä
        weather_data = response.json()

        if weather_data.get("cod") != 200:
            city_label.config(text="Error")
            temp_label.config(text="")
            desc_label.config(text=weather_data.get("message", "City not found"))
            icon_label.config(image='')
        else:

            city_name = weather_data['name']
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            icon_code = weather_data['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"

            city_label.config(text=city_name)
            temp_label.config(text=f"{temperature}°C")
            desc_label.config(text=description.capitalize())
            humidity_label.config(text=f"Humidity: {humidity}%")
            wind_label.config(text=f"Wind Speed: {wind_speed} m/s")




            # Haetaan kuvakkeet

            icon_response = requests.get(icon_url)
            icon_image = Image.open(io.BytesIO(icon_response.content))
            icon_photo = ImageTk.PhotoImage(icon_image)
            icon_label.config(image=icon_photo)
            icon_label.image = icon_photo


    except requests.exceptions.RequestException as e:
            city_label.config(text="Error")
            temp_label.config(text="")
            desc_label.config(text=f"Request failed: {e}")
            icon_label.config(image='')


# Luodaan ikkuna
window = tk.Tk()
window.title("Weather App")
window.geometry("400x500")
window.resizable(False, False)



#Käytetään parempaa ulkoasua

style = ttk.Style()
style.configure("TFrame", background="#2c3e50")
style.configure("TLabel", background="#2c3e50", foreground="white")
style.configure("TButton", background="#7393B3", font=('Arial', 14), padding=10)
style.map("TButton",
          background=[('active', '#7393B3')],
          foreground=[('active', 'black')])





# Luodaan kirjoituskentälle reunat

input_frame = ttk.Frame(window, padding="10")
input_frame.pack(fill='x', padx=10, pady=10)

# Luo kentän kaupungin nimen syöttämiseen
city_entry = ttk.Entry(input_frame, font=('Arial', 18))
city_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))

# Luo painikkeen jolla haetaan säätiedot
button = ttk.Button(input_frame, text="Sää", command=get_weather, style="DarkButton.TButton")
button.pack(side='left', padx=(10, 0))

# Luo kentän jossa näytetään säätiedot
weather_frame = ttk.Frame(window, padding="10")
weather_frame.pack(fill='both', expand=True, padx=10, pady=10)




# Säätietojen kentät
city_label = ttk.Label(weather_frame, font=('Arial', 24))
city_label.pack(pady=10)

icon_label = ttk.Label(weather_frame)
icon_label.pack(pady=10)

temp_label = ttk.Label(weather_frame, font=('Arial', 48))
temp_label.pack(pady=10)

desc_label = ttk.Label(weather_frame, font=('Arial', 18))
desc_label.pack(pady=5)

humidity_label = ttk.Label(weather_frame, font=('Arial', 18))
humidity_label.pack(pady=5)

wind_label = ttk.Label(weather_frame, font=('Arial', 18))
wind_label.pack(pady=5)



# Set the background color for the main window
window.configure(bg="#2c3e50")


window.mainloop()