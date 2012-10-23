
import json
import urllib
import urllib2


class RavenToolsException(Exception):
	pass


class RavenTools(object):
	
	BASE_URL = "https://api.raventools.com/api"
	
	def __init__(self, api_key):
		self.api_key = api_key
	
	
	def _make_api_request(self, method, params = None, request_type = 'GET'):
		if not params:
			params = {}
		
		params['key'] = self.api_key
		params['method'] = method
		params['format'] = 'json'
		
		params = urllib.urlencode(params)
		
		if request_type == 'GET':
			url = self.BASE_URL + "?" + params
			req = urllib2.Request(url)
		elif request_type == 'POST':
			url = self.BASE_URL
			req = urllib2.Request(url, params)
		else:
			raise RavenToolsException("Invalid request type passed - GET or POST is required")
		
		response = urllib2.urlopen(req)
		result = response.read()
		
		json_result = json.loads(result)
		return json_result
	
	
	def domains(self):
		'''This request will return the available domains for the profile associated with your API key.
		
		Params:
			None
		Output:
			[list of domain strings]
		'''
		return self._make_api_request('domains')
	
	
	def add_domain(self, domain):
		'''This request will add the domain provided.
		
		Params:
			domain
				The domain name you want to add. "www." prefixes are ignored for purposes of matching ranks, but will be stored as part of the domain name for future requests.
		Output:
			None on success, RavenToolsException on error
		
		'''
		params = {'domain': domain, 'engine_id': '1,2,3'}
		result = self._make_api_request('add_domain', params)
		if result['response'] != 'success':
			raise RavenToolsException("Response from add_domain() was not a success!")
	
	
	def add_links(self, links, domain = None):
		'''This request allows you to pass in a JSON encoded string with link data for the links you would like to create and returns a liew of new Link IDs.
		
		Params:
			domain
				The domain name you want the links to be added under. This value is optional, it can be passed in on the individual link records as well, but must be passed in either here or on each link record.
			
			link
				JSON Encoded string representing the link data you would like to create. Columns available are:
			
				domain - Website Domain within your Raven Profile the link is part of. You can retrieve all of the domains in this profile with the API's 'domains' method
				status - Status of link in Raven. Examples: 'active', 'queued','requested','inactive','declined'
				link type - Type of link in Raven. Examples: 'User Submitted', 'Blog Comment', 'Paid (Permanent)', etc
				link text - Anchor text of the link on the source page
				link url - URL the link on the source page points to
				link description - Description of this link in Raven
				website name - Name for the website this link is associated with
				website url - The URL of the source page the link is found on
				website type - Type of website this link is from
				contact name - Name to use as the contact on this link
				contact email - Email address to use as the contact on this link
				creation date - Creation date to use for link
				owner name - Raven user who owns the link
				tags - Tags to associate this link with in the system, comma delimited
				
				Paid Link Options
				cost - Estimated Cost associated with link
				cost type - Examples: One Time, Daily, Weekly, Monthly, Quarterly, Annually
				payment method - How payment was made
				payment reference - Notes relating to payment (255 character max)
				start date - Start Date for this payment's range
				end date - End Date for this payment's range
		
		Output:
			[list of corresponding link ids]
		'''
		params = {'link': json.dumps(links)}
		if domain:
			params['domain'] = domain
		
		return self._make_api_request('add_links', params)
	
	
	def delete_links(self, link_ids):
		'''This request allows you to pass in a JSON encoded string with link data for the links you would like to update and returns a list of the link ID's and if they were properly updated.
		
		Params:
			link_ids [list of link ids to be deleted]
		
		Output:
			{dict of int:boolean results for deleting the links}
		'''
		links = [{"link id": link_id} for link_id in link_ids]
		params = {'link': json.dumps(links)}
		
		results = self._make_api_request('delete_links', params)
		
		for k, v in results.iteritems():
			results[k] = v and True or False
		
		return results

