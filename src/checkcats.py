event = {"food1": True, 
         "food2": True, 
         "toy1": True,
         "toy2": True,
         "toy3": False,
         "cat1": True,
         "cat2": False,
         "cat3": True,
         "cat4": False,
         "cat5": True}

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
	

