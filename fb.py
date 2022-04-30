import facebook


groups = ['214913493879373']
msg = 'Test Graph facebook post'
link = 'https://google.com/'
token = input("Please enter token = ")
graph = facebook.GraphAPI(access_token=token)

for group in groups:
	x = graph.put_object(group, 'feed', message=msg, link=link)
	print("Post successfully")