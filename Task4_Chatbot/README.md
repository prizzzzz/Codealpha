# Task 4: Chatbot

An interactive chatbot with pattern matching and context awareness.

## 🤖 Features

- **Pattern Matching**: Uses regex to understand user input
- **Context Awareness**: Remembers user's name and conversation count
- **Multiple Topics**: Handles greetings, questions, programming topics, math, time/date
- **Randomized Responses**: Varied responses for better conversation flow
- **Error Handling**: Graceful handling of interruptions and errors
- **Help System**: Built-in help command

## 💬 Capabilities

- Greetings and casual conversation
- Name recognition and personalization
- Python/programming discussions
- Basic math calculations (+, -, *, /)
- Time and date information
- Question handling
- Polite goodbyes

## 🚀 How to Run

```bash
cd Task4_Chatbot
python chatbot.py
```

## 📝 Example Interactions

```
WELCOME TO CODEALPHA BOT! 🤖
======================================================================

Hi! I'm CodeAlpha Bot. I'm here to chat with you.
Type 'help' to see what I can do, or just start chatting!
Type 'bye' to exit the chat.
======================================================================

You: Hello
Bot: Hi! 👋 How can I help you today?

You: My name is Alice
Bot: Nice to meet you, Alice! 😊 I'm CodeAlpha Bot. How can I help you today?

You: What is 5 + 3?
Bot: 🧮 5 + 3 = 8

You: What time is it?
Bot: Current date and time: 2024-01-15 14:30:45 🕐

You: Tell me about Python
Bot: Python is a great programming language! 🐍 It's known for its simplicity and readability. Are you learning Python?

You: Bye
Bot: Goodbye, Alice! 👋 It was nice chatting with you. Have a great day!

Chat ended, Alice. Thank you for using CodeAlpha Bot!
Total messages exchanged: 5
```

## 🎯 Supported Commands

- **Greetings**: hello, hi, hey, howdy, greetings
- **Name**: "My name is [name]", "I am [name]", "I'm [name]"
- **Questions**: "What is your name?", "Who are you?"
- **Math**: "5 + 3", "10 - 2", "4 * 5", "20 / 4"
- **Time**: "What time is it?", "What date is it?"
- **Help**: "help", "what can you do"
- **Goodbye**: bye, goodbye, exit, quit

## 🔧 Requirements

- Python 3.6+
- Standard library only (uses `re`, `random`, `datetime`)

## 📦 Files

- `chatbot.py` - Main chatbot file
- `README.md` - This documentation

## 💡 Code Features

- Clean, well-documented code
- Pattern matching with regex
- Context tracking (name, conversation count)
- Randomized responses for variety
- Error handling and graceful exits
- Follows Python PEP 8 style guidelines

## 🧠 How It Works

1. **Input Processing**: Converts user input to lowercase and strips whitespace
2. **Pattern Matching**: Uses regex patterns to identify user intent
3. **Context Management**: Tracks user name and conversation count
4. **Response Generation**: Selects appropriate response based on patterns
5. **Randomization**: Randomly selects from multiple response options for variety
