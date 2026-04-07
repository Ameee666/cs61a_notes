"""首先是list部分的代码,关键在于画环境图，另外，索引是名字->对象的绑定
赋值操作可以通过层层引用来找到原有的对象，但一定要分清修改的哪个名字
"""
s=[2,3]
t=[5,6]
s.append([t])
s[-1][0][0]=1
print(t)
"""[1,6]"""
"""有趣的代码"""
t = [1,2,3]
t[1:3] = [t]
t.extend(t)
"""[1,[...],1,[...]]"""
t = [[1,2],[3,4]]
t[0].append(t[1:2])
"""[[1,2,[3,4]],[3,4]]"""
"""类继承"""
class Worker:
    greeting = 'sir'
    def __init__(self):
        self.elf = Worker 
        """这里实际上将类属性绑定到类上"""
    def work(self):
        return self.greeting + ', i work'
    def __repr__(self):
        return Bourgeoisie.greeting
class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'I gather wealth'
""">>> Worker().work()
>>> 'sir, i work'
>>> jack = Worker()
>>> john = Bourgeoisie()
>>> john.greeting = 'Maam'
>>> jack 
>>> Peon
>>> jack.work()
>>> 'Maam, i work'
>>> john.work()
>>> Peon, i work
>>> 'I gather wealth'
>>> john.elf.work(john)
>>> ''Peon, i work'"""
def min_abs_indice(s):
    '''返回s中绝对值最小元素的索引'''
    return [i for i in range(len(s)) if abs(s[i])==min([abs(k) for k in s])]
    """another way: return [i for i in range(len(s)) if abs(s[i]) == min(map(abs,s))]
       another way:
       min_abs = min(map(abs,s))
       f = lambda x: abs(s[x]) == min_abs
       list(filter(f,range(len(s))))"""
def largest_adj_sum(s):
    """返回s中两个相邻元素的最大值"""
    return max([s[i]+s[i+1] for i in range(len(s)-1)])
    """another way with zip()
    m = list(zip(s[:-1],s[1:]))
    return max([a+b for a,b in m])"""
def digit_dict(s):
    """把每个数字d映射到以d为结尾的元素列表，结果是一个字典"""
    return {d:[x for x in s if x%10 == d] for d in range(10) if any([x%10 == d for x in s ])}
    """another way: 
    last_digit = [x%10 for x in s]
    return {d:[x for x in s if x %10 == d]for d in range(10) if d in last_digit}"""
def all_have_an_equal(s):
    '''返回是否s中每个元素都有相同的元素'''
    return all([s[i] in s[:i]+s[i+1:] for i in range(len(s))])
    """值得一提的是，切片不会触发bug，超过索引限制时只会返回空集"""
    """another way: 
    return all([sum([1 for y in s if y == x]) > 1 for x in s])
    return min([s.count(x) for x in s]) > 1"""
"""现在进入链表时间"""
class Link:
    empty=()
    def __init__(self,first,rest=[]):
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest:
            rest_repr = ', '+repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
def order(s,key = lambda x:x):
    '这个链表是有序的吗'
    if s == Link.empty() or s.rest == Link.empty():
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return order(s.rest,key)
def merge(s,t):
    """返回分类后的链表"""
    if s is Link.empty():
        return t
    elif t is Link.empty():
        return s
    elif s.first <= t.first:
        return Link(s.first,merge(s.rest,t))
    else:
        return Link(t.first,merge(s,t.rest))
def merge_in_place(s,t):
    if s is Link.empty():
        return t
    elif t is Link.empty():
        return s
    elif s.first <= t.first:
        # return Link(s.first,merge(s.rest,t))
        s.rest = merge_in_place(s.rest,t)
    else:
        t.rest = merge_in_place(s,t.rest)
    
        

