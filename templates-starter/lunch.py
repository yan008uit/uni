from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/lunch', methods=["GET", "POST"])

def lunchCalculator() -> 'html':

    if request.method == "POST":
        name = request.form['name']
        cost = request.form.get('cost', type=float)
        days = request.form.get('days', type=int)
        return render_template('lunch.html',
                           the_title='Python lunch calculator', name=name, lunchCost=cost*days,)
    else:
        return render_template('lunch.html',
                           the_title='Python lunch calculator')

if __name__ == "__main__":
    app.run(debug=True)