from flask import Flask, render_template, jsonify

JOBS = [
    {
        'id': "Accountant", 
        'salary': "$100,000",
        'location': "New York"
    },
    {
        'id': "Software Developer", 
        'salary': "$160,000",
        'location': "San Francisco"
    },
    {
        'id': "Product Manager", 
        'salary': "$120,000",
        'location': "Mountain View"
    }]


app = Flask(__name__)
@app.route("/")
def helloWorld():
    return render_template('home.html', jobs = JOBS, companyname = 'Ulas')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)