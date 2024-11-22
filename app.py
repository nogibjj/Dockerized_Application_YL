from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def guess_my_number(input):
    secret = random.randint(1, 10)
    if input == secret:
        answer = "Congratulations, you got it!"
    else:
        answer = "Sorry, you missed it."
    return answer


if __name__ == "__main__":
    app.run(debug=True)
    guess = input("Guess what integer is on my mind between 1 to 10: ")
    output = guess_my_number(guess)
    print(output)
