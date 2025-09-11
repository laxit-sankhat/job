from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rs. 12,00,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$150,000'
    }
    
]

@app.route("/")
def hello_world():  
    return render_template("home.html", jobs=JOBS,company_name="Jovian")

@app.route("/jobs")
def jobs():
    return render_template("jobs.html", jobs=JOBS, company_name="Jovian")

@app.route("/about")
def about():
    return render_template("about.html", company_name="Jovian")

@app.route("/contact")
def contact():
    return render_template("contact.html", company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)