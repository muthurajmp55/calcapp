import sys

class Ackermann:
    count = 0
    cache = {}
    cache_hit = 0
    cache_miss = 0
    
    def calculate(self, m, n):
        self.count = self.count + 1
        if m in self.cache and n in self.cache[m]:
            self.cache_hit = self.cache_hit + 1
            return self.cache[m][n]
        else:
            self.cache_miss = self.cache_miss + 1
            if m == 0:
                result = n + 1
            if m == 1:
                result = n + 2
            elif n == 0:
                result = self.calculate(m - 1, 1)
            else:
                result = self.calculate(m - 1, self.calculate(m, n - 1))
            if m not in self.cache:
                self.cache[m] = {}
            self.cache[m][n] = result
        return result

    def run(self, m, n):
        print("Inside run")
        sys.setrecursionlimit(50000)
        if m==0:
            return n+1
        return self.calculate(m, n)

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

def fib(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]
if __name__ == "__main__":
    from datetime import datetime
    import sys

    if len(sys.argv) != 3:
		#print_usage()
        exit()
    m = (int)(sys.argv[1])
    n = (int)(sys.argv[2])

    sys.setrecursionlimit(1000000)
    start_time = datetime.now()
    ackermann = Ackermann()
    print('ackermann(%d,%d): %d' % (m, n, ackermann.run(m, n)))
    end_time = datetime.now()
    time_diff = end_time - start_time
    print('execution time: %s' % time_diff)
    print('Number of calls: %d' % ackermann.count)
    if ackermann.cache != {}:
        print('Cache Hit count: %d' % ackermann.cache_hit)
        print('Cache Miss count: %d' % ackermann.cache_miss)
        print('Cache Hit ratio: %.2f' % ((float)(ackermann.cache_hit) / ackermann.cache_miss * 100))
