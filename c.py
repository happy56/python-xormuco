"""
	How to use this Caching :
	for example you need to cache this function -> duc([agumnet])
	instead of call the function rex = duc([agumnet])
	you change the call into rex = ncache(duc, [agumnet])
	just One change when you call the function. 

	How it is done:
	Simple hash table for each function results for a certain time
	
	What can be done in future:
	1. Get muiltple agrument from the function
	2. Use backend Database not overloading the Ram


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
