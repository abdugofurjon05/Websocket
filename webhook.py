from fastapi import FastAPI, Request


app = FastAPI()

@app.post("/webhook")
async def payment_webhook(request: Request):
    data = await request.json()
    print(f"Received webhook data: {data}")
    user_id = data["user_id"]
    status = data["status"]
    amount = data["amount"]

    if status == "paid":
        print(f"User {user_id} has paid {amount}.")

    return {"received": True}



