
# Item Catalog

The application Item Catalog allows users to maintain a list of items, and to manage these items in categories.

Author: M. Dören, April 2019

## Prerequisites

The program runs in a virtual machine and requures a couple of prerequisites to be fulfilled:
	- Vagrant needs to be installed on the host machine. The program has been tested and developed with Vagrant 2.2.3.
	- VirtualBox needs to be installed on the host machine. The program has been tested and developed with VirtualBox 6.0.
	- A virtual machine based on the Full Stack Nanodegree VM (FSDN) runnning on the host:
          - Download the VM configuration from https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
          - Unzip the downloaded file and `cd` into the created diredctory `FSND-Virtual-Machine`
          - Change directory into `vagrant`
          - Run `vagrant up` to start the VM
          - Login to the VM using `vagrant ssh` and change the working directory to `/vagrant`

## Installation

- Put all files from this repository into the `vagrant` folder of the VM
- Login to the VM using `vagrant ssh`

## Execution

- If the VM is not running, start it with `vagrant up`
- Login to the VM using `vagrant ssh`
- Change the working directory to /vagrant
- Start the application with `/usr/bin/python project.py`

The program starts a web server that listens on http://localhost:5000
