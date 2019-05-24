# Cat Collector - Little Cat Rescue
Put food out at the dumpster behind the QuickieMart and feed the strays.
Attract them all with various toys and foods.


A serverless backend handles all game logic. Front end is a minimal web page.

The AWS StepFunctions service controls application flow.

The StepFunctions service makes calls to lambda functions written in python. 

The lambda function execute game logic.

State for the application is maintained within the application in a JSON string. State is also stored in a DynamoDB table to facilitate transfer of data between the front and back ends.

A graphical worldview is generated server-side and stored in S3. This graphic is displayed to the user by the front end.


Technologies used: Javascript, React, Lambda, Python, AWS Step Functions, S3, DynamoDB.
