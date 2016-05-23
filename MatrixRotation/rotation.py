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

def MarkMatrix( matrix , startX , endX , startY , endY , depth ) :
     matrix[startY] = MarkRow( matrix[startY] ,  startX , endX , depth )
     matrix[endY] = MarkRow( matrix[endY] ,startX , endX , depth  )
     matrix = MarkColumn( startX , startY , endY , matrix , depth  )
     matrix = MarkColumn( endX - 1 , startY , endY  , matrix , depth  )
     return matrix

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
        matrix = MarkMatrix( matrix , startX , endX , startY , endY , str(depth) )
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
    
    
    
def MapoutMatrix( matrixToMap , xSize , ySize , rot ) :
    matrixToMap = MarkDepths( 0 , xSize - 1 , 0 , ySize  , 1,  matrixToMap )
    
    return matrixToMap


xSize = 5
ySize = 4
numOfRotations = 1
testMatrix = CreateTextMatrix( xSize , ySize  )
testMatrix = MapoutMatrix( testMatrix , xSize , ySize , numOfRotations  )
printMatrix( testMatrix )



