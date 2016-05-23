import math


def printMatrix( matrix ) :
    for row in matrix : 
        print row
            
def CreateTextMatrix( size ) : 
    matrix = []
    
    for x in range( 0 , 5 ) :
        matrix.append( [] ) 
        for y in range( 0 , size ) :
            matrix[x].append("x")    
    
    return matrix
 


def MarkDepths( startX , endX , startY , endY , depth , matrix ) :
    
    if  startX >= endX  :
        return matrix
    else :
        matrix[startY] = MarkRow( matrix[startY] ,  startX , endX , str(depth) )
        matrix[endY] = MarkRow( matrix[endY] ,startX , endX , str( depth ) )
        matrix = MarkDepths( startX + 1 , endX - 1 , startY + 1 , endY - 1 , depth + 1 , matrix)
        return matrix
        
def MarkRow( row , startX , endX  , val ) :
    
    for x in  range( startX , endX ) :
        row[x] = val     
    return row

def MapoutMatrix( matrixToMap ) :
    matrixToMap = MarkDepths( 0 , 4 , 0 , 4 , 1, matrixToMap )
    
    return matrixToMap



testMatrix = CreateTextMatrix( 4 )
testMatrix = MapoutMatrix( testMatrix)
printMatrix( testMatrix )



