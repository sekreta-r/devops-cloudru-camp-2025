from dataclasses import dataclass
import os
import socket
import logging
from typing import Optional

logger = logging.getLogger(__name__)

@dataclass
class HostInfo:
    hostname: str
    ip_address: str
    author: str

    _instance: Optional["HostInfo"] = None
    
    @classmethod
    def from_env(cls) -> "HostInfo":
        if cls._instance is None:
            try:
                hostname = socket.gethostname()
                ip_address = socket.gethostbyname(hostname)
                author = os.getenv("AUTHOR", "Unknown Author")

                cls._instance = cls(
                    hostname=hostname,
                    ip_address=ip_address,
                    author=author
                )
            except Exception as e:
                logger.warning(f"Failed to initialize HostInfo: {e}")
                cls._instance = cls(
                    hostname="unknown-host",
                    ip_address="127.0.0.1",
                    author=os.getenv("AUTHOR", "Unknown Author")
                )

        return cls._instance
