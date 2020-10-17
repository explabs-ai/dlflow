import os
import json

class DLFLOW:
    def __init__(self):
        # Load the config object
        script_path = os.path.realpath(__file__)
        script_path = script_path.replace('\\', '/') if '\\' in script_path else script_path

        with open(script_path[:script_path.rindex('/')]+'/settings/.flow', 'r') as f:
            data = f.read()
            self.config = json.loads(data)

    def execute(self, function, params):
        function(params)