from dlflow.utils.create import create_user

user_config = {
    'q':[
        {
            'type': 'input',
            'name': 'username',
            'message': 'User Name'
        },{
            'type': 'input',
            'name': 'github',
            'message': 'Github Id Or Email'
        }
    ],
    'function': create_user
}