import requests
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/meteorology.db'
db = SQLAlchemy(app)


class Meteorology(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(5), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(15), nullable=False)
    probability = db.Column(db.Integer, nullable=False)
    precipitation = db.Column(db.Integer, nullable=False)
    temp_min = db.Column(db.Integer, nullable=False)
    temp_max = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        tasks = Meteorology.query.order_by(Meteorology.id).all()
        return render_template("index.html", tasks=tasks)


@app.route('/reorder/<preference>', methods=['GET', 'POST'])
def reorder(preference):
    if preference == 'name':
        tasks = Meteorology.query.order_by(Meteorology.name).all()
    else:
        tasks = Meteorology.query.order_by(Meteorology.id).all()
    return render_template("index.html", tasks=tasks)


@app.route('/cidade', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect('/')
    else:
        prefix = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/'
        id_city = request.args['id']
        suffix = '/days/15?token=b22460a8b91ac5f1d48f5b7029891b53'

        if Meteorology.query.filter_by(id=id_city).first():
            app.logger.info('id=%s is already stored', id_city)
            return 'Already stored'

        try:
            r = requests.get(prefix + id_city + suffix)

            new_data = Meteorology(
                id=r.json()['id'],
                name=r.json()['name'],
                state=r.json()['state'],
                country=r.json()['country'],
                date=r.json()['data'][0]['date'],
                probability=r.json()['data'][0]['rain']['probability'],
                precipitation=r.json()['data'][0]['rain']['precipitation'],
                temp_min=r.json()['data'][0]['temperature']['min'],
                temp_max=r.json()['data'][0]['temperature']['max']
            )

            db.session.add(new_data)
            db.session.commit()

            app.logger.info('id=%s was successfully stored', id_city)
            return 'Successfully stored'

        except:
            app.logger.info('id=%s error storing', id_city)
            return 'There was an issue adding this new meteorology data'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')