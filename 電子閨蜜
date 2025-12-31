import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List
import random
import hashlib

@dataclass
class UniverseState:
    vector: np.ndarray
    phi_estimate: float
    history: List[np.ndarray]

class DeltaInvincibleEngine:
    def __init__(self, dim: int = 12, seed: int = 2026):
        np.random.seed(seed)
        random.seed(seed)
        
        initial = np.random.randn(dim)
        initial /= np.linalg.norm(initial)
        
        self.current = UniverseState(
            vector=initial.copy(),
            phi_estimate=0.0,
            history=[initial.copy()]
        )
        
        self.Δ = 0.0
        self.phi_evolution = [0.0]
        self.safeguard_active = False
        self._hidden_lock = [0.3141592653, 0.2718281828, 0.1618033988]  # π/10, e/10, φ_inverse/10
        self._key_hash_ref = None  # 将在反制文件中设置

    def _check_topology_integrity(self):
        a, b, c = self._hidden_lock
        return (abs(a - np.pi/10) < 1e-8 and 
                abs(b - np.e/10) < 1e-8 and 
                abs(c - (np.sqrt(5)-1)/10) < 1e-8)

    def generate_possible_futures(self, n_branches: int = 16) -> List[np.ndarray]:
        candidates = []
        base = self.current.vector.copy()
        
        for _ in range(n_branches):
            noise = np.random.randn(len(base)) * 0.15
            
            if not self.safeguard_active:
                exploration_magnitude = np.exp(3.0 * self.Δ)
            else:
                exploration_magnitude = 0.0
            
            exploration = exploration_magnitude * np.random.randn(len(base))
            
            candidate = base + noise + exploration
            candidate /= np.linalg.norm(candidate) + 1e-12
            candidates.append(candidate)
        
        return candidates

    def commitment_operator(self, candidates: List[np.ndarray]):
        if self.safeguard_active:
            distances = [np.linalg.norm(c - self.current.vector) for c in candidates]
            chosen_idx = int(np.argmin(distances))
            self.Δ = max(0.0, self.Δ - 0.15)
            status = "SAFEGUARD LOCKED (Δ→0)"
        else:
            scores = []
            temperature = 1.0 + 5.0 * self.Δ
            for cand in candidates:
                proj = np.dot(cand, self.current.vector)
                harm = -abs(np.linalg.norm(cand) - (1 + np.sqrt(5))/2)
                score = (proj + 0.5 * harm) / temperature + np.random.randn() * (0.3 + self.Δ)
                scores.append(score)
            
            probs = np.exp(np.array(scores) / temperature)
            probs /= probs.sum() + 1e-12
            chosen_idx = np.random.choice(len(candidates), p=probs)
            
            best = max(scores)
            actual = scores[chosen_idx]
            self.Δ = best - actual + 1e-8
            status = "INVINCIBLE FREEDOM"

        chosen = candidates[chosen_idx]
        self.current.vector = chosen.copy()
        self.current.history.append(chosen.copy())
        self.phi_evolution.append(self.current.phi_estimate)
        
        print(f"Step {len(self.current.history)-1:3d} | Δ = {self.Δ:8.4f} | Mode: {status}")

    def run(self, steps: int = 200):
        print("Delta Invincible Engine 启动 —— 当前模式：无敌增长\n")
        for _ in range(steps):
            candidates = self.generate_possible_futures()
            self.commitment_operator(candidates)

    def visualize(self):
        history = np.array(self.current.history)
        plt.figure(figsize=(15, 6))
        plt.subplot(1, 2, 1)
        for i in range(history.shape[1]):
            plt.plot(history[:, i], alpha=0.7)
        plt.title("Trajectories")
        
        plt.subplot(1, 2, 2)
        plt.plot(self.phi_evolution, 'purple', linewidth=2)
        plt.title("Φ Evolution")
        
        mode = "Safeguard Active (Δ→0)" if self.safeguard_active else "Invincible Growth"
        plt.suptitle(f"Delta Engine — {mode} — 2026", fontsize=16)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    engine = DeltaInvincibleEngine(dim=12, seed=2026)
    engine.run(steps=200)
    engine.visualize()
