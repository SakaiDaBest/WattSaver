from flask import Flask, render_template, url_for, request

app = Flask(__name__)

#route == link == url

#main route
@app.route("/") 
def main():
    return render_template("homepage.html", home=True)

@app.route("/bulb")
def bulb():
    return render_template("index.html")

@app.route("/Light_Bulbs")
def Bulbs():
    return render_template("Light_Bulbs.html")

@app.route("/DC_app")
def DC():
    return render_template("DC_app.html")

@app.route("/AC_app")
def AC():
    return render_template("AC_app.html")

@app.route("/calculate", methods=["post"])
def calculate():
    Country = str(request.form["Country"])
    Bulb = str(request.form["Bulb"])
    timeUsed = float(request.form["timeUsed"])
    power = float(request.form["power"])
    appn = int(request.form["applianceNumber"])
    m = timeUsed*power*appn
    calculated = False

    note = ""
    color = "alert-success"
    if timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Bulb == "LED":
        result1 = round(0.218*m,3)
        result2 = round(m*0.571,3)
        cresult1= round(m*0.758, 3)
        calculated = True
    elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Bulb == "CFL":
        result1 = round(0.218*m*0.75,3)
        result2 = round(m*0.571*0.75,3)
        cresult1= round(m*0.758*0.75, 3)
        calculated = True
    else:
        note = "One input is illogical. Try again"
        color = "alert-warning"
        return render_template("Light_Bulbs.html", note=note)
    return render_template("Light_Bulbs.html", calculated = calculated, cresult1=cresult1,result1=result1,result2=result2, note=note, color=color,Bulb=Bulb,cresult2=round(cresult1*2.33,3),result3=round(result1*2.33,3),result4=round(result2*2.33,3))




@app.route("/calculate_DC", methods = ["post"])
def calculate_DC():
    Country = str(request.form["Country"])
    Star = str(request.form["Star"])
    timeUsed = float(request.form["timeUsed"])
    power = float(request.form["power"])
    appn = int(request.form["applianceNumber"])
    m = timeUsed*power*appn
    calculated = False
    note = ""
    color = "alert-success"
    if timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "1 ⭐":
        result1 = round(0.218*m,3)
        result2 = round(m*0.571,3)
        cresult1= round(m*0.758, 3)
        calculated = True
        perc1 = 0.1
        perc2 = 0.15 
    elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "2 ⭐":
        result1 = round(0.218*m,3)
        result2 = round(m*0.571,3)
        cresult1= round(m*0.758, 3)
        calculated = True
        perc1 = 0.21
        perc2 = 0.32
    elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "3 ⭐":
        result1 = round(0.218*m,3)
        result2 = round(m*0.571,3)
        cresult1= round(m*0.758, 3)
        calculated = True
        perc1 = 0.331
        perc2 = 0.52 
    elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "4 ⭐":
        result1 = round(0.218*m,3)
        result2 = round(m*0.571,3)
        cresult1= round(m*0.758, 3)
        calculated = True
        perc1 = 0.464
        perc2 = 0.75
    elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and (Star == "5 ⭐" or Star == "None"):
        result1 = round(0.218*m,3)
        result2 = round(m*0.571,3)
        cresult1= round(m*0.758, 3)
        calculated = True
    else:
        note = "One input is illogical. Try again"
        color = "alert-danger"
        return render_template("DC_app.html", note=note)
    return render_template("DC_app.html", Star=Star,result1=result1, result2=result2,cresult1=cresult1, note=note, color=color, calculated=calculated, aresult2=round(((1-perc2/0.8625)*result2),3),aresult1=round(((1-perc1/0.5104))*result1,3), caresult1=round((1-perc1/0.5104)*cresult1,3),caresult2=round(((1-perc2/0.8625)*cresult1),3))

@app.route("/calculate_AC", methods = ["post"])
def calculate_AC():
    Country = str(request.form["Country"])
    Star = str(request.form["Star"])
    timeUsed = float(request.form["timeUsed"])
    power = float(request.form["power"])
    appn = int(request.form["applianceNumber"])
    PF = float(request.form["PF"])
    m = timeUsed*power*appn*PF
    calculated = False
    note = ""
    color = "alert-success"
    if timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "1 ⭐":
        result1 = round(0.218*m,3)
        result2 = round(m*0.571,3)
        cresult1= round(m*0.758, 3)
        calculated = True
        perc1 = 0.1
        perc2 = 0.15 
    elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "2 ⭐":
        result1 = round(0.218*m,3)
        result2 = round(m*0.571,3)
        cresult1= round(m*0.758, 3)
        calculated = True
        perc1 = 0.21
        perc2 = 0.32
    elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "3 ⭐":
        result1 = round(0.218*m,3)
        result2 = round(m*0.571,3)
        cresult1= round(m*0.758, 3)
        calculated = True
        perc1 = 0.331
        perc2 = 0.52 
    elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "4 ⭐":
        result1 = round(0.218*m,3)
        result2 = round(m*0.571,3)
        cresult1= round(m*0.758, 3)
        calculated = True
        perc1 = 0.464
        perc2 = 0.75
    elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and (Star == "5 ⭐" or Star == "None"):
        result1 = round(0.218*m,3)
        result2 = round(m*0.571,3)
        cresult1= round(m*0.758, 3)
        calculated = True
    else:
        note = "One input is illogical. Try again"
        color = "alert-danger"
        return render_template("AC_app.html", note=note)
    return render_template("AC_app.html", Star=Star,result1=result1, result2=result2,cresult1=cresult1, note=note, color=color, calculated=calculated, aresult2=round(((1-perc2/0.8625)*result2),3),aresult1=round(((1-perc1/0.5104))*result1,3), caresult1=round((1-perc1/0.5104)*cresult1,3),caresult2=round(((1-perc2/0.8625)*cresult1),3))

    

if __name__ == "__main__":
    app.run(debug=True)