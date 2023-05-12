# CrackMapExec LDAP Modules
Here are some CME LDAP modules I created to help with AD enumeration. 

If you ever wanted to know who the Domain Admins are quickly without building an ldap search string, running ldapdomaindump or starting up BloodHound then the 'GROUP-MEM' module is for you. 

GROUP-MEM helps return all the members of any Active Directory group whether it be a group of users or computers. 

If you ever wanted a list of Computers described as 'Server' or some other decription of your choice then the 'COMP-DESC' module is for you. 

COMP-DESC searches the operating system attribute in all computer objects, for any user supplied text, so we can easily return all computers that are named 'server' for example. 

# Installation

Place them in: `~/.cme/modules`

# Usage

To run them is very easy:

**GROUP-MEM Module: Returning Domain Admins**

`crackmapexec ldap $DC-IP -u Username -p Password -d $DOMAIN -M GROUP-MEM -o GROUP="domain admins"`

**GROUP-MEM Module:  Returning Domain Controllers**

`crackmapexec ldap $DC-IP -u Username -p Password -d $DOMAIN -M GROUP-MEM -o GROUP="domain controllers"`

**COMP-DESC Module: Returning Computers with 'server' in their description**

`crackmapexec ldap $DC-IP -u Username -p Password -d $DOMAIN -M COMP-DESC -o DESC="server"`

# GROUP-MEM Results

Examples of the output from the GROUP-MEM module are shown below:

**Returning Domain Computers**

This example shows an example of specifying an incorrect group name 'Computers' and the error handling in place. 

Then it shows the output of when a correct computers group named 'Domain Computers' is specified. 

Here you can also easily verify if any **RBCD** machine such as the EVILPC shown was successfully added or not during your testing. 

<img alt="da" src="/images/COMPUTERS.jpg"/>

**Returning Domain Controllers and Domain Admins**

<img alt="da" src="/images/DCDA.jpg"/>


# COMP-DESC Results 

Examples of the output from the COMP-DESC module are shown below:

**Returning Servers matching the supplied description**

This example displays 2 scenarios, returning a Computer object described with the word 'Server' and also with the text '10'. 
If the IP can be retrieved it will also do so.

<img alt="da" src="/images/COMP-DESC.jpg"/>

**Returning a failed server lookup which illustrates its error handling**

This example shows a scenario of a Computer object described with the word 'z' being unable to be found. 

<img alt="da" src="/images/COMP-DESC-FAIL.jpg"/>
