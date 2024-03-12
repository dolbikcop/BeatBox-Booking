from fastapi import FastAPI


app = FastAPI(title="TochkaReservation", version="0.0.1")


@app.on_event("startup")
async def startup():
    # Include routers
    # app.include_router(...)
    print("hello, world!")
