# https://www.blog.pythonlibrary.org/2016/08/03/python-3-concurrency-the-concurrent-futures-module/
#
import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping for {seconds} second(s)...")
    time.sleep(seconds)
    return  f'Done Sleeping in {seconds}...'

with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 2)
    # f2 = executor.submit(do_something, 2)
    # print(f1.result())
    # print(f2.result())
    secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    results = executor.map(do_something, secs)
    for result in results:
        print(result)

# threads = []
# for i in range(0,10):
#     t = threading.Thread(target=do_something, args=[2])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()

finish = time.perf_counter()
time_elapsed = round(finish - start)

print("Finished in", str(time_elapsed), "second(s)")
