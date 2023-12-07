from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        with open("contacts.txt", "a+") as file:
            file.write(f"{name}, {email}, {subject}, {message}\n")

    return render_template("index.html")


if __name__=="__main__":
    app.run(port=8080, debug=True)