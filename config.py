import os

from data_structures import ModelInfo

initial_peers = [peer for peer in os.environ.get("INITIAL_PEERS", "").split(" ") if peer]
if initial_peers:
    INITIAL_PEERS = initial_peers
else:
    from petals.constants import PUBLIC_INITIAL_PEERS
    INITIAL_PEERS = PUBLIC_INITIAL_PEERS

MODELS = [
    ModelInfo(
        dht_prefix="StableBeluga2-hf",
        repository="https://huggingface.co/petals-team/StableBeluga2",
        num_blocks=80,
    ),
    ModelInfo(
        dht_prefix="Llama-2-70b-hf",
        repository="https://huggingface.co/meta-llama/Llama-2-70b-hf",
        num_blocks=80,
    ),
]

UPDATE_PERIOD = 60
