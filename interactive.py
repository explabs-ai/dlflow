'''
	Project Name : DLFlow
	DLFLOW : A simple command line tool for making the Machine Learning Project Pipeline easier
	Developed By : abtexp<abt.exp@gmail.com>
	Organization : explabs<explabs.io>

'''

from colorama import init
from os import listdir
from termcolor import colored
import colorama
from pyfiglet import figlet_format
from PyInquirer import (Token, ValidationError, Validator, print_json, prompt,
                        style_from_dict)

# Local module imports
from dlflow.configs import *

# imports

import os
import re
import sys
import six
import click



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
				'message': 'What Do You Want To Do?',
				'choices': ['Create', 'Delete', 'Deploy', 'Activate', 'Push', 'Exit'],
            }
        ]

	command = prompt(q, style=style)['command']

	if command == 'Exit':
		return False

	main_command = configs[command]

	subcommand = prompt(main_command['q'], style=style)['subcommand']

	inputs = prompt(main_command['subconfigs'][subcommand]['q'], style=style)

	main_command['subconfigs'][subcommand]['function'](inputs)

	return True


@click.command()
def askQs():
	log('DLFlow', color='blue', figlet=True)
	log('Command Line Utility For Easy ML Development To Deployment Pipeline', 'green')

	keep_running = True

	while keep_running:
		keep_running = get_commands()


if __name__ == '__main__':
	askQs()