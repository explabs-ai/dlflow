from dlflow.dlflow import DLFLOW
from dlflow.utils.activate import activate

temp_dlflow = DLFLOW()

activate_config = {
    'q': [
        {
            'type': 'list',
            'name': 'project_name',
            'message': 'Select The Project To Activate',
            'choices': temp_dlflow.config.all_projects
        }
    ],

    'function': activate
}