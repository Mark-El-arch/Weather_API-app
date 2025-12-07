import sys, requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QVBoxLayout, QPushButton)
from PyQt5.QtCore import Qt

class Weather_App(QWidget):
    def __init__(self):
        super().__init__()
        #creating needed widgets below
        self.city_label = QLabel('Enter city name: ', self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton('Get Weather', self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather App') #to ste title of app

        #adding vertical layout to widgets
        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        #aligning widgets to the centre
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        #setting object names for widgets for easy handling when applying styles
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        #applying css-like styles to widgets
        self.setStyleSheet('''
            QPushButton, QLabel {
                font-family: calibri;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label {
                font-size: 50px;
            }
        ''')

        self.get_weather_button.clicked.connect(self.get_weather)

    #adding functionalities to weather app
    def get_weather(self):
        api_key = '35515e5068af2d210ee8e6468abe547f'
        city = self.city_input.text()
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        try:
            response  = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data['cod'] == 200:
                self.display_weather()
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    print('Bad request!\nPlease check your input.')
                case 401:
                    print('Unauthorized!\nInvalid API key.')
                case 403:
                    print('Forbidden!\nAccess is denied.')
                case 404:
                    print('Not Found!\nCity not found.')
                case 500:
                    print('Internal Server Error!\nPlease try again later.')
                case 502:
                    print('Bad Gateway!\nInvalid response from the server.')
                case 503:
                    print('Service Unavailable!\nServer is down.')
                case 504:
                    print('Gateway Timeout!\nNo response from the server.')
                case _:
                    print(f'HTTP error occurred\n{http_error}')
        except requests.exceptions.RequestException:
            pass

    def display_error(self):
        pass

    def display_weather(self):
        pass

def main():
    #creating main application window
    app = QApplication(sys.argv)
    weather_app = Weather_App()
    weather_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__': #ensures our program runs only when this program is run directly,i.e, when it's needed
    main()