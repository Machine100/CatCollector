# Cat Collector - Little Cat Rescue
Put food out at the dumpster behind the QuickieMart and feed the strays.
Attract them all with various toys and foods.



A web implementation of the Neko Astume game.

A serverless backend handles all game logic. The front end is a minimal web page.

The AWS StepFunctions service controls application flow.

The StepFunctions service makes calls to lambda functions written in python. 

The lambda functions execute game logic.

State for the application is maintained within the application using a JSON string. The string is passed from lambda to lambda through the StepFunctions service. To facilitate transfer of data between the front and back ends, another state is maintained in a dynamoDB table.

A graphical worldview is generated server-side and stored in S3 as a .png image. The graphic is then displayed to the user by the front end.


Technologies used: Javascript, React, Lambda, Python, AWS Step Functions, S3, DynamoDB, IAM.
