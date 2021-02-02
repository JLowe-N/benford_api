# Benford's Law API

Benford's Law observes that '1' is the most common leading digit (~30% proportion)
in many sets of natural occuring numbers.  This API uses the Tornado framework to
set up routes and handling HTML templates.  On the backend,  it reads a CSV
into memory, transforms the data using the pandas library, and plots it with the 
seaborn library after which it is inserted into the frontend application.

## Installation

### Docker

This project contains a Dockerfile which can be used to build a Docker Image
and run a Container.  In the project top directory (Question1 aka benford_project),
run the following commands:

Build image:
`docker build -t benford-project`

This downloads, and caches all the Container dependencies OS, Python runtime,
Python libraries, source code. It will allow you quickly spin up multiple instances
of the project server.

Start container:
`docker run --name test-benford -p 8881:8881 benford_project`

What's important here is the -p tag. This docker flag allows you to set
the outer and inner ports that allows you to communicate with the container.
The left side of the colon is the port you would like to access with your browser:
http://localhost:8881 - or whatever port is available to use.  The right side
of the colon is the port inside the container which is dependent on the project code.
The port set for the project code is also 8881.

### Local Python Runtime

Alternatively, this application can be installed with a local installation of Python.
This project has been tested in Python 3.8.  The project dependencies are included
in the requirements.txt file and can be installed with the following command:

`pip install -r requirements.txt`

From there, you can run the app.py file in the benford_api directory.

`python ./benford_api/app.py`

Just be sure to have your PYTHONPATH set to the Question1 (benford_project)
folder.  You can accomplish this by creating a .env file.  If you have issues
importing the benford_plot package, this is likely the cause.

## Acknowledgements

Thank you again for this opportunity and for taking the time to review this 
project submission.  I would love the opportunity to discuss it in more detail
with your team, as it presented many interesting challenges.  There are also
quite a few opportunities to improve upon the application, but I tried to balance
the timeliness of this submission with the complexity I could accomplish.