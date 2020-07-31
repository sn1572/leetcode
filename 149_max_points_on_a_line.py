# Definition for a point.

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints(self, points: 'List[Point]') -> 'int':


        def getGcd(a, b):
            if b==0: 
                return a 
            else: 
                return getGcd(b,a%b)


        def getQRD(num, denom):
            Q, R, D = num // denom, num % denom, denom
            gcd = getGcd(R, D)
            R, D = R/gcd, D/gcd
            return((Q, R, D))


        def getSlopeAndIntercept(point1, point2):
            '''
            Gets the slope and y intercept.
            Values are stored in the format (Q, R, D) 
            where Q is quotient, R is remainder, D is divisor.
            R and D are coprime so that we have a unique representation.
            Avoids loss of precision due to computer rounding errors.
            '''
            x1 = point1.x
            y1=  point1.y
            x2 = point2.x
            y2 = point2.y
            rise = y1-y2
            run = x1-x2
            if run != 0:
                slope = getQRD(rise, run)
            else:
                return('inf', x1)
            rise = x1*y2-x2*y1
            intercept = getQRD(rise, run)
            return(slope, intercept)


        L = len(points)
        if L <= 2:
            return(L)
        results = {}
        L = len(points)
        for i in range(L):
            point1 = (points[i].x, points[i].y, i)
            for j in range(i+1,L):
                point2 = (points[j].x, points[j].y, j)
                slope, intercept = getSlopeAndIntercept(points[i], points[j])
                lineIdentifier = (slope, intercept)
                try:
                    #this cannot fail if results[lineIdentifier] is a dictionary at all
                    results[lineIdentifier][point1] = 1
                    results[lineIdentifier][point2] = 1
                except:
                    results[lineIdentifier] = {point1 : 1, point2: 1}

        maximum = 0
        for line, pointsDict in results.items():
            current = len(pointsDict)
            if current > maximum:
                maximum = current
        return(maximum)


if __name__ == '__main__':


    def convertToPoints(array):
        hold = []
        for element in array:
            hold.append(Point(element[0], element[1]))
        return(hold)


    example1 = convertToPoints([[1,1],[2,2],[3,3]])
    example2 = convertToPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])
    example3 = convertToPoints([[0,0],[1,1],[0,0]])
    example4 = convertToPoints([[0,0],[1,1],[0,0],[1,1],[2,2]])
    example5 = convertToPoints([[0,0],[0,0],[0,0],[1,2]])
    example6 = convertToPoints([[0,0],[0,0]])
    example7 = convertToPoints([[0,-1],[0,3],[0,-4],[0,-2],[0,-4],[0,0],[0,0],[0,1],[0,-2],[0,4]])
    example8 = convertToPoints([[0,0],[94911151,94911150],[94911152,94911151]])
    sol = Solution()
    assert(sol.maxPoints(example1) == 3)
    assert(sol.maxPoints(example2) == 4)
    assert(sol.maxPoints(example3) == 3)
    assert(sol.maxPoints(example4) == 5)
    assert(sol.maxPoints(example5) == 4)
    assert(sol.maxPoints(example6) == 2)
    assert(sol.maxPoints(example7) == 10)
    assert(sol.maxPoints(example8) == 2)