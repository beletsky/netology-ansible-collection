#!/usr/bin/python

# Copyright: (c) 2020, Your Name <YourName@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This is my learning module that creates a file on a remote host

version_added: "1.0.0"

description: This module creates the text file with the given content on a remote host.

options:
    path:
        description: Full file name including path on a remote host to create.
        required: true
        type: str
    content:
        description: Content that the created file should have.
        required: false
        type: str
        default: ""

author:
    - Andrey Beletsky (@beletsky)
'''

EXAMPLES = r'''
# Create a file
- name: Create a file
  my_namespace.my_collection.my_own_module:
    path: /tmp
    content: "File content"
'''

RETURN = r'''
# Nothing is returned
'''

from ansible.module_utils.basic import AnsibleModule

import os


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default=''),
    )

    result = dict(
        changed=False,
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    try:
        # Check existence of the file.
        path = module.params['path']
        file_exists = os.path.isfile(path)
        file_content = None
        if file_exists:
            with open(path, 'r') as file:
                file_content = file.read()
        # Decide if the file should be created or changed.
        file_differs = not file_exists or file_content != module.params['content']

    except BaseException as e:
        module.fail_json(msg=str(e), **result)

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        if file_differs:
            result['changed'] = True
        module.exit_json(**result)

    if file_differs:
        try:
            # Create/change the file if necessary.
            with open(path, 'w') as file:
                file.write(module.params['content'])
                result['changed'] = True

        except BaseException as e:
            module.fail_json(msg=str(e), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
