from flask import Flask, request

app = Flask(__name__)

@app.route('/query-example')
def query_example():
    try:
        # if key doesn't exist, returns None
        language = request.args.get('language')

        # if key doesn't exist, returns a 400, bad request error
        framework = request.args['framework']

        # if key doesn't exist, returns None
        website = request.args.get('website')

        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>
                  <h1>The website value is: {}'''.format(language, framework, website)
    except Exception as e:
        return (str(e))

if __name__ == "__main__":
    app.run(debug=True)

