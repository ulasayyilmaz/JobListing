from flask import Flask, render_template, jsonify, request
from database import load_jobs_fromDB, load_job_from_DB
#from dotenv import load_dotenv

'''JOBS = [
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
    }]'''

#def configure():
#    load_dotenv()

app = Flask(__name__)
@app.route("/")
def helloWorld():
    jobs = load_jobs_fromDB()
    return render_template('home.html', jobs = jobs, companyname = 'Ulas')

@app.route("/api/jobs")
def list_jobs():
    jobs= load_jobs_fromDB
    return jsonify(jobs)

@app.route("/job/<id>")
def look_job():
    job = load_job_from_DB()
    if not job:
        return "Page Not Found", 404
    return render_template('jobpage.html', job = job)

@app.route("job/<id>/apply", methods=['post'])
def apply_to_job(id): #to get the information people filled on html, import request from flask
    data = request.form # args when no method as post, form when wtih post if i don't want data encoded in url
    #return jsonify(data)
    return render_template('application_submitted.html', application = data)

if __name__ == '__main__':
    #configure()
    app.run(host='0.0.0.0', debug = True)