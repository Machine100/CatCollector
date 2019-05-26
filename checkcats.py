#This function determines which cats will appear in the game world based on the food and toys put out. 

def lambda_handler(event, context):
    
    if (event['food1'] and event['toy1']):
        event['cat1'] = True
    if (event['food1'] and event['toy2']):
        event['cat2'] = True
    if (event['food2'] and event['toy1']):
        event['cat3'] = True
    if (event['food2'] and event['toy2']):
        event['cat4'] = True
    if (event['food2'] and event['toy3']):
        event['cat5'] = True
	
    return event
