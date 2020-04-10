from colorama import init
from os import listdir
from termcolor import colored
import colorama
from pyfiglet import figlet_format
from PyInquirer import (Token, ValidationError, Validator, print_json, prompt,
                        style_from_dict)
'''
	Project Name : DLFlow
	Developed By : abtexp<abt.exp@gmail.com>
	Organization : explabs<explabs.io>

'''

# Local module imports
from dlflow.settings import vars
from dlflow.utils import *
from dlflow.scripts import *
from dlflow.configs import *

# imports
import click
from argparse import ArgumentParser

import os
import re

import click
import six

import sys

import logging

logging.getLogger('tensorflow').disabled = True
logging.getLogger('keras').disabled = True


'''
DLFLOW : A simple command line tool for making the Machine Learning Project Pipeline easier

'''
# if __name__ == '__main__':
# 	parser = ArgumentParser(
#             prog='dlflow',
#             description='dlflow commandline utility',
#             usage='dlflow __command__ [__subcommand__ [? options]]'
#         )

# 	parser.add_argument_group('commands', 'Specify the main command to run.')
# 	parser.add_argument(
# 		'command', help='Name of the main command to run. Check https://explabs.ai/dlflow/docs/commands for more details')
# 	parser.add_argument_group('subcommands', 'Specify subcommand to run.')
# 	parser.add_argument(
# 		'subcommand', help='Name of the subcommand to run. Check https://explabs.ai/dlflow/docs/subcommands for more details')

# 	args = parser.parse_args()

# 	print(args)

logging.getLogger('tensorflow').disabled = True
logging.getLogger('keras').disabled = True

init()

style = style_from_dict({
	Token.QuestionMark: '#fac731 bold',
	Token.Answer: '#4688f1 bold',
	Token.Instruction: '',  # default
	Token.Separator: '#cc5454',
	Token.Selected: '#0abf5b',  # default
	Token.Pointer: '#673ab7 bold',
	Token.Question: '',
})


def log(string, color, font="slant", figlet=False):
	if colored:
		if not figlet:
			six.print_(colored(string, color))
		else:
			six.print_(colored(figlet_format(
				string, font='slant'), color))
	else:
		six.print_(string)


def get_commands():
	q = [
            {
                'type': 'list',
				'name': 'command',
				'message': 'Select Main Command',
				'choices': ['Create', 'Delete', 'Deploy', 'Activate', 'Push'],
            }
        ]

	# Conditional Additions To The q

	command = prompt(q, style=style)['command']

	main_command = configs[command]

	subcommand = prompt(main_command['q'], style=style)['subcommand']

	inputs = prompt(main_command['subconfigs'][subcommand]['q'], style=style)

	main_command['subconfigs'][subcommand]['function'](inputs)


def parse_answers(answers):
	selection = answers['selection']
	user = answers['user_name']
	mode = answers['mode']

	return


@click.command()
def askQs():
	log('DLFlow', color='blue', figlet=True)
	log('Command Line Utility For Easy ML Development To Deployment Pipeline', 'green')

	commands = get_commands()



	# if recast_mode == 'Puppet':
	# 	print('Not Implemented Yet!!!!')
	# 	return

	# questions = [
	# 	{
	# 		'type': 'list',
	# 		'name': 'selection',
	# 		'message': 'Want To Select From List Or Upload Your Own',
	# 		'choices': ['List', 'Upload'],
	# 	}, {
	# 		'type': 'list',
	# 		'name': 'file_select',
	# 		'message': 'Choose One Of The Following Available Files',
	# 		'choices': get_available_files(recast_mode),
	# 		'when': lambda x: x['selection'] == 'List',
	# 		'filter':lambda x: 'D:/recast/data/video/target/'+x
	# 	}, {
	# 		'type': 'input',
	# 		'name': 'file_pick',
	# 		'message': 'Enter Path To Your File',
	# 		'when': lambda x: x['selection'] == 'Upload'
	# 	}, {
	# 		'type': 'input',
	# 		'name': 'user_name',
	# 		'message': 'Please Enter Your User Name'
	# 	}
	# ]

	# answers = prompt(questions, style=style)
	# answers['mode'] = recast_mode

	# params, rid, final_aud = parse_answers(answers)

	# src_aud = ''
	# src_vid = ''


if __name__ == '__main__':
	askQs()