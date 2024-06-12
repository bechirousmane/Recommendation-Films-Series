from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add_rating', methods=['GET', 'POST'])
def add_rating():
    if request.method == 'POST':
        rating = request.form['rating']
        return redirect(url_for('home'))
    return render_template('add_rating.html')


@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        movie_title = request.form['title']
        return redirect(url_for('home'))
    return render_template('add_movie.html')

if __name__ == '__main__':
    app.run(debug=True)
