from flask import Flask, render_template, request, redirect, url_for


app=Flask(__name__)

db = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        newTask = request.form["newTask"]
        if len(newTask) > 0 and newTask not in db:
            db.append(newTask)

    return render_template("index.html", tasks=db, name="Minu")


@app.route("/delete/<task>")
def delete(task):
    db.remove(task)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()

