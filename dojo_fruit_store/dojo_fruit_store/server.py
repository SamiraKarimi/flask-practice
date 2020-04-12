from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print('*'*60)
    str=request.form['strawberry']
    ra=request.form['raspberry']
    ap=request.form['apple']
    print(f'the number of fruit: {int(str)+int(ra)+int(ap)}')
    return render_template("checkout.html",fn=request.form['first_name'],
    ln=request.form['last_name'],id=request.form['student_id'],  
    str=request.form['strawberry'],
    ra=request.form['raspberry'],ap=request.form['apple'])


@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    