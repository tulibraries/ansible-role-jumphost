TULibraries Ansible Role for a Jumphost ssh config file
=========

This role dynamically creates an ssh config file on your Ansible Control machine
that helps deal with host_key checking for deployments to machines that can only
be access via a Jumphost / bastion host.

Usage
-------------

Add a play to the beginning of your playbook with this role and uses 'localhost' as th host

```
- name: Set up an ssh_config for use to make using the jumphost easier
  hosts: localhost
  role:
    - role: tulibraries.ansible_role_jumphost
      jumphost: "{{ groups['lb'][0] }}"
```

Then, configure each inventory hosts file to use that config

```
...
[all:vars]
ansible_ssh_common_args='-F /tmp/ssh_config'


```


Role Variables
--------------

### Required
`jumphost`: The ip/host of the jumphost that your Ansible control machine will
talk use to deploy to otherwise inaccessible machines. This can be a

### optional
`ssh_config_path` -  where the templated ssh_config file gets created". Defaults to `/tmp/ssh_config`
`jumphost_user` -  the user that will be used in from the jumphost. Defaults to `ansible_user`


Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```
- name: Set up an ssh_config for use to make using the jumphost easier
  hosts: localhost
  role:
    - role: tulibraries.ansible_role_jumphost
      jumphost: "{{ groups['lb'][0] }}"
```

License
-------

BSD
