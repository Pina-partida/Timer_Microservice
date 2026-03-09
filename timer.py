import time
from fastapi import FastAPI
import random


app = FastAPI()
timers = {}

# Test logging speed mat cause slow down
#def timed_request(duration = int):

    #timer_id = random.randint(0, 5000) try moving to post so that we can incorprate get method
    #timer_length = duration
    #start = time.perf_counter()
    #while time.perf_couter() - start < timer_length:
        #time.sleep(.01)


   # return {"status": "completed"}




@app.post("/upload-time")
async def upload_time(
    duration: int
):
    timer_id = random.randint(1000, 5555)

    timers[timer_id] = {
        "duration": duration,
        "start_time": time.perf_counter(),
        "timer_id": timer_id,
        "completed": False

    }

    return {"timer_id": timer_id, "status": "started"}
    


@app.get("/fetch-time/{timer_id}")
async def fetch_time(timer_id: int):
    timer = timers.get(timer_id)
    # if timer id not found
    if not timer:
        return {"error": "Timer not found"}
    # if id is found yes
    timer_count = time.perf_counter() - timer["start_time"]

    if timer_count >= timer["duration"]:
        timer["completed"] = True

    return {"timer_id": timer_id,"completed": timer["completed"]}
    

@app.put("/update-time/{timer_id}")
async def update_time(timer_id: int, duration: int):
    timer = timers.get(timer_id)
    # if timer id not found
    if not timer:
        return {"error": "Timer not found"}

    else:
        timer["completed"] = False
        timer["duration"] = duration
        timer["start_time"] = time.perf_counter()

    return {"timer_id": timer_id, "status": "updated"}


