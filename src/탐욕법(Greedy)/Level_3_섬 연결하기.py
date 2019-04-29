parent={}#각 노드의 부모
rank={}#트리의 노드 수

def make_set(v):#각 노드를 집합으로 만들기
    parent[v]=v#일단 부모는 자기 자신
    rank[v]=0#

def findRoot(v):
    if parent[v]!=v:#부모가 자기 자신이 아니면
        parent[v]=findRoot(parent[v])#최상위의 부모로 갱신
    return parent[v]#부모가 자기 자신이라면 최상위이므로 반환

def union(r1,r2):
    if r1!=r2:#루트값이 서로 다르면 다른 집합임
        if rank[r1]>rank[r2]:#노드 수가 적은 집합의 루트가 노드 수가 많은 집합의 루트로 변경됨
            parent[r2]=r1
        else:
            parent[r1]=r2
            if rank[r1]==rank[r2]:#집합의 개수가 같다면
                rank[r2]+=1# r1이 속한 집합의 부모 루트가 r2로 변경되었으므로 r2의 개수를 더 많다고 해주기

def solution(n,costs):
    for i in range(n):#모든 노드에 대해 집합화
        make_set(i)
    mst=[]#최소 비용 신장(spanning) 트리
    s=0#최소 비용 누적을 위한 변수
    costs=sorted(costs,key=lambda costs:costs[2])#비용 기준으로 정렬
    for j in costs:
        v,u,w=j# v=노드1 u=노드2 w=비용
        r1=findRoot(v)#노드 v에 대한 루트
        r2=findRoot(u)
        if r1!=r2:#노드의 루트가 다르면
            union(r1,r2)#두 노드 중 하나의 집합 수가 많은 집합에 넣기
            s+=w
            mst.append(j)
    return s #최단거리
    # return mst #최단거리를 만들기 위해 선택된 노드,간선,비용들

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

x = solution(n, costs)
print(x)
