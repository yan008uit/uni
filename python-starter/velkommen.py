from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def hello() -> 'html':

    return render_template('velkommen.html',
                           the_title='Velkommen til Python & templates')

if __name__ == "__main__":
    app.run()