from dlflow.utils.create import create_repository

git_config = {
    'q':[
        {
            'type': 'list',
            'name': 'existing',
            'message': 'Use An Existing Repository?',
            'choices': ['Yes', 'No']
        },{
            'type': 'input',
            'name': 'repo_name',
            'message': 'Name Of The Repository'
        },{
            'type': 'list',
            'name': 'add_readme',
            'message': 'Add Readme File?',
            'choices': ['Yes', 'No']
        }
    ]
}