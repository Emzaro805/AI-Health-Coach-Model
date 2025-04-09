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

env_path = os.path.join(os.path.dirname(__file__), "Keys/.env")

load_dotenv(env_path)



# Retrieve API keys

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")



if not OPENAI_API_KEY or not CLAUDE_API_KEY:

    raise ValueError("⚠️ ERROR: Missing API keys! Ensure 'keys/.env' contains both OpenAI and Anthropic keys.")



# Initialize LangChain models for OpenAI (ChatGPT) & Claude (Anthropic)

openai_model = ChatOpenAI(model_name="gpt-4-turbo", openai_api_key=OPENAI_API_KEY)

claude_model = ChatAnthropic(model="claude-3-opus-20240229", anthropic_api_key=CLAUDE_API_KEY)


# Memory to track conversation history

memory = ConversationSummaryMemory(

    llm=openai_model, 

    prompt=PromptTemplate(input_variables=["new_lines", "summary"], template="{summary}\n{new_lines}"),

    memory_key="history"

)   


import re

# List of diet types to detect

DIET_KEYWORDS = ["vegan", "vegetarian", "keto", "paleo", "gluten-free", "dairy-free", "low-carb", "high-protein", "Mediterranean"]



def detect_diet(user_input):

    """Detects a dietary preference from user input based on known diet keywords."""

    for diet in DIET_KEYWORDS:

        if re.search(rf"\b{diet}\b", user_input, re.IGNORECASE):  # Looks for whole word match

            return diet.lower()

    return "general"  # Default if no diet is mentioned



def evaluate_formatting(response_text):

    """Assigns a formatting score based on readability factors like structure, bullet points, and clarity."""

    score = 0

    if response_text.count("\n") > 3:

        score += 2

    if re.search(r"[-•*]\s", response_text) or re.search(r"\d+\.\s", response_text):

        score += 2

    if re.search(r"##?\s[A-Za-z0-9]", response_text):

        score += 2

    if "|" in response_text and "-" in response_text:

        score += 3

    if re.search(r"[,;:\-]\S", response_text):

        score -= 1

    if len(response_text) > 800:

        score -= 2

    return max(score, 1)



def evaluate_customization(response_text, diet_type):

    """Checks if the response correctly references the requested diet type."""

    score = 5  

    # Penalize if diet type is not mentioned

    if diet_type.lower() not in response_text.lower():

        score -= 2  

    return max(score, 1)



def chat_with_ai(user_input):

    """Queries OpenAI and Claude, selects the best response based on accuracy & formatting."""

    # Detect dietary preference

    diet_type = detect_diet(user_input)

    # Get responses

    openai_response = openai_model.invoke(user_input)

    claude_response = claude_model.invoke(user_input)


    openai_text = openai_response.content if hasattr(openai_response, "content") else str(openai_response)

    claude_text = claude_response.content if hasattr(claude_response, "content") else str(claude_response)


    # Evaluate customization (accuracy to diet)

    openai_customization_score = evaluate_customization(openai_text, diet_type)

    claude_customization_score = evaluate_customization(claude_text, diet_type)


    # Evaluate formatting

    openai_format_score = evaluate_formatting(openai_text)

    claude_format_score = evaluate_formatting(claude_text)


    # Final score (equal weight)

    openai_final_score = openai_customization_score + openai_format_score

    claude_final_score = claude_customization_score + claude_format_score


    # Select the best response

    best_response = openai_text if openai_final_score > claude_final_score else claude_text


    # Display the scores for both OpenAI and Claude

    print(f"\n📊 OpenAI Scores (Customization: {openai_customization_score}, Formatting: {openai_format_score}, Final: {openai_final_score})")

    print(f"\n📊 Claude Scores (Customization: {claude_customization_score}, Formatting: {claude_format_score}, Final: {claude_final_score})\n")


    # Save conversation

    memory.save_context({"input": f"{user_input} (Diet: {diet_type})"}, {"output": best_response})


    return f"\n🤖 AI Coach (Diet: {diet_type.capitalize()}):\n{best_response}"







if __name__ == "__main__":

    print("""👋 Welcome to MyMealMatch! Your Personalized Path to Healthy Eating Starts Here!  

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

            print("\nGoodbye! Stay healthy! 🏋️‍♂️🥗")

            break



        response = chat_with_ai(user_input)

        print(response)



