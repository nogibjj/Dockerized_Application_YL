from flask import Flask, request
import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def guess_my_number():
    secret = random.randint(1, 10)

    # If a POST request is received with user input
    if request.method == "POST":
        try:
            user_guess = int(request.form.get("guess"))
            if user_guess == secret:
                return "Congratulations, you got it!"
            else:
                return f"Sorry, you missed it. The correct number was {secret}."
        except ValueError:
            return "Please provide a valid integer between 1 and 10."

    # For GET requests, display the guessing form
    return """
        <form method="POST">
            <label for="guess">Guess what integer is on my mind between 1 to 10:</label><br>
            <input type="text" name="guess" id="guess"><br>
            <button type="submit">Submit</button>
        </form>
    """


if __name__ == "__main__":
    app.run(debug=True)
