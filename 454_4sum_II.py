class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """


        def getIndices(X, Y, decreasing = True):
            '''
            Produces indices in the correct order for traversal from sorted
            lists X, Y. 
            '''
            i,j = 0,0
            XY_indices = []
            n_X, n_Y = len(X), len(Y)
            while i < n_X and j < n_Y:
                if i == n_X-1:
                    #i == n_C-1 and j != n_D-1
                    XY_indices.append([n_X-i-1,n_Y-j-1])
                    j += 1
                elif j == n_Y-1:
                    #i != n_C-1 and j == n_D-1
                    XY_indices.append([n_X-i-1,n_Y-j-1])
                    i += 1
                else:
                    #i != n_C-1 and j != n_D-1
                    XY_indices.append([n_X-i-1,n_Y-j-1])
                    val1 = X[-i-2]+Y[-j-1]
                    val2 = X[-i-1]+Y[-j-2]
                    if val2 < val1:
                        XY_indices += [[n_X-i-2, n_Y-j-1], [n_X-i-1, n_Y-j-2]]
                    else:
                        XY_indices += [[n_X-i-1, n_Y-j-2], [n_X-i-2, n_Y-j-1]]
                    i += 1
                    j += 1
            if not decreasing:
                XY_indices = XY_indices[::-1]
            return(XY_indices)


        N = len(A)

        #preprocess lists to remove duplicates
        A_counts = {}
        B_counts = {}
        C_counts = {}
        D_counts = {}
        originals = [A, B, C, D]
        uniques = [A_counts, B_counts, C_counts, D_counts]
        for i in range(N):
            for j in range(4):
                try:
                    uniques[j][originals[j][i]] += 1
                except:
                    uniques[j][originals[j][i]] = 1
        A, B, C, D = [sorted(unique.keys()) for unique in uniques]

        out = 0
        AB_indices = getIndices(A, B, False)
        CD_indices = getIndices(C, D)
        AB_i = CD_i = 0
        while AB_i < len(AB_indices):
            i,j = AB_indices[AB_i]
            k,l = CD_indices[CD_i]
            AB_sum = A[i]+B[j]
            CD_sum = C[k]+D[l]
            while CD_sum > -AB_sum and CD_i < len(CD_indices)-1:
                CD_i += 1
                k,l = CD_indices[CD_i]
                CD_sum = C[k]+D[l]
            if CD_sum+AB_sum == 0:
                out += A_counts[A[i]]*B_counts[B[j]]*C_counts[C[k]]*D_counts[D[l]]
                print(str(i)+' '+str(j)+' '+str(k)+' '+str(l))
                print(A_counts[A[i]]*B_counts[B[j]]*C_counts[C[k]]*D_counts[D[l]])
            try:
                k_n, l_n = CD_indices[CD_i+1]
                CD_sum_n = C[k_n]+D[l_n]
                if CD_sum_n == CD_sum:
                    out += A_counts[A[i]]*B_counts[B[j]]*C_counts[C[k_n]]*D_counts[D[l_n]]
                    print(str(i)+' '+str(j)+' '+str(k_n)+' '+str(l_n))
                    print(A_counts[A[i]]*B_counts[B[j]]*C_counts[C[k_n]]*D_counts[D[l_n]])
                    CD_i += 2
            except:
                pass
            AB_i += 1

        return(out)


if __name__ == '__main__':
    A = [1,2]
    B = [-2,-1]
    C = [-1,2]
    D = [0,2]
    sol = Solution()
    assert sol.fourSumCount(A,B,C,D) == 2

    A = [1,1,-1,-1]
    B = [-1,-1,1,1]
    C = [1,-1,0,-1]
    D = [1,1,-1,1]
    assert sol.fourSumCount(A,B,C,D) == 28

    A = [-1,-1]
    B = [-1,1]
    C = [-1,1]
    D = [1,-1]
    assert sol.fourSumCount(A,B,C,D) == 6

    A = [0,1,-1]
    B = [-1,1,0]
    C = [0,0,1]
    D = [-1,1,1]
    assert sol.fourSumCount(A,B,C,D) == 17


'''
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """            
        AB_sums = {}
        CD_sums = {}
        N = len(A)
        
        #preprocess lists to remove duplicates
        A_unique = {}
        B_unique = {}
        C_unique = {}
        D_unique = {}
        originals = [A, B, C, D]
        uniques = [A_unique, B_unique, C_unique, D_unique]
        for i in range(N):
            for j in range(4):
                try:
                    uniques[j][originals[j][i]] += 1
                except:
                    uniques[j][originals[j][i]] = 1
        A, B, C, D = [list(unique.keys()) for unique in uniques]

        #double sums for A, B
        for i in range(len(A)):
            for j in range(len(B)):
                AB_val = A[i]+B[j]
                try:
                    AB_sums[AB_val] += A_unique[A[i]]*B_unique[B[j]]
                except:
                    AB_sums[AB_val] = A_unique[A[i]]*B_unique[B[j]]

        #double sums for C, D
        for i in range(len(C)):
            for j in range(len(D)):
                CD_val = C[i]+D[j]
                try:
                    CD_sums[CD_val] += C_unique[C[i]]*D_unique[D[j]]
                except:
                    CD_sums[CD_val] = C_unique[C[i]]*D_unique[D[j]]

        out = 0
        for val, AB_count in AB_sums.items():
            try:
                CD_count = CD_sums[-val]
                out += AB_count*CD_count
            except:
                pass
        return(out)
'''