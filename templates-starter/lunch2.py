from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/lunch', methods=["GET", "POST"])

def lunchCalculator() -> 'html':

    if request.method == "POST":
        req = request.form

        missing = []

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template('lunch2.html',  the_title='Python lunch calculator', feedback=feedback)

        name = request.form['name']
        cost = request.form.get('cost', type=float)
        days = request.form.get('days', type=int)
        return render_template('lunch2.html',
                           the_title='Python lunch calculator', name=name, lunchCost=cost*days,)
    else:
        return render_template('lunch2.html',
                           the_title='Python lunch calculator')

if __name__ == "__main__":
    app.run(debug=True)