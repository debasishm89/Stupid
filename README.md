Stupid v0.1 - The dumbest file format fuzzer in the whole world
===============================================================

![Alt text](http://1.bp.blogspot.com/-pP0pSl5dTp4/U7fY1275h2I/AAAAAAAAA3Q/pi00kVZCR0I/s1600/1.png)


Stupid was developed in late 2011 to automate fuzzing of different file formats( mainly Music/Video Players etc).

Licence
=======
This software is licenced under a Beerware licence although the following libraries are included with Stupid and are licensed separately.

- pydbg
- paimei - https://github.com/pedramamini/paimei


**"THE BEER-WARE LICENSE" (Revision 42):**

Debasish Mandal <debasishm89 [at] gmail.com> wrote this file. As long as you retain this notice you can do whatever you want with this stuff. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return Debasish Mandal.


Running this Fuzzer
===================
This was developed and tested with **Python 2.7(x86)**. So it's recommended to use the same version of python. Also make sure **pydbg(x86)** also installed on the system. 

You need to provide the target application binary path (.exe) and at least one base file to run this fuzzer. You can to modify the configuration section of "stupid.py" as per your requirement.

Test Case Generation
====================
**mutate()** routine is responsible for generating test cases from given bases files. It has two sub parts

- Bitflip 
- Random Byte Flip

**You may want to change / modify these functions to make this fuzzer more effective. ;)**

Monitoring
==========
To monitor target application for different types of crashes (access violation), Stupid uses **pydbg**(Python debugger). Also it uses **utils** of https://github.com/pedramamini/paimei framework to collect crash information which can be used later to identify interesting app crashes.

Reprducing Crashes
==================

Crash files and crash information can be found in "Crashes" folder which can be used to reproduce app crashes.
