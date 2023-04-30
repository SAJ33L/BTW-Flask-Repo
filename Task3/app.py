from flask import Flask, render_template, request
import requests
import os

# Initialize App
app = Flask(__name__)

# Define route and methods
@app.route('/', methods = ["GET", "POST"])
def home():
    # Check if request is POST
    if request.method == 'POST':
        # Get API key
        api_key = os.environ.get('API_KEY')
        # Get city name from form
        city_name = request.form.get('city')
        # Create url for API request
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"
        # Get weather data from API
        weather_data = requests.get(url).json()
        # Extract relevant data from response
        min_temp = weather_data['main']['temp_min']
        max_temp = weather_data['main']['temp_max']
        hum = weather_data['main']['humidity']
        current_temp = weather_data['main']['temp']
        # Render template with extracted data
        return render_template('index.html', temp = current_temp, min_temp=min_temp, max_temp=max_temp, hum=hum)

    else:
        return render_template('index.html')


# Run App
if __name__ == '__main__':
    app.run(debug= True, port = 5001)