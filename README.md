# Installation

Requirements:

- Python3
- PIP3
- git client

```shell
sudo pip3 install -U git+https://github.com/bonya/bt-aws-dump.git#egg=bt-aws-dump
```

Usage example:

```shell

source MY-AWS-TEST-KEYS  # Load you AWS keys to enviroment
bt-aws-dump create -e TEST -s LevelC -o bt-level-c.xlsx


```