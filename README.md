
# Ansible Role:  `monit`


Installs and configure a monit on various linux systems.


[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-monit/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-monit)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-monit)][releases]
[![Ansible Quality Score](https://img.shields.io/ansible/quality/50067?label=role%20quality)][quality]

[ci]: https://github.com/bodsch/ansible-monit/actions
[issues]: https://github.com/bodsch/ansible-monit/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-monit/releases
[quality]: https://galaxy.ansible.com/bodsch/monit

## Requirements & Dependencies

Ansible Collections

- [bodsch.core](https://github.com/bodsch/ansible-collection-core)

```bash
ansible-galaxy collection install bodsch.core
```
or
```bash
ansible-galaxy collection install --requirements-file collections.yml
```

## tested operating systems

* ArchLinux
* Debian based
    - Debian 10 / 11
    - Ubuntu 20.04

> **RedHat-based systems are no longer officially supported! May work, but does not have to.**


## usage

```yaml
monit_daemon:
  cycle: 120
  delay: 240

monit_log_destination: /var/log/monit.log
monit_lib_folder: /var/lib/monit
monit_state_file: "{{ monit_lib_folder }}/state"
monit_id_file: "{{ monit_lib_folder }}/id"

monit_services: []
monit_service_delete_unlisted: true

monit_eventqueue:
  enabled: false
  base_directory: /var/monit
  slots: 100

monit_mail:
  enabled: false
  server_host: localhost
  server_port: 25

monit_alert:
  alert_addresses: []
  mail_format: {}

monit_webinterface:
  enabled: false
  bind: 127.0.0.1
  port: 2812
```

Configurations [examples](https://mmonit.com/wiki/Monit/ConfigurationExamples)


### `monit_services`

```yaml
monit_services:
  - type: 'process'
    name: sshd
    target: '/run/sshd.pid'
    start: '/etc/init.d/sshd start'
    stop: '/etc/init.d/sshd stop'
    restart: '/etc/init.d/sshd restart'
    rules:
      - if failed port 22 protocol ssh then restart
```

### `monit_webinterface`

[upstream documentation](https://mmonit.com/monit/documentation/monit.html#MONIT-HTTPD)

```bash
curl -u foo:bar "localhost:2812/_status?format=json&level=full"
```

## Author and License

- Bodo Schulz

### License

[Apache](LICENSE)

**FREE SOFTWARE, HELL YEAH!**
