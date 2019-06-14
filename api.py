import requests as r

class FacebookApi():
	base_url = "https://graph.facebook.com/"
	user_token = None

	def set_user_token(self, user_token):
		self.user_token=user_token

	def get_user_info(self):
		return r.get(
			self.base_url+"me?fields=id,name,accounts&access_token={}".format(self.user_token))

	def post_page_post(self, page_token, message):
		return r.post(
			self.base_url+"feed?access_token={}".format(page_token), json={'message':message})