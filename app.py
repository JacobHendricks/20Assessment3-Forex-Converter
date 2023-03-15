from flask import Flask, render_template, request, redirect, flash
import requests
from currency import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "Super Secret"
# app.debug = True


converted_amount = {"result": 0,
                    "from": "USD",
                    "to": "EUR",
                    "amt": 0
                    }


@app.route("/")
def main_page():
    """Start page"""

    return render_template("index.html")


@app.route("/result")
def result():
    """Results page, shows converted amount along with from and to currencies"""

    return render_template("convert.html", result=converted_amount["result"], from_curr=converted_amount["from"], to_curr=converted_amount["to"], amount=converted_amount["amt"])


@app.route("/convert", methods=["POST"])
def submit_form():
    """"""

    conv_from = request.form["conv-from"].upper()
    conv_to = request.form["conv-to"].upper()
    amount = request.form["amount"]

    symbols = get_symbols()

    errors = []

    if len(conv_from) != 3 or len(conv_to) != 3:
        errors.append("Currency code should be 3 letters (e.g. USD, EUR)")
    if conv_from not in symbols:
        errors.append(f"Not a valid From Currency: {conv_from}")
    if conv_to not in symbols:
        errors.append(f"Not a valid To Currency: {conv_to}")
    if amount.isnumeric() is False:
        errors.append("Amount should be a number")

    if len(errors) > 0:
        for e in errors:
            flash(e, 'error')
    else:
        converted_amount["result"] = convert(conv_from, conv_to, amount)
        converted_amount["from"] = conv_from
        converted_amount["to"] = conv_to
        converted_amount["amt"] = amount

    return redirect("/result")
