''' Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible. 

solution explaination - we put all the characters and the frequency of their occurences in a max heap. then we alternatively pop intems from maxheap and place them in our resultant string then decrease the frequency by one and push them back in the maxheap.
we're using negative frequency values because python's inbuilt heap is min heap so to make it as max heap we use this trick of storing negative values. 
If anything remains after while operation, use another if case to fill it. if the frequency of remaining item is more than one then we wont be able to store alternativly that means solution is not possible. no need to import libraries in leetcode.
'''

class Solution:
    def reorganizeString(self, s: str) -> str:
        res=[]
        dic={}
        for i in s:
            dic[i]=dic.get(i,0)+1
        mh = [(-v,k) for k,v in dic.items()]
        heapq.heapify(mh)

        while len(mh)>=2:
            f1,c1=heapq.heappop(mh)
            f2,c2=heapq.heappop(mh)
            res.extend([c1,c2])
            if f1+1<0:
                heapq.heappush(mh,(f1+1,c1))
            if f2+1<0:
                heapq.heappush(mh,(f2+1,c2))

        if mh:
            f,c=heapq.heappop(mh)
            if -f>1:
                return ""
            res.append(c)
        return "".join(res)
