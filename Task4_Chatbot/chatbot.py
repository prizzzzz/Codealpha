"""
================================================================================
TASK 4: CHATBOT
================================================================================
An interactive chatbot with pattern matching and context awareness.
================================================================================
"""

import random
import re

# Conversation context
conversation_context = {
    "user_name": None,
    "conversation_count": 0
}

def get_bot_response(user_input):
    """Enhanced chatbot response based on user input with pattern matching"""
    
    user_input_lower = user_input.lower().strip()
    original_input = user_input.strip()
    
    # Update conversation count
    conversation_context["conversation_count"] += 1
    
    # Greeting responses
    if re.search(r'\b(hello|hi|hey|howdy|greetings|good morning|good afternoon|good evening)\b', user_input_lower):
        greetings = [
            "Hi! 👋 How can I help you today?",
            "Hello there! 😊 What can I do for you?",
            "Hey! Nice to see you! How can I assist you?",
            "Hi! Great to meet you! What would you like to know?"
        ]
        return random.choice(greetings)
    
    # Name extraction and responses
    name_match = re.search(r'\b(?:my name is|i am|i\'m|call me|name\'s)\s+([a-z]+)', user_input_lower)
    if name_match:
        name = name_match.group(1).capitalize()
        conversation_context["user_name"] = name
        return f"Nice to meet you, {name}! 😊 I'm CodeAlpha Bot. How can I help you today?"
    
    if re.search(r'\b(what is your name|who are you|what\'s your name|tell me about yourself)\b', user_input_lower):
        return "I'm CodeAlpha Bot! 🤖 I'm here to chat and help you with various topics. What would you like to talk about?"
    
    # How are you responses
    if re.search(r'\b(how are you|how\'re you|how u doing|how are things|how\'s it going)\b', user_input_lower):
        responses = [
            "I'm doing great, thanks for asking! 😊 How are you?",
            "I'm fantastic! Thanks! How about you?",
            "I'm doing well! Hope you're having a great day too! 😊"
        ]
        name_part = f", {conversation_context['user_name']}" if conversation_context["user_name"] else ""
        return random.choice(responses).replace("you", f"you{name_part}")
    
    # Help responses
    if re.search(r'\b(help|what can you do|what do you do|capabilities|features)\b', user_input_lower):
        help_text = "I can chat with you about various topics! Here's what I can do:\n"
        help_text += "  • Answer questions about myself\n"
        help_text += "  • Have casual conversations\n"
        help_text += "  • Tell you about programming and Python\n"
        help_text += "  • Provide information and assistance\n"
        help_text += "\nTry asking: 'hello', 'how are you', 'what is your name', 'tell me about Python', or 'bye'"
        return help_text
    
    # Thank you responses
    if re.search(r'\b(thanks|thank you|appreciate it|thx)\b', user_input_lower):
        responses = [
            "You're welcome! 😊 Is there anything else I can help you with?",
            "Happy to help! 😊 Anything else?",
            "My pleasure! Feel free to ask if you need anything else!"
        ]
        return random.choice(responses)
    
    # Python/programming related
    if re.search(r'\b(python|programming|code|coding|developer|software)\b', user_input_lower):
        responses = [
            "Python is a great programming language! 🐍 It's known for its simplicity and readability. Are you learning Python?",
            "Programming is awesome! Python is one of the most popular languages. What would you like to know about it?",
            "I love talking about programming! Python is versatile and beginner-friendly. What interests you about it?"
        ]
        return random.choice(responses)
    
    # Weather (simple response)
    if re.search(r'\b(weather|temperature|rain|sunny|cloudy)\b', user_input_lower):
        return "I don't have access to real-time weather data, but I hope you're having a great day! ☀️"
    
    # Time/date
    if re.search(r'\b(time|date|what time|what date|clock)\b', user_input_lower):
        from datetime import datetime
        now = datetime.now()
        return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')} 🕐"
    
    # Math questions (simple)
    math_match = re.search(r'(\d+)\s*([+\-*/])\s*(\d+)', user_input)
    if math_match:
        try:
            num1 = int(math_match.group(1))
            operator = math_match.group(2)
            num2 = int(math_match.group(3))
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    return "❌ Division by zero is not allowed!"
                result = num1 / num2
            else:
                return "I can help with basic math (+, -, *, /). Try asking something like '5 + 3'"
            
            return f"🧮 {num1} {operator} {num2} = {result}"
        except:
            pass
    
    # Goodbye responses
    if re.search(r'\b(bye|goodbye|see you|farewell|exit|quit|see ya|later)\b', user_input_lower):
        name_part = f", {conversation_context['user_name']}" if conversation_context["user_name"] else ""
        responses = [
            f"Goodbye{name_part}! 👋 It was nice chatting with you. Have a great day!",
            f"See you later{name_part}! 😊 Take care!",
            f"Farewell{name_part}! 👋 Hope to chat again soon!"
        ]
        return random.choice(responses)
    
    # Questions
    if user_input_lower.endswith('?'):
        responses = [
            "That's an interesting question! I'm still learning, but I'll do my best to help.",
            "Hmm, let me think about that... Could you rephrase it?",
            "I'm not entirely sure about that. Could you provide more context?"
        ]
        return random.choice(responses)
    
    # Default response with context
    default_responses = [
        f"That's interesting! I'm not sure how to respond to that. Try typing 'help' to see what I can do.",
        f"I'm still learning! Could you try asking something else? Type 'help' for suggestions.",
        f"Hmm, I don't have a response for that. What else would you like to talk about? Type 'help' for ideas."
    ]
    return random.choice(default_responses)

def chatbot_main():
    """Enhanced main chatbot function with conversation tracking"""
    
    print("=" * 70)
    print("WELCOME TO CODEALPHA BOT! 🤖")
    print("=" * 70)
    print("\nHi! I'm CodeAlpha Bot. I'm here to chat with you.")
    print("Type 'help' to see what I can do, or just start chatting!")
    print("Type 'bye' to exit the chat.")
    print("=" * 70)
    
    while True:
        try:
            print()
            user_input = input("You: ").strip()
            
            # Check for exit
            if not user_input:
                print("Bot: Please enter something! 😊")
                continue
            
            # Get and display bot response
            response = get_bot_response(user_input)
            print(f"\nBot: {response}")
            
            # Check if user wants to exit
            if re.search(r'\b(bye|goodbye|see you|farewell|exit|quit|see ya|later)\b', user_input.lower()):
                print("\n" + "=" * 70)
                name_part = f", {conversation_context['user_name']}" if conversation_context["user_name"] else ""
                print(f"Chat ended{name_part}. Thank you for using CodeAlpha Bot!")
                print(f"Total messages exchanged: {conversation_context['conversation_count']}")
                print("=" * 70)
                break
        
        except KeyboardInterrupt:
            print("\n\n" + "=" * 70)
            print("Chat interrupted. Thank you for using CodeAlpha Bot!")
            print("=" * 70)
            break
        except Exception as e:
            print(f"\nBot: Oops! Something went wrong: {e}")
            print("Let's continue chatting!")

if __name__ == "__main__":
    chatbot_main()
