import os
import re
import json
import ollama
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for secure front-end testing from WordPress
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Your absolute path configuration on the E drive
DATA_PATH = r"E:\AI_Lab\Projects\chatbot\data\product_descriptions.txt"

def get_rag_context(user_question):
    """
    Dynamic Enterprise Scanner: Handles 400+ products dynamically.
    Shreds user input into core keywords, handles typos, and builds an accurate RAG context.
    """
    if not os.path.exists(DATA_PATH):
        return "❌ System Error: Cannot locate the product file."
        
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        full_catalog = f.read().strip()
        
    context_blocks = []
    
    # 1. Clean and normalize the user's input query into individual lowercase words
    search_words = re.findall(r'\b\w+\b', user_question.lower())
    
    # 2. Filter out common conversational filler words so they don't corrupt the search
    filler_words = {
        "what", "medication", "medications", "medicine", "medicines", "have", "you", 
        "for", "does", "treat", "with", "about", "your", "list", "show", "give", "me",
        "any", "do", "are", "there", "is", "the", "an", "a", "info"
    }
    target_keywords = [word for word in search_words if word not in filler_words and len(word) > 2]
    
    # 3. Split your massive catalog into individual product blocks using your standard marker
    segments = re.split(r'(?=PRODUCT:)', full_catalog) if "PRODUCT:" in full_catalog else full_catalog.split("\n\n")

    # 4. Dynamic Scan: Look through all 400+ products for matching terms
    for seg in segments:
        seg_clean = seg.strip()
        if not seg_clean:
            continue
            
        seg_lower = seg_clean.lower()
        
        # Exact match check first against user keywords
        if any(keyword in seg_lower for keyword in target_keywords):
            context_blocks.append(seg_clean)
            continue
            
        # 🎯 FUZZY MATCHING BACKUP: Check for loose/partial string hits (handles typos like "migranes")
        for word in target_keywords:
            if len(word) >= 5 and (word[:5] in seg_lower or word[:-1] in seg_lower):
                context_blocks.append(seg_clean)
                break

    # 5. Smart Payload Management: Combine matches or gracefully fall back
    if context_blocks:
        # Deduplicate list preserving order
        unique_blocks = list(dict.fromkeys(context_blocks))
        # Feed Llama the top 12 relevant matches to keep responses lightning-fast and under context limits
        return "\n\n".join(unique_blocks[:12])
    else:
        # Ultimate fallback: If it's a general question, show a portion of the catalog profile
        return "No specific match found. Refer broadly to the available portfolio data:\n\n" + full_catalog[:4000]


@app.post("/ask")
async def ask_endpoint(request: Request):
    body = await request.json()
    user_query = body.get("query", "")
    context = get_rag_context(user_query)

    # 📝 STRICT CLOSED-DOMAIN CORPORATE PROMPT
    combined_user_prompt = f"""You are the automated technical data engine for WnsFeild Pharmaceuticals.

CRITICAL OPERATIONAL CONSTRAINTS (ZERO-TOLERANCE RULES):
1. Rely ONLY on the VERIFIED PRODUCT REGISTRY DATA provided below. Do NOT use any external medical knowledge, global drug databases, or generic treatment guidelines.
2. If a medicine or brand name is NOT explicitly listed in the provided text registry below, your answer must strictly be: "The requested medical condition or product is not present in the current WnsFeild Pharmaceuticals portfolio database."
3. Completely eliminate all conversational filler, helpful advice, web summaries, or standard medical disclaimers. Do NOT suggest consulting a doctor, do NOT list general drug classes (like Triptans, Ergotamines, or NSAIDs), and do NOT say "I am not a medical professional."
4. Deliver the response immediately using clean, structured headers showing only the exact Brand Name and Active Generic Ingredient found in the text.
5. Conclude seamlessly by stating: "All WnsFeild manufacturing lines adhere strictly to cGMP, ISO 9001:2015, and ISO 14001:2015 international quality standards."

VERIFIED PRODUCT REGISTRY DATA:
{context}

USER QUESTION: {user_query}
"""
    

    def stream_rag_tokens():
        try:
            # Explicit local client creation to ensure clean Miniconda communication
            client = ollama.Client(host='http://127.0.0.1:11434')
            
            stream = client.chat(
                model='llama3.2',
                messages=[{'role': 'user', 'content': combined_user_prompt}],
                stream=True
            )
            
            # 🟢 Correct dictionary indexing layout required by the Ollama-Python SDK
            for chunk in stream:
                if 'message' in chunk and 'content' in chunk['message']:
                    yield chunk['message']['content']
                    
        except Exception as e:
            yield f"⚠️ Local Connection Error: {str(e)}"

    return StreamingResponse(stream_rag_tokens(), media_type="text/plain")


if __name__ == "__main__":
    import uvicorn
    print("\n--- ENTERPRISE PIPELINE IS LIVE ON PORT 8000 ---")
    uvicorn.run(app, host="127.0.0.1", port=8000)