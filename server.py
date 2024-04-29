from flask import Flask, render_template
from flask import redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


@app.route('/')
@app.route('/main_window')
def index():
    title = "Загатовка"
    return render_template('base.html', title=title)


@app.route('/themes')
def training():
    title = "Тренировочный центр"
    if "инженер" in prof or "строитель" in prof:
        professional_orientation = "Инженерные тренажеры"
    else:
        professional_orientation = "Научные симуляторы"
    return render_template('training.html', title=title, professional_orientation=professional_orientation)


@app.route('/list_paragraphs/<lesson>')
def list_prof(lesson):
    list_professions = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач",
                        "инженер по терраформированию", "климатолог", "спеиалист по радиаионной защите", "астролог",
                        "гляциолог", "инженер жизнеобеспечения", "метеоролог", "оператор марсохода", "киберинженер",
                        "штурман", "пилот дронов"]
    return render_template('list_prof.html', list_professions=list_professions, display_methodist=display_method)


@app.route('/paragraph/<number>')
def distribution(number):
    astronauts = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template('distribution.html', astronauts=astronauts)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
