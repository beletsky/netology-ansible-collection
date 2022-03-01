Create a text file with given content
=====================================

The role create a text file of given name with given content.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

| Variable name | Default    | Description                           |
|---------------|------------|---------------------------------------|
| path          | "" | Full file name to create on the host  |
| content       | "" | Content of the file                   |


Example Playbook
----------------

    - hosts: servers
      roles:
         - role: create_file
           path: "/tmp/test.txt"
           content: "Test content"

License
-------

MIT

Author Information
------------------

Any suggestions for improvements e-mail to [abeletskiy@ppr.ru](mailto:abeletskiy@ppr.ru).
