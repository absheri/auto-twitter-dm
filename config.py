import os

# configure the dm text
def generate_dm_text(name):
	return '''Hey {}, It great to connect
			with you on twitter'''.format(name)

scheduler_time = 15 #in minutes

tw_username = os.environ['TW_ACCOUNT']
