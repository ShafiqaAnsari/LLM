from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/home')
def index():
    # return "This is my home page <h1>Hello</hello>"
    return render_template("index.html", content="Hiiii", r=2)

@app.route('/<name>')
def user(name):
    return f"Hello {name}!"

#redirect to another page - use its function name
@app.route('/admin')
def admin():
    # return redirect(url_for('index')
    return redirect(url_for('user', name="admin!"))




if __name__ == "__main__":
    app.run(debug=True)