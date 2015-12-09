import string
from TwitterAPI import TwitterAPI

SEARCH_TERM = 'Hillary' #here change term

# Enter the four API keys: z
CONSUMER_KEY = '' 
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''
#asscess twitter
api = TwitterAPI(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET);
f = open('/Users/William/Documents/Test.txt','w') #Set .txt path
f.write('No,TID,Text,Time,UID\n');  
search = {'q':SEARCH_TERM,'count':'100'} #change 'until' date to set latest date
#fetch tweets
j = 0;
while j<5000:
	r = api.request('search/tweets', search)
	for item in r:
		str1 = str(j).zfill(6)
		time = item['created_at'];
		time = time[:-11]
		text = item['text']
		text = text.lower();
		for i in '.,:!%$&*\n':
			text = text.replace(i,'')
		str1 = str1 +','+ str(item['id']) +','+ text +','+time+','+str(item['user']['id'])+'\n'
		search['max_id']= item['id']
		try:
			f.write(str1)
		except UnicodeEncodeError:
			continue
		else:
			j+=1
			print 'No:',j	
	print item['id'];
    
