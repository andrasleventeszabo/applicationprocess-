from flask import Flask, request, redirect, render_template
from constants import *

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)