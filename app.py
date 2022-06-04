import json
import funkce
import plotly
import plotly.express as px
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    getAVG = funkce.GetAvgDayStepsForAll
    getAVG = getAVG.rename(columns={"STEPS": "Počet kroků"})
    #print(str(getAVG))
    stepsGraph = px.bar(getAVG, labels=dict(
        DAY="DEN", STEPS="Počet kroků", value="Denní průměr kroků", variable=""))
    graphJSON = json.dumps(stepsGraph, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("pages/home/home.html", stepsGraph=graphJSON)


@app.route('/user/<alias>/<args>')
def user(alias, args):
    getUser = funkce.GetUserByAliasFunc(alias, args)
    return render_template('pages/user/user.html', user=getUser)


@app.route('/class/')
def classRoom():
    schedule = funkce.FormatSchedule()
    dny = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    new_schedule = []
    for den in dny:
        new_schedule.append(schedule[den])
    nejvic_den = None
    max_subjects = 0
    count_subjects = None
    for i in range(len(new_schedule)):
        count_subjects = len(new_schedule[i])
        if count_subjects > max_subjects:
            max_subjects = count_subjects
            nejvic_den = i
    return render_template('pages/class/class.html', schedule=new_schedule, nejvic_den=nejvic_den)


if(__name__ == "__main__"):
    app.run(debug=True)
