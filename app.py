from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    energy_data = [
        {'year': 2010, 'energy': 1000},
        {'year': 2011, 'energy': 1200},
        {'year': 2012, 'energy': 1350},
        {'year': 2013, 'energy': 1100},
        {'year': 2014, 'energy': 1250},
        # Add more data points as needed
    ]

    years = [data['year'] for data in energy_data]
    energy_values = [data['energy'] for data in energy_data]

    return render_template('index.html', years=years, energy_values=energy_values)

@app.route('/counties')
def count_yolo():
    return render_template('counties.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
