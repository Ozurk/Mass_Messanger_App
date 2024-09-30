This mass messenger app uses a twilio rest api to send sms messages to a list of recipients.

Before starting, store the twilio Account SID and Auth Token as system environment variables with the following names:
  TWILIO_ACCOUNT_SID
  TWILIO_AUTH_TOKEN

To use this program:
  - Create a file called 'SF Employee.csv' in the "data" folder.
    - Within this document, name the first column: "Full Name" and the second "Work Phone". Feel free to add more columns if you want.
    - The text under 'Full Name' will be the text that is visible later on.
    - The Work Phone is the number the twilio API will try to send the message to.
    * Make sure the phone numbers are formatted exactly like this: ########## no spaces or dashes*
- If the app is not working, it is possible that the twilio account needs funded.
- If the app is still not working, try checking to see if your twilio client SID or Auth Token are saved as environment variables.
- Please send me an email if you need any assitance.
