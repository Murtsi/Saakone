# Weather App

Welcome to the Weather App project! This repository contains two versions of a simple weather application: a Python-only version and a web-based version using HTML and JavaScript.

## Features

- **Python Version**: A command-line application that fetches and displays weather data.
- **HTML & JavaScript Version**: A web-based application with a user-friendly interface for displaying weather data.

## Installation

### Python Version

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app/python-version
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

### HTML & JavaScript Version

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app/web-version
   ```

2. **Open `index.html` in your web browser**.

## Usage

### Python Version

- After running `main.py`, you will be prompted to enter a city name.
- The application will fetch and display the current weather for the specified city.

### HTML & JavaScript Version

- Open `index.html` in your browser.
- Enter the city name in the input field and click the "Get Weather" button.
- The current weather for the specified city will be displayed on the page.

## API Key

Both versions of the application use the OpenWeatherMap API to fetch weather data. You will need an API key to use this service.

1. Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get your API key.
2. **For the Python version**: Place your API key in the `config.py` file.
3. **For the HTML & JavaScript version**: Place your API key in the `script.js` file.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to open an issue or reach out to me at [your.email@example.com](mailto:your.email@example.com).

Happy coding!
