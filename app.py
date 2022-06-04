import json
import funkce
import komponenty
import plotly
import plotly.express as px
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    getAVG = funkce.GetAvgDayStepsForClass()
    getAVG = getAVG.rename(columns={"STEPS": "Počet kroků"})
    print(str(getAVG))
    stepsGraph = px.bar(getAVG, labels=dict(
        DAY="DEN", STEPS="Počet kroků", value="Denní průměr kroků", variable=""))
    graphJSON = json.dumps(stepsGraph, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("pages/home/home.html", stepsGraph=graphJSON)


@app.route('/class/')
def classRoom():
    komponenty.getTimeTable()
    return render_template('pages/class/class.html')


if(__name__ == "__main__"):
    app.run(debug=True)
