import itertools as it

# [ [ from node, to node, color ] ]
cMap = [ [ 0, 1, 'b' ],
        [ 0, 2, 'r' ],
        [ 0, 4, 'g' ],
        [ 1, 0, 'b' ],
        [ 1, 2, 'g' ],
        [ 1, 5, 'r' ],
        [ 2, 1, 'g' ],
        [ 2, 0, 'r' ],
        [ 2, 3, 'b' ],
        [ 3, 2, 'b' ],
        [ 3, 5, 'g' ],
        [ 3, 4, 'r' ],
        [ 4, 0, 'g' ],
        [ 4, 3, 'r' ],
        [ 4, 5, 'b' ],
        [ 5, 1, 'r' ],
        [ 5, 3, 'g' ],
        [ 5, 4, 'b' ] ]



path = []
for n in cMap:
    path.append( [n] )
    
for l in range( 5 ):

    # put the new connections in here, we might have many paths off one node
    newPath = []
    
    for n0 in path:

        for n1 in cMap:

            # match n0[ len - 1 ].to with n1.from
            if n0[ len( n0 ) - 1 ][ 1 ] == n1[ 0 ]:
                
                checkNode = n0[:]
                checkNode.append( n1 )

##                print( l )
##                print( n0 )
##                print( len( n0 ) )
                newPath.append( checkNode )
                #break
                # don't break here, let it find all possible paths 

    # and after traversing the whole of possibilities, put the new path in the old path to restart
    path = newPath[:]

            
# full structure, all paths
for n in path:
    print( n )



print( "all paths, formatted" )

# all paths, formatted
for n in path:

    thePath = []
    theColors = []
    for n0 in n:

        thePath.append( str( n0[ 0 ] ) )
        theColors.append( n0[ 2 ] )
        
    print( ''.join( thePath ), ''.join( theColors ) )




startPoint = 5
endPoint = 0

print( "all paths, formatted, start to finish" )

# full structure, start to finish
for n in path:

    if n[ 0 ][ 0 ] == startPoint and n[ len( n ) - 1 ][ 1 ] == endPoint:
        print( n )


# formatted, start to finish
print( "start to finish" )

for n in path:

    thePath = []
    theColors = []
    for n0 in n:

        thePath.append( str( n0[ 0 ] ) )
        theColors.append( n0[ 2 ] )

    thePath.append( str( endPoint ) )

    # check the start and end points
    if n[ 0 ][ 0 ] == startPoint and n[ len( n ) - 1 ][ 1 ] == endPoint:

        print( ''.join( thePath ), ''.join( theColors ) )





print( "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" )
print( "start to finish, with conditions" )
# colors tiles available
colorsNeeded = [ 'r', 'b', 'g', 'g', 'g', 'g' ]
# crystal corners to visit
pointsNeeded = [ '3', '4' ]

for n in path:

    thePath = []
    theColors = []
    for n0 in n:

        thePath.append( str( n0[ 0 ] ) )
        theColors.append( n0[ 2 ] )

    thePath.append( str( endPoint ) )

    # check the start and end points
    if n[ 0 ][ 0 ] == startPoint and n[ len( n ) - 1 ][ 1 ] == endPoint:

        # check if we failed
        failCheck = False
        
        # check the needed points visited
        # save the path, we might need to visit a point twice
        currPath = ''.join( thePath )
        currColors = ''.join( theColors )
        for needPoint in pointsNeeded:

            # if this path has the point we need
            if currPath.find( needPoint ) != -1:

                # remove this needed point and keep checking
                currPath = currPath[ 0 : currPath.find( needPoint ) ] + currPath[ currPath.find( needPoint ) + 1 : ]

            # doesn't have the point we need, FAIL!
            else:
                failCheck = True

        # if we have the points we needed, check the colors
        if not failCheck:
        
            # check the needed colors used
            for needColor in colorsNeeded:
                
                # if this path has the color we need
                if currColors.find( needColor ) != -1:

                    # remove this needed point and keep checking
                    currColors = currColors[ 0 : currColors.find( needColor ) ] + currColors[ currColors.find( needColor ) + 1 : ]

                # doesn't have the point we need, FAIL!
                else:
                    failCheck = True

        if not failCheck:
            
            print( ''.join( thePath ), ''.join( theColors ) )

