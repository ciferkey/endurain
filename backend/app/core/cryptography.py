import os
from cryptography.fernet import Fernet
from fastapi import HTTPException, status

import core.logger as core_logger


def create_fernet_cipher():
    try:
        # Get the key from environment variable and encode it to bytes
        key = os.environ["FERNET_KEY"].encode()
        return Fernet(key)
    except Exception as err:
        # Log the exception
        core_logger.print_to_log(
            f"Error in encrypt_token_fernet: {err}", "error", exc=err
        )

        # Raise an HTTPException with a 500 Internal Server Error status code
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        ) from err


def encrypt_token_fernet(token) -> str | None:
    try:
        if token is None:
            # If the token is None, return None
            return None

        # Create a Fernet cipher
        cipher = create_fernet_cipher()

        # Convert to string if token is not already a string
        if not isinstance(token, str):
            token = str(token)

        # Encrypt the token
        return cipher.encrypt(token.encode()).decode()
    except Exception as err:
        # Log the exception
        core_logger.print_to_log(
            f"Error in encrypt_token_fernet: {err}", "error", exc=err
        )

        # Raise an HTTPException with a 500 Internal Server Error status code
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        ) from err


def decrypt_token_fernet(encrypted_token) -> str | None:
    try:
        if encrypted_token is None:
            # If the encrypted token is None, return None
            return None

        # Create a Fernet cipher
        cipher = create_fernet_cipher()

        # Decrypt the token
        return cipher.decrypt(encrypted_token.encode()).decode()
    except Exception as err:
        # Log the exception
        core_logger.print_to_log(
            f"Error in decrypt_token_fernet: {err}", "error", exc=err
        )

        # Raise an HTTPException with a 500 Internal Server Error status code
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        ) from err
