"""在本讲的代码里，我们主要想要实现模块化设计的理念
example:search restaurants"""

def search(query,ranking=lambda x:-x.stars):
    results = [r for r in Restaurants.all if query in r.name]
    """接下来，根据模块化设计思想，我们不妨在传入一个ranking函数来排序"""
    return sorted(results,key=ranking)
    """接下来，我们不妨为ranking设置一个默认值"""
"""这里，我们想要实现similarity的一种实现方式"""
def review_both(r,s):
    return len([x for x in r.reviewers if x in s.reviewers])
"""这里必须时刻牢记操作对象是类，不能直接写个r，s了事，同时这里提示我们，类里需要reviewers这个属性"""
def fast_overlap(s,t):
    i,j,count=0,0,0
    while i<len(s) and j<len(t):
        if s[i] == t[j]:
            count,i,j=count+1,i+1,j+1
        elif s[i] > t[j]:
            j+=1
        else:
            i+=1
    return count




"""接下来，我们用什么来实现restaurants呢，class是很自然的选择"""
class Restaurants:
    all = []
    def __init__(self,name,stars,reviewers):
        self.name,self.stars = name,stars
        """接下来我们不妨把全局名称换成类属性，譬如search函数中的results"""
        Restaurants.all.append(self)
        self.reviewers = reviewers
    """接下来是另一个任务，我们怎么定义similar呢"""
    def similar(self,k,similarity):
        
        others = list(Restaurants.all)
        others.remove(self)
        return sorted(others,key=lambda other:-similarity(self,other))[:k]
    """这里我们就实现了一个模块化的similar函数"""
    def __repr__(self):
        return "<"+self.name+">"
"""ok，现在我们来演示怎么从一个json文件里读取出东西"""
import json
reviewers_for_restaurant={}
for line in open('restaurants.json'):
    r = json.loads(line)
    biz = r['business_id']
    if biz not in reviewers_for_restaurant:
        reviewers_for_restaurant['biz']=[r['user_id']]
    else:
        reviewers_for_restaurant['biz'].append(r['user_id'])



for line in open('restaurants.json'):
    r = json.loads(line)
    reviewers = reviewers_for_restaurant[r['business_id']]
    Restaurants(r['name'],r['stars'],reviewers)



Restaurants('Thai Delight',2)
Restaurants('Thai Basil',3)
Restaurants('Top Dog',5)



"""首先我们想要实现一个搜索功能"""
results = search('Thai')
for r in results:
    print(r,'shared reviewers with',r.similar(3))
"""现在我们需要一个search 函数，由于代码执行问题，search函数被丢到了头上"""
"""我们要实现一个正确的使用了"""
while True:
    print(">",end=" ")
    results = search(input().strip())
    for r in results:
        print(r,'shared reviewers with',r.similar(3))
        
"""看起来我们的similarity占用了过多时间
def fast_overlap(s,t):
    i,j,count=0,0,0
    while i<len(s) and j<len(t):
        if s[i] == t[j]:
            count,i,j=count+1,i+1,j+1
        elif s[i] > t[j]:
            j+=1
        else:
            i+=1
    return count
双指针，不必废话

"""
"""
另外，关于超前引用。定义函数时可以超前，执行时就不可以。"""