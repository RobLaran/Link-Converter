from flask import Flask, render_template, url_for, request, redirect
import requests
import re

app = Flask(__name__, template_folder='template')

@app.route('/', methods=['POST', 'GET'])
def home():
    converted = ""
    if request.method == 'POST':
        data = request.form.get('mobile')
        
        lines = data.split('\n')

        for line in lines:
            converted += f"{getDesktopUrl(line)}\n"
        
        return redirect(url_for('result', data=converted))
    
    return render_template('home.html')

@app.route('/result')
def result():
    converted = request.args.get('data')
    return render_template('home.html', data=converted)

def getDesktopUrl(mobileURL):
    try:
        response = requests.get(mobileURL, allow_redirects=True)
        desktopURL = response.url
    except:
        print(f"error reading link: '{mobileURL}' \n")
        return f"{mobileURL}"    
    
    return re.split("\\?_.=", desktopURL)[0]  

if __name__ == '__main__':
    app.run(debug=True)