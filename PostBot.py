from mastodon import Mastodon
import yaml
import time
import re
from datetime import datetime, timedelta

class PostBot:
	"""Posts content created by the createContent function, by default every hour"""
	def __init__(self):
		self.config_path = "config.yaml"
	
	def createContent(self):
		#Write your content-creating function here
		
def main():
	bot = PostBot()
	with open(bot.config_path, 'r') as stream:
		try:
			config = yaml.safe_load(stream)
		except yaml.YAMLError as exc:
			input(exc)
			sys.exit()
	next = datetime.utcnow().replace(minute=0, second=0) + timedelta(minutes=config["interval"])
	api = Mastodon(client_id=config["client_key"], client_secret=config["client_secret"], access_token=config["access_token"], api_base_url=config["base_url"])
	while True:
		time.sleep(5)
		now = datetime.utcnow()
		if now > next:
			try:
				status = api.toot(bot.createContent())
				print("posted status", status['url'])
			except Exception as exc:
				print("Error tooting: " + str(exc))
			next = datetime.utcnow().replace(minute=0, second=0) + timedelta(hours=config['interval'])
		config["since_id"] = checkNotifications(api, bot, config["since_id"], config["handle"])
		with open(bot.config_path, 'w') as outfile:
			try:
				yaml.dump(config, outfile)
			except yaml.YAMLError as exc:
				print("Error saving to config: " + exc)
			
def checkNotifications(api, bot, since, handle):
	notifications = []
	try:
		notifications = api.notifications(since_id=since)
	except Exception as e:
		print("Error getting notifications: " + str(e))
		return since
	cleanr = re.compile('<.*?>')
	for notification in notifications:
		if notification['type'] == "mention":
			status_re = re.sub(cleanr, '', notification.status.content)
			if status_re.startswith("@" + handle):
				replytext = "@" + notification.account.acct + " " + bot.createContent()
				try:
					api.status_post(replytext, in_reply_to_id = notification.status.id)
				except Exception as exc:
					print("Error replying: " + str(exc))
		since = notification.id
	return since

if __name__ == '__main__':
	main()