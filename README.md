# 🛍️ Agentic Retail Intelligence

An AI-powered retail assistant that simulates two real-world roles:

- **Personal Shopper (Revenue Agent)** → Recommends products based on user preferences  
- **Customer Support Assistant (Operations Agent)** → Handles return eligibility using policy rules  

This project demonstrates a **tool-based AI agent system** where the model does not guess answers but instead calls structured functions to make accurate decisions.

---

## 🚀 Features

### 🛍️ Personal Shopper
- Understands user requirements (price, size, style, tags)
- Checks **stock availability**
- Prioritizes **sale items**
- Considers **bestseller popularity**
- Returns **top recommendations with reasoning**

---

### 📦 Customer Support Assistant
- Fetches order details
- Retrieves product information
- Applies return policies
- Gives **clear decisions**:
  - Full refund  
  - Store credit  
  - Exchange only  
  - Not eligible  

---

### 🧠 Agent Capabilities
- Uses **function/tool calling**
- Separates **reasoning from data retrieval**
- Avoids hallucination
- Handles edge cases:
  - Invalid order ID  
  - Missing input  

---

## 🏗️ Project Structure
<img width="353" height="622" alt="image" src="https://github.com/user-attachments/assets/7678348f-dc1d-4d57-9129-4b9a370ac75d" />


---

## ⚙️ How It Works

1. User enters a query in CLI  
2. Agent understands intent  
3. Agent selects the correct tool:
   - Product search → `search_products`
   - Order query → `get_order`
4. Tool fetches real data  
5. System applies logic (ranking / policy rules)  
6. Final result is returned with explanation  

---

## 🛠️ Tech Stack

- **Python**
- **OpenRouter API (LLM for tool calling)**
- **Pandas** (data handling)
- **Dotenv** (environment variables)

---

## 📂 Data Used

### Product Inventory
- price, tags, sizes, stock, sale status, bestseller score  

### Orders
- order_id, product_id, size, date  

### Policy
- return rules (normal, sale, clearance, vendor exceptions)

---

## ▶️ How to Run

### 1. Clone the repo

git clone https://github.com/GAURAV0440/agentic-retail-intelligence.git

cd agentic-retail-intelligence


---

### 2. Create virtual environment

python3 -m venv .venv
source .venv/bin/activate


---

### 3. Install dependencies

pip install -r requirements.txt


---

### 4. Add environment variables

Create a `.env` file:


OPENROUTER_API_KEY=your_api_key
BASE_URL=https://openrouter.ai/api/v1

MODEL=openai/gpt-4o-mini


---

### 5. Run the project

python main.py


---

## 🧪 Example Queries

### 🛍️ Shopping

I need a modest evening gown under 300 in size 8 on sale


---

### 📦 Returns

Order O0001 can I return this?


---

### ❌ Edge Case

Order O9999 can I return this?


---

## 🎯 Key Highlights

- Real-world **agent design (not just chatbot)**
- Deterministic decision-making using tools
- Clean separation of:
  - AI reasoning  
  - Business logic  
- Scalable and modular architecture  

---

## 📌 Note

This is a **simulation-based system** using local CSV data.  
No external APIs or databases are required.

---

## 👨‍💻 Author

**Gaurav**

---

## ⭐ Final Thought

This project demonstrates how AI agents can be built using:
- structured tools  
- real data  
- clear logic  

instead of relying on guess-based responses.

### Loom Screen Recording
https://www.loom.com/share/2155cc2260c54bbab4db267e4fe0656c
