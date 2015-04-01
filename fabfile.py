import re
from subprocess import Popen, PIPE
from fabric.api import local

def update():
    local('rm themes/base/jquery-ui.min.css')
    local('rm jquery-ui.min.js')
    local('rm -rf themes/base/images')
    local('bower install jquery-ui')
    local('cp bower_components/jquery-ui/jquery-ui.min.js .')
    local('cp bower_components/jquery-ui/themes/base/jquery-ui.min.css themes/base/')
    local('cp -r bower_components/jquery-ui/themes/base/images themes/base/')
    local('rm -rf bower_components')
    output = Popen(["bower", "info", "jquery-ui"], stdout = PIPE).communicate()[0]
    latest_version = re.findall(r"version: '([1-9]\.\d+\.\d+)',", output)[0]
    print('latest version: {0}'.format(latest_version))
