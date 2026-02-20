class ConversationMemory:
    def __init__(self, max_messages=6):
        self.history = []
        self.max_messages = max_messages

    def add_user_message(self, message: str):
        self.history.append({"role": "user", "content": message})
        self._trim_history()

    def add_bot_message(self, message: str):
        self.history.append({"role": "assistant", "content": message})
        self._trim_history()

    def _trim_history(self):
        """
        Keep only last N messages to optimize token usage
        """
        if len(self.history) > self.max_messages:
            self.history = self.history[-self.max_messages:]

    def get_conversation(self) -> str:
        conversation_text = ""
        for msg in self.history:
            if msg["role"] == "user":
                conversation_text += f"User: {msg['content']}\n"
            else:
                conversation_text += f"Assistant: {msg['content']}\n"
        return conversation_text

    def clear(self):
        self.history = []