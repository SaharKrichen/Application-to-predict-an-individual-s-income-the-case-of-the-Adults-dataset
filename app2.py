from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)
model = pickle.load(open('adult.pkl', 'rb'))
@app.route('/')
def man():
    return render_template('home.html')
@app.route('/result')
def result():
    df = pd.read_csv (r"F:\1ère mastere SIDATA\2ème semestre\Atelier fouille de données\adult.csv", delimiter=';')
    return render_template("after.html", df_view=df)
@app.route('/predict', methods=['POST'])
def home():
  if request.method == 'POST':
    age = request.form['a']
    sexe = request.form['sexe']
    workclass = request.form['workclass']
    educational_num = request.form['d']
    occupation = request.form['occupation']
    race = request.form['race']
    hours = request.form['g']
    continent = request.form['content']
    marital = request.form['i']
    age = age
    educational_num =educational_num
    hours=hours
    if sexe == "Homme":
        sexe= 0
    else:
        sexe = 1
    if workclass == "Foderal - gov":
        workclass= 0
    elif workclass == "Local-gov":
        workclass=1
    elif workclass == "private":
        workclass=2
    elif workclass == "Self-emp-inc":
        workclass = 3
    elif workclass == "Self-emp-not-inc":
        workclass =4
    elif workclass == "State_gov":
        workclass =5    
    else:
        workclass=6
    if occupation == "prof":
            occupation = 9.0
    elif occupation == "handlers":
           occupation = 5.0
    elif occupation == "craft":
           occupation = 2.0
    elif occupation == "exec":
           occupation = 3.0
    elif occupation == "sadm":
           occupation =0.0
    elif occupation == "machine":
            occupation=6.0
    elif occupation == "transport":
            occupation = 13.0
    elif occupation == "sales":
           occupation=11.0
    elif occupation == "ff":
            occupation = 4.0
    elif occupation == "tech":
            occupation=12.0
    elif occupation == "protective":
            occupation = 10.0
    elif occupation == "priv":
            occupation = 8.0
    elif occupation == "armed":
            occupation = 1.0
    else :
            occupation = 7.0
    if race == "white":
        race = 4.0
    elif race == "black":
            race =2.0
    elif race == "asian":
            race = 1.0
    elif race == "amer":
            race = 0.0
    else:
            race =3.0
    
    if continent == "Asia":
           continent = 0 
    elif continent == "Europe":
             continent = 2
    elif continent == "North America":
             continent = 3
    else:
             continent=1
    if marital == "Married":
            marital = 0
    else:
            marital= 1  

    lst = list()
    lst.append((age))
    lst.append((educational_num))
    lst.append((hours))
    lst.append((sexe))
    lst.append((workclass))
    lst.append((occupation))
    lst.append((race))
    lst.append((continent))
    lst.append((marital))
    ans = model.predict([np.array(lst,dtype='int64')])
    result=ans[0]
    return render_template("after.html",age=age,sexe=sexe,hours=hours,educational_num=educational_num,workclass=workclass,continent=continent,race=race,marital=marital,occupation=occupation,result=result)
  else:
       return render_template("home.html") 

if __name__ == "__main__":
    app.run(debug=True)  