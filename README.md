# ansible-juicity-install

Juicity Installation with Ansible

## Usage

Prepare the ansible inventory file, then customize it based on the comments

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
