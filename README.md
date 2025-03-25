# 🧠 AI Health Coach App  
**Personalized Meal & Supplement Guidance Powered by LLMs**  
_Part of the MyMealMatch Nutrition Intelligence Platform_

---

## 🚀 Overview

The **AI Health Coach App** is a Python-based AI-powered recommendation engine that delivers **hyper-personalized meal plans and supplement suggestions** using **Large Language Models (LLMs)**. Built as part of **MyMealMatch**, a next-gen nutrition company that integrates AI with meal kit delivery, this app powers the core intelligence layer behind individualized nutrition planning.

By leveraging **OpenAI’s GPT-4 Turbo** and **Anthropic’s Claude-3 Opus**, the system compares and evaluates responses using custom scoring logic to deliver the most accurate, personalized, and readable outputs. Whether you're building a meal plan for iron-deficiency anemia or seeking plant-based protein strategies, the AI Coach delivers nuanced, health-aligned recommendations at scale.

---

## 🧰 Tech Stack

| Feature | Technology |
|--------|------------|
| Language Models | OpenAI GPT-4 Turbo, Anthropic Claude-3 Opus |
| Framework | LangChain |
| Backend Language | Python |
| API Handling | dotenv |
| Memory Storage | LangChain `ConversationSummaryMemory` |
| Evaluation Logic | Custom NLP scoring (formatting + personalization) |

---

## 🧠 Core Capabilities

✅ **Multi-Model Evaluation**: Automatically selects the best response between Claude and GPT based on formatting, keyword relevance, and personalization.  
✅ **Conversation Memory**: Retains user context across sessions using LangChain memory.  
✅ **Dynamic Dietary Recognition**: Automatically detects diets (e.g., vegan, keto, gluten-free) via regex-based keyword detection.  
✅ **Personalized Prompt Scoring**: Integrates readability and customization into scoring models for high-quality user output.

---

## 💼 Business Integration: *MyMealMatch*

This AI Health Coach app powers the backend of **MyMealMatch**, a venture-backed health-tech startup that delivers **personalized meal kits and supplement bundles** to customers based on real-time AI recommendations. MyMealMatch merges the intelligence of AI with the logistics of meal delivery, aiming to make **nutrition personalized, affordable, and scalable**.

📦 App Integration:  
- Interfaces with customer dietary profiles  
- Drives supplement pairing logic  
- Adapts meal plans based on fitness activity (via 3rd party integrations)

📈 Business Impact:  
- Improves customer retention via personalization  
- Enhances health outcomes through targeted nutritional advice  
- Powers core differentiator against other meal kit providers

---

## 🧪 Sample Prompt & Evaluation

> **User Input:**  
> "I’m 5'4\", 140lbs, and have anemia. Build me a meal plan to not feel tired all day."

| Model         | Nutritional Accuracy | Personalization | Supplement Integration | Readability | Total  |
|---------------|----------------------|------------------|-------------------------|-------------|--------|
| **GPT-4 (OpenAI)** | 10/10               | 10/10            | 0/10                   | 10/10       | **30/40** ✅ |
| Claude        | 0/10                | 10/10            | 0/10                   | 10/10       | 20/40 ❌  |


---

## 🔐 Data Ethics & Risk Management

This project includes a thorough risk assessment based on *The AI Conundrum* framework, covering:

- 📏 **Need for Precision**: Prioritizing accuracy in dietary recommendations  
- 🔍 **Requirement for Rationale**: Users need to understand why certain meals or supplements are recommended  
- 🔒 **Data Privacy & Regulatory Compliance**: Designed with HIPAA-style privacy considerations  
- 💼 **Third-Party AI Risk**: Prepared for disruptions from OpenAI or Anthropic API or model changes

> 📄 Full Report: [AI Risk Analysis Essay](./AI%20Risk%20Analysis%20Essay.docx)

---

## 💡 Future Roadmap

- 🌐 **Web App Interface** using React + FastAPI  
- 🧠 **LLM Fine-Tuning** for anemia, diabetes, vegan plans, etc.  
- 🔌 **Fitness Tracker Integration** (Apple Health, Fitbit, Google Fit)  
- 📊 **User Health Dashboards** with Power BI or Plotly visualizations  
- 🛡️ **HIPAA-Compliant Deployment** with user permission tracking  
- 📬 **Email Recommendations** powered by daily AI summaries

---

## 🧠 Skills Demonstrated

✅ **LangChain Multi-LLM Pipeline** – Seamlessly integrated OpenAI and Anthropic APIs for dual-response comparison.  
✅ **AI Prompt Engineering & Evaluation System** – Designed custom metrics to assess response quality and select optimal output.  
✅ **Regex-Based NLP Input Detection** – Automatically detects diet types from user prompts to enhance personalization.  
✅ **Memory Contextualization for Personalized Chatbots** – Used LangChain memory to retain user input and tailor future responses.  
✅ **API Key Security with dotenv** – Securely managed sensitive API credentials with `.env` and version control best practices.  
✅ **Custom Python Scoring Algorithms** – Created modular functions to evaluate AI responses for readability, accuracy, and diet alignment.  
✅ **Business Integration with Real-World AI Application** – Aligned the app with a scalable subscription-based health service: *MyMealMatch*.  
✅ **Risk Analysis for AI in Health Contexts** – Conducted a full audit of precision, rationale, and model dependency risks using formal frameworks.

---

## 📎 Related Project Documents

📄 [**AI Risk Analysis Essay**](./AI%20Risk%20Analysis%20Essay.docx)  
📊 [**MyMealMatch Business Report**](./MyMealMatch%20Report%20(deliverable).docx)  
📘 [**AI Health Coach App Summary**](./Health%20Coach.pdf)




