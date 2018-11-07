#!/usr/bin/python

import sys
import os
import subprocess

passed_args = sys.argv

play = passed_args[1]
args = passed_args[2:]

def git(arguments):
    path = subprocess.check_output("pwd", shell=True)

    action = arguments[0]

    if action == "scp":
        msg = arguments[1]
        branch = arguments[2]

        print("Running git.yaml with msg: {} | and branch: {}".format(msg, branch))

        os.system("ansible-playbook --extra-vars=\"msg={} branch={} repo_path={}\" ~/.playbooks/git.yaml -f 10".format(msg, branch, path))

    elif action == "test":
        print("Yup, this works!")

    elif action == "clone":

        user = arguments[1]
        repo = arguments[2]

        os.system("git clone https://github.com/{}/{}.git".format(user, repo))

    else:
        print("Please enter an action")

plays = {
    'git': git(args),
}


if __name__ == 'main':
    plays[play]    