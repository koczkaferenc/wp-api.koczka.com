from flask import Flask, render_template, render_template_string, redirect, request

app = Flask(__name__)

##########################################################
# Error handler
##########################################################
@app.errorhandler(404)
def page_not_found(error = ""):
    return render_template('hu/404.html'), 404

@app.route('/', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        # POST kérés esetén a beérkező adatokat a form-data-ból kapjuk
        form_data = request.form.to_dict()  # Az összes mező adatainak kigyűjtése
        return render_template_string(display_form_data(form_data))
    
    # GET kérésnél csak egy üzenetet jelenítünk meg
    return "<h2>Küldj egy űrlapot POST metódussal!</h2>"

def display_form_data(form_data):
    # Az űrlap adatait kulturáltan megjelenítő HTML generálása
    html = "<h2>Beérkező űrlap mezők és értékek:</h2><ul>"
    for key, value in form_data.items():
        html += f"<li><strong>{key}:</strong> {value}</li>"
    html += "</ul>"
    return html

############################################################
# A függvény a route-ban megadott statikus oldalt rendereli
############################################################
@app.route('/')
@app.route('/<path:path>.html')
def statpage(path = "index.html"):
    page = 'index.html' if request.path == '/' else request.path
    try:
        return render_template(
            f"{page}"
        )
    except Exception as e:
        return page_not_found()

if __name__ == '__main__':
    app.run(debug=True)
