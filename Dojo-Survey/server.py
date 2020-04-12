from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result',methods=['post'])
def servey_result():
    print('*'*200)
    print(request.form)
    return render_template("result.html",name=request.form["username"],lo=request.form['location'],la=request.form['language'],com=request.form['com'])

if __name__ =="__main__":
    app.run(debug=True)
