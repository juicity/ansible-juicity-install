# ansible-juicity-install

Juicity Installation with Ansible

## Prerequisites

- Ansible (>= 2.15.2)

## Bootstrap

> **Note**
> Running the `install` script will install all the dependencies required for the module

```bash
./install
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
# install binary from the build_type: {latest pr-build,main-build,daily-build}
# use default build_type: pr-build
./scripts/update

# build_type: main
./scripts/update build

# build_type: daily-build
./scripts/update daily-build

# install binary from a given github action url
./scripts/update <github_action_url>
# e.g
./scripts/update https://github.com/juicity/juicity/actions/runs/5927920609
```
