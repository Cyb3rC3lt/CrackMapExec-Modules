**Update:** These 3 modules are now live on the CrackMapExec [repository](https://github.com/mpgn/CrackMapExec/tree/master/cme/modules).

# CrackMapExec Modules
Here are some CME modules I created to help with AD enumeration and exploitation. 

If you ever wanted to know who the 'Domain Admins' are quickly without building an ldap search string, running ldapdomaindump or starting up BloodHound then the 'GROUP-MEM' module is for you. 

GROUP-MEM helps to return all the members of any Active Directory group whether it be a group of users, groups or computers.

If you ever wanted to easily add or delete a computer account then the ADD-COMPUTER module is for you. You can also update an existing computers password.

ADD-COMPUTER allows you to do all of the above very easily and can also use Kerberos. Thanks to the guys at impacket for the original code.

If you ever wanted a list of Computers described as 'Server' or some other decription of your choice then the 'COMP-DESC' module is for you. 

FIND-COMPUTER searches the operating system and name attribute of all computer objects for any user supplied text, so we can easily return all computers that are named 'server' for example. 

# Usage

To run them is very easy:

**GROUP-MEM Module: Returning Domain Admins**

`crackmapexec ldap $DC_IP -u Username -p Password -M GROUP-MEM -o GROUP="domain admins"`

**GROUP-MEM Module:  Returning Domain Controllers**

`crackmapexec ldap $DC_IP -u Username -p Password -M GROUP-MEM -o GROUP="domain controllers"`

**ADD-COMPUTER Module:  Adding a new Computer**

`crackmapexec smb $DC_IP -u Username -p Password -M ADD-COMPUTER -o NAME="BADPC1001" PASSWORD="Password1?"`

**ADD-COMPUTER Module:  Adding a new Computer via Kerberos**

`crackmapexec smb $DC_IP -k -M ADD-COMPUTER -o NAME="BADPC1001" PASSWORD="Password1?"`

**ADD-COMPUTER Module:  Changing a Computer password**

`crackmapexec smb $DC_IP -u Username -p Password -M ADD-COMPUTER -o NAME="BADPC1001" PASSWORD="Password1?" CHANGEPW=TRUE`

**ADD-COMPUTER Module:  Deleting a Computer**

`crackmapexec smb $DC_IP -u Username -p Password -M ADD-COMPUTER -o NAME="BADPC1001" DELETE=TRUE`

**FIND-COMPUTER Module: Returning Computers with 'server' in their description**

`crackmapexec ldap $DC_IP -u Username -p Password -M FIND-COMPUTER -o TEXT="server"`

**Usage also visible via the command line**

<img src="/images/GROUP-MEM-OPTIONS.jpg" width="700"/>

<img src="/images/ADD-OPTIONS.jpg" width="700"/>

<img src="/images/FIND-OPTIONS.jpg" width="700"/>


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


# FIND-COMPUTER Results 

Examples of the output from the FIND-COMPUTER module are shown below:

**Returning Servers matching the supplied description**

This example displays 2 scenarios, returning a 'Computer' object described with the word 'server' and also with the text 'DC'. 
If the IP can be retrieved it will also do so.

<img alt="da" src="/images/FIND-SERVER.jpg"/>

<img alt="da" src="/images/FIND-DC.jpg"/>

**Returning a failed server lookup which illustrates its error handling**

This example shows a scenario of a 'Computer' object described with the letter 'z' which is unable to be found. 

<img alt="da" src="/images/FIND-ERROR.jpg"/>
