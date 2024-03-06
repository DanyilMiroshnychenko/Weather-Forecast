# Weather Forecast

#### Video demo: https://youtu.be/P0ce__vDvHU

#### Description:
The Weather Forecast is a Python-based tool designed to fetch and display weather forecasts for a chosen location, offering forecasts for periods ranging from 1 to 8 days. This is achieved using the [OpenWeatherMap API](https://openweathermap.org/api/one-call-3). The script allows users to input a city name in English and, optionally, a country code following the ISO 3166 standard. For locations in the USA, a state code can also be specified. If the country or state code is left empty, the script attempts to identify the most accurate location using the [OpenWeatherMap Geocoding API](https://openweathermap.org/api/geocoding-api).

### Installation:
Before running the script, ensure that all required Python dependencies are installed. This can be done by running the following command in your terminal:

```
pip install -r requirements.txt
```

### Files in the Project:
- **`test_project.py`**: The main Python script that interfaces with the OpenWeatherMap APIs. It handles user inputs and displays the weather forecast.
- **`requirements.txt`**: Contains all the necessary Python libraries required for the script to function properly.

### How to Run the Script:
1. **Input City Name**: Enter the name of the city in English.
2. **Country Code (Optional)**: Provide the country code as per ISO 3166 standard format. If omitted, the script will guess the location.
3. **State Code (USA Only, Optional)**: For USA locations, you may specify a state code.
4. **Specify the Duration**: Choose the number of forecast days (from 1 to 8).
5. The script will then fetch and display the weather forecast for your specified location and duration.

### Output Description:
Upon successful execution, the script outputs the weather forecast for the specified number of days, with each forecast separated by an empty line. The output is formatted as follows:

```
Forecast for Lieto, FI

29.12.2023:
Summary: Expect a day of partly cloudy with snow
Temperature is: 0.26°C
Wind speed is: 4.04 m/s
```

### Design Choices:
- **Modular Code Structure**: The code is divided into smaller, focused functions for simplicity, adherence to the single responsibility principle, and ease of testing.
- **User-Friendly Interface**: The script is designed for ease of use, with clear prompts and a straightforward workflow.
- **Flexible Location Input**: The option to specify country and state codes allows for more precise location identification, enhancing the accuracy of the weather forecast.
