from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
  

app = Flask(__name__)
  
@app.route('/hello')
def helloIndex():
    return 'Hello World from Python Flask!'
if __name__ == '__main__':
  app.debug=True
  app.run()
