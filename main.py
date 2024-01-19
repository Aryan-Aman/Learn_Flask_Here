# Integrating HTML & Flask
# Jinja2 Templating 
'''{% %}->statements,condns,for loops
{{}}->print output
{#...#}->comments
'''
#methods
#request -read the posted values

from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    # if score<=50:
    #     res='FAIL'
    # else:
    #     res='PASS'
    res=""
    if score<=50:
        res='FAIL'
    else:
        res='PASS'
    
    exprssn={'score':score,'res':res}#DICT with key value pair //exprssn discnry passing in result
    return render_template('result.html',result=exprssn) #in result.html {{result//same name}}

@app.route('/fail/<int:score>')  
def fail(score):
    return f"The student has scored below passing marks with a score of {score}"

#check result
@app.route('/results/<int:marks>') 
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result ='success'
    return redirect(url_for(result,score=marks))

#submit result -GET POST methods
@app.route('/submit',methods=['GET','POST'])
def submit():
    total_marks=0
    if request.method=='POST':
        maths=float(request.form['maths']) #convrted to float bcz we'll get by default as string
        science=float(request.form['science'])#name (in html file) -> reqst.form['name']
        python=float(request.form['python'])
        flask=float(request.form['flask'])
        total_marks=(maths+science+python+flask)/4
        res=""
        # if total_marks<=50:
        #     res='fail'
        # else:
        #     res='success'
        return redirect(url_for('success',score=total_marks)) #url_for (res..) changed to 'success' ->just pass through success ,one url able to handle

        


    
    
if __name__ == '__main__':
    app.run(debug=True)
