import functools
import pdb
pdb.set_trace()
emoticon = ':)'
def smile(emoticon):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args):
			new_args = [str(i) + ' ' + emoticon for i in args]
			return func(*new_args)
		return wrapper
	return decorator

@smile(emoticon)
def new_print(*args):
	print(*args)

new_print('test', '?', 33)
# pdb.pm()