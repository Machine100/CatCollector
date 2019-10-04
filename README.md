# Cat Collector - Little Cat Rescue

live at endpoint http://ccccollector.s3-website-us-east-1.amazonaws.com

6/19 Current status: Initial project goals have been achieved and this project is no longer in active development.

This is a graphical game where users place food and toys out at the dumpster behind the QuickieMart to feed the strays.

The front end is a single-page webapp that makes calls to lambdas through APIGateway.

Game logic is executed on the back end by AWS lambda. 

A graphical worldview is generated server-side and stored in S3 as a .png file. The graphic is then displayed to the user by the front end.

To facilitate transfer of data between the front and back ends, state is maintained in a dynamoDB table.

AWS StepFunctions service controls application flow.

AWS StepFunctions service makes calls to lambda functions written in python. 

State within the step function is maintained in a JSON string. The string is passed from lambda to lambda through the StepFunctions service. 


Technologies used: Javascript, React, Lambda, Python, AWS Step Functions, S3, DynamoDB, IAM.

A few issues: MVP needs browser cache to be disabled. Web page needs to be refreshed manually. The deliver button needs to manually depressed. None of this is ideal. These are limitations of the basic web-service architecture - primarily that DynamoDB is not a database that will live-sync to the client. It is a web service running over http and therefore push notifications from the back end are not possible without setting up something complicated similar to websockets.

Currently I am rewriting this app in my FireBox repo. The new app will use firebase's database which live-syncs to the client though a js API using promises. It is an async setup, which is something I wanted to learn about anyway. 
