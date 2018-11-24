#!/bin/bash
cd ./Didi-Training-Release-1/trackletspy/
chmod u+x ./*.sh
sudo ./build.sh

sudo ./run-bag_to_kitti.sh -i $(cd .. ; pwd ; cd ./trackletspy/) -o $(cd .. ; pwd ; cd ./trackletspy/)/TRACKLETS/


