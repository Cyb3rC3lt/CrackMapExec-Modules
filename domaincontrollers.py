#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

class CMEModule:
    '''
      Module by CyberCelt

      Initial module:
        https://github.com/Cyb3rC3lt/CrackMapExec-Modules
    '''

    def options(self, context, module_options):
        pass


    name = 'DC'
    description = 'Retrieves the Domain Controllers within a domain'
    supported_protocols = ['ldap']
    opsec_safe = True
    multiple_hosts = False

    def on_login(self, context, connection):
        domain = connection.domain
        ldap_domain = domain.replace(".",",dc=")

        # Building the search filter
        searchFilter = "(primaryGroupID=516)"

        try:
            context.log.debug('Search Filter=%s' % searchFilter)
            resp = connection.ldapConnection.search(searchFilter=searchFilter,
                                        attributes=['dNSHostName'],
                                        sizeLimit=0)
        except ldap_impacket.LDAPSearchError as e:
            if e.getErrorString().find('sizeLimitExceeded') >= 0:
                context.log.debug('sizeLimitExceeded exception caught, giving up and processing the data received')
                resp = e.getAnswers()
                pass
            else:
                logging.debug(e)
                return False

        answers = []
        context.log.debug('Total of records returned %d' % len(resp))
        for item in resp:
            if isinstance(item, ldapasn1_impacket.SearchResultEntry) is not True:
                continue
            dNSHostName =  ''
            try:
                for attribute in item['attributes']:
                    if str(attribute['type']) == 'dNSHostName':
                        dNSHostName = str(attribute['vals'][0])                   
                if dNSHostName != '':
                    answers.append([dNSHostName])
            except Exception as e:
                context.log.debug("Exception:", exc_info=True)
                context.log.debug('Skipping item, cannot process due to error %s' % str(e))
                pass
        if len(answers) > 0:
            context.log.success('Found the following Domain Controllers: ')
            for answer in answers:
                IP = socket.gethostbyname(answer[0])
                context.log.highlight(u'{} ({})'.format(answer[0],IP))
































