import pytest


@pytest.mark.parametrize(
    "path,username,groupname,mode",
    [
        ("/usr/local/bin/composer", "root", "root", 0o755),
    ],
)
def test_composer_is_installed(host, path, username, groupname, mode):
    composer = host.file(path)
    assert composer.exists
    assert composer.is_file
    assert composer.user == username
    assert composer.group == groupname
    assert composer.mode == mode


def test_composer_command_works(host):
    cmd = host.run("composer --version")
    assert cmd.rc == 0
    assert "Composer version" in cmd.stdout


def test_composer_diagnose_command_works(host):
    cmd = host.run("composer diagnose")
    assert cmd.rc == 0


@pytest.mark.parametrize(
    "path,user,group,mode",
    [
        ("/root/.composer", "root", "root", 0o755),
    ],
)
def test_composer_directory_exists(host, path, user, group, mode):
    directory = host.file(path)
    assert directory.exists
    assert directory.is_directory
    assert directory.user == user
    assert directory.group == group
    assert directory.mode == mode


@pytest.mark.parametrize(
    "path,user,group,mode,content",
    [
        ("/root/.composer/auth.json", "root", "root", 0o640, "github.com"),
    ],
)
def test_auth_file_exists(host, path, user, group, mode, content):
    auth = host.file(path)
    assert auth.exists
    assert auth.is_file
    assert auth.user == user
    assert auth.group == group
    assert auth.mode == mode
    assert auth.contains(content)


def test_auth_file_is_valid_json(host):
    auth = host.file("/root/.composer/auth.json")
    assert auth.contains('"http-basic"')
    assert auth.contains('"github.com"')
