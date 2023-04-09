# basic flask HBX website
 
from flask import Flask, render_template
 

# To include html&css include template folder = folder names as written in flask root directory
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
  
@app.route('/')
def index():
    return render_template('index.html')
 
if __name__=='__main__':
    app.run(debug = True)