from flask import Flask, render_template, request
from form import InputForm
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

Blue = []
Green =[]
Red = []
for i in range(1, 61):
    Blue.append(i)
for i in range(61, 86):
    Green.append(i)
for i in range(86, 101):
    Red.append(i)

@app.route('/', methods=['POST', 'GET'])
def input():
    if request.method == 'GET':
        form = InputForm()
        return render_template('html/inputform.html', form=form)
    if request.method == 'POST':
        form = InputForm()
        return render_template('html/inputform.html', form=form)


@app.route('/output', methods=['POST'])
def output():
    if request.method == 'POST':
        if int(request.form['Предмет']) in Blue:
            message = "Скорее всего ваш предмет синего цвета!"
            return render_template('html/output.html', message=message)
        elif int(request.form['Предмет']) in Green:
            message = "Скорее всего ваш предмет зеленого цвета!"
            return render_template('html/output.html', message=message)
        elif int(request.form['Предмет']) in Red:
            message = "Скорее всего ваш предмет красного цвета!"
            return render_template('html/output.html', message=message)
        else:
            message = "Такого предмета нет!"
            return render_template('html/output.html', message=message)

if __name__ == "__main__":
    app.run()
