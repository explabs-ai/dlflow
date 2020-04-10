from .edit import *
from .push import *
from .create import *
from .delete import *
from .deploy import *
from .actions import *
from .activate import *
from .deactivate import *

configs = {
	'Edit': edit_config,
	'Push': push_config,
	'Delete': delete_config,
	'Create': create_config,
	'Deploy': deploy_config,
	'Actions' : actions_config,
	'Activate': activate_config,
	'Deactivate': deactivate_config
}