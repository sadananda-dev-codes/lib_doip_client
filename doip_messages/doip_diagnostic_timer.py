import asyncio
import time

def sadananda_maharaj(*args):
    time.sleep(3.9)
    print('time inside sadananda ', time.perf_counter())

class TesterPresent:

    def __init__(self,
                 call_back,
                 call_back_periodicity,
                 *call_back_param):

        self._task = False
        self._start_stop = False
        self._call_back = call_back
        self._call_back_param = call_back_param
        self._call_back_periodicity = call_back_periodicity

    async def _job(self):
        while True:
            if self._start_stop:
                _call_back_start_time = time.perf_counter()
                self._call_back(self._call_back_param)
                _call_back_end_time = time.perf_counter()
                _sleep_time = self._call_back_periodicity - (_call_back_end_time - _call_back_start_time)
                if _sleep_time > self._call_back_periodicity:
                    _sleep_time = 0
                await asyncio.sleep(_sleep_time)

    def start(self):
        if not self._start_stop:
            self._start_stop = True
            loop = asyncio.get_running_loop()
            self._task = loop.create_task(self._job())

    def stop(self):
        self._start_stop = False
        self._task.cancel()

t_p = TesterPresent(sadananda_maharaj,
                    (32, 85),
                    2)

async def main():
    t_p = TesterPresent(sadananda_maharaj, 5, (32, 85))
    t_p.start()
    await asyncio.sleep(15)
    t_p.stop()

asyncio.run(main())

