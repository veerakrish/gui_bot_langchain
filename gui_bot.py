import tkinter as tk
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

templete = """
Answer the question below.
Here is the conversation history: {context}
Question: {question}
Answer:
"""

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("AI Chatbot")

        self.textbox = tk.Text(self.window, height=15, width=60)
        self.entry = tk.Entry(self.window, width=50)

        self.textbox.grid(row=0, column=0, rowspan=3, padx=(20, 20), pady=(10, 0))
        self.entry.grid(row=3, column=0, pady=(10, 0))

        self.chatbot_button = tk.Button(self.window, text="Chat", command=self.handle_chatbot)
        self.exit_button = tk.Button(self.window, text="Exit", command=self.window.destroy)

        self.chatbot_button.grid(row=4, column=0, pady=(10, 20))
        self.exit_button.grid(row=5, column=0, pady=(10, 20))

        self.window.mainloop()

    def handle_chatbot(self):
        context = self.textbox.get("1.0", tk.END).strip()
        user_input = self.entry.get().strip()
        self.entry.delete(0,tk.END)

        if user_input == "exit":
            return

        model = OllamaLLM(model="llama3.2")
        prompt = ChatPromptTemplate.from_template(templete)
        chain = prompt | model
        result = chain.invoke({'context':context,'question':user_input})

        self.textbox.insert(tk.END, f"\n User: {user_input}\nAI: {result}")
        self.textbox.see("end")

if __name__ == "__main__":
    app = GUI()