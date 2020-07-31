import bisect


class Solution(object):
    def kthSmallest(self, matrix, k):
        smallest = matrix[0][:]
        N = len(matrix)
        for i in range(1,N):
            for num in matrix[i]:
                bisect.insort_left(smallest, num)
        return smallest[k-1]


'''
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        smallest = k*[0]
        smallest[0] = matrix[0][0]
        last = 1
        possible = {}
        N = len(matrix)
        try:
            val1 = matrix[0][1]
            val2 = matrix[1][0]
            if val1 != val2:
                possible[val1] = [(0,1)]
                possible[val2] = [(1,0)]
            else:
                possible[val1] = [(0,1), (1,0)]
        except:
            return(smallest[0])
        while last < k:
            choice = min(possible.keys())
            smallest[last] = choice
            last += 1
            i,j = possible[choice].pop()
            if possible[choice] == []:
                del possible[choice]
            if i == N-1 and j == N-1:
                pass
            elif i != N-1 and j == N-1:
                val = matrix[i+1][j]
                try:
                    if (i+1,j) not in possible[val]:
                        possible[val].append((i+1,j))
                except:
                    possible[val] = [(i+1,j)]
            elif i == N-1 and j != N-1:
                val = matrix[i][j+1]
                try:
                    if (i,j+1) not in possible[val]:
                        possible[val].append((i,j+1))
                except:
                    possible[val] = [(i,j+1)]
            else:
                val1 = matrix[i+1][j]
                val2 = matrix[i][j+1]
                try:
                    if (i+1,j) not in possible[val1]:
                        possible[val1].append((i+1,j))
                except:
                    possible[val1] = [(i+1,j)]
                try:
                    if (i,j+1) not in possible[val2]:
                        possible[val2].append((i,j+1))
                except:
                    possible[val2] = [(i,j+1)]
        print(possible)
        return(smallest[-1])
'''


if __name__ == '__main__':
    sol = Solution()
    test = [[ 1,  5,  9], [10, 11, 13], [12, 13, 15]]
    test2 = [[3,5,9,9,9],[5,8,13,13,16],[10,10,14,14,16],[15,18,20,24,26],[20,24,29,32,37]]
    test3 = [[1,3,5],[6,7,12],[11,14,14]]