from flask import Flask,render_template,request,redirect,flash

app= Flask(__name__)
app.secret_key= 'Admin321'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    file = request.files['file']
    file.save(f'static/{file.filename}')
    return redirect ('/')                       

@app.route('/greet', methods=['POST', 'GET'])
def greet():
    flash("What's your name")
    return render_template('greet.html')

@app.route('/welcome',methods=["POST", "GET"])
def welcome():
    flash ('hai  ' + str(request.form['uname']) +' to my website')
    return render_template('greet.html')

if __name__ == '__main__':
    app.run(debug=True)

