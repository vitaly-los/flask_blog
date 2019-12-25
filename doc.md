python3 -m venv venv        *Create a virtual envoriment in python 3*

For python3.6
 
Step 1) Make a Virtual Environment with Python 3.6 ...

*python3.6 -m venv env --without-pip*

Step 2) Activate your virtual environemnt ...

*source env/bin/activate*

Step 3) Install pip into your environemnt ...

*curl https://bootstrap.pypa.io/get-pip.py | python3*

>for development flask run on <http://127.0.0.1:5000>
>
>>source venv/bin/activate    *Activate virtual envoriment* 

>>python3  index.py           *Run app*
Pylint give error for db.Model. Switch to flake8

Install flask-wtf for working with forms.

Flask-wtf  *Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA.*

Install flask-sqlalchemy for working with database
