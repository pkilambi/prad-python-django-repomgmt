#!/bin/bash
for pkg in glance swift python-swiftclient python-quantumclient quantum cinder nova horizon keystone python-cinderclient python-novaclient python-keystoneclient python-glanceclient
do
    echo "Processing $pkg"
    mkdir $pkg
    bzr init-repo ~/$pkg
    bzr branch lp:~openstack-ubuntu-testing/$pkg/precise-grizzly $pkg/grizzly
    cd $pkg/grizzly
    bzr add debian
    bzr push lp:~cisco-openstack/$pkg/grizzly
done

