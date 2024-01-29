
# Import necessary modules
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)

# Set up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///research_papers.db'
db = SQLAlchemy(app)

# Define the ResearchPaper model
class ResearchPaper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    authors = db.Column(db.String(255))
    abstract = db.Column(db.Text)

# Define the routes
@app.route('/')
def index():
    papers = ResearchPaper.query.all()
    return render_template('index.html', papers=papers)

@app.route('/summary/<int:id>')
def summary(id):
    paper = ResearchPaper.query.get_or_404(id)
    return render_template('summary.html', paper=paper)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/add-summary/', methods=['GET', 'POST'])
def add_summary():
    if request.method == 'POST':
        title = request.form['title']
        authors = request.form['authors']
        abstract = request.form['abstract']
        new_paper = ResearchPaper(title=title, authors=authors, abstract=abstract)
        db.session.add(new_paper)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add-summary.html')

@app.route('/edit-summary/<int:id>', methods=['GET', 'POST'])
def edit_summary(id):
    paper = ResearchPaper.query.get_or_404(id)
    if request.method == 'POST':
        paper.title = request.form['title']
        paper.authors = request.form['authors']
        paper.abstract = request.form['abstract']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit-summary.html', paper=paper)

@app.route('/delete-summary/<int:id>')
def delete_summary(id):
    paper = ResearchPaper.query.get_or_404(id)
    db.session.delete(paper)
    db.session.commit()
    return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    # Create the database tables if they don't exist
    db.create_all()
    # Run the Flask app
    app.run(debug=True)


This code generates the main Python script (`main.py`) for the Flask application. It includes all the routes and views necessary for the blog, as well as the database model for research papers. The code is well-structured, indented correctly, and uses descriptive variable names.