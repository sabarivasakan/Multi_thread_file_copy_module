import time
st=time.perf_counter()
import threading
src=r"C:\Users\K.SABARI VASAKAN\Downloads\ubuntu-24.04.4-desktop-amd64.iso"
destination=r"C:\Users\K.SABARI VASAKAN\PyCharmMiscProject\test\test2.iso"
thread=2

with open(src, "rb") as f:
    f.seek(0,2)
    file_size=f.tell()
def threat(start_,size):
    with open(src, "rb") as f:
        with open(destination,"rb+") as g:
            f.seek(start_)
            g.seek(start_)
            chunk=size

            while chunk>0:
                packet=f.read(min(4096,chunk))
                if not packet:
                    break
                g.write(packet)
                chunk=chunk-len(packet)


unit_size=file_size//thread
th=[]
for i in range(thread):
    part_size=i*unit_size
    if i==thread-1:
        size=file_size-part_size
    else:
        size=unit_size
    t=threading.Thread(target=threat,args=(part_size,size))
    t.start()
    th.append(t)

for t in th:
    t.join()
ed=time.perf_counter()
print("Completed....")
print(ed-st)

