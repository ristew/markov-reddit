import praw, markov, time


done = set()
m = markov.markov()
r = praw.Reddit('comment getter thing')

def add_comments(sub):
    for i in range(1):
	    cmts = r.get_comments(sub)
	    for comment in cmts:
		    if comment.id not in done:
			    done.add(comment.id)
			    m.addwords(comment.body)
	    time.sleep(30)
#print m.gen(30)
