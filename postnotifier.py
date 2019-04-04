import praw
import sys

try:
	reddit = praw.Reddit('postnotifierbot', user_agent='postnotifierbot by /u/darkstarohio')
except:
	sys.exit("Login to Reddit Failed, check praw.ini file")

# Add additional Subs Here
subs = ['delusionalartists','donthelpjustfilm']
# Set upvote threshold here
score_threshold = 1000
# Set user to message here
userToMessage = 'darkstarohio'
postCount = 0

msgBody = "Here are the new popular posts:\n\n---\n\n"

for sub in subs:
	subreddit = reddit.subreddit(sub)
	for submission in subreddit.new(limit=100):
		if submission.score >= score_threshold and not submission.saved:
			msgBody += "**[{}](https://reddit.com/{})**\n\nCurrent score: {}\n\n---\n\n".format(submission.title, submission.id, submission.score)
			submission.save()
			postCount += 1

if postCount < 1:
	sys.exit("No new posts to notify")

msgTitle = "Post Notification Bot: {} new posts".format(postCount)
reddit.redditor(userToMessage).message(msgTitle,msgBody)