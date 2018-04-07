from flask import Flask, render_template
import os
import requests

app = Flask(__name__)

api_url = 'http://borough-data.herokuapp.com'
