#!/bin/bash
vagrant destroy --force
is_updated=`git log -1 --name-only | grep -e provision.sh -e travis_ros_install.bash`
if [ ${#is_updated} -gt 0 ]; then
  vagrant up --provision-with=init
else
  vagrant up --provision-with=test
fi
vagrant halt
