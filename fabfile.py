from fabric.api import env, run, cd

USERNAME = 'root'
SERVER = 'helloflask.example.org'
APP_NAME = 'helloflask'
PROJECT_DIR = '/www/%s/%s' % (SERVER, APP_NAME)
WSGI_SCRIPT = 'application.wsgi'

env.hosts = ["%s@%s" % (USERNAME, SERVER)]

def deploy():
    with cd(PROJECT_DIR):
        run('git pull')
        run('source bin/activate; pip install -r requirements.txt')
        run('touch %s' % WSGI_SCRIPT)
