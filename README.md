# Imperial College London EIE Final Year Project - Pirasite

This project is a KVM-over-IP switch for the Raspberry Pi. 

To install the device, download the ROM from here:

To install flash the SD card with the ROM, run the following command in Terminal:
  `sudo dd bs=4M if=/home/username/Pirasite.img of=/dev/name_of_sd_card`

The name of the SD card can be found by running the following command in Terminal:
`sudo fdisk -l` and finding the corresponding path name to the SD card.

