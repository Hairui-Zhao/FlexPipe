torchrun --nproc_per_node=4 \
 --nnodes=1 \
 --node_rank=0 \
 --master_add="127.0.0.1" \
 --master_port=2655 \
 runtime.py
