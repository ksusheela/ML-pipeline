from flask import Flask
from visa.logger import logging
from visa.exception import customException
import os,sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception(" we are testing our custom exception file")
    except Exception as e:
        visa = customException(e,sys)
        logging.info(visa.error_message)
        logging.info("we are testing loging  module ")
        return " Hello world"
    
    

if __name__ =="__main__":
    app.run(debug=True)
