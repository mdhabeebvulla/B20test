from fastapi import FastAPI
app = FastAPI()
samples =[
{"stid":"1001",
"stname":"peter"
},
{"stid":"1002",
"stname":"John"
}
]

@app.get("/",tags=["Habeeb"])
def example():
    return'hello'
@app.get("/sample",tags=["Sample Data"])
def example_data():
    return {'Data':samples}
@app.post("/sample",tags=["Sample Data"])
def add_data(sample:dict):
    samples.append(sample)
    return {'sample':"sample added "}  
#GET --> read todo
#Post ----> create todo
#put ---> update todo
@app.put("/sample/{stid}",tags=["Sample Data"])
def put_data(stid:int,body:dict):
    for s in samples:
        if int((s['stid'])) == stid:
            s['stname'] = body['stname']
    return {"data":"updated"}
    
    
    return {"sample":"sample added "} 
#delete -----> delete todo
@app.delete("/sample/{stid}",tags=["Sample Data"])
def del_data(stid:int):
    for s in samples:
        if int((s['stid'])) == stid:
            samples.remove(s)
    return {"data":f"samples with stid {stid} removed"}