# What is this script for?
- This script is used to auto-generate cpu.txt and nvidia.txt config files for the xmr-stack monero miner. It is compatible with xmr-stak-win64-2.5.2.
- It is designed specifically for a Threadripper 1950x CPU and Nvidia GPU's (tested with 4 1080 ti's).
- If you want to use this with a different CPU or GPU (or more than 4 GPU's), you should be able to edit the setup_cpu and setup_gpu functions.

# How to use this script
- Change the `file_path` variable to the location where your xmr-stak miner is located.
- Using python 3, run the script from the command line with the following parameters: number of cores to mine with, number of GPU's to mine with.
- Examples:
	- `python monero_setup.py 16 4` will enable 16 CPU cores to mine with and 4 GPU's.
	- `python monero_setup.py 12 3` will enable 12 CPU cores and 3 GPU's

### A little background
I created this script because I found myself constantly changing my cpu and gpu config files when I wanted to mine with only some of my computer's resources. I also enjoy writing python code, so this script was fun to write. This script has a very niche use case, but if you enjoy writing python code or want to learn, it can be a fun exercise to modify this script for your own use.
