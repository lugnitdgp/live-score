Live Score Notifier
===================


This is a simple Python script to send Desktop and Text Message notifications on the latest Cricket scores.

----------


Requirements
-------------
**python-pip**

Install pip for Python3.

 - Windows : Pip is installed automatically for Python3.
 - Debian/Ubuntu : `sudo apt-get install python3-pip`
 - Mac : `sudo easy_install pip`

**notify2**

Install notify2 for Python3 using pip.

`pip install notify2`

> Note: If Python3 is not your default, then run `pip3 install notify2`

**Twilio API**

We will be using the Twilio client to send messages on your mobile.

`pip install twilio`

> Note: If Python3 is not your default, then run `pip3 install twilio`


## Deployment ##

- Clone the repository :
 `git clone git@github.com:lugnitdgp/live-score.git`

- Create a trial account on [Twilio](https://twilio.com) and obtain your Account SID and Auth Token, which gives you an international number.

- In the *notifier.py* file, key in the Account details and desired number to receive messages on.

- Run the script :
`python notifier.py`

> Note: If Python3 is not your default, then run `python3 notifier.py`

- Enjoy!
