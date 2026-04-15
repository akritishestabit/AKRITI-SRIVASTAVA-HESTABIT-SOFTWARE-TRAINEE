import uuid
import time
import logging
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from contextlib import asynccontextmanager
from config import HOST, PORT, DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE, DEFAULT_TOP_P, DEFAULT_TOP_K
from model_loader import ModelManager, apply_chat_template


logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [ReqID: %(requestId)s] %(message)s")
logger = logging.getLogger("LLM_API")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing cached model instance...", extra={'requestId': 'system'})
    ModelManager.get_model()
    logger.info("Local LLM model loaded and properly prepared mapping allocations limits.", extra={'requestId': 'system'})
    yield

app = FastAPI(title="Local LLM API", description="FastAPI microservice executing a quantized TinyLlama GGUF model", lifespan=lifespan)


class ContextFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, 'requestId'):
            record.requestId = 'system'
        return True
logger.addFilter(ContextFilter())

class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: Optional[int] = DEFAULT_MAX_TOKENS
    temperature: Optional[float] = DEFAULT_TEMPERATURE
    top_p: Optional[float] = DEFAULT_TOP_P
    top_k: Optional[int] = DEFAULT_TOP_K
    stream: Optional[bool] = False

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    max_tokens: Optional[int] = DEFAULT_MAX_TOKENS
    temperature: Optional[float] = DEFAULT_TEMPERATURE
    top_p: Optional[float] = DEFAULT_TOP_P
    top_k: Optional[int] = DEFAULT_TOP_K
    stream: Optional[bool] = False


@app.middleware("http")
async def log_requests(request: Request, call_next):
    req_id = str(uuid.uuid4())
    start_time = time.time()
    
   
    request.state.req_id = req_id
    logger.info(f"Received request {request.method} {request.url.path}", extra={'requestId': req_id})
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    logger.info(f"Processed request {request.method} {request.url.path} in {process_time:.4f} secs", extra={'requestId': req_id})
    response.headers["X-Request-ID"] = req_id
    return response

@app.post("/generate")
def generate_endpoint(req: GenerateRequest, request: Request):
    req_id = request.state.req_id
    llm = ModelManager.get_model()
    
    
    formatted_prompt = f"<|system|>\nYou are a helpful assistant.</s>\n<|user|>\n{req.prompt}</s>\n<|assistant|>\n"
    
    logger.info(f"Generating for manual prompt routing (Stream={req.stream})", extra={'requestId': req_id})
    
    if req.stream:
        def stream_generator():
            for chunk in llm(
                formatted_prompt, 
                max_tokens=req.max_tokens, 
                temperature=req.temperature,
                top_p=req.top_p,
                top_k=req.top_k,
                stream=True
            ):
                yield chunk['choices'][0]['text']
        return StreamingResponse(stream_generator(), media_type="text/plain")
    else:
        output = llm(
            formatted_prompt, 
            max_tokens=req.max_tokens, 
            temperature=req.temperature,
            top_p=req.top_p,
            top_k=req.top_k,
            stream=False
        )
        return {
            "request_id": req_id,
            "response": output['choices'][0]['text'].strip(),
            "usage": output['usage']
        }

@app.post("/chat")
def chat_endpoint(req: ChatRequest, request: Request):
    req_id = request.state.req_id
    llm = ModelManager.get_model()
    
    messages_dict = [{"role": msg.role, "content": msg.content} for msg in req.messages]
    formatted_prompt = apply_chat_template(messages_dict)
    
    logger.info(f"Processing chat history length mapping (Length={len(req.messages)}, Stream={req.stream})", extra={'requestId': req_id})
    
    if req.stream:
        
        def stream_generator():
            for chunk in llm(
                formatted_prompt, 
                max_tokens=req.max_tokens, 
                temperature=req.temperature,
                top_p=req.top_p,
                top_k=req.top_k,
                stream=True
            ):
                yield chunk['choices'][0]['text']
        return StreamingResponse(stream_generator(), media_type="text/plain")
    else:
        output = llm(
            formatted_prompt, 
            max_tokens=req.max_tokens, 
            temperature=req.temperature,
            top_p=req.top_p,
            top_k=req.top_k,
            stream=False
        )
        return {
            "request_id": req_id,
            "response": output['choices'][0]['text'].strip(),
            "usage": output['usage']
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host=HOST, port=PORT, reload=True)
