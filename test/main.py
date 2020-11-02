from flask import Flask, render_template, request
import test
app = Flask(__name__)
@app.route('/', methods =["GET", "POST"])
def hello_world():
    if request.method == "POST":
    	myDict = request.form
    	name1 = myDict['name']
    	email1=myDict['email']
    	dob1=myDict['dob']
    	phone1=myDict['phone']
    	role1=myDict['role']
    	print("{}\n{}\n{}\n{}\n{}".format(name1,email1,dob1,phone1,role1))
    	imfs = test.work(request.form.get('chat'))
    	#return render_template('signup.html')
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)