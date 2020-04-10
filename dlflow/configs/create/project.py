from dlflow.utils.create import create_project

project_config = {
	'q': [
            {
                'type': 'list',
				'name': 'existence',
				'message': 'Create New Project Or Choose Existing?',
				'choices': ['New', 'Existing']
            }, {
				'type': 'input',
				'name': 'project_name',
				'message': 'Project Name'
            }, {
				'type': 'input',
				'name': 'description',
				'message': 'Description Of Your Project',
				'when': lambda x: x['existence'] == 'New'
			}, {
                'type': 'input',
				'name': 'root',
				'message': 'Project Location',
				'default': './'
            }, {
                'type': 'list',
				'name': 'git',
				'message': 'Link Git Repository?',
				'choices': ['Yes', 'No']
            }, {
                'type': 'input',
				'name': 'repo',
				'message': 'Link To Repository',
				'when': lambda x: x['git'] == 'Yes'
            }
        ],
	'function': create_project
}
