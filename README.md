* Cat Collector - Little Cat Rescue
Put food out at the dumpster behind the QuickieMart and feed the strays.
Attract them all with various toys and foods.

Technologies:
Implement a state machine at AWS using the StepFunctions service.
The state machine makes calls to lambda functions written in python. 
The state machine will control application flow.

The Lambda functions will execute the game logic.
JSON is pased to to and from each lambda through the state machine to maintain state.

The back end serverless.
Front end is a minimal React web page.
The graphical worldview is generated server-side and stored in S3.

