"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTNESS = [
    'lame', 'crappy', 'sucky', 'boring', 'horrible', 'terrible', 'very-meh',
    'dumb', 'stinky', 'weird not in a good way', 'sad']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page.<br><a href=\"http://localhost:5000/hello\">Hello page</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    page = choice(['diss', 'greet'])

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/about-you">
          What's your name? <input type="text" name="person">
          <div>
          You are:
            <input type="radio" name="compliment" value="smart">Smart
            <input type="radio" name="compliment" value="funny">Funny
            <input type="radio" name="compliment" value="kind">Kind
            <input type="radio" name="compliment" value="pretty">Pretty
          </div>

          <select name="complimentorinsult">
            <option value="compliment" name="cori">Compliment</option>
            <option value="insult" name="cori">Insult</option>
          </select>
          <div>
          You like:
            <input type="checkbox" name="food" value="chocolate">Chocolate
            <input type="checkbox" name="food" value="tacos">Tacos
            <input type="checkbox" name="food" value="melons">Melons
            <input type="checkbox" name="food" value="sushi">Sushi
          <p>Tell us about yourself:</p>
          <div>
            <textarea name="about-me"></textarea>
          </div>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/about-you')
def about_you():
  """Users information based on selections"""
    
  player = request.args.get("person")
  complimentorinsult = request.args.get("cori")
  food = request.args.get("food")
  about = request.args.get("about-me")
  insult = choice(INSULTNESS)



  if complimentorinsult == "compliment":
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}! <br>
        You like foods {food}. A little about you - {about}
      </body>
    </html>
    """.format(player=player, compliment=compliment, food=food, about=about)
  else:
    return """
    <!doctype html>
    <html>
      <head>
        <title>Zinger!</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}! HAH! You like {food}
        This is who you are: {about}
      </body>
    </html>
    """.format(player=player, insult=insult, food=food, about=about)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    food = request.args.get("food")

    about = request.args.get("about-me")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}! <br>
        You like foods {food}. A little about you - {about}
      </body>
    </html>
    """.format(player=player, compliment=compliment, food=food)

@app.route('/diss')
def diss_person():
  """Disses user with an insult by name """
  player = request.args.get("person")

  insult = choice(INSULTNESS)

  about = request.args.get("about-me")

  return """
    <!doctype html>
    <html>
      <head>
        <title>Zinger!</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}! HAH! This is who you are: {about}
      </body>
    </html>
    """.format(player=player, insult=insult, about=about)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
