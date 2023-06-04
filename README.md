# CrackMapExec Modules
Here are some CME modules I created to help with AD enumeration and exploitation. 

If you ever wanted to know who the 'Domain Admins' are quickly without building an ldap search string, running ldapdomaindump or starting up BloodHound then the 'GROUP-MEM' module is for you. 

GROUP-MEM helps to return all the members of any Active Directory group whether it be a group of users, groups or computers.

if you ever wanted to easily add, or delete or a computer account then the ADD-COMPUTER module is for you. You can also update an existing computers password. 

ADD-COMPUTER allows you to do all of the above very easily and can also use Kerberos.

If you ever wanted a list of Computers described as 'Server' or some other decription of your choice then the 'COMP-DESC' module is for you. 

COMP-DESC searches the operating system attribute of all computer objects for any user supplied text, so we can easily return all computers that are named 'server' for example. 

# Installation

Place them in: `~/.cme/modules`

# Usage

To run them is very easy:

**GROUP-MEM Module: Returning Domain Admins**

`crackmapexec ldap $DC-IP -u Username -p Password -M GROUP-MEM -o GROUP="domain admins"`

**GROUP-MEM Module:  Returning Domain Controllers**

`crackmapexec ldap $DC-IP -u Username -p Password -M GROUP-MEM -o GROUP="domain controllers"`

**ADD-COMPUTER Module:  Adding a new Computer**

`crackmapexec smb $DC-IP -u Username -p Password -M ADD-COMPUTER -o NAME="BADPC1001" PASSWORD="Password1?"`

**ADD-COMPUTER Module:  Adding a new Computer via Kerberos**

`crackmapexec smb $DC-IP -k -M ADD-COMPUTER -o NAME="BADPC1001" PASSWORD="Password1?"`

**ADD-COMPUTER Module:  Changing a Computer password**

`crackmapexec smb $DC-IP -u Username -p Password -M ADD-COMPUTER -o NAME="BADPC1001" PASSWORD="Password1?" -o NAME="BADPC1001" CHANGEPW=TRUE`

**ADD-COMPUTER Module:  Deleting a Computer**

`crackmapexec smb $DC-IP -u Username -p Password -M ADD-COMPUTER -o NAME="BADPC1001" PASSWORD="Password1?" -o NAME="BADPC1001" DELETE=TRUE`

**COMP-DESC Module: Returning Computers with 'server' in their description**

`crackmapexec ldap $DC-IP -u Username -p Password -M COMP-DESC -o DESC="server"`

**Usage also visible via the command line**

<img src="/images/GROUP-MEM-OPTIONS.jpg" width="600"/>

<img src="/images/ADD-OPTIONS.jpg" width="600"/>

<img src="/images/COMP-DESC-OPTIONS.jpg" width="600"/>


# GROUP-MEM Results

Examples of the output from the GROUP-MEM module are shown below:

**Returning Domain Computers**

This example illustrates specifying an incorrect group name 'Computers' and the subsequent error handling in place to manage this. 

Then it shows the output of when a correct 'Computers' group named 'Domain Computers' is specified. 

Here you can also easily verify if any **RBCD** machines such as the EVILPC shown below was successfully added or not during your testing. 

<img alt="da" src="/images/COMPUTERS.jpg"/>

**Returning Domain Controllers and Domain Admins**

<img alt="da" src="/images/DCDA.jpg"/>

# ADD-COMPUTER Results

Examples of the output from the ADD-COMPUTER module are shown below:

**Adding a Computer with credentials, hashes or using Kerberos**

<img src="/images/ADD-MACHINE.jpg"/>

<img src="/images/ADD-HASH.jpg"/>

<img src="/images/ADD-MACHINE-KERB.jpg"/>

**Changing a Computer password**

<img src="/images/ADD-CHANGEPW.jpg"/>

**Deleting a Computer**

<img src="/images/ADD-DELETE.jpg"/>

**Error handling if a Computer already exists with that name**

<img src="/images/ADD-EXISTS.jpg"/>


# COMP-DESC Results 

Examples of the output from the COMP-DESC module are shown below:

**Returning Servers matching the supplied description**

This example displays 2 scenarios, returning a 'Computer' object described with the word 'server' and also with the text '10'. 
If the IP can be retrieved it will also do so.

<img alt="da" src="/images/COMP-DESC.jpg"/>

**Returning a failed server lookup which illustrates its error handling**

This example shows a scenario of a 'Computer' object described with the word 'z' which is unable to be found. 

<img alt="da" src="/images/COMP-DESC-FAIL.jpg"/>
