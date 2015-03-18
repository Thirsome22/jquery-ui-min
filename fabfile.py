import re
from subprocess import Popen, PIPE
from fabric.api import local


def update():
    local('rm jquery-ui.min.css')
    local('rm jquery-ui.min.js')
    output = Popen(["bower", "info", "jquery-ui"], stdout = PIPE).communicate()[0]
    latest_version = re.findall(r"version: '([1-9]\.\d+\.\d+)',", output)[0]
    print('latest version: {0}'.format(latest_version))
    local('wget http://jqueryui.com/resources/download/jquery-ui-{0}.zip'.format(latest_version))
    local('unzip jquery-ui-{0}.zip && rm jquery-ui-{0}.zip'.format(latest_version))
    local('cp jquery-ui-{0}/jquery-ui.min.css .'.format(latest_version))
    local('cp jquery-ui-{0}/jquery-ui.min.js .'.format(latest_version))
    local('rm -rf jquery-ui-{0}'.format(latest_version))
