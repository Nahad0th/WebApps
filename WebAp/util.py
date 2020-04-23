import json
import random

def parse_activities(query_result):
	result_list = []
	for element in query_result:
		result_list.append({'activity_name': element.name, 'description': element.desc, 'image': element.img})
	
	return json.dumps({'activities':result_list})

def rand_act(query_result):
	
	result_list = []
	for element in query_result:
		result_list.append({'activity_name': element.name, 'description': element.desc, 'image': element.img})
	element = random.choice(result_list)
	return json.dumps(element)