Stupid v0.1 - The dumbest file format fuzzer in the whole world
===============================================================

Stupid was developed in late 2011 to automate fuzzing of different file formats( mainly Music/Video Players etc).

License
=======
This software is licenced under **BEER WARE** licence although the following libraries are included with Stupid and are licensed separately.

- pydbg
- paimei - https://github.com/pedramamini/paimei


**"THE BEER-WARE LICENSE" (Revision 42):**


![Alt text](http://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/BeerWare_Logo.svg/170px-BeerWare_Logo.svg.png)


**Debasish Mandal** <debasishm89 [at] gmail.com> wrote this file. As long as you retain this notice you can do whatever you want with this stuff. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return.


Running this Fuzzer
===================
Stupid was developed and tested with **Python 2.7(x86)**. So it's recommended to use the same version of python. Also make sure **pydbg(x86)** installed on the system. 

![Alt text](http://1.bp.blogspot.com/-pP0pSl5dTp4/U7fY1275h2I/AAAAAAAAA3Q/pi00kVZCR0I/s1600/1.png)


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

**Sample Crash Synopsis File**

![Alt text](http://1.bp.blogspot.com/-gytAL33g-aI/U7gYR5unVVI/AAAAAAAAA3g/4cem3roDNnI/s1600/1.png)

Bug Fixes/Thanks/Hate Emails
============================
Send them to debasishm89 [at] gmail.com


Cheers
======

Happy Fuzzing

Debasish Mandal 
(*http://www.debasish.in*)

