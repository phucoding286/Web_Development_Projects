import asyncio
from characterai import aiocai
import threading

default_id = "YntB_ZeqRq2l_aVf2gWDCZl4oBttQzDvhj9cXafWcF8"
default_token = "d8a092f270dfc8baa0a2aa9a273b1aec398f7af3"

class CharacterAI:
    def __init__(self, token_account: str, char_id: str):
        self.char_id = char_id
        self.token_account = token_account
        self.output = None
        self.input = None
        self.error = False
        self.send_msg_chk = False
        self.check_in = self.input
        self.check_out = self.output
        self.event_loop = asyncio.new_event_loop()
        threading.Thread(target=self.run_main, daemon=True).start()

    def check_input(self):
        if self.send_msg_chk:
            self.check_in = self.input
            self.send_msg_chk = False
            return True
        else:
            return False
    
    def check_output(self):
        if self.output != self.check_out:
            self.check_out = self.output
            return True
        else:
            return False
    
    async def main(self):
        while True:
            try:

                char = self.char_id
                client = aiocai.Client(self.token_account)
                me = await client.get_me()
                chat = await client.connect()
                new, answer = await chat.new_chat(char, me.id)

                while True:
                    if self.error == True:
                        text = self.input
                        message = await chat.send_message(char, new.chat_id, text)
                        self.output = message.text
                        self.error = False

                    if self.check_input():
                        text = self.input
                        message = await chat.send_message(char, new.chat_id, text)
                        self.output = message.text

                    else:
                        await asyncio.sleep(0.5)
                        continue
            
            except:
                await asyncio.sleep(0.5)
                print("had error will reconnect again")
                self.error = True
                continue

    def run_main(self):
        asyncio.set_event_loop(self.event_loop)
        self.event_loop.run_until_complete(self.main())
    
    def send_message(self, inp):
        self.input = inp
        self.send_msg_chk = True
        while True:
            if self.check_output():
                break
        return self.output