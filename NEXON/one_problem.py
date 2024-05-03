from collections import deque
def getMinTime(cache_size, cache_time, server_time, urls):
    # 캐시를 나타내는 FIFO 큐를 초기화합니다. maxlen을 설정하면 자동으로 오래된 항목이 제거됩니다.
    cache = deque(maxlen=cache_size)
    # 각 URL 조회에 소요되는 시간을 저장할 리스트를 초기화합니다.
    times = []

    # 각 URL에 대해 순회합니다.
    for url in urls:
        # URL이 캐시에 있다면, 캐시 시간을 추가합니다.
        if url in cache:
            times.append(cache_time)
            # UPDATE
        else:
            # 캐시에 없다면, 서버 시간을 추가하고 URL을 캐시에 추가합니다.
            times.append(server_time)
            cache.append(url)
            
    # 각 URL 조회에 소요된 시간의 리스트를 반환합니다.
    return times

# 테스트 코드와 결과 출력은 아래와 같습니다.

if __name__ == '__main__':
    # 간단한 테스트를 위해 출력을 터미널에 직접 출력합니다.
    cache_size = int(input().strip())
    cache_time = int(input().strip())
    server_time = int(input().strip())
    urls_count = int(input().strip())
    urls = [input().strip() for _ in range(urls_count)]
    result = getMinTime(cache_size, cache_time, server_time, urls)
    print('\n'.join(map(str, result)))

# 2
# 2
# 3
# 5
# www.google.com
# www.yahoo.com
# www.google.com
# www.yahoo.com
# www.coursera.com