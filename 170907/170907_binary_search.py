data = [1,2,3,4,5]
def binary_search(data, target):
    '''
    data에서 target의 인덱스
    target이 없다면 None
    '''
    start = 0
    end = len(data) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None
