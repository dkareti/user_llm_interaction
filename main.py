# Import libraries
from flask import Flask

app = Flask(__name__)

@app.route('/') #to run this endpoint use `curl url`
def print_info():
    '''
    This function is a test of a system that interacts with the user and an llm.
    '''

    return 'This function is a test of a system that interacts with the user and an llm.\n'

# driver function
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=3001, debug = True)