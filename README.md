The task is to write a simple rest API backend system that is responsible for handling messages between users.

a message contains :

1. sender (owner)
2. Receiver
3. Message
4. Subject
5. creation date

   
The rest API should contains :

- Write message
- Get all messages for a specific user
- Get all unread messages for a specific user
- Read message (return one message)
- Delete message (as owner or as receiver)
  
The output for the project should be:
- an hosted server on one of the free sites (heroku is a good option)
- a postman requests file with examples of how to use the API. Please make the code clean and simple.


Bonus Task:

use authentication method to set up the request for the logged in user. So if you ask for the get messages API you will only get the messages for the current logged in user.
