# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem crescente de matriculas
def partition(arr, low, high): 
    i = (low -1)        
    pivot = arr[high]    
  
    for j in range(low, high): 
  
        if arr[j] >= pivot: 
          
            i += 1
            arr[i], arr[j] = arr[j], arr[i] 


    arr[i + 1], arr[high] = arr[high], arr[i + 1]  
    return (i + 1) 
  
def quickSort(arr,low,high): 
    if low < high: 
  
        pi = partition(arr, low, high) 
		
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
	return arr

def retorna_matriculas_decrescente(alist):

	low = 0
	high = len(alist)

	return quickSort(alist, low, high - 1)
