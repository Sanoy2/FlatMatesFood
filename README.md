# FlatMatesFood
Project description coming soon
# How to run the app
Prerequirements:
* Python 3 installed - application was tested on Python 3.6
* Created gmail account with permission to acccess the account by other applications
* A way to host the application over the Internet so anyone can access it

## First steps:
1. Create virtual environment for the application, for example:

``` virtualenv <name_of_the_environment> ```

2. Activate the virtual environment, for virtualenv:

``` ./<name_of_the_environment>/Scripts/activate ``` for Windows

``` source <name_of_the_environment>/bin/activate ``` For Linux / Mac

3. Install the requirements by pip using requirements.txt file:

``` pip install -r requirements.txt ```

4. Create the config.json file or copy the example_config.json file as config.json file and fill with your data:
* username of the gmail account, ex: john.doe@gmail.com
* password for the gmail account
* list of addresses to send the asking email every day
* address of your application - this address will be attached to asking mails, user by clicking on one of the options in the mail will create a http GET request with chosen option. This address must be publicly available.
 5. (optional) change the time in app.py file to choose the hour of sending asking and summary mails
 
 ## How I host the application:
 I am going to host this application on RaspberryPi computer with Raspbian OS installed. 
 The application is run as normal python application (with virtual environment activated):
 
 ``` python app.py ```
 
Better way is to use:
 
 ``` nohup python app.py & ```
 
Now the application is running on localhost (default port 5000), but nobody has access to it from the outside of my local network.
 
To expose the application to the Internet I use: https://localtunnel.github.io/www/

Localtunnel requires NodeJS to be installed. Information how it work, how to install it and run can be found on the site of the project given above.

When the application is running, there is only one last step to expose the application by localtunnel using a command:

``` lt --port XXXX --subdomain <your_subdomain> ```

The port must be specified, as default it is port 5000.

The subdomain should be specified and should be exactly the same as the host option inside config.json file, but remember that localtunnel will always add ".localtunnel.me" to the given subdomain, so
the host inside config.json file should look like: ` https://<your_subdomain>.localtunnel.me `

When the localtunnel is started it prints the information about full address to open to call the application.
