import asyncio

from pyzeebe import ZeebeClient
from utils import create_secure_oauth_channel


async def run():
    grpc_addr = "localhost:26500"

    channel = create_secure_oauth_channel(
        grpc_address=grpc_addr,
        client_id="orchestration",
        client_secret="secret",
        audience="orchestration-api",
        authorization_server="http://localhost:18080/auth/realms/camunda-platform/protocol/openid-connect/token"
    )

    client = ZeebeClient(channel)

    print("Publishing - odebranie zaliczki...")

    await client.publish_message(
        name="odebranie zaliczki",
        correlation_key="odebranie_zaliczki_ck",
        variables={
            "down_payment_amount": 5000,
            "payment_method": "bank_transfer"
        }
    )

    print("Message published")


if __name__ == "__main__":
    asyncio.run(run())