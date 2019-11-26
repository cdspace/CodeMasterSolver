import itertools as it

# [ [ from node, to node, color ] ]
cMap = [ [ 0, 1, 'r' ],
        [ 0, 2, 'r' ],
        [ 0, 4, 'b' ],
        [ 1, 0, 'r' ],
        [ 1, 2, 'b' ],
        [ 1, 3, 'g' ],
        [ 2, 0, 'g' ],
        [ 2, 1, 'b' ],
        [ 2, 5, 'r' ],
        [ 3, 1, 'g' ],
        [ 3, 4, 'r' ],
        [ 3, 5, 'b' ],
        [ 4, 0, 'b' ],
        [ 4, 3, 'r' ],
        [ 4, 5, 'g' ],
        [ 5, 2, 'r' ],
        [ 5, 3, 'b' ],
        [ 5, 4, 'g' ] ]


path = []
for n in cMap:
    path.append( [n] )
    
for l in range( 3 ):

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
            

for n in path:
    print( n )

print( "@@@@@@" )

for n in path:

    thePath = []
    theColors = []
    for n0 in n:

        thePath.append( str( n0[ 0 ] ) )
        theColors.append( n0[ 2 ] )
        
    print( ''.join( thePath ), ''.join( theColors ) )

print( "@@@@@@@@" )

for n in path:

    if n[ 0 ][ 0 ] == 2 and n[ len( n ) - 1 ][ 1 ] == 4:
        print( n )
        



for n in path:

    thePath = []
    theColors = []
    for n0 in n:

        thePath.append( str( n0[ 0 ] ) )
        theColors.append( n0[ 2 ] )

    if n[ 0 ][ 0 ] == 2 and n[ len( n ) - 1 ][ 1 ] == 4:

        print( ''.join( thePath ), ''.join( theColors ) )
