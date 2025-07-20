from flask import Flask, render_template, request, redirect, url_for
from contact_book import ContactBook

app = Flask(__name__)
contact_book = ContactBook()

@app.route("/")
def index():
    return render_template("index.html", contacts=contact_book.contacts if contact_book.contacts else None)

@app.route("/add", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        contact_book.add_contact(name, phone)
        return redirect(url_for("index"))
    return render_template("add_contact.html")

@app.route("/delete/<name>")
def delete_contact(name):
    contact_book.delete_contact(name)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
