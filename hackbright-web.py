from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github','jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    github, grade, title = hackbright.get_grade_by_github_title(github, grade, title)
    
    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            grade=grade,
                            title=title)
    return html

@app.route("/add-student-form")
def add_student_form():
    """display form to add student"""

    return render_template("student_add.html")

@app.route("/student-add", methods=["POST"])
def student_add():
    """Add a student."""

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    github = request.form.get("github")

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("submission.html",
                            first_name=first_name,
                            last_name=last_name,
                            github=github)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
