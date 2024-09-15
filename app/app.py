from flask import Flask, render_template, render_template_string, redirect, request

app = Flask(__name__)

##########################################################
# Error handler
##########################################################
@app.errorhandler(404)
def page_not_found(error = ""):
    return render_template('hu/404.html'), 404

@app.route('/processform', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        return render_template(
            "processform.html",
            method=request.method,
            data=data
        )
    
    if request.method == 'GET':
        data = request.args.to_dict()
        return render_template(
            "processform.html",
            method=request.method,
            data=data
        )
        
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

if __name__ == '__main__':             # A webszerver indítása
    app.run(
        host="0.0.0.0",
        port="5000", 
        debug=True
    )