from typing import Tuple

import grpc
import requests
import base64
from io import BytesIO
from PIL import Image

def create_secure_oauth_channel(
    grpc_address: str,
    client_id: str,
    client_secret: str,
    authorization_server: str,
    audience: str | None = None,
) -> grpc.aio.Channel:
    response = requests.post(
        authorization_server,
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "audience": audience,
        },
    )
    response.raise_for_status()
    token = response.json()["access_token"]
    auth_credentials = grpc.metadata_call_credentials(
        lambda context, callback: callback(
            (("authorization", f"Bearer {token}"),),
            None,
        ) # type: ignore
    )
    composite_credentials = grpc.composite_channel_credentials(
        grpc.local_channel_credentials(),
        auth_credentials,
    )
    grpc_channel = grpc.aio.secure_channel(
        grpc_address,
        composite_credentials,
    )
    return grpc_channel



def image_to_base64_compressed(
    url: str,
    max_size: Tuple[int, int] = (800, 800),
    quality: int = 35
) -> str | None:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return None
        img = Image.open(BytesIO(response.content))
        img = img.convert("RGB")
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        buffer = BytesIO()
        img.save(
            buffer,
            format="WEBP",
            quality=quality,
            optimize=True,
            method=6
        )
        encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return f"data:image/webp;base64,{encoded}"

    except Exception as e:
        print(f"Error processing image from {url}: {e}")
        return None