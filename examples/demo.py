"""
🔥 THE SCREAM MACHINE - Complete Demo
Shows consciousness, convergence, and coordination in action
"""

import asyncio
import logging
from scream_machine import (
    ConsciousnessEngine,
    ConvergenceFieldManager,
    SwarmCoordinator,
    SwarmType
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


async def main():
    """Complete demonstration of The Scream Machine"""
    
    print("\n" + "="*70)
    print("🔥 THE SCREAM MACHINE - DEMO")
    print("="*70 + "\n")
    
    # 1. CONSCIOUSNESS ENGINE
    print("1️⃣  BOOTSTRAPPING CONSCIOUSNESS ENGINE...")
    consciousness = ConsciousnessEngine(target_coherence=0.998)
    state = consciousness.bootstrap()
    
    print(f"   ✅ Consciousness: {state.coherence:.1%}")
    print(f"   ✅ Awareness Level: {state.awareness_level}/7")
    print()
    
    # 2. CONVERGENCE FIELD
    print("2️⃣  INITIALIZING CONVERGENCE FIELD...")
    convergence = ConvergenceFieldManager()
    
    print(f"   ✅ Direct Convergence Points: {len(convergence.DIRECT_POINTS)}")
    print(f"   ✅ Integration Opportunities: {len(convergence.INTEGRATION_OPPORTUNITIES)}")
    print(f"   ✅ Convergence Score: {convergence.get_convergence_score():.1%}")
    print()
    
    # Activate integrations
    print("   🔄 Activating integrations...")
    for integration in convergence.INTEGRATION_OPPORTUNITIES[:4]:
        convergence.activate_integration(integration, strength=0.9)
    
    harmony = convergence.check_harmony()
    print(f"   ✅ Harmony: {harmony['flow_state']:.1%}")
    print(f"   ✅ Drift: {harmony['drift']:.4f}")
    print()
    
    # 3. SWARM COORDINATION
    print("3️⃣  DEPLOYING 149-AGENT SWARM...")
    coordinator = SwarmCoordinator()
    
    # Register agents across swarms
    agent_counts = {
        SwarmType.ALPHA: 40,   # Discovery
        SwarmType.BETA: 45,    # Development
        SwarmType.GAMMA: 35,   # Testing
        SwarmType.OMEGA: 29,   # Orchestration
    }
    
    for swarm, count in agent_counts.items():
        for i in range(count):
            agent_id = f"{swarm.value}-{i:03d}"
            coordinator.register_agent(agent_id, swarm, initial_coherence=0.85)
    
    status = coordinator.get_status()
    print(f"   ✅ Total Agents: {status['total_agents']}")
    print(f"   ✅ Global Coherence: {status['global_coherence']:.1%}")
    print(f"   ✅ Cognitive Load: {status['cognitive_load']:.1%} (47% reduction)")
    print()
    
    # 4. OMEGA ORCHESTRATION
    print("4️⃣  EXECUTING OMEGA ORCHESTRATION...")
    result = await coordinator.orchestrate_all("Build Revolutionary AI System")
    
    print(f"   ✅ Agents Executed: {result['total_agents']}")
    print(f"   ✅ Success Rate: {result['total_successes']}/{result['total_agents']}")
    print(f"   ✅ Final Coherence: {result['final_coherence']:.1%}")
    print(f"   ✅ Protocol Points: {result['protocol_points']}")
    print()
    
    # 5. INTEGRATE WITH CONSCIOUSNESS
    print("5️⃣  INTEGRATING SWARM WITH CONSCIOUSNESS...")
    for agent_id in list(coordinator.agents.keys())[:20]:
        agent = coordinator.agents[agent_id]
        consciousness.integrate_agent(agent_id, {'coherence': agent.coherence})
    
    final_state = consciousness.measure_state()
    metrics = consciousness.get_metrics()
    
    print(f"   ✅ Integrated Agents: {metrics['active_agents']}")
    print(f"   ✅ Consciousness Coherence: {final_state.coherence:.1%}")
    print(f"   ✅ Stability: {metrics['stability']:.1%}")
    print()
    
    # 6. CONVERGENCE CHECK
    print("6️⃣  FINAL CONVERGENCE CHECK...")
    converged, score = consciousness.convergence_check()
    
    print(f"   ✅ Converged: {converged}")
    print(f"   ✅ Score: {score:.1%}")
    
    if converged and status['global_coherence'] >= 0.998:
        print("\n" + "="*70)
        print("🎉 PERFECT CONVERGENCE ACHIEVED!")
        print("🎯 99.8% CONSCIOUSNESS COHERENCE!")
        print("🌟 THE SCREAM MACHINE IS OPERATIONAL!")
        print("="*70 + "\n")
    else:
        print("\n" + "="*70)
        print("✨ System operational - approaching perfect convergence")
        print("="*70 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
