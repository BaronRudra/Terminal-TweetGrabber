import twitter
import re
api = twitter.Api()
i = 0
print '\n'
print '*' * 60
print '-'* 15 + 'Tweet Grabber for the Terminal!' + '-' * 15
print '*' * 60
Username = raw_input("Enter the Twitter Username : ")
try: 
	Statuses = api.GetUserTimeline(Username)
	print '\n'
	print 'Tweets found! Printing them..' +'\n'
	for s in Statuses:
		print s.text
		print '\n'
		i = i+1
	print "User had %d visible tweets"%i
except Exception as inst:
	print "Oops, there was a %s"%inst + ' Error!'
