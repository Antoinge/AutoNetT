# AutoNetT
# AutoNetT
Final year OU Project.
This software can be used to discover logical topology of an IPv4 computer network. 
This software is meant to be a tool that can aid network engineers in mapping networks they have no 
previous knowledge of.
AutoNetT is split into several functions these are listed below:

1. an IPv4 validator: this function takes a string as input and checks it is in the correct IPv4 format i.e. xxx.xxx.xxx.xxx.
the validator makes use of IPv4 format where there are four octets where each octet is >=0 and <=255. 
raw_input() was deprecated for Python 3 as a result the input must be converted from str to int prior to comparison. 
The code snippet below show the function.
