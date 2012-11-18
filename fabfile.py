from fabric.api import local, hosts
import fabric.contrib.project as project
import os

PROD = 'slackorama@slackorama'
DEST_PATH = '/home/slackorama/sethmason.com/'
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DEPLOY_PATH = os.path.join(ROOT_PATH, '_site')


def clean():
    """
    Clean up the generated files.
    """
    local('rm -rf ./_site')


def generate():
    """
    Generate the site files.
    """
    local('jekyll --pygments')


def regen():
    """
    Clean up the files and then generate them.
    """
    clean()
    generate()


def serve():
    """
    Serve everything locally and start up server to watch for changes.
    """
    local('jekyll --server --auto --pygments')


@hosts(PROD)
def publish():
    """
    Regenerate everything and push to the public website.

    Helpful to run this with the '-u' option since fabric ignores .ssh/config.
    """
    regen()
    project.rsync_project(
        remote_dir=DEST_PATH,
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
        )
