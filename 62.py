x=raw_input()
"""if all(c in '01' for c in q):
    print "Yes"
else:
    print "No"
    """
if not(x.translate(None,'01')):
    print "Yes"
else:
    print "No"
