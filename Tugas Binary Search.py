def binarysearch(A, low, high, x): #disini terdapat fungsi (def) binary search dengan parameter A disini adalah sebuah array, low disini sebagai index/posisi terendah yang ada di array (batas bawah) jadi low  = 0, high disini sebagai index atau posisi tertinggi (batas atas), caranya menggunakan len(arr)-1 maka hasil tersebut akan menjadi high, x disini sebagai angka yang dicari dalam arrray
    if (low > high): #disini adalah Base case, kondisi dimana batas bawah lebih besar maka akan mengembalikan  program menjadi -1
        return -1
    
    mid = low + (high - low) //2 #mid yaitu posisi/index tengah untuk dipakai sebagai acuan mencari x
    if x == A[mid]: #disni juga Base case, hasil akhir dari pencarian akan berhenti disini
        return mid
    elif x < A[mid]: #Rekursif case, melakukan pemanggilan terhadap dirinya sediri, dengan posisi batas atas akan berubah
        return binarysearch(A, low, mid-1, x) 
    else: #Rekursif case, melakukan pemanggilan terhadap dirinya sediri, dengan posisi batas bawah akan  berubah
        return binarysearch(A, mid+1, high, x)

def main():
    while True:
        print("==========================================") #untuk memberi jarak dilayar output
        print("\nSelamat datang di program Binary Search\n") #untuk judul program dioutput
        arr = eval(input("Masukkan array : ")) #untuk menginput data array yang diinginkan
        arr.sort() #untuk mengurutkan array
        print("Array yang sudah diurutkan : ", arr) #menampilkan array dilayar
        cari = eval(input("Angka yang ingin dicari : ")) #untuk menginput data yang ingin dicari
    
        hasil = binarysearch(arr, 0, len(arr)-1, cari)#pemanngilan untuk fungsi binary
        if hasil != -1:#kondisi dimana hasil angka yg dicari mempunyai index atau tidak terdapat dalam array
            print("Angka terdapat dalam array di index % r" % hasil)
        else : 
            print("Angka tidak ada pada array")
        

main()#pemanngilan untuk fungsi seluruhnya