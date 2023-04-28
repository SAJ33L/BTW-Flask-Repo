from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == 'POST':
        api_key = ''
        city_name = request.form.get('city')
        print(city_name)
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+api_key
        weatherData = requests.get(url.format(city_name)).json()
        min_temp = weatherData['main']['temp_min']
        max_temp = weatherData['main']['temp_max']
        hum = weatherData['main']['humidity']
        current_temp = weatherData['main']['temp']
        print(weatherData)
        print(min_temp, max_temp, hum, current_temp)
        return render_template('index.html', temp = current_temp, min_temp=min_temp, max_temp=max_temp, hum=hum)

    else:
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug= True, port = 5001)
