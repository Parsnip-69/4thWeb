from flask import Flask, render_template
app = Flask (__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about-us/')
def aboutus():
    return render_template("AboutUs.html")

@app.route('/about-us/history/')
def history():
    return render_template("History.html")

@app.route('/about-us/badges/')
def badges():
    return render_template("Badges.html")

@app.route('/about-us/documents/')
def documents():
    return render_template("Documents.html")

@app.route('/about-us/trustee/')
def trustee():
    return render_template("Trust.html")

@app.route('/sections/')
def sections():
    return render_template("Sections.html")

@app.route('/sections/squirrels/')
def squirrels():
    return render_template("Squirrels.html")

@app.route('/sections/beavers/')
def beavers():
    return render_template("Beavers.html")

@app.route('/sections/cubs/')
def cubs():
    return render_template("Cubs.html")

@app.route('/sections/scouts/')
def scouts():
    return render_template("Scouts.html")

@app.route('/join-us/')
def joinus():
    return render_template("JoinUs.html")

@app.route('/sitemap/')
def sitemap():
    return render_template("Sitemap.html")

@app.route('/basic-template/')
def test():
    return render_template("base.html")


app.run(debug=True)