<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Weatherly 🌤️</title>
</head>
<body>

<h1 align="center">Weatherly 🌤️</h1>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.11-blue" alt="Python">
  </a>
 
</p>

<p align="center">
  A <strong>Python desktop weather app</strong> that shows real-time weather with a <strong>day/night GUI</strong>. Enter a city and get current temperature, rain, and snowfall instantly!
</p>

<hr>

<h2>✨ Features</h2>
<ul>
  <li>🌡️ Shows current temperature, rain, and snowfall</li>
  <li>🌞 Automatic day/night mode with matching background</li>
  <li>🖼️ Dynamic weather icons using <strong>Pillow (PIL)</strong></li>
  <li>🖱️ Simple <strong>Tkinter GUI</strong> with input placeholder</li>
  <li>🌐 Fetches data via APIs (<code>open-meteo.com</code> & <code>geocode.maps.co</code>)</li>
</ul>

<h2>🖼️ Screenshots</h2>
<p><strong>Day Mode:</strong></p>
<img src="sun-cloud.png" alt="Day Mode" width="300">
<p><strong>Night Mode:</strong></p>
<img src="night-mode.png" alt="Night Mode" width="300">

<h2>💻 Installation</h2>
<pre>
git clone https://github.com/yourusername/Weatherly.git
cd Weatherly
pip install requests pillow
</pre>
<p>Make sure <code>sun-cloud.png</code> and <code>night-mode.png</code> are in the project folder.</p>

<h2>🚀 Usage</h2>
<pre>
python weather_app.py
</pre>
<ol>
  <li>Enter your city or address</li>
  <li>Click <strong>Press to get Weather</strong></li>
  <li>See real-time weather with day/night visuals!</li>
</ol>

<h2>⚡ Notes</h2>
<ul>
  <li>Requires internet connection</li>
  <li>Replace <code>API_LOCATE</code> with your API key if needed</li>
  <li>Uses <code>open-meteo.com</code> for weather and <code>geocode.maps.co</code> for location</li>
</ul>

<h2>🛠️ Built With</h2>
<ul>
  <li>Python 3</li>
  <li>Tkinter (GUI)</li>
  <li>Requests (API calls)</li>
  <li>Pillow (PIL) (image handling)</li>
</ul>

</body>
</html>
