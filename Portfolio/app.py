from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message('New Contact Form Submission', sender='your-email@example.com', recipients=['your-email@example.com'])
    msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'

    mail.send(msg)
    
    # Return the rendered template to stay on the same page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)