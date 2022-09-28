from flask import Flask, request, render_template
from conceptproof import getDirector
app = Flask(__name__, template_folder='templates')

@app.route('/', methods =["GET", "POST"])
def getDirectorFrom():
    if request.method == 'POST':
        movie = request.form.get("Director")
        return getDirector(movie)
    return render_template("form.html")

if __name__ == '__main__':
    app.debug = True
    app.run()