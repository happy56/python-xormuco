"""
	Simple hash table for each function results for a certain time

"""
import time, math

## CACHE_LIFE_TIME_IN_SEC = 2 # for testing I used 2
CACHE_LIFE_TIME_IN_SEC = 2000

results 	= {}
saved_time 	= {}

def ncache(func, arr):

	id = func.__name__ + str(arr)
	if id in results:
		# time check
		if math.floor(time.time() - saved_time[id]) <= CACHE_LIFE_TIME_IN_SEC :
			#print "this is cached"
			return results[id]

	## else 
	results[id] = func(arr)
	saved_time[id] 	= time.time()
	return results[id]
