# fibborestapi
Rest api to get fibbonacci series

Ensure that you have python and pip installed on your system

Then run below command to install virtual environment for python

$ sudo python2 -m pip install virtualenv

$ virtualenv venv

#Then activate the virtual environment

$ . venv/bin/activate

#Then install flask , pytest and coverage

$ pip install Flask pytest coverage

#Then export environment variables 

$ export FLASK_APP=fibboApp

$ export FLASK_ENV=development

#Now run the application

$ flask run

#The application will be available at : http://localhost:5000/fibbonacci/api/v1.0/series/12

#Try other urls to get error messages

#To run the test execute command pytest.




For windows user:-


go to your code base through command prompt<local repository>
  run below command
  
  \Python27\Scripts\virtualenv.exe venv
  then activate the vertual environment 
  run below command
  
  venv\Scripts\activate
  
  Install Flask
  
  pip install Flask
  SET FLASK_APP=fibboApp
  SET FLASK_ENV=development
  flask run
  
  then hit the test URL in your browser
  
  
  
  
  
  
  
