# Ansible role WikiJS

![Tests](https://github.com/rgarrigue/ansible-role-wikijs/workflows/Tests/badge.svg)

Setup [WikiJS](https://wiki.js.org/).

This role is tested using [Molecule](https://molecule.readthedocs.io/). Run `tox` to setup environment and start testing.

A [Vagrantfile](https://www.vagrantup.com/) is provided for development purpose.

## Requirements

None.

## Role Variables

See `defaults/main.yml`.

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  roles:
    - ansible-role-wikijs
```

## License

MIT

## Author Information

Rémy Garrigue for Wazo https://wazo.io
