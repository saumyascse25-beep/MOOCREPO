from flask import flask
app = Flask(__name__)
@app.route("\"):
 def home:
    return "Home page"

if __name__==__main__:
    app.run(debug=True)