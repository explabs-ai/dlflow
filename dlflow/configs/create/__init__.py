from .git import *
from .user import *
from .file import *
from .project import *

create_config = {
	'q':[{
		'type': 'list',
		'name': 'subcommand',
				'message': 'Select What To Create',
				'choices': ['Project', 'Repository', 'File', 'User'],
	}],
	'subconfigs': {
		'Project': project_config,
		'Repository': git_config,
		'File': file_config,
		'User': user_config
	}
}

