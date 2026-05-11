import asyncio
from typing import Any, Dict
from utils import create_secure_oauth_channel
from pyzeebe import  ZeebeWorker
from  database_mock import DatabaseMock

async def run():
    grpc_addr = "localhost:26500"
    channel = create_secure_oauth_channel(
        grpc_address=grpc_addr,
        client_id="orchestration",
        client_secret="secret",
        audience="orchestration-api",
        authorization_server=r"http://localhost:18080/auth/realms/camunda-platform/protocol/openid-connect/token"
    )
    worker = ZeebeWorker(channel)
    database_mock = DatabaseMock()

    @worker.task(task_type="is_available")
    async def is_model_available(recommended_model_id: str) -> Dict[str, Any]: # pyright: ignore[reportUnusedFunction]
        print(f"Rcv: {recommended_model_id}")
        car = database_mock.get_car_by_model_id(recommended_model_id)
        if car == None:
            return {"is_available": False, "car": None}
        return {"is_available": True, "car": car.to_dict()}

    print("Worker start")
    await worker.work()


if __name__ == "__main__":
    asyncio.run(run())