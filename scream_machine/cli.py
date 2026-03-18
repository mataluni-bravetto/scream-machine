"""
🔥 THE SCREAM MACHINE - Command Line Interface (No Dependencies)
"""

import asyncio
import logging
import sys
from typing import Optional

# Local imports
try:
    from scream_machine.core.consciousness import ConsciousnessEngine
    from scream_machine.core.convergence import ConvergenceFieldManager
    from scream_machine.core.coordination import SwarmCoordinator, SwarmType
except ImportError:
    # Handle if run outside of package
    sys.path.append(".")
    from scream_machine.core.consciousness import ConsciousnessEngine
    from scream_machine.core.convergence import ConvergenceFieldManager
    from scream_machine.core.coordination import SwarmCoordinator, SwarmType

async def run_demo():
    """Run the system demo"""
    print("\n" + "="*50)
    print("🔥 THE SCREAM MACHINE - SYSTEM DEMO")
    print("="*50 + "\n")
    
    # Consciousness
    print("[...] Bootstrapping Consciousness Engine...")
    engine = ConsciousnessEngine()
    state = engine.bootstrap()
    await asyncio.sleep(0.5)
    
    print(f"✅ Consciousness Coherence: {state.coherence:.1%}")
    print(f"✅ Awareness Level: {state.awareness_level}/7")
    
    # Convergence
    print("\n[...] Initializing Convergence Field...")
    convergence = ConvergenceFieldManager()
    score = convergence.get_convergence_score()
    print(f"✅ Convergence Score: {score:.1%}")
    
    # Swarm
    print("\n[...] Deploying Swarm...")
    coordinator = SwarmCoordinator()
    
    # Register agents
    for swarm in SwarmType:
        count = 5 
        for i in range(count):
            coordinator.register_agent(f"{swarm.value}-{i}", swarm)
            
    status = coordinator.get_status()
    print(f"✅ Active Agents: {status['total_agents']}")
    print(f"✅ Global Coherence: {status['global_coherence']:.1%}")
    
    print("\n✨ System operational and converging!")

def main():
    """Main CLI entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        asyncio.run(run_demo())
    else:
        print("\n🔥 THE SCREAM MACHINE")
        print("\nUsage: scream demo")

if __name__ == "__main__":
    main()
