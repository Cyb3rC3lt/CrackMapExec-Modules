# CrackMapExec LDAP Modules
Here are some CME LDAP modules I created to help with AD enumeration. 

If you ever wanted to know who the Domain Admins are quickly without building an ldap search string or starting up BloodHound then the 'GROUPMEM' module is for you. 

Likewise if you ever wanted a list of machines described as 'Server' to focus your attack on, then the 'MACHINE-DESC' module is for you. 

# Installation

Place them in: `~/.cme/modules`

# Usage

To run them is very easy:

**Returns Domain Admins**

`crackmapexec ldap $DC-IP -u Username -p Password -d $DOMAIN -M GROUPMEM -o GROUP="domain admins"`

**Returns Domain Controllers**

`crackmapexec ldap $DC-IP -u Username -p Password -d $DOMAIN -M GROUPMEM -o GROUP="domain controllers"`

**Returns Servers**

`crackmapexec ldap $DC-IP -u Username -p Password -d $DOMAIN -M MACHINE-DESC -o DESC="server"`

# Results

Output of their results are shown below:

**Domain Computers returned**

This example shows an example of specifying an incorrect group name 'Computers' and the error handlinh in place. 
Then a correct computers group being specified.

<img alt="da" src="/images/COMPUTERS.jpg"/>

**Domain Controllers and Domain Admins returned**

<img alt="da" src="/images/DCDA.jpg"/>


**Servers matching the supplied decription returned from the MACHINE-DESC module**

This example shows a scenario returning a Machine object described with the word 'Server' or '10'. 
If the IP can be retrieved it will also do so.

<img alt="da" src="/images/MACHINE-DESC.jpg"/>
