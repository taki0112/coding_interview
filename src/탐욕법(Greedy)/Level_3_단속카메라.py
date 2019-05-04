
def solution(routes):
    routes.sort() #진입점 기준 오름차순 정렬
    length = len(routes)
    count = 0 #실제 카메라 설치 개수
    cam = [0]*length #각 구간에 카메라가 커버되는지, 1이면 카메라 커버됨
    camera = 0 #진입점 기준으로 설치된 카메라 위치

    for i in range(length-1, -1, -1): #진입점이 가장 큰 구간부터 진입점이 작은 구간까지 1개씩 이동
        if cam[i] == 0: #카메라가 커버 못하는 구간이라면
            camera = routes[i][0]#현 진입점을 카메라 설치 위치로
            count += 1 #카메라 1개 설치
        for j in range(i, -1, -1): #진입점(camera) 하나를 기준으로 삼고 매 구간의 진출점(routes[j][1])과 비교
            if cam[j] == 0 and routes[j][1] >= camera:#카메라가 커버 못하면서 이전 진입점(camera)이 현재 진출점보다 작거나 같다면
                cam[j] = 1 #이전 진입점에 설치된 카메라가 현 구간을 커버함

    return count



routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
x = solution(routes)

print(x)