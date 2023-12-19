[![tests](https://github.com/boutetnico/ansible-role-composer/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-composer/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.composer-blue.svg)](https://galaxy.ansible.com/boutetnico/composer)

ansible-role-composer
=====================

This role installs and configures [Composer](https://getcomposer.org/).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

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
              group: root
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
