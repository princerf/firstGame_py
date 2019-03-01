import sys , random , table , pickle

basket = 0

def print_basket():
    print basket

def return_basket():
    return basket

blue_golds = random.randint(1,19)
red_golds = random.randint(1,50)
green_golds = random.randint(1,250)

#define the blue room which contains duck and 21 golds
def blue_room():
    print '''
    You are in the blue room, which contains a duck who is the guardian of the golds of this room.
    for search for golds, you must first take foods to the duck with 'food' command, then you can search with 'search' and 'claim' the golds.
    when your jobs finished, you must type 'return' for return to master room and resume searching for other room's golds. good luck
    '''

    golds = blue_golds
    relaxed = False
    claimed = False
    searched = False

    while True:
        myInput = raw_input('> ')
        inp = myInput.lower()

        if inp == 'food' and relaxed:
            print 'The duck is not hungry, dont try to make it angry'

        elif inp == 'food' and not relaxed:
            relaxed = True
            print 'The duck got relaxed, now you can start searching for golds ;)'

        elif inp == 'search' and not relaxed:
            print 'The duck is awakened, so you are loosed :('
            sys.exit(0)

        elif inp == 'search' and relaxed:
            print 'Congratulations, you found %s golds' %golds
            searched = True

        elif inp == 'knock' or inp == 'sing' and relaxed:
            print 'You awakened the duck and you loosed :('
            sys.exit(0)

        elif inp == 'claim' and relaxed and not claimed and searched:
            global basket
            basket += golds
            print 'All %s golds you founded here added to your basket, for see how much golds you claimed so far type basket' %golds
            claimed = True

        elif inp == 'claim' and claimed:
            print 'You claimed all the golds! get away soon as possible ;)'

        elif inp == 'basket':
            print_basket()

        elif inp == 'return':
            master_room()

        else:
            print 'Enter a valid value'

#define the red room which contains bear and 49 golds
def red_room():
    print '''
    Here is Red room, which contains a bear who actually loves honey ! for friendly relationship with that, you can
    give he a glass of honey by command 'honey' for your purposes. then you can 'search' and 'claim' all the golds available
    in this room. you must type 'return' for return to master room and resume searching for other room's golds. good luck friend ;)
    '''
    golds = red_golds
    relaxed = False
    claimed = False
    searched = False

    while True:
        inp = raw_input('> ').lower()

        if inp == 'honey' and not relaxed:
            print 'Congratulations! the bear loves honey more than golds! be careful and search to find golds ;)'
            relaxed = True

        elif inp == 'honey' and relaxed:
            print 'The bear not more hungry :| pick the golds and be aware soon'

        elif inp == 'knock' or inp == 'sing':
            print 'I bet you are crazy! dont do these guy, DON\'T DO THIS ... '

        elif inp == 'search' and relaxed:
            print 'You found %s golds in this room, claim that and go' %golds
            searched = True

        elif inp == 'search' and not relaxed:
            print 'Ommmmm . The bear eats YOU :| good luck'
            sys.exit(0)

        elif inp == 'claim' and relaxed and not claimed and searched:
            global basket
            basket += golds
            print 'All golds you found here is %d' %golds
            claimed = True

        elif inp == 'claim' and claimed:
            print 'You have claimed all the golds! Why do you stay here so far??'

        elif inp == 'basket':
            print_basket()

        elif inp == 'return':
            master_room()

        else:
            print 'Please enter a valid Value'

#define the green room which contains tiger and 99 golds
def green_room():
    relaxed = False
    claimed = False
    searched = False

    golds = green_golds

    if golds < 125:
        print 'The tiger was awakened and you loosed :('
        sys.exit(0)
    else:
        print 'You are so lucky, the tiger was slept and you can search for golds :)'

    while True:
        inp = raw_input('> ').lower()

        if inp == 'search' and not searched:
            print '%d golds founds here' %golds
            searched = True

        elif inp == 'search' and searched:
            print golds

        elif inp == 'claim' and not claimed:
            global basket
            basket += golds
            print '%d golds was append to your basket' %golds
            claimed = True

        elif inp == 'claim' and claimed:
            print 'the golds has been claimed'

        elif inp == 'basket':
            print_basket()

        elif inp == 'return':
            master_room()

        else:
            print 'You must enter a valid value!\n'








room_entered = False

counter = {}
counter_i = 0

def master_room():
    global basket
    global room_entered
    global counter
    global counter_i
    cond = True

    counter_i += 1

    while cond:
        inp=raw_input('Which room? >>>  ').lower()
        if inp == 'blue':
            blue_room()


        elif inp == 'red':
            red_room()

        elif inp == 'green' and not room_entered:
            print '''
            Here is Green room, which contains a tiger. you must really so lucky if you open the door and our little friend was slept,
            if not, I can only tell you rest in peace my friend ;)
            You can enter to the room and if the tiger was slept, then you can 'search' and 'claim' all the golds were there. also you
            must type 'return' for return to master room and resume searching for other room's golds. and the golds
            you can found there was between 0 and 250 !!! Remember that survive may be impossible if the tiger was awakened ;)

            >>>  For enter to the room, Retype 'green' ***
            '''

            room_entered = True

        elif inp == 'green' and room_entered:
            green_room()

        elif inp == 'basket':
            print basket , '\n'
            master_room()

        elif inp == 'table':
            table.print_table()

        elif inp == 'clear table':
            table.clear_list()

        elif inp == 'exit':
            print '\nDo you want save your points?\n Y or N ?'
            ex_inp = raw_input('> ').lower()

            if ex_inp == 'y':
#***********************************************************************
                if len(table.points) > 0 and basket in counter.itervalues():
                    print '\nYour point is similar to the last\n'
                elif basket == 0:
                    print "\nYour point is 0 and you can't save that.\n"
                else:
                    counter[counter_i] = basket
                    table.points.append(basket)
                    table.savePoint(table.points)
                    print '\nYour point was saved ! Now the table is:   ' , table.loadPoint() , '\n'
                    #sys.exit(0)
#*************************************************************************
            else:
                print '\nYour points not saved. Good luck ;)\n'
                sys.exit(0)

        else:
            print 'You must enter a valid Value\n'
            master_room()
