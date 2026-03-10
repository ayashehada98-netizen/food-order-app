from flask import Flask, render_template

app = Flask(__name__)

# الصفحة الأولى
@app.route("/")
def index():
    return render_template("index.html")


# صفحة الفاتورة
@app.route("/receipt")
def receipt():
    return render_template("receipt.html")


if __name__ == "_main_":
    app.run(debug=True)
