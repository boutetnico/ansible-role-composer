import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('path,username,groupname,mode', [
  ('/usr/local/bin/composer', 'root', 'root', 0o755),
])
def test_composer_is_installed(host, path, username, groupname, mode):
    path = host.file(path)
    assert path.exists
    assert path.is_file
    assert path.user == username
    assert path.group == groupname
    assert path.mode == mode


@pytest.mark.parametrize('path,user,group,mode,content', [
  ('/root/.composer/auth.json', 'root', 'root', 0o640, 'github.com'),
])
def test_auth_file_exists(host, path, user, group, mode, content):
    path = host.file(path)
    assert path.exists
    assert path.is_file
    assert path.user == user
    assert path.group == group
    assert path.mode == mode
    assert path.contains(content)
