import pandas as pd
from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression
app = Flask(__name__)