from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="Welcome to TeeMusic Recording Studio", current_page="home")

@app.route("/about")
def about():
    return render_template("about.html", title="About | TeeMusic Recording Studio", current_page="about")

@app.route("/services")
def services():
    return render_template("services.html", title="Services | TeeMusic Recording Studio", current_page="services")

@app.route("/artists")
def artists():
    return render_template("artists.html", title="Artists | TeeMusic Recording Studio", current_page="artists")

@app.route("/events")
def events():
    return render_template("events.html", title="Upcoming Events | TeeMusic Recording Studio", current_page="events")

@app.route("/bookings", methods=["GET", "POST"])
def bookings():

    error = ""
    return render_template(
	"bookings.html",
	title="Bookings | TeeMusic Recording Studio",
	current_page="bookings",
	error=error
        )


if __name__ == "__main__":
    app.run(debug=True)
