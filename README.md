# Data Science Tools 1

## Course Description

It is recommended that you consult this github repo often for material related to this course.
Also monitor the 2DU container for messages and shared content. Course assignments will be upload here and are available in the course container, although it's possible that some modifications will be made to assignments, so the safest option is to use the assignments from this repo.  If you're trying to replicate the activities from the asynch, you may occassionally notice that some of the demos are a bit out of date.  For example, the Twitter API has changed and the website used in the scraping demo is now defunct.  I'll push additional notebooks to this repository in order to provide some updated context for those examples.  Additionally, many of the notebooks used in the asynch are available at this [repo](https://github.com/wkossekdu/data_science_tools_1).

The main objective of data science tools 1 is to learn various tools to perform data analysis. The focus in tools 1 is data cleanup, summarization, and visualization. It is more like a hacking skill set but our primary focus will be on the scientific python and Linux ecosystem. We’ll primarily use Jupyter Notebooks for in-class demos and homework. This should make our learning interactive.

For the final project, students will work through individual or team projects applying course-work to the data lifecycle within a particular domain. The focus will also be on best data science/software engineering practices and reproducible work.

Please select a project by the end of week 3 as per your preference. You are allowed to have a group of 2 to 3 students but project work must justify team count. There will be a homework asking about the detail of your final project. We’ll provide feedback about feasibility of the final project.

## Software Requirements

### Python

You'll need a Python 3 distribution.  Any 3.x version should be fine.  I'm currently using 3.8.10. The requirements.txt file in this repository can be used for any virtual environments that you use in this class.

## bash 

We'll use bash for all of our command line work in this class. If you're on a Mac or a Linux machine, then you'll have access to bash, but note that bash is no longer the default shell on Mac OS.  However, you can easily switch to bash.  See [here](https://www.howtogeek.com/444596/how-to-change-the-default-shell-to-bash-in-macos-catalina/) for details.  

To check your current shell from the command line run: **echo $0**
If you're not using bash, then you can switch to bash with the following command: **chsh -s /bin/bash**

If you're on a Windows machine, then you'll need to install Windows Subsystem for Linux (WSL).  This will give you access to bash and will allow you to interact with your Windows file system using linux commands. I recommend using WSL1 as it's a bit more straightforward to access your Windows file system.  This [post](https://medium.com/hugo-ferreiras-blog/using-windows-subsystem-for-linux-for-data-science-9a8e68d7610c) gives a nice overview of the WSL1 setup. **Ignore the part about installing an Anaconda distribution**.

## Editors/IDEs

We'll lean on Jupyter Notebooks in this course, although you'll have need for a code editor from time to time. Feel free to use whatever you want, but if you're using WSL, then I strongly recommend using VS Code.  The [Windows documentation](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode) on setting up VS code to work with WSL is great.  The part of the documentation you want to focus on here is the section titled **Install VS Code and the Remote WSL extension**.  

## Creating a Virtual Environment

We'll go over these steps during our first class, but I encourage your to build a virtual environment using the provided requirements.txt file before class.  Steps for creating a virtual environment in bash are below. 

* Run `apt-get install python3-venv`
* `cd` into the directory where you want to keep your course files.
* Create the virtual environment with `python3 -m venv venv` (The last argument here is the name of the virtual environment. Using venv simplifies things.)
* Activate the virtual environment with `source venv/bin/activate` (This is our default interpreter until we end our session or `deactivate` the environment.)
* Update pip: `pip install --upgrade pip`
* Run: `curl -O https://github.com/bennybenibene/data_science_tools1/blob/master/requirements.txt` (The requirements.txt file will be saved in your working directory.)
* Run: `pip install -r requirements.txt` to install the packages in the requirements file.
* If there are issues installing particular files you can try to install them individually.  For example, `pip install numpy==1.15.4`

## Adding Virtual Environment as an ipykernel

Opening a Jupyter session will utilize the default Python3 ipykernel.  However, you can add your virtual envvironment as a kernel to use in Jupyter.

* Activate the virtual environment you want to add.
* From your virtual environment directory, run `pip install ipykernel`
* Run: `ipython kernel install --user --name=name_of_venv`
* To uninstall a kernel run: `jupyter kernelspec uninstall name_of_venv`
* When you open a Jupyter session you should now be able to select the kernel you've created from your virtual environment.