from flask import Flask, render_template, url_for


app = Flask(__name__)




@app.route("/")
def palin():
    return render_template('palin.html')


@app.route("/palin-store")
def palin_store():
    return render_template('palin_store.html')

@app.route("/buy")
def buy():
    return render_template('buy.html')













if __name__ == "__main__":
    app.run(debug=True)
