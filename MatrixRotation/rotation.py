import math


def printMatrix( matrix ) :
    for row in matrix : 
        print row
            
def CreateTextMatrix( xSize , ySize ) : 
    matrix = []
    
    for x in range( 0 , xSize ) :
        matrix.append( [] ) 
        for y in range( 0 , ySize ) :
            matrix[x].append("x")    
    
    return matrix
 
 
def ShouldStop( min , max ) :
    return min >= max


def MarkDepths( startX , endX , startY , endY , depth , matrix ) :
    xSize = endX - startX
    ySize = endY - startY 
    
    stop = False    
    if ( xSize < ySize ) :
        stop = ShouldStop( startX , endX )
    else : 
        stop = ShouldStop( startY , endY )
    
    if  stop :
        return matrix
    else :
        matrix[startY] = MarkRow( matrix[startY] ,  startX , endX , str(depth) )
        matrix[endY] = MarkRow( matrix[endY] ,startX , endX , str( depth ) )
        matrix = MarkColumn( startX , startY , endY , matrix , str(depth ) )
        matrix = MarkColumn( endX - 1 , startY , endY  , matrix , str(depth ) )
        matrix = MarkDepths( startX + 1 , endX - 1 , startY + 1 , endY - 1 , depth + 1 , matrix)
        return matrix
        
def MarkRow( row , startX , endX  , val ) :
    
    for x in  range( startX , endX ) :
        row[x] = val     
    return row

def MarkColumn( xVal , startY , endY , matrix , val ) :
    for col in range( startY , endY ) :
        matrix[col][xVal] = val
    return matrix 
    
    
    
def MapoutMatrix( matrixToMap ) :
    matrixToMap = MarkDepths( 0 , 4 , 0 , 4 , 1, matrixToMap )
    
    return matrixToMap



testMatrix = CreateTextMatrix( 5 , 4  )
testMatrix = MapoutMatrix( testMatrix)
printMatrix( testMatrix )



