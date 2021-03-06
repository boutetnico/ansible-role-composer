[![tests](https://github.com/boutetnico/ansible-role-composer/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-composer/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.composer-blue.svg)](https://galaxy.ansible.com/boutetnico/composer)

ansible-role-composer
=====================

This role installs and configures [Composer](https://getcomposer.org/).

Requirements
------------

Ansible 2.7 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable                 | Required | Default                     | Choices   | Comments                                      |
|--------------------------|----------|-----------------------------|-----------|-----------------------------------------------|
| composer_path            | true     | `/usr/local/bin/composer`   | string    |                                               |
| composer_keep_updated    | true     | `false`                     | bool      |                                               |
| composer_users           | true     |                             | list      | Configuration object. See `defaults/main.yml`.|

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-composer
          composer_users:
            - user: root
              home: /root/.composer
              auth:
                http-basic:
                  github.com:
                    username: alice
                    password: foo

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
