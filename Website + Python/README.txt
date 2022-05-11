*Please do not move files in this directory* 
**ESSENTIAL: you will need to install Flask and Shodan to be able to local host this project, to do this, follow the steps below.**

To install Flask and Shodan:

1- Open CMD

2- type "pip install shodan"

3- type "pip install Flask"



To start the webpage, run the python file through powershell (shift + rightclick within the host folder to bring up the option "python backend.py", alternatively,
double click python file. This is a local host, so type "localhost" into any browsers taskbar, section within dissertation covers tested and verified browsers, although
this should have no issue with functionality on any browsers.)

To test:

1 - get testable IP's, this can be through Shodan itself although an account will have to be made to use filters, (preferably with University email to gain escalated
privaleges).

2- for the first form:
Go to Shodan.io and type "port:1883" into the Shodan taskbar, this will give you a prescanned port that uses MQTT to test the first form.

3- for the second form:
 Go to Shodan.io and type "port:1883 has_vuln:true" into the taskbar, this will give you any vulnerable IP's within Shodans database, these are not specific and just a general
result group.

https://www.shodan.io/dashboard


4- to test whether its a false positive, use any IP you want, you can create random IP's to test using this website:

https://www.browserling.com/tools/random-ip


While the forms are repeatable, the account level the Author has only has an allowed 100 tokens per month by Shodan's API.
The first form is infinitely repeatable however.

1 token = 1 specified IP search, the author has made sure to not use too many.

The response from Shodan should be visible within the powershell window.