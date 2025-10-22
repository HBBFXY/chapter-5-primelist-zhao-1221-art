# 在此文件中实现 PrimeList 函数

def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    prime = []
    if N < 2:
        return ''
    else:
        for n in range(2,N):
            is_prime = True
            for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime.append(str(n))
        return ''.join(prime)
