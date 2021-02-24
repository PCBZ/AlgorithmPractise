class Sort(object):
    def quick_sort(self, array):
        self.item_quick_sort(array, 0, len(array)-1)
        return
        
    def item_quick_sort(self, array, start, end):
        if start >= end:
            return
        pivot = start
        i, j = start, start
        while i <= end:
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
                if j == pivot:
                    pivot = i
                j += 1
                
            i += 1
            print(array)
        array[pivot], array[j] = array[j], array[pivot]
        self.item_quick_sort(array, start, j)
        self.item_quick_sort(array, j+1, end)
        
if __name__ == "__main__":
    print("&***")
    s = [0, 9, 7, 1, 3, 8]
    sort = Sort()
    sort.quick_sort(s)
    print(s)
