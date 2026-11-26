from flask import flask
app = Flask(__name__)
@app.route("\"):
 def home:
    return "Home page"
@app.route("search"):
 def search:
    return "Search feature"
@app.route("Agencies"):
 def agencies:
    return "1.INFOSYS,2.NPTEL"
if __name__==__main__:
    app.run(debug=True)
