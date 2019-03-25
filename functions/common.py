#!/usr/bin/python3

import gitlab,click,os

def defineGitlabHost(url): # Simple checker for host
    if url:
        return url
    else:
        return os.environ.get('PGCLI_URL')


def defineGitlabToken(token): # Simple checker for private token
    if token:
        return token
    else:
        return os.environ.get('PGCLI_TOKEN')


def performConnection(url, token): # Gitlab connection function (url + private token)
    connection_host = defineGitlabHost(url)
    connection_token = defineGitlabToken(token)
    return gitlab.Gitlab(connection_host, private_token=connection_token)


def validateProjectName(project_name):
    if(len(project_name.split('/')) != 2):
        click.echo('[' + click.style('ERROR', fg='red') + '] The project name should be defined as <group>/<project_name>.')
        return False
    else:
        return True
