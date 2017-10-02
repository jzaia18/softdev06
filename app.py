from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def root():
    if 'name' in request.args:
        return render_template('index.html', mostrecent=request.args['name'])
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

