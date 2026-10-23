
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Docker!"

@app.route('/data')
def data():
    group_number = "Group 2"
    group_members = ["Mahmoud Ahmed", "Talal Afifi"]
    current_date = "October 23, 2026"
    docker_description = "Docker is a platform that packages applications and their dependencies into containers so they can run consistently across different environments."

    return render_template(
        'index.html',
        group_number=group_number,
        group_members=group_members,
        current_date=current_date,
        docker_description=docker_description
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')
