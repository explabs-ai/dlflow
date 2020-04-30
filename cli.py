import os
import click

from dlflow.configs import *

class COMMAND():
	def __init__(self, main_command, sub_command=None):
		self.main_command = main_command
		self.sub_command = sub_command
		self.config = {
			'main_command_config': {},
			'sub_command_config': {}
		}

	def set_config(self, nest_level, prop, val):
		self.config[nest_level][prop] = val

	def run_actions(self):
		configs[self.config[self.main_command]]['subconfigs'][self.sub_command]['function']()

pass_config = click.make_pass_decorator(COMMAND)

@click.group(chain=True)
def dlflow():
	pass

@dlflow.command()
@click.argument('create_type')
@click.pass_context
def create(ctx, create_type):
	if not create_type:
		print('No Creation Mode Provided!!')
		exit(0)

	ctx.config_obj = COMMAND('create', create_type)




if __name__ == '__main__':
	dlflow()
