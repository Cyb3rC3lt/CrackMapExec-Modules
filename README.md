# CrackMapExec LDAP Modules
Here are some CME LDAP modules I created to help with AD enumeration. 

If you ever wanted to know who the Domain Admins are quickly without building an ldap search string or starting up Bloodhound then the 'DA' module is for you. 

Likewise if you ever wanted a list of the domain controllers and machines described as 'Servers' to focus your attack on, then the 'DC' and 'Servers' modules are for you. 

# Installation

Place them in ~/.cme/modules

# Usage

To run these is very easy:

Returns Domain Admins

`crackmapexec ldap $DC-IP -u Username -p Password -d $DOMAIN -M DA`

Returns Domain Controllers

`crackmapexec ldap $DC-IP -u Username -p Password -d $DOMAIN -M DC`

Returns Servers

`crackmapexec ldap $DC-IP -u Username -p Password -d $DOMAIN -M Server`

# Results

Output of their results are shown below:


