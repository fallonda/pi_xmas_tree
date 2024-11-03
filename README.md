# Raspberry Pi ZeroW LED Christmas Tree

Small LED Christmas tree with a 7-segment display counting down the time to Christmas day.

Hardware and OS info: 
```bash
cat /proc/cpuinfo | grep "Model"
Model		: Raspberry Pi Zero W Rev 1.1

hostnamectl | grep "Operating System"
Operating System: Raspbian GNU/Linux 11 (bullseye)
```

__Note:__ In order to get the current date and time, the Pi must be able to connect to a network. 

# Venv setup

```bash
# Creating the venv in repo directory
python3 -m venv .venv

# Activating
source ./.venv/bin/activate

# Install from requirements.txt
pip install -r ./requirements.txt
```

`ZeroSeg` needs to be installed from it's repo shown below. 

# 7-segment display
 
ZeroSeg library from git [here](https://github.com/AverageMaker/ZeroSeg).  
The instructions in the README are excellent. The steps I performed are summarised below: 

* Clone the repo and navigate into it. 
* With `.venv` activated, `sudo python3 setup.py install`. This should install the package within your virtual environment. 

The ZeroSeg [README](https://github.com/AverageMaker/ZeroSeg/blob/master/README.md) has loads of step-by-step detail if you need more info or need to troubleshoot. There are also some example scripts to test your installation. 

Your virtual environment should have everything it needs now to run the display and any scripts in this repo. 


