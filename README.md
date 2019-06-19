# Cat Collector - Little Cat Rescue
Put food out at the dumpster behind the QuickieMart and feed the strays.
Attract them all with various toys and foods.


The front end is a single-page webapp that makes calls to lambdas through APIGateway.

Game logic is executed on the back end by AWS lambda. 

A graphical worldview is generated server-side and stored in S3 as a .png file. The graphic is then displayed to the user by the front end.

To facilitate transfer of data between the front and back ends, state is maintained in a dynamoDB table.

AWS StepFunctions service controls application flow.

AWS StepFunctions service makes calls to lambda functions written in python. 

State within the step function is maintained in a JSON string. The string is passed from lambda to lambda through the StepFunctions service. 


Technologies used: Javascript, React, Lambda, Python, AWS Step Functions, S3, DynamoDB, IAM.
