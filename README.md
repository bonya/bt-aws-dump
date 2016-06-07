# Installation

Requirements:

- Python3
- PIP3
- git client

```shell
sudo pip3 install -U git+https://github.com/bonya/bt-aws-dump.git#egg=bt-aws-dump
```

Usage example:

- load you TEST AWS Keys to environment

```shell

source MY-AWS-TEST-KEYS
bt-aws-dump create -e TEST -s LevelC -o bt-level-c.xlsx


```