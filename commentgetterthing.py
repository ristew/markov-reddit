import praw, markov, time


done = set()
m = markov.markov()
r = praw.Reddit('comment getter thing')

#m.addfile('austen-emma.txt')
for i in range(1):
	print i
	cmts = r.get_comments('askreddit')
	for comment in cmts:
		if comment.id not in done:
			done.add(comment.id)
			m.addwords(comment.body)
	#time.sleep(5)
print m.gen(30)
