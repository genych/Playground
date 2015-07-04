import logging

logging.basicConfig(level='DEBUG', filename='some.log')
log = logging.getLogger(__name__)

input_text = 'Enter number: '
for i in range(0, 3):
	something = input(input_text)
	log.info('%s %s' %(input_text, something))
	
	try:
		convert = int(something)
	except ValueError:
		log.exception('')


