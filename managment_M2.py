import easysnmp
from easysnmp import Session
# Create an SNMP session to be used for all our requests
session = Session(hostname='localhost', community='public', version=2)
# You may retrieve an individual OID using an SNMP GET
location = session.get_next('sysLocation.0')
name = session.get('sysName.0')
objectid = session.get('sysObjectID.0')
Contact = session.get('sysContact.0')
Description = session.get('sysDescr.0')

# You may also specify the OID as a tuple (name, index)
# Note: the index is specified as a string as it can be of other types than
# just a regular integer
#contact = session.get(('sysContact', '0'))

# And of course, you may use the numeric OID too
#description = session.get('.1.3.6.1.2.1.1.1.0')

# Set a variable using an SNMP SET
#session.set('sysLocation.0', 'The SNMP Lab')

# Perform an SNMP walk
#system_items = session.walk('system')

# Each returned item can be used normally as its related type (str or int)

print( '{oid}.{oid_index} {snmp_type} = {value}'.format(oid=location.oid,
oid_index=location .oid_index,
snmp_type=location .snmp_type,
value=location.value ))

print( '{oid}.{oid_index} {snmp_type} = {value}'.format(oid=name.oid,
oid_index=name.oid_index,
snmp_type=name.snmp_type,
value=name.value ))

print( '{oid}.{oid_index} {snmp_type} = {value}'.format(oid=Contact.oid,
oid_index=Contact.oid_index,
snmp_type=Contact.snmp_type,
value=Contact.value ))

print( '{oid}.{oid_index} {snmp_type} = {value}'.format(oid=Description.oid,
oid_index=Description.oid_index,
snmp_type=Description.snmp_type,
value=Description.value ))