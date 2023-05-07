# CrackMapExec LDAP Modules
Here are some CME LDAP modules I created to help with AD enumeration. 

If you ever wanted to know who the Domain Admins are quickly without building an ldap search string or starting up Bloodhound then the 'DA' module is for you. 

Likewise if you ever wanted a list of the domain controllers and machines described as 'Servers' to focus your attack on then then the 'DC' and 'Servers' modules are for you. 

# Installation

Place them in ~/.cme/modules

# Usage

To run these is very easy:

Domain Admins
`crackmapexec ldap $DC-IP -u Username - P Password -M DA`

Domain Controllers
`crackmapexec ldap $DC-IP -u Username - P Password -M DC`

Servers
`crackmapexec ldap $DC-IP -u Username - P Password -M Server`

# Results

Output of their results are shown below:


