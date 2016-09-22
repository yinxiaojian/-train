"""Train tickets query via command-line.

Usage:
	tickets.py [-gdtkz] <from> <to> <date>

Options:
	-h,--help	显示帮助菜单
	-g 			高铁
	-d 			动车
	-t 			特快
	-k 			快速
	-z			直达

Example:
	tickets beijing shanghai 2016-08-25
"""
from docopt import docopt
def cli():
	"""command-line interface"""
	arguments = docopt(__doc__, version='Naval Fate 2.0')
	print(arguments)

if __name__ == '__main__':
	cli()