from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Aman!'
#build url dynamically
#hardcoded-html 

@app.route('/success/<int:score>')
def success(score):
    return f"<html><body><h1>The student has passed with a score of {score}</h1></body></html>"  

@app.route('/fail/<int:score>')  
def fail(score):
    return f"The student has scored below passing marks with a score of {score}"

@app.route('/results/<int:marks>') 
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result ='success'
    return redirect(url_for(result,score=marks))

    
    
if __name__ == '__main__':
    app.run(debug=True)
