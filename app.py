from flask import Flask, render_template
from flask import request,redirect,url_for

app = Flask(__name__)
names = ['ben', 'anna', 'carlo']
@app.route("/")
def home():
    return render_template("index.html", names=names,edit_index=None)

@app.route("/index",methods=["GET", "POST"])
def index():
 
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            names.append(name)
        return redirect(url_for("index"))

    return render_template("index.html", names=names,edit_index=None)

@app.route("/update/<int:index>", methods=["GET","POST"])
def update(index):
    if not 0 <= index < len(names):
        return redirect(url_for("index"))
    if request.method == "POST":
        new_name = request.form.get("name", "").strip()
        if new_name:
            names[index] = new_name
        return redirect(url_for("index"))

    return render_template("index.html", names=names, edit_index=index)

@app.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    if 0 <= index < len(names):
        names.pop(index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=False)