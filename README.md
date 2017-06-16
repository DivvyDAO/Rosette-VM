Link to original [README](README)

# Instructions for compiling Rosette using Vagrant (Ubuntu 16.04)

1.Install VirtualBox
2.Install vagrant
3.Install git
4.Run gitbash
5.mkdir git    # make a directory in gitbash (anything after # is comments ignored by bash)
6.cd git    # change directory to the directory you just made
7.git clone https://github.com/KentShikama/Rosette-VM    # get the source code for Rosette 
8.cd Rosette-VM    # change directory to Rosette-VM
9.vagrant init    # sets up vagrant virtual machine in this directory
10.vagrant up    # boot the virtual machine for the first time this may take some time, go get coffee or something
11.vagrant ssh    # give you the ubuntu secure shell bash command line on the virtual machine you just started
12.cd /vagrant    # where you were was in the /git/Rosette-VM directory windows
13.sudo apt update && sudo apt upgrade  # update the virtual machine software
14.sudo apt install g++ g++-multilib    #set user superuser-do allows you to install packages on the machine as an administrator
15.cd Rosette-VM
16.make # runs rosette after building it the first time taking you to the rosette prompt: rosette&gt;

17.(+ 5 5)

Note the make command invokes the rbl.

```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 14.04.5 LTS
Release:	14.04
Codename:	trusty
```
