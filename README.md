# NIRS_I2BL
Data server for the I2BL Lab, using Django to connect to an android application

## File Structure
The main file has the following sub-directories:

### dataserver:
This is the server, it has all the files and file structure of a typical Django Server, noteable portions include:
```
urls.py: This tells the server what a url means, whether that is linking to an html page in the html (templates) subfolder or a view in views.py
views.py: This is where "views" are located, these are more complicated than simple HTML scripts, for exmaple, inserting data into an HTML table, or creating a datapoint from an HTTP request, this is for more dynamic portions of the display.
serializers.py: This is for data-validation on importing data from an android/http request
models.py: This is where a datamodel is specified, with what goes inside of it.
manage.py: This is where you can use the command line to influence the server, create users, run the server for testing, etc.
```

### Data_Scripts:
This has all the independent python scripts, matlab scripts, and sample data. It contains the following subdirectories:
```
ArduinoCode
ImportingAssets
SampleData
CSRF bashScript.sh
```
#### ArduinoCode: This includes arduino code for sending things to the android app before they are sent to the server. This is largely irrelevant due to the android app being the one that formats the data, but was useful in early testing stages and data comprehension.

#### ImportingAssets: In the beginning of setting up the server I wanted to import data from excel sheets. This contains python scripts for importing from excel, including processing data if that needed to be done aswell.

#### SampleData: This contains sample excel data in order to test matlab algorithms and eventually their python counterparts

#### CSRF bashScript.sh: This was for debugging purposes, trying to learn how to use a CSRF token with Http Requests. It is no longer needed.

