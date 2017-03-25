#!usr/bin/bash
from cricbuzz import *
from twilio.rest import TwilioRestClient
import notify2
import time

accountSid = "AC6d6587b8dc3af6a7dd4a5cd7adb06277"
authToken = "574b97ea96d4997a4088bcab1ad8dfb8"
twilioClient = TwilioRestClient(accountSid, authToken)
notify2.init("Live Scores")
myTwilioNumber = "+18036757939"
destCellPhone = "+919674825450"
cric = CricbuzzParser()

def handleTestMatch(**match):
  if match['State']:
    s = match['Match']+ "      Test Match at "+match['Venue']+"\n"+match['Status']
  return s

def displayScore():
  try:
   match = cric.getXml()
  except Exception:
   notify2.Notification("Error: ","No Internet").show()
   exit()
  details = cric.handleMatches(match)
  details = filter(None,details)
  message = ''
  count=0
  for i in details:
      if i['Match Format']=='TEST':
         count+=1
         message = message+"\n"+handleTestMatch(**i)
      elif 'Match State' in i:
         if i['Match State'] == 'inprogress' or i['Match State'] == 'rain' or i['Match State'] == 'innings break':
             count+=1
             message = message+"\n\n"+ i['Team']+ "      "+ i['Match Format'] + ' Match at ' + i['Venue']+  "\n" +i['Batting team'] + ' ' + i['Batting Team Runs'] +'/'+i['Batting Team Wickets'] + '  Overs: ' + i['Batting Team Overs'] + "\n" + i['Match Status']
         elif (i['Match State'] == 'complete' or i['Match State'] == 'result' or i['Match State'] == 'Result'):
             message =message+"\n\n"+i['Team']+"          "+ i['Match Format'] + ' Match at ' + i['Venue']+"\n"+i['Match Status']
             count+=1
  if count == 0 :
     message='No Match Available'
  notify2.Notification("Score Update: ",message).show()
  myMessage = twilioClient.messages.create(body = "Score Update:" + message, from_=myTwilioNumber, to=destCellPhone)
  if not message == 'No Match Available':
       time.sleep(30)
  else:
    exit()

if __name__=='__main__':
  while True:
    displayScore()
