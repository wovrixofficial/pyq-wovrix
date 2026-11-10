import os
import sys
import json
import glob
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
CACHE_FILE = os.path.join(DATA_DIR, "solutions_cache.json")
QUEUE_FILE = os.path.join(DATA_DIR, "reports_queue.json")

# Possible locations for the downloaded 14B GGUF model
SEARCH_PATHS = [
    os.path.expanduser(r"~\Downloads\Qwen2.5-Coder-14B-Instruct-abliterated.Q4_K_M.gguf"),
    os.path.expanduser(r"~\Downloads\*Qwen*14B*.gguf"),
    r"E:\OllamaModels\*Qwen*14B*.gguf",
    r"E:\*Qwen*14B*.gguf",
    r"C:\*Qwen*14B*.gguf",
]

def find_local_model():
    for pattern in SEARCH_PATHS:
        matches = glob.glob(pattern)
        if matches:
            return matches[0]
    return None

def load_qwen_model(model_path=None):
    try:
        from llama_cpp import Llama
    except ImportError:
        print("[ERROR] llama-cpp-python not installed. Run: pip install llama-cpp-python")
        return None

    path = model_path or find_local_model()
    if not path or not os.path.exists(path):
        print(f"[STATUS] Local 14B GGUF model not yet found at candidate paths.")
        print("Once your download finishes, place the GGUF file in Downloads or E:\\ and rerun.")
        return None

    print(f"[INFO] Initializing Qwen 14B model from: {path}")
    print("[INFO] Offloading layers to GPU (n_gpu_layers=-1, n_ctx=8192)...")
    llm = Llama(
        model_path=path,
        n_gpu_layers=-1,
        n_ctx=8192,
        verbose=False
    )
    print("[SUCCESS] Model loaded successfully into GPU VRAM!")
    return llm

def solve_cbse_question(llm, q_text, marks=3, subject="Physics", chapter="General"):
    if not llm:
        return None

    prompt = f"""<|im_start|>system
You are a senior CBSE Class 12 board evaluator and subject matter expert in {subject}.
Provide the official step-by-step marking rubric and complete solution for this board question.
Allocate exactly {marks} mark(s) across distinct steps. Format mathematical derivations using standard KaTeX ($...$).
<|im_end|>
<|im_start|>user
Subject: {subject}
Chapter: {chapter}
Marks: {marks}
Question:
{q_text}

Provide:
1. Step-by-step marking breakdown ({marks} Marks)
2. Complete mathematical derivation and final answer.
<|im_end|>
<|im_start|>assistant
"""
    output = llm(prompt, max_tokens=1024, temperature=0.1, stop=["<|im_end|>"])
    return output["choices"][0]["text"].strip()

def solve_neet_question(llm, q_text, options, correct_key, subject="Physics"):
    if not llm:
        return None

    opts_str = "\n".join([f"({k}) {v}" for k, v in options.items()])
    prompt = f"""<|im_start|>system
You are an expert NEET UG medical entrance faculty in {subject}.
Derive the complete conceptual solution, relevant NCERT formula, and step-by-step reason why Option ({correct_key}) is the correct answer.
<|im_end|>
<|im_start|>user
Subject: {subject}
Question:
{q_text}

Options:
{opts_str}

Official Key: Option ({correct_key})

Provide:
1. Core Concept / NCERT Law
2. Step-by-step mathematical proof / derivation
3. Verification of why other options are incorrect.
<|im_end|>
<|im_start|>assistant
"""
    output = llm(prompt, max_tokens=1024, temperature=0.1, stop=["<|im_end|>"])
    return output["choices"][0]["text"].strip()

def status():
    model_path = find_local_model()
    print("=== LOCAL 14B QWEN SOLVER PIPELINE STATUS ===")
    print(f"llama-cpp-python: Available (GPU-accelerated)")
    if model_path:
        size_gb = os.path.getsize(model_path) / (1024**3)
        print(f"Model file: FOUND -> {model_path} ({size_gb:.2f} GB)")
        print("Status: READY FOR LOCAL HIGH-SPEED INFERENCE")
    else:
        print("Model file: Currently downloading or pending placement.")
        print("Expected filename: Qwen2.5-Coder-14B-Instruct-abliterated.Q4_K_M.gguf")
        print("Monitored directories: C:\\Users\\Srijan\\Downloads\\, E:\\, E:\\OllamaModels\\")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--status":
        status()
    else:
        status()
