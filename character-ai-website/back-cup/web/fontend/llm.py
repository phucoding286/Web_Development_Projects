import asyncio
from characterai import aiocai
import threading

default_id = "YntB_ZeqRq2l_aVf2gWDCZl4oBttQzDvhj9cXafWcF8"
default_token = "d8a092f270dfc8baa0a2aa9a273b1aec398f7af3"

class CharacterAI:
    def __init__(self, char_id: str, token_account: str):
        self.char_id = char_id
        self.token_account = token_account
        self.output = None
        self.input = None
        self.check_in = self.input
        self.check_out = self.output
        self.event_loop = asyncio.new_event_loop()
        threading.Thread(target=self.run_main, daemon=True).start()

    def check_input(self):
        if self.input != self.check_in:
            self.check_in = self.input
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
        char = self.char_id
        client = aiocai.Client(self.token_account)
        me = await client.get_me()
        
        chat = await client.connect()
        new, answer = await chat.new_chat(char, me.id)

        # print(f'{answer.name}: {answer.text}')
        # print("Đang lắng nghe...")

        while True:
            if self.check_input():
                text = self.input
            else:
                continue
            
            message = await chat.send_message(char, new.chat_id, text)
            self.output = message.text

    def run_main(self):
        asyncio.set_event_loop(self.event_loop)
        self.event_loop.run_until_complete(self.main())
    
    def send_message(self, inp):
        self.input = inp
        while True:
            if self.check_output():
                break
        return self.output