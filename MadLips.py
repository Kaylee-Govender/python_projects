adj = input("Provide adjective: ")
colr = input("Provide colour: ")
vrb = input("Provide verb: ")

if len(adj) == 0:
    print("Invalid input, adjective not given.")

elif len(colr) == 0:
    print("Invalid input, colour not given.")

elif len(vrb) == 0:
    print("Invalid input, verb not given.")

else:
    print("Once upon a time, there was a princess who was " + adj + ". \n"
                                                                    "Her lips were " + colr + " as blood. \n"
                                                                                              "She would " + vrb + " red apples before she slept. ")
