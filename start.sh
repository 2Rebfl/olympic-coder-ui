
# Set CUDA library path
export LD_LIBRARY_PATH=/usr/local/cuda-12.4/targets/x86_64-linux/lib:

# Activate virtual environment
source ~/olympic-env/bin/activate

# Start vLLM API server in the background
echo Starting vLLM API server...
python -m vllm.entrypoints.api_server --model ~/olympic-coder-7b --port 8000 --max-model-len 4096 --gpu-memory-utilization 0.95 &
VLLM_PID=

# Wait for vLLM to start
echo Waiting for vLLM server to initialize...
sleep 10

# Start Streamlit UI
echo Starting Streamlit UI...
streamlit run olympic_ui.py --server.port 8501

# Cleanup when Streamlit is closed
kill 
