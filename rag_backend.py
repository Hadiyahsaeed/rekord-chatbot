import os
import re
import ollama

# 1. Path Configuration
DATA_PATH = r"E:\AI_Lab\Projects\chatbot\data\product_descriptions.txt"

def ask_rag_bot(user_question):
    """Scans the clean catalog, aggregates multiple products for variety, and shapes the tone."""
    
    if not os.path.exists(DATA_PATH):
        return f"❌ System Error: Cannot locate the product file at: {DATA_PATH}"
        
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        full_catalog = f.read().strip()
        
    context_blocks = []
    search_query = user_question.lower()
    
    # Split the clean catalog using your standard product boundary marker
    segments = re.split(r'(?=PRODUCT:)', full_catalog) if "PRODUCT:" in full_catalog else full_catalog.split("\n\n")

    # 🎯 THERAPEUTIC MAPPING SAFETY NET (Aggregates multiple options for variety)
    is_malaria = any(kw in search_query for kw in ["malaria", "fever", "arme", "resnat"])
    is_migraine = any(kw in search_query for kw in ["migran", "headache", "samdix"])
    is_cardio = any(kw in search_query for kw in ["heart", "blood pressure", "hypertension", "ateno"])

    for seg in segments:
        seg_clean = seg.strip()
        if not seg_clean:
            continue
            
        # Group matching items into the context together to show portfolio depth
        if is_malaria and any(kw in seg_clean.lower() for kw in ["arme", "resnat", "malaria"]):
            context_blocks.append(seg_clean)
        elif is_migraine and any(kw in seg_clean.lower() for kw in ["samdix", "migraine"]):
            context_blocks.append(seg_clean)
        elif is_cardio and any(kw in seg_clean.lower() for kw in ["atenowin", "cardio", "hypertension"]):
            context_blocks.append(seg_clean)

    # Broad backup sweep if the structured categories didn't catch the user's specific text
    if not context_blocks:
        for seg in segments:
            seg_clean = seg.strip()
            if any(word in seg_clean.lower() for word in search_query.split() if len(word) > 4):
                context_blocks.append(seg_clean)

    # Ultimate fallback if everything misses
    context = "\n\n".join(context_blocks) if context_blocks else full_catalog[:3000]

    # 📝 HIGH-AUTHORITY CORPORATE PROMPT
    combined_user_prompt = f"""You are the official corporate AI Assistant for WnsFeild Pharmaceuticals. 

TONE AND EXECUTIVE DIRECTIVES:
- Deliver an absolute, definitive, and highly professional corporate response. 
- Eliminate all conversational fluff, placeholders, or meta-commentary (do NOT say "As per the registry", "Based on the context", or "Here are the products").
- Present the available medicines immediately using clean, structured headers.
- Showcase our pharmaceutical variety by clearly listing multiple relevant products from the data if available.
- State the exact facts, Brand Names, and Active Generic Ingredients provided. Never guess or generalize missing formulas.
- Conclude seamlessly by highlighting our commitment to quality, noting that all WnsFeild manufacturing lines adhere strictly to cGMP, ISO 9001:2015, and ISO 14001:2015 international quality standards.

VERIFIED PRODUCT REGISTRY DATA:
{context}

USER QUESTION: {user_question}
"""
    
    response = ollama.chat(
        model='llama3.2',  
        messages=[
            {'role': 'user', 'content': combined_user_prompt}
        ]
    )
    return response['message']['content']

if __name__ == "__main__":
    print("\n--- RUNNING REFINED BACKEND DIAGNOSTIC ---")
    print(ask_rag_bot("What medications do you have for malaria?"))