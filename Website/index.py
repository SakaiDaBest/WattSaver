from flask import Flask, render_template, url_for, request
import requests
api_key = '914154ae01eb76e3418f4b86'
countries = {
    "USD": (0.14, 0.454), # United States
    "GBP": (0.20, 0.233), # United Kingdom
    "RUB": (0.06, 0.475), # Russia
    "IDR": (0.15, 0.688), # Indonesia
    "EUR": (0.35, 0.424), # Germany
    "BRL": (0.12, 0.412), # Brazil
    "JPY": (0.20, 0.385), # Japan
    "THB": (0.13, 0.828), # Thailand
    "AUD": (0.21, 0.82), # Australia
    "NZD": (0.19, 0.19), # New Zealand
    "KHR": (0.29, 0.637), # Cambodia
    "MMK": (0.10, 0.835), # Myanmar
    "ARS": (0.05, 0.458), # Argentina
    "BGN": (0.12, 0.422), # Bulgaria
    "HKD": (0.17, 0.523), # Hong Kong
    "SGD": (0.17, 0.511), # Singapore
    "MXN": (0.07, 0.408), # Mexico
    "COP": (0.12, 0.469), # Colombia
}

def currency(Country):
    from_ = "USD"
    to_ = Country
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_}'
    response = requests.get(url)
    data = response.json()
    exchange_ = data['conversion_rates'][f'{to_}']
    return exchange_
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')


#route == link == url

#main route
@app.route("/")
def main():
    return render_template("index.html", home=True)

@app.route('/Facts')
def Facts():
    return render_template('Facts.html')

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
    power = (float(request.form["power"]))/1000
    appn = int(request.form["applianceNumber"])
    m = timeUsed*power*appn*30
    calculated = False

    note = ""
    color = "alert-success"
    if Country == "Malaysia":
        if timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Bulb == "LED":
            result1 = round(0.218*m,3)
            result2 = round(m*0.571,3)
            cresult1= round(m*0.758, 3)
            calculated = True
            note = "Succesfully calculated!"
        elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Bulb == "CFL":
            result1 = round(0.218*m*0.75,3)
            result2 = round(m*0.571*0.75,3)
            cresult1= round(m*0.758*0.75, 3)
            calculated = True
            note = "Succesfully calculated!"
        else:
            note = "One input is illogical. Try again"
            color = "alert-warning"
            calculated = True
            return render_template("Light_Bulbs.html", note=note, calculated=calculated)
    else:
        z = currency(Country)
        if timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Bulb == "LED":
            result1 = round(countries[Country][0]*m*z,3)
            cresult1= round(countries[Country][1]*m*z, 3)
            result2 = 0
            calculated = True
            note = "Succesfully calculated!"
        elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Bulb == "CFL":
            result1 = round(countries[Country][0]*m*z*0.75,3)
            cresult1= round(countries[Country][1]*m*z*0.75, 3)
            result2=0
            calculated = True
            note = "Succesfully calculated!"
        else:
            note = "One input is illogical. Try again"
            color = "alert-warning"
            calculated = True
            return render_template("Light_Bulbs.html", note=note, calculated=calculated)

    return render_template("Light_Bulbs.html", calculated = calculated, cresult1=cresult1,result1=result1,result2=result2, note=note, color=color,Bulb=Bulb,cresult2=round(cresult1*2.33,3),result3=round(result1*2.33,3),result4=round(result2*2.33,3),Country=Country)




@app.route("/calculate_DC", methods=["post"])
def calculate_DC():
    Country = str(request.form["Country"])
    Star = str(request.form["Star"])
    timeUsed = float(request.form["timeUsed"])
    power = (float(request.form["power"]))/1000
    appn = int(request.form["applianceNumber"])
    m = timeUsed * power * appn*30
    calculated = False
    note = ""
    color = "alert-success"
    if Country == "Malaysia":
        if timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0:
            result1 = round(0.218 * m, 3)
            result2 = round(m * 0.571, 3)
            cresult1 = round(m * 0.758, 3)
            calculated = True
            note = "Succesfully calculated!"
            if Star == "1 ⭐":
                perc1 = 0.1
                perc2 = 0.15
            elif Star == "2 ⭐":
                perc1 = 0.21
                perc2 = 0.32
            elif Star == "3 ⭐":
                perc1 = 0.331
                perc2 = 0.52
            elif Star == "4 ⭐":
                perc1 = 0.464
                perc2 = 0.75
            elif Star == "5 ⭐" or Star == "None":
                perc1 = 0
                perc2 = 0
            else:
                note = "One input is illogical. Try again"
                color = "alert-danger"
                calculated = True
                return render_template("DC_app.html", note=note, calculated=calculated)
        else:
            note = "One input is illogical. Try again"
            color = "alert-danger"
            calculated = True
            return render_template("DC_app.html", note=note, calculated=calculated)
    else:
        z = currency(Country)
        if timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0:
            result1 = round(countries[Country][0] * m * z, 3)
            result2 = 0
            cresult1 = round(countries[Country][1] * m * z, 3)
            calculated = True
            note = "Succesfully calculated!"
            if Star == "1 ⭐":
                perc1 = 0.1
                perc2 = 0.15
            elif Star == "2 ⭐":
                perc1 = 0.21
                perc2 = 0.32
            elif Star == "3 ⭐":
                perc1 = 0.331
                perc2 = 0.52
            elif Star == "4 ⭐":
                perc1 = 0.464
                perc2 = 0.75
            elif Star == "5 ⭐" or Star == "None":
                perc1 = 0
                perc2 = 0
            else:
                note = "One input is illogical. Try again"
                color = "alert-danger"
                calculated = True
                return render_template("DC_app.html", note=note, calculated=calculated)
        else:
            note = "One input is illogical. Try again"
            color = "alert-danger"
            calculated = True
            return render_template("DC_app.html", note=note, calculated=calculated)

    aresult1 = round((1 - perc1 / 0.5104) * result1, 3)
    caresult1 = round((1 - perc1 / 0.5104) * cresult1, 3)
    caresult2 = round((1 - perc2 / 0.8625) * cresult1, 3)

    return render_template("DC_app.html", Country=Country, Star=Star, result1=result1, result2=result2, cresult1=cresult1, note=note, color=color, calculated=calculated, aresult2=round((1 - perc2 / 0.8625) * result2, 3), aresult1=aresult1, caresult1=caresult1, caresult2=caresult2)

@app.route("/calculate_AC", methods = ["post"])
def calculate_AC():
    Country = str(request.form["Country"])
    Star = str(request.form["Star"])
    timeUsed = float(request.form["timeUsed"])
    power = (float(request.form["power"]))/1000
    appn = int(request.form["applianceNumber"])
    PF = float(request.form["PF"])
    m = timeUsed*power*appn*PF*30
    calculated = False
    note = ""
    color = "alert-success"
    if Country == "Malaysia":
        if timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "1 ⭐" and PF > 0 and PF < 1:
            result1 = round(0.218*m,3)
            result2 = round(m*0.571,3)
            cresult1= round(m*0.758, 3)
            calculated = True
            perc1 = 0.1
            perc2 = 0.15
            note = "Sucessfully calculated!"
        elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "2 ⭐" and PF > 0 and PF < 1:
            result1 = round(0.218*m,3)
            result2 = round(m*0.571,3)
            cresult1= round(m*0.758, 3)
            calculated = True
            perc1 = 0.21
            perc2 = 0.32
            note = "Sucessfully calculated!"
        elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "3 ⭐" and PF > 0 and PF < 1:
            result1 = round(0.218*m,3)
            result2 = round(m*0.571,3)
            cresult1= round(m*0.758, 3)
            calculated = True
            perc1 = 0.331
            perc2 = 0.52
            note = "Sucessfully calculated!"
        elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "4 ⭐" and PF > 0 and PF < 1:
            result1 = round(0.218*m,3)
            result2 = round(m*0.571,3)
            cresult1= round(m*0.758, 3)
            calculated = True
            perc1 = 0.464
            perc2 = 0.75
            note = "Sucessfully calculated!"
        elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and (Star == "5 ⭐" or Star == "None") and PF > 0 and PF < 1:
            result1 = round(0.218*m,3)
            result2 = round(m*0.571,3)
            cresult1= round(m*0.758, 3)
            perc1=0
            perc2=0
            calculated = True
            note = "Sucessfully calculated!"
        else:
            note = "One input is illogical. Try again"
            color = "alert-danger"
            calculated = True
            return render_template("AC_app.html", note=note, calculated=calculated)
    else:
        z = currency(Country)
        #round(countries[Country][0]*m*z,3)  round(countries[Country][1]*m*z, 3)
        if timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "1 ⭐":
            result1 = round(countries[Country][0]*m*z,3)
            result2 = 0
            cresult1= round(countries[Country][1]*m*z, 3)
            calculated = True
            note = "Sucessfully calculated!"
            perc1 = 0.1
            perc2 = 0.15
        elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "2 ⭐":
            result1 = round(countries[Country][0]*m*z,3)
            result2 = 0
            cresult1= round(countries[Country][1]*m*z, 3)
            calculated = True
            note = "Sucessfully calculated!"
            perc1 = 0.21
            perc2 = 0.32
        elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "3 ⭐":
            result1 = round(countries[Country][0]*m*z,3)
            result2 = 0
            cresult1= round(countries[Country][1]*m*z, 3)
            calculated = True
            note = "Sucessfully calculated!"
            perc1 = 0.331
            perc2 = 0.52
        elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and Star == "4 ⭐":
            result1 = round(countries[Country][0]*m*z,3)
            result2 = 0
            cresult1= round(countries[Country][1]*m*z, 3)
            calculated = True
            note = "Sucessfully calculated!"
            perc1 = 0.464
            perc2 = 0.75
        elif timeUsed > 0 and timeUsed <= 24 and appn >= 0 and power >= 0 and (Star == "5 ⭐" or Star == "None"):
            result1 = round(countries[Country][0]*m*z,3)
            result2 = 0
            cresult1= round(countries[Country][1]*m*z, 3)
            calculated = True
            perc1=0
            perc2=0
            note = "Sucessfully calculated!"
        else:
            note = "One input is illogical. Try again"
            color = "alert-danger"
            calculated = True
            return render_template("AC_app.html", note=note, calculated=calculated)

    return render_template("AC_app.html", Country=Country,Star=Star,result1=result1, result2=result2,cresult1=cresult1, note=note, color=color, calculated=calculated, aresult2=round(((1-perc2/0.8625)*result2),3),aresult1=round(((1-perc1/0.5104))*result1,3), caresult1=round((1-perc1/0.5104)*cresult1,3),caresult2=round(((1-perc2/0.8625)*cresult1),3))



if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
