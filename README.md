# PCAP File Analysis
This is a simple program made for Texas Tech University CS 4392 Project 2 part A. 
The program accepts a PCAP file and parses the TCP connections inside.

# Installation and Execution
To install this program, you can clone or download it from the GitHub repository 
(https://github.com/marshallr7/PCAP_analysis).
To install Scapy, you will need to execute the following command in your environment: `pip install scapy`.
Once installed, open your terminal and navigate to the installation folder. 
Once there, run `Python3 src/main.py`.

# Utilization
To use this program, upload a PCAP file that to the assets' folder. After that,
update the `FILE` variable located in `const.py` to match your file name.
Then run the program. The program will then parse your PCAP file and return 
the total amount of TCP flow connections and the total number of TCP flow
connections from the sender (specified in `const.py`).

# Environment & Libraries
This project depends on Python 3.10 and the Scapy library.

# Issues, Suggestions, and Feedback
The only issue we had on this part of the project is the following warning
messages upon execution<br/>
`WARNING: No IPv4 address found on anpi1 !`<br/>
`WARNING: No IPv4 address found on anpi0 !`<br/>
`WARNING: more No IPv4 address found on en3 !` <br/>We believe these warning messages
only occur on a MacOS environment, but we haven't been able to test other
environments. 
<br/>For a suggestion, it would be nice to have a couple suggestion libraries to work with. 
<br/>For feedback, the project  went well, it was simple to follow and easy to execute.