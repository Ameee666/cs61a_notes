#本讲知识点
这里只记录关键点，实操部分已被放置代码部分
## 时间 即big theta and big o notations for order of growth
###指数增长(exponential growth):e.g fib(n)
incrementing n ——multiply time by a constant  $\Theta(b^n)$ $O(b^n)$
###二次增长:e.g overlop
increment n———increase time by n times a constant $\Theta(n^2)$ $O(n^2)$
###线性增长：
increment n————increase time by a constant $\Theta(n)$ $O(n)$
###对数增长：
double n————increase time by a constant $\Theta(logn)$ $O(logn)$
###常数增长:
时间恒定 $\Theta(1)$ $O(1)$
###对于 $\Theta$:要求函数所用时间最多是(表达式)的，最少也是(表达式)的
对于 $O$:要求函数所用时间上限为(表达式)的
### 二次增长
用于处理线性输入中所有元素对或长度为n的序列中所有值对的函数
###def overlap(a,b):
        count = 0
        for item in a:
            for other in b:
                if item == other:
                count +=1
        return count
## 空间
任何时间段都会有活动环境，active environment
在活动环境中的内存被保留，用于其他值和帧的任何内存，不在活动环境，会被回收
###活动环境是什么呢：
正在被调用而未返回值的函数所在的环境
存在于一个活动环境中函数的父环境
