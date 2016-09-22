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

import requests
from docopt import docopt
from stations import stations
from prettytable import PrettyTable
from colored import colored

class TrainCollection(object):

	header = 'train station time duration first second softsleep hardsleep hardsit'.split()

	def __init__(self, rows):
		self.rows = rows

	def _get_duration(self, row):
		duration = row.get('lishi').replace(':', 'h') + 'm'
		if duration.startswith('00'):
			return duration[4:]
		if duration.startswith('0'):
			return duration[1:]
		return duration

	@property
	def pretty_print(self):
		pt = PrettyTable()
		pt._set_field_names(self.header)
		for row in self.rows:
			train = [
				#station_train_code
				row['station_train_code'],
				#from and to
				'\n'.join([colored('green',row['from_station_name']), colored('red',row['to_station_name'])]),
				#time
				'\n'.join([colored('green',row['start_time']), colored('red',row['arrive_time'])]),
				#time take
				self._get_duration(row),
				#first-class
				row['zy_num'],
				#second-class
				row['ze_num'],
				#soft sleeper
				row['rw_num'],
				#hand sleeper
				row['yw_num'],
				#hard seat
				row['yz_num']
			]
			pt.add_row(train)
		print(pt)

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
	rows = result.json()['data']['datas']
	trains = TrainCollection(rows)
	trains.pretty_print()


if __name__ == '__main__':
	cli()