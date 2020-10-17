import os
import subprocess
from ..settings import vars
from os.path import isdir, exists
from os import mkdir, chdir, rmdir, removedirs


def create_project(params):
	pth = params['root']
	git_create = params['git']
	existence = params['existence']
	project_name = params['project_name']

	if not exists(pth):
		mkdir(pth)

	if 'repo' in params.keys():
		repo = params['repo']

	if 'description' in params.keys():
		description = params['description']
	else:
		description = project_name

	if isdir('{}/{}'.format(pth, project_name)):
		removedirs('{}/{}/'.format(pth, project_name))

	mkdir('{}/{}'.format(pth, project_name))

	if not exists('{}/{}/Readme.md'.format(pth, project_name)):
		text = description
		with open('{}/{}/Readme.md'.format(pth, project_name), 'w') as f:
			f.write(text)

	chdir('{}/{}/'.format(pth, project_name))

	root_files = vars.CREATE_PROJECT_PROPS['root_files']
	root_dirs = vars.CREATE_PROJECT_PROPS['root_dirs']

	for file in root_files:
		with open(file, 'w') as f:
			pass

	for folder in root_dirs:
		mkdir(folder)

	# Make The Root Project Directory
	mkdir(project_name)

	all_folders = vars.CREATE_PROJECT_PROPS['all_folders']

	for folder in all_folders:
		path = '{}/{}/{}/{}'.format(pth, project_name, project_name, folder)
		if not isdir(path):
			mkdir(path)
			if not exists('{}/Readme.md'.format(path)):
				text = '{} help'.format(folder)
				with open(path+'/Readme.md', 'w') as f:
					f.write(text)

				with open(path+'/__init__.py', 'w') as f:
					f.write('')


def create_user(params):

	return

def create_repository(repo):
	cmd =  'git init . &&\
			git remote add origin {} && \
			git add . &&\
			git commit --m "initial commit" && \
			git push --set-upstream origin master'.format(repo)

	subprocess.call(cmd, shell=True)

def create_file(params):
	return
