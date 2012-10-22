
from pprint import pprint

from raventools import RavenTools


rt = RavenTools('[your API key here]')

pprint(rt.domains())

rt.add_domain('blog.samsandberg.com')

pprint(rt.domains())

pprint(rt.add_links([{
					'domain': 'blog.samsandberg.com',
					'status': 'active',
					'link text': 'Dr. Dog - Wild Race EP',
					'link url': 'http://www.spin.com/articles/dr-dog-wild-race-ep-stream',
					'website url': 'http://blog.samsandberg.com/2012/10/02/tuesdays-and-coughing/',
					'creation date': '2012-10-02',
					'tags': 'Zemanta',
					}]))
