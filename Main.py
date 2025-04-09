import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.memory import ConversationSummaryMemory
from langchain_core.prompts import PromptTemplate

"""
This script demonstrates how to use LangChain to build a conversational AI health coach that leverages two different models: ChatGPT from OpenAI and Claude from Anthropic.

pip install -r requirements.txt

To run this script, you need to set up API keys for OpenAI and Anthropic. You can obtain these keys by signing up for the respective services:

"""


# Load API keys from keys/.env (inside Health_Coach_Project)
env_path = os.path.join(os.path.dirname(__file__), "keys/.env")
load_dotenv(env_path)

# Retrieve API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

if not OPENAI_API_KEY or not CLAUDE_API_KEY:
    raise ValueError("ERROR: Missing API keys. Ensure 'keys/.env' contains both OpenAI and Anthropic keys.")

# Initialize LangChain models for OpenAI (ChatGPT) & Claude (Anthropic)
openai_model = ChatOpenAI(model_name="gpt-4-turbo", openai_api_key=OPENAI_API_KEY)
claude_model = ChatAnthropic(model="claude-3-opus-20240229", anthropic_api_key=CLAUDE_API_KEY)


# Memory to track conversation history
memory = ConversationSummaryMemory(
    llm=openai_model, 
    prompt=PromptTemplate(input_variables=["new_lines", "summary"], template="{summary}\n{new_lines}"),
    memory_key="history"
)   


def score_response(response):
    """Scores AI response based on nutritional relevance for meal & supplement planning."""
    scores = {
        "Nutritional Accuracy": 0,
        "Personalization": 0,
        "Supplement Integration": 0,
        "Readability & Clarity": 0
    }

    # Scoring logic
    if any(keyword in response.lower() for keyword in ["protein", "carbs", "fats", "macronutrients"]):
        scores["Nutritional Accuracy"] += 10

    if any(keyword in response.lower() for keyword in ["custom", "personalized", "goal", "dietary needs"]):
        scores["Personalization"] += 10

    if any(keyword in response.lower() for keyword in ["creatine", "whey", "omega-3", "multivitamin"]):
        scores["Supplement Integration"] += 10

    if len(response.split()) > 30:  # Checks if it's a well-explained response
        scores["Readability & Clarity"] += 10

    return sum(scores.values()), scores

def save_to_file(user_input, response, model_used):
    """Saves conversation to a text file."""
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"\nUser: {user_input}\n")
        file.write(f"Best Model: {model_used}\n")
        file.write(f"AI Response:\n{response}\n")
        file.write("="*50 + "\n")  # Separator for readability


def chat_with_ai(user_input):
    """Queries both ChatGPT (OpenAI) and Claude (Anthropic) and selects the best response based on score."""
    
    openai_response = openai_model.invoke(user_input).content
    claude_response = claude_model.invoke(user_input).content

    # Score responses
    openai_score, openai_breakdown = score_response(openai_response)
    claude_score, claude_breakdown = score_response(claude_response)

    # Select the best response based on highest score
    best_response = openai_response if openai_score > claude_score else claude_response
    best_model = "ChatGPT (OpenAI)" if openai_score > claude_score else "Claude (Anthropic)"

    # Print Score Comparisons
    print("\n🔹 **ChatGPT (OpenAI) Score:**", openai_score, "/ 40", openai_breakdown)
    print("🔹 **Claude (Anthropic) Score:**", claude_score, "/ 40", claude_breakdown)
    print("\n✅ **Best Model for This Query:**", best_model)

    # Save conversation in memory
    memory.save_context({"input": user_input}, {"output": best_response})

    # Save to file
    save_to_file(user_input, best_response, best_model)

    return best_response



if __name__ == "__main__":
    print("""
👋 Welcome to MyMealMatch! Your Personalized Path to Healthy Eating Starts Here!  

Maintaining a balanced diet has never been easier! At MyMealMatch, we tailor meal plans and supplements to your unique health goals, dietary needs, and lifestyle**—so you can enjoy nutritious, delicious meals without the hassle of meal planning or grocery shopping.  

✨ Here’s how it works:  
✅ Personalized meal & supplement recommendations based on your preferences  
✅ Seamless integration with fitness & health apps for real-time adjustments  
✅ Flexible subscriptions—adjust, pause, or swap meals anytime  
✅ Eco-friendly packaging & portion-controlled servings** for sustainability  

💡 Let’s get started! Tell us about your health goals & food preferences, and we’ll craft your perfect meal plan! 🍽️🚀  

Would you like a step-by-step guide or jump straight into building your first meal plan? 😊
""")
    
    while True:
        user_input = input("\nUser: ")
        if user_input.lower() == "exit":
            print("\nGoodbye! Stay healthy! ")
            break
        
        response = chat_with_ai(user_input)
        print("\n AI Coach:", response)
