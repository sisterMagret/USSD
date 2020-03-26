from flask import Flask, request, make_response, render_template
import random
import string


app = Flask(__name__)

@app.route('/')
def index():
    ussdChannel = "*384*8040#" # Your ussd channel from Africa's Talking
    return render_template('index.html', channel=ussdChannel)

@app.route('/ussd', methods=['POST'])
def ussdSession():

    sessionId   = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phoneNumber = request.values.get("phoneNumber", None)
    text        = request.values.get("text", None)

    textArray    = text.split("*") if text else text
    userResponse = textArray[-1] if isinstance(textArray, list) else text

    # Screens
    firstMenu = '''Hi sisterMagret

    1. First thing to do
    2. Second thing to do
    3. Third thing to do
    98. MORE
    '''
    secondMenu = '''Hi sisterMagret

    4. Other thing to do
    5. Even more thing to do
    6. Last thing to do
    0. BACK
    '''
    # More menu screens ...

    error     = "END Invalid input"

    # Session logic
    if userResponse == 0  or userResponse == '':
        menu = firstMenu
    elif userResponse == '98':
        menu = secondMenu
    else:
        menu = error
    #  More logic
    '''

    if userResponse == 1 :
        do something
    if userResponse == 2 :
        do something else
    ...

    '''

    

    resp = make_response(menu, 200)
    resp.headers["Content-type"] = "text/plain"
    return resp

if __name__ == "__main__":
    app.run(debug=True)
