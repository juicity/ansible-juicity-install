# ansible-juicity-install

Juicity Installation with Ansible

## Prerequisites

- Ansible (>= 2.15.2)

## Bootstrap

> **Note**
> Running the `bootstrap` script will install all the dependencies required for the module

```bash
./bootstrap
```

## Usage

Prepare an inventory file, then customize it based on your needs.

```bash
cp example-inventory.yml inventory.yml
```

### Juicity Server Installation

```bash
ansible-playbook install.yml
```

### Juicity Server Configuration

```bash
ansible-playbook config.yml
```

### Juicity Server Upgrade

GitHub Action: https://github.com/juicity/juicity/actions

> **Note**
> ONLY works for GitHub Action builds, not available for stable releases at the moment.

```bash
# install binary from the build_type: {latest pr-build,build,daily-build}
# use default build_type: pr-build
./scripts/update
# or
# ./scripts/update pr-build

# build_type: main-build
./scripts/update build

# build_type: daily-build
./scripts/update daily-build

# build_type: custom
# install binary from a given github action url
./scripts/update <github_action_url>
# e.g
./scripts/update https://github.com/juicity/juicity/actions/runs/5927920609

# build_type: release
./scripts/update release <release_tag>
# e.g
./scripts/update release v0.3.0
```

### Juicity Server Restart

```bash
# restart all remote hosts
./scripts/restart

# exclude particular host(s), separate with comma
./scripts/restart --limit '!host1,!host2'

# include particular host(s), separate with comma
./scripts/restart --limit 'host1,host2'
```
