from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route('/')
def index():
    return 'Welcome to guess game! Go to /guess to play.'

@app.route('/guess', methods=['GET'])
def get_number():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
    return render_template('guess.html', message="Please enter your guess.")

@app.route('/guess', methods=['POST'])
def guess_number():
    if "number" not in session:
        return redirect("get_number")
    number = session["number"]
    try:
        user_guess = int(request.form.get('guess'))
    except ValueError:
        return "Please enter a valid number."
    else:
        msg = check_guess(user_guess, number)
        return render_template('guess.html', message=msg, number=number)

@app.route('/reset', methods=['GET'])
def reset_number():
    session.pop("number", None)
    return redirect('/guess')
def check_guess(guess: int, number: int):
    if guess < 0:
        return "Enter a positive number."
    if guess < number:
        return "Too low! Try again."
    elif guess > number:
        return "Too high! Try again."
    else:
        return "Congratulations! You've guessed the number!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)