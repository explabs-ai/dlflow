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
            },{
				'type': 'list',
				'name': 'project_type',
				'message': 'Select The Project Type',
				'choices' : ['Classification', 'Regression', 'Generation', 'Detection']
			},{
				'type': 'list',
				'name': 'data_type',
				'message': 'Select The Data Type',
				'choices': ['Image', 'Text', 'Audio', 'Structured']
			},{
				'type': 'input',
				'name': 'dset_dir',
				'message': 'Path To Dataset Directory'
			}
        ],
	'function': create_project
}
