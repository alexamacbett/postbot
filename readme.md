# PostBot

Postbot is a template for simple bots designed to post procedurally generated content to the [fediverse](https://en.wikipedia.org/wiki/Fediverse), (a decentralised social media alternative) via [Mastodon](https://joinmastodon.org/); both on a regular basis and in response to messages directed at the bot's account.

## Installation

You will need [Python 3](https://www.python.org/) Once installed, use pip to install pyyaml, which will allow python to parse the YAML file format the bot's settings are stored in

```bash
pip install pyyaml
```

## Setting up a Mastodon account and application for your bot

In order to post on Mastodon, and therefore to the wider fediverse, your bot will need an account on a Mastodon instance. Choose an instance, preferably a bot-friendly one. I personally recommend Colin Mitchell's [Bots in Space](https://botsin.space), which is a popular instance just for bots where you know you won't run into problems.

Once you have created your account, your bot needs an application interface on that account to make and read posts. This can be done programmatically but if you're setting up a single bot it's simpler and cleaner to access /settings/applications on your bot's instance from the browser and make a new application. The permissions you allow the bot from the application page are ultimately up to you, it is not necessary to change these at all if you know that config.yaml will be securely stored, but at the very least the bot requires permission to write statuses, and to read notifications.

## Setting up config.yaml

Copy the client key, client secret and access token from the application page into config.yaml in their respective places. If you haven't yet run the bot, or are using a fresh copy of config.yaml, the comments in the file will indicate what you should do with each line. In addition to the key, secret and token, you will need the base url of the instance the bot is on (check if the instance is using https or http as this can be important to getting the bot functioning correctly) and the bot's handle (the name it posts as, not its display name) without the leading @. Put these in config.yaml in their appropriate places also. 

Set "interval" to the number of minutes the bot waits in between posts. For your convenience it might help to remember that a day is 1440 minutes and a week is 10080 minutes. Leave "since_id" alone entirely. This is the value the bot uses to keep track of the id of the last notification it received, and is what allows you to turn the bot off and on again without it re-replying to every single person who has ever mentioned it in a post, in order.

## Writing createContent()

Finally, in order for the bot to work, you will need to write your content creation function in createContent(). It is not necessary to keep all content creation functions inside createContent(), as long as what createContent() returns is the final text of the post the bot will make. If your bot is intended to be a humorous regular repetition type bot in the vein of the "The same X every day" fad, you may simply write

```python
	return "(whatever text you want the bot to post every time)"
```

inside createContent(). Otherwise, your function is likely to be a little more complicated. Remember that a result of createContent() whether it be static or procedurally generated, will be the contents of every status the bot posts, either regularly at the interval you have specified, or in response to somebody directly mentioning the bot's account.

Go forth and create bots!

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)