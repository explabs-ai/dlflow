def activate(project):
    dlflow.config.active_project = project
    project.config.active = True