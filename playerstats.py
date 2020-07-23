# This is an api wrapper for chess.com that grabs a players stats from the cli via 'python playerstats.py'.
# It takes 5 or 6 clicks to get to a players statistics on the website, and you must open another tab
# in browser, so this is to simplify and quicken the process if you like to access your opponents stats
# at the time your game challenge is accepted.

import sys
import requests

try:
	print("This is the name of the script: ", sys.argv[0])
	print("Number of arguments: ", len(sys.argv))
	print("The arguments are: " , str(sys.argv))


	# this checks if the user entered the correct syntax to search for a user's statistics
	try: 
		print("chess.com username: ", str(sys.argv[1]))
		response = requests.get('https://api.chess.com/pub/player/' + sys.argv[1] + '/stats')

		if response: # this will evaluate to TRUE is status code is between 200 and 400
			print(response)
		else:
			print('Request returned an error.')

	except IndexError as er:
		print("Correct command line syntax is 'python playerstats.py USERNAME'")
		# print(er.args)

except ValueError as err:
    print(err.args)