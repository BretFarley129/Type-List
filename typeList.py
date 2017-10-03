def typeList(arr):
    # CATCH STATEMENT
    if not arr:
        print "Empty list. Nice try."
        return
    string = ""
    total = 0
    # PROCESS
    for i in arr:
        if type(i) == str:
            string += i
        elif (type(i) == int) or (type(i) == float):
            total += i

    # DETERMINE TYPE -- used if statement; using type(thing) had a weirdly formatted return
    if (total and string):
        x = "mixed"
    else:
         if type(i) == str:
            x = "string"
        elif (type(i) == int) or (type(i) == float):
            x = "integer"

    # OUTPUT
    print "The list you entered is of " + str(x) + " type"
    if string:
        print "String: " + string
    if total:
        print "Sum: " + str(total)

#END TYPELIST()

l = ['magical unicorns',19,'hello',98.98,'world']
typeList(l)
l = [2,3,1,7,4,12]
typeList(l)
l = ['magical','unicorns']
typeList(l)
l = []
typeList(l)

