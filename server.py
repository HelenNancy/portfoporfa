from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/index.html')
def my_home():
	return render_template('index.html')
    
@app.route('/blog')
def blog():
	return 'I love glass bricks'

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_csv(data):
	with open('database.csv', mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
       if request.method == 'POST':
       	try:
       		data = request.form.to_dict()
       		write_to_csv(data)
       		return redirect('/thankyou.html')
       	except:
       		return('did not send to database')	
       else:
       	return 'Something went wrong, please try again'




