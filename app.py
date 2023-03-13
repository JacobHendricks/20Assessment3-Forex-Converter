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

    if len(conv_from) != 3 or len(conv_to) != 3:
        flash("Currency code should be 3 letters (e.g. USD, EUR)", 'error')
    elif conv_from not in symbols:
        flash(f"Not a valid From Currency: {conv_from}", 'error')
    elif conv_to not in symbols:
        flash(f"Not a valid To Currency: {conv_to}", 'error')
    elif amount.isnumeric() is False:
        flash("Amount should be a number", 'error')
    else:
        converted_amount["result"] = convert(conv_from, conv_to, amount)
        converted_amount["from"] = conv_from
        converted_amount["to"] = conv_to
        converted_amount["amt"] = amount
    return redirect("/result")
