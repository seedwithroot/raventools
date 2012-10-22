raven-tools
===========

Python wrapper for Raven Tools API

https://api.raventools.com/docs/


rt = RavenTools('[your API key here]')

from pprint import pprint

pprint(rt.domains())
pprint(rt.add_domain('blog.samsandberg.com'))
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
