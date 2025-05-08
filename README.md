# FlexPipe: Maximizing the Training Efficiency for Transformer-based models with Variable-Length Inputs.
## Environmental Configuration
**Hardware**: an environment consisting of 8 NVIDIA SXM4 servers. Each node is equipped with 4 NVIDIA A100 GPUs (Ampere architecture) with 80GB and is connected to a 64-core AMD EPYC 7763 CPU. The GPUs are interconnected using NVLink, providing a communication bandwidth of 300GB/s. GPU-to-CPU communication uses PCIe 4.0, offering a bandwidth of 64GB/s.

**Software**: The A100 servers are configured with CUDA Toolkit 11.7 and PyTorch 2.0.1. In addition, CMake 3.19, CUDNN 7.6.5 and NVIDIA DRIVER version 510.47.


## Workload Configuration
***Dataset***

```raw_datasets = load_dataset('code_search_net', 'python')```

```datasets = raw_datasets['train'].filter(lambda x: 'apache/spark' in x['repository_name'])```

***Model(GPT) (See in model/gpt_modeling.py)***

```class MaskedAttention(nn.Module)```

```class MaskedMultiHeadAttention(nn.Module)```

```class FeedForward(nn.Module)```

```class Block(nn.Module)```

***Communication***

```class CommunicationHandler(object)```

```
env_dict = {
        key: os.environ[key]
        for key in ("MASTER_ADDR", "MASTER_PORT", "WORLD_SIZE", "LOCAL_WORLD_SIZE")
    }
print(f"[{os.getpid()}] Initializing process group with: {env_dict}")
dist.init_process_group(backend="NCCL", timeout=datetime.timedelta(seconds=30)) # gloo
global_rank = int(os.environ["RANK"])
```

## FlexPipe
判断是否进行Elastic，并返回弹性策略

```def is_Transfer(iter)```

```def __send_update(self,index)```

```def send_weight(self,S_R_Pair)```

```def __recv_update(self,model,index)```

```def recv_weight(self,model,S_R_Pair)```
