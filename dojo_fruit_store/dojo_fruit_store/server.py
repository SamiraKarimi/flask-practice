from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)  
app.secret_key = 'keep it secret, keep it safe'
@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print('*'*60)
    session['fn'] = request.form['first_name']
    session['ln'] = request.form['last_name']
    session['id'] = request.form['student_id']
    session['str'] = request.form['strawberry']
    session['ra'] = request.form['raspberry']
    session['ap'] = request.form['apple']

    str=request.form['strawberry']
    ra=request.form['raspberry']
    ap=request.form['apple']
    print(f'the number of fruit: {int(str)+int(ra)+int(ap)}')
    return redirect('/fruits')
@app.route('/fruits')
def show_result():
    return render_template("checkout.html",fn=session['fn'],
    ln=session['ln'],id=session['id'],  
    str=session['str'],
    ra=session['ra'],ap=session['ap'])

if __name__=="__main__":   
    app.run(debug=True)    