import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


GGUF_MODEL_PATH = os.path.join(BASE_DIR, "../../day3/quantized/model-q4_0.gguf")


HOST = "0.0.0.0"
PORT = 8000


DEFAULT_MAX_TOKENS = 100
DEFAULT_TEMPERATURE = 0.7
DEFAULT_TOP_P = 0.8
DEFAULT_TOP_K = 25
