def sortthis(data, value):
    low = 0
    high = len(data) -1
    mid = 0


    while low <= high:
        mid = round((high+low)/2)
        print(f"the low index is {low}, its value is {data[low]}\nthe high index is {high}, its value is {data[high]}\nthe mid index is {mid}, its value is {data[mid]}\n")
        if value > data[mid]:
            low = mid + 1
        elif value < data[mid]:
            high = mid - 1
        else:
            print(f"found at index {mid}")
            break    
            

if __name__ == "__main__":
    nums = [1, 6, 11, 14, 23, 26, 30, 31, 32, 40, 50, 58, 69, 420]
    sortthis(nums, 11)



