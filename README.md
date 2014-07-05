Stupid v0.1 - The dumbest file format fuzzer in the whole world
===============================================================
Stupid was developed in late 2011 to fuzz different file formats( mainly Music/Video Players etc) and It's released under BEER WARE licence.

Licence
=======
This software is licenced under a Beerware licence. 
THE BEER-WARE LICENSE" (Revision 42):
<debasishm89 [at] gmail.com> wrote this file. As long as you retain this notice you can do whatever you want with this stuff. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return Debasish Mandal.

Running this Fuzzer
===================
This was developed and tested with Python 2.7(x86). So it's recommended to use the same version of python. Also make sure pydbg(x86) also installed on the system. 

You need to provide the target application binary path (.exe) and at least one base file to run this fuzzer. You can to modify the configuration section of "stupid.py" as per your requirement.

Test Case Generation
====================
mutate() function is actually responsible for generating testcases from given bases files. It has two sub parts
1. Bitflip 
2. Random Byte Flip

You may want to change / modify these functions to make this fuzzer more effective. ;)

Monitoring
==========
To monitor target application for different types of crahses (access violation), Stupid uses pydbg(Python debugger). Also it uses utils of https://github.com/pedramamini/paimei framework to collect crash information which can be used later to identify interesting app crashes.

Reprducing Crases
==================

Crash files and crash information can be found in "Crashes" folder which can be used to reproduce app crashes.