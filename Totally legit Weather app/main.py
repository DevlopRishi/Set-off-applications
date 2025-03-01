import requests

def get_weather(city):
    # Fake weather data (since we're not using a real API)
    return {
        "city": city,
        "temperature": 20,
        "description": "Partly cloudy"
    }

def fake_ai_analysis(weather_data):
    print("Analyzing weather data using AI...")
    # Simulate some fake analysis
    analysis_result = f"The weather in {weather_data['city']} is {weather_data['description']} with a temperature of {weather_data['temperature']}°C."
    return analysis_result

def main():
    print("Welcome to the Fake AI Weather App!")
    city = input("Enter the name of your city: ")

    # Get weather data
    weather_data = get_weather(city)

    # Perform fake AI analysis
    analysis_result = fake_ai_analysis(weather_data)

    # Display the results
    print(analysis_result)
    print("At the end of the day, remember to touch grass!")

if __name__ == "__main__":
    main()