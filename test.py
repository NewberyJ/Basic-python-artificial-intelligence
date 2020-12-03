import time
import multiprocessing

def sleep_for_a_bit(seconds):
    print(f"sleeping {seconds} second(s)")
    time.sleep(seconds)
    print("Done sleeping")


p1 = multiprocessing.Process(target=sleep_for_a_bit, args=[1])

if __name__ == '__main__':
    p1.start()

finish = time.perf_counter()
print("finished")