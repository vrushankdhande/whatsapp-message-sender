"""
WhatsApp Auto Message Sender using PyWhatKit

Features:
- Sends WhatsApp messages automatically
- Clean and production-ready structure
- Error handling included
- Easy configuration
- Suitable for GitHub projects

Requirements:
    pip install pywhatkit

Important:
- WhatsApp Web must already be logged in
- Internet connection is required
- The browser will open automatically
"""

import time
import pywhatkit
from datetime import datetime


class WhatsAppSender:
    def __init__(self, phone_number: str):
        """
        Initialize WhatsApp sender.

        Args:
            phone_number (str): Receiver phone number with country code
                                Example: +919876543210
        """
        self.phone_number = phone_number

    def send_message(
        self,
        message: str,
        wait_time: int = 15,
        close_tab: bool = True,
        close_time: int = 3,
    ):
        """
        Send WhatsApp message instantly.

        Args:
            message (str): Message text
            wait_time (int): Time to wait before sending
            close_tab (bool): Close browser tab after sending
            close_time (int): Seconds before tab closes
        """

        try:
            print("\n====================================")
            print(" WhatsApp Message Sender Started")
            print("====================================")

            print(f"Recipient : {self.phone_number}")
            print(f"Message   : {message}")
            print(f"Time      : {datetime.now()}")

            print("\nOpening WhatsApp Web...")
            time.sleep(2)

            pywhatkit.sendwhatmsg_instantly(
                phone_no=self.phone_number,
                message=message,
                wait_time=wait_time,
                tab_close=close_tab,
                close_time=close_time,
            )

            print("\n✅ Message sent successfully!")

        except Exception as error:
            print("\n❌ Failed to send message")
            print(f"Error: {error}")


# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":

    PHONE_NUMBER = "+918977707204"

    MESSAGE = """
Hello Vrushank!

This is an automated WhatsApp message sent using Python 🚀

Regards,
AI Automation Bot
"""

    sender = WhatsAppSender(PHONE_NUMBER)

    sender.send_message(
        message=MESSAGE,
        wait_time=15,
        close_tab=True,
        close_time=3,
    )
