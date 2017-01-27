#!/usr/bin/env bash

# TODO: figure out a way to parametrize/normalize the disk id.

mkfs.ext4 -F -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/disk/by-id/google-galaxy-data-2
mkdir -p /mnt/disks/data
mount -o discard,defaults /dev/disk/by-id/google-galaxy-data-2 /mnt/disks/data
chmod a+w /mnt/disks/data
echo UUID=`sudo blkid -s UUID -o value /dev/disk/by-id/google-galaxy-data-2` /mnt/disks/data ext4 discard,defaults,
nobootwait 0 2 | tee -a /etc/fstab
cd /mnt/disks/data
apt-get install gcc python-dev python-setuptools
easy_install -U pip
pip uninstall crcmod
pip install -U crcmod

mkdir /mnt/disks/data/dream
chmod a+w /mnt/disks/data/dream
gsutil -m cp -R gs://public-dream-data/* /mnt/disks/data/dream/ &