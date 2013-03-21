#!/bin/bash
cat "./pkgsrc-puppet.txt" | while read pkg;
do
    echo $pkg
    bzr branch lp:~cisco-openstack/puppet-openstack-cisco/folsom-$pkg grizzly-$pkg
    cd grizzly-$pkg
    bzr push lp:~cisco-openstack/puppet-openstack-cisco/grizzly-$pkg
done

