'''
Problem1.

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

'''
Solution1.

1. answer을 선언한다.
2. N 미만의 n1의 배수를 모두 answer에 더한다.
3. N 미만의 n2의 배수를 모두 answer에 더한다.
4. N 미만의 n1과 n2의 최소공배수의 배수를 모두 answer에서 뺀다.
'''

def getLCM(n1, n2):
    for i in range(max(n1, n2), (n1*n2)+1):
        if i%n1==0 and i%n2==0:
            print('lcm of {0} and {1} is {2}'.format(n1, n2, i))
            return i

def calculate(N, n1, n2):
    result = 0
    result += sum([i for i in range (n1, N, n1)])
    result += sum([i for i in range (n2, N, n2)])
    lcm = getLCM(n1, n2)
    result -= sum([i for i in range (lcm, N, lcm)])
    return result

answer = calculate(1000, 3, 5)
print('answer: {0}'.format(answer))