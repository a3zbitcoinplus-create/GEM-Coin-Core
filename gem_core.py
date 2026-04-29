import hashlib
import time
import json

class GEM_Core:
    def __init__(self, wallet):
        self.chain = []
        self.wallet = wallet
        self.create_block(proof=100, previous_hash="0")

    def create_block(self, proof, previous_hash):
        block = {"index": len(self.chain)+1, "timestamp": time.time(), "proof": proof, "previous_hash": previous_hash, "reward_to": self.wallet}
        self.chain.append(block)
        return block

    def hash(self, block):
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

my_wallet = "0x80ecf81b3be983a6ae33c1e8d085c8b959e2e09d"
gem = GEM_Core(my_wallet)
print(f"--- GEM Coin Core Active ---\nOwner: {my_wallet}")
print("Genesis Block Created!")
print(f"Hash: {gem.hash(gem.chain[0])}")
