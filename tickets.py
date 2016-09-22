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
from stations import stations
def cli():
	"""command-line interface"""
	arguments = docopt(__doc__, version='Naval Fate 2.0')
	from_station = stations.get(arguments['<from>'])
	to_station = stations.get(arguments['<to>'])
	date = arguments['<date>']

	#build URL
	url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(
		date, from_station, to_station
	)
	result = requests.get(url, verify = False)
	row = r.json()['data']['datas']
if __name__ == '__main__':
	cli()