import time
st=time.perf_counter()
import threading
src=r" ---Source Path--- "
destination=r" ---Destination Path---"
thread=2

with open(src, "rb") as f:
    try:
        f.seek(0,2)
        file_size=f.tell()
    except FileNotFoundError:
        print("File not found!!")
    except PermissionError:
        print("Permission denied!!")
    except OSError:
        print("OS error!!")
    except Exception as error:
        print(error)
def threat(start_,size):
    try:
        with open(src, "rb") as f:
            with open(destination,"rb+") as g:
                f.seek(start_)
                g.seek(start_)
                chunk=size

                while chunk>0:
                    packet=f.read(min(2048*2048,chunk))
                    if not packet:
                        break
                    g.write(packet)
                    chunk=chunk-len(packet)
    except FileNotFoundError:
        print("File not found!!")
    except PermissionError:
        print("Permission denied!!")
    except OSError:
        print("OS error!!")
    except Exception as error:
        print(error)
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

