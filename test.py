states={
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities={
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY']= 'New York'
cities['OR']= 'Portland'


print '\nSome cities' , '-'*10,'\n'
print 'NY state has',cities['NY']
print 'OR state has %s' %cities['OR']

print '\nSome states', '-'*10 , '\n'
print "Michigan's abbreviation is: %s" %states['Michigan']
print "Florida's abbreviation is: %s" %states['Florida']

print 'Michigan has ' , cities[states['Michigan']]
print 'Florida has ' , cities[states['Florida']]
print 'Oregon has ' , cities[states['Oregon']]

print '\n' ,'-'*10 , '\n'
for a , b in states.items():
    print '%s is abbreviated %s' %(a,b)

print '\n'
for a,b in cities.items():
    print '%s has city %s' %(a,b)

print '\n'
for state,abbreviate in states.items():
    print '%s abbreviated to %s and has city %s' %(state, abbreviate, cities[abbreviate])


err = 'does not exists'
state = states.get('California',err)
print state
city = states.get('texas',err)
print city
a = ('California','CA')
if a in states.items():
    print 'sadasd'
