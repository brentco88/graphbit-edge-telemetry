import math

def cosine_similarity(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a * a for a in v1))
    mag2 = math.sqrt(sum(b * b for b in v2))
    if mag1 == 0 or mag2 == 0:
        return 0.0
    return dot / (mag1 * mag2)

def evaluate_stigmergic_convergence():
    gamma = 0.85
    t_current = 4
    
    # Negative failure vectors deposited on Blackboard during turns 1 and 2
    failure_history = [
        {"turn": 1, "vector": [0.92, 0.15, 0.88, 0.05]},
        {"turn": 2, "vector": [0.85, 0.22, 0.94, 0.10]}
    ]
    
    dim = len(failure_history[0]["vector"])
    s_t = [0.0] * dim
    for record in failure_history:
        decay = gamma ** (t_current - record["turn"])
        for i in range(dim):
            s_t[i] += decay * record["vector"][i]
            
    # Candidate path attempting a near-identical tool retry loop
    candidate_loop = [0.89, 0.18, 0.91, 0.08]
    rejection_score = cosine_similarity(candidate_loop, s_t)
    
    # Candidate path attempting a diversified discovery angle
    candidate_novel = [0.05, 0.85, 0.12, 0.78]
    novel_score = cosine_similarity(candidate_novel, s_t)
    
    print(f"Aggregated Stigmergic Field S_t: {[round(x, 4) for x in s_t]}")
    print(f"Candidate Loop Rejection Score: {round(rejection_score, 4)}")
    print(f"Candidate Novel Angle Score:    {round(novel_score, 4)}")
    
    assert rejection_score >= 0.70, "Loop candidate failed to trigger >= 0.70 rejection threshold"
    assert novel_score < 0.70, "Novel candidate falsely triggered rejection threshold"
    print("PHASE 11 SWARM VECTOR CONVERGENCE: VERIFIED.")

if __name__ == "__main__":
    evaluate_stigmergic_convergence()
