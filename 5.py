"""这是在lec23里出现的主要代码，主要用于追踪"""
"""这里的斐波那契函数只是用来作为示范"""
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
def count(f):
    """这是一个用于追踪函数被调用次数的装饰器函数"""
    def counted(n):
        counted.called_times += 1
        """这里return顺序不可以颠倒，否则上面的代码本质没写"""
        return f(n)
    counted.called_times = 0
    return counted
def cache_func(f):
    """缓存装饰器，通过缓存手法来减少重复计算"""
    cache = {}
    def new_func(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return new_func
"""调用示例
f = count(cache_func(fib)),通过类似的装饰来实现追踪的目的"""
"""现在我们来追踪空间占用，即函数占用了多少帧"""
def count_frames(f):
    def counted(n):
        counted.open_frame += 1
        if counted.open_frame > counted.max_frame:
            counted.max_frame = count.open_frame
        result = f(n)
        counted.open_frame -=1
        return result
    counted.open_frame = 0
    counted.max_frame = 0
    return counted
