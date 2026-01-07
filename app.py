from flask import Flask
from flask import request
from flask import jsonify
from flask import flash
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET!!!123'

team = [{"name":"Hasan", "role":"CEO"}, {"name":"Yehya","role":"Janitor"}, {"name":"John","role":"Frontend Developer"}]

def validate(form_data):
    errors = []
    if not form_data['name']:
        errors.append("Name is required")
    if '@' not in form_data['email']:
        errors.append("Invalid email")
    if len(form_data['password']) < 8:
        errors.append("Password must be at least 8 characters")
    if form_data['password'] != form_data['confirm_password']:
        errors.append("Passwords do not match")
    if form_data['bio'] and len(form_data['bio']) < 20:
        errors.append("Bio must be at least 20 characters long")
    if form_data['agreement'] != 'agree':
        errors.append("You must agree to the terms")
    return errors

@app.route('/', methods=["GET", "POST"])
def home_page():
    
    if request.method == "POST":
        data = {
            "name": request.form.get("name", "").strip(),
            "email": request.form.get("email", "").strip(),
            "password": request.form.get("password", "").strip(),
            "confirm_password": request.form.get("confirm_password", "").strip(),
            "bio": request.form.get("bio", "").strip(),
            "agreement": request.form.get("agreement")
        }
        error = validate(data)
        if error:
            return render_template('index.html', error = error, form_data=data)

        flash("Registration successful!", "success") 
        render_template('index.html', success = True)
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run