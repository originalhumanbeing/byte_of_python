ab = {
    'SWAROOP' : 'SWAROOP@SWAROOPCH.COM',
    'LARRY' : 'LARRY@WALL.ORG',
    'MATSUMOTO' : 'MATZ@RUBY-LANG.ORG',
    'SPAMMER' : 'SPAMMER@HOTMAIL.COM'
}

print ("Swaroop's address is ", ab['SWAROOP'])

del ab['SPAMMER']

print ('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print ('Contact {} at {}'.format(name, address))

ab['GUIDO'] = 'guido@python.org'

if 'GUIDO' in ab :
    print ("\nGuido's address is ", ab['GUIDO'])

