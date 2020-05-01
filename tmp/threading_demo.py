import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping for {seconds} second(s)...")
    time.sleep(seconds)
    print("Done Sleeping...")


# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

threads = []
for i in range(0,10):
    t = threading.Thread(target=do_something, args=[2])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
time_elapsed = round(finish - start)

print("Finished in", str(time_elapsed), "second(s)")

# cpu bound - multiprocessing
#   - data crunching
#   - a

# i/o bound - threading suitable for this kind of operation
#   - disk / filesystem
#   - network
#
