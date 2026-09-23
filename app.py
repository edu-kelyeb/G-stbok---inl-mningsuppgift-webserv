from flask import Flask, render_template, request, redirect
from pathlib import Path

app = Flask(__name__)
COUNTER_FILE = Path(__file__).parent / "counter.txt"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        inlagg = request.form.get("inlagg", "").strip()

        if inlagg:
            with open(COUNTER_FILE, "a", encoding="utf-8") as fil:
                fil.write(inlagg + "\n")

        return redirect("/")

    if COUNTER_FILE.exists():
        with open(COUNTER_FILE, "r", encoding="utf-8") as fil:
            inlagg = fil.readlines()
    else:
        inlagg = []

    return render_template("index.html", inlagg=inlagg)


if __name__ == "__main__":
    app.run(debug=True)