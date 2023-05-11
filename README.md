# CrackMapExec LDAP Modules
Here are some CME LDAP modules I created to help with AD enumeration. 

If you ever wanted to know who the Domain Admins are quickly without building an ldap search string or starting up BloodHound then the 'GROUP-MEM' module is for you. 

Likewise if you ever wanted a list of Computers described as 'Server' or some other decription of your choice then the 'COMP-DESC' module is for you. 

# Installation

Place them in: `~/.cme/modules`

# Usage

To run them is very easy:

**GROUPMEM Module: Returning Domain Admins**

`crackmapexec ldap $DC-IP -u Username -p Password -d $DOMAIN -M GROUP-MEM -o GROUP="domain admins"`

**GROUPMEM Module:  Returning Domain Controllers**

`crackmapexec ldap $DC-IP -u Username -p Password -d $DOMAIN -M GROUP-MEM -o GROUP="domain controllers"`

**COMP-DESC Module: Returning Computers with 'server' in their description**

`crackmapexec ldap $DC-IP -u Username -p Password -d $DOMAIN -M COMP-DESC -o DESC="server"`

# Results

Output of their results are shown below:

**GROUPMEM Module: Returning Domain Computers**

This example shows an example of specifying an incorrect group name 'Computers' and the error handling in place. 
Then a correct computers group named 'Domain Computers' being specified.

<img alt="da" src="/images/COMPUTERS.jpg"/>

**GROUPMEM Module: Returning Domain Controllers and Domain Admins**

<img alt="da" src="/images/DCDA.jpg"/>



**COMP-DESC Module: Returning Servers matching the supplied description**

This example shows a scenario returning a Computer object described with the word 'Server' or '10'. 
If the IP can be retrieved it will also do so.

<img alt="da" src="/images/COMP-DESC.jpg"/>

**COMP-DESC Module: Returning a failed server lookup which illustrates some error handling**

This example shows a scenario of a COmputer object described with the word 'z' being unable to be found. 

<img alt="da" src="/images/COMP-DESC-FAIL.jpg"/>
