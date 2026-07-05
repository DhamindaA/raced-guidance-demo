from dataclasses import dataclass


@dataclass
class EnforcementGuidanceResult:
    route_name: str
    guidance_text: str
    branches: list[dict]
    expected_evidence: list[str]
    cautions: list[str]


def evaluate_enforcement_guidance(
    include_safe_halt: bool,
    include_dafny_limitation: bool,
    include_timing_caution: bool,
) -> EnforcementGuidanceResult:
    """
    Creates guidance text for the IndependentSafetyEnforcement pattern.

    This function does not validate evidence, run verification tools, inspect
    source code, read ROS logs, or approve a safety claim. It only presents
    pattern-specific guidance and selected cautions.
    """

    branches = [
        {
            "name": "Trigger detection and interpretation",
            "guidance": (
                "The assurance case should show that the Safety System receives "
                "and interprets safety-relevant inputs, including proximity or "
                "geofence triggers, safe-halt requests, and robot motion state."
            ),
        },
        {
            "name": "Override priority",
            "guidance": (
                "The assurance case should show that, when a safety trigger occurs, "
                "the Safety System stop action takes priority over SRAS mode or "
                "SRAS command intent."
            ),
        },
        {
            "name": "Independent enforcement path",
            "guidance": (
                "The assurance case should show that the Safety System can enforce "
                "stopping through an independent command path, such as an "
                "orchestrator or command interceptor, without relying on correct "
                "SRAS decision-making."
            ),
        },
        {
            "name": "Formal verification of Safety System and integration logic",
            "guidance": (
                "The assurance case should connect formalised requirements to "
                "AJPF/MCAPL verification of the Gwendolen Safety System and to "
                "Dafny model verification or other evidence for the command "
                "interception logic."
            ),
        },
        {
            "name": "Persistence of stopped state",
            "guidance": (
                "The assurance case should show that once enforced stop or safe "
                "halt is active, motion remains suppressed until an explicit reset "
                "or clearance condition is satisfied."
            ),
        },
    ]

    expected_evidence = [
        "FRET/FRETish-derived formalised Safety System requirements.",
        "AJPF/MCAPL verification evidence for geofence/proximity stop behaviour.",
        "Gwendolen/MCAPL implementation evidence showing relevant percepts, beliefs, plans, and stop actions.",
        "ROS architecture and integration evidence showing topic subscription and command path integration.",
        "Orchestrator/interceptor evidence showing that Safety System stop requests override or block SRAS velocity commands.",
        "Simulation evidence showing induced triggers cause stop enforcement and continued suppression of SRAS motion commands.",
        "Physical robot evidence, where available, showing corresponding stop behaviour on the robot platform.",
        "Scope and limitation note explaining what the pattern does and does not claim.",
    ]

    cautions = []

    if include_safe_halt:
        expected_evidence.append(
            "AJPF/MCAPL safe-halt evidence covering safe_halt_req with tick and no halt_observed leading to entry_stop, safe_halt_req with halt_observed leading to safe_halt_active, and safe_halt_active with move percept leading to entry_stop."
        )

    if include_dafny_limitation:
        expected_evidence.append(
            "Dafny model verification evidence for command interception or orchestration logic, plus traceability, review, or testing evidence for the deployed Python orchestrator."
        )
        cautions.append(
            "Dafny evidence should be described as verification of the Dafny model of the orchestration logic. The deployed Python orchestrator remains outside the Dafny proof unless separately verified."
        )

    if include_timing_caution:
        expected_evidence.append(
            "Timing evidence clarifying whether the claim is an agent-level tick/percept claim or a deployed real-time stopping claim."
        )
        cautions.append(
            "AJPF verifies the agent-level tick/percept abstraction. A deployed real-time stopping bound requires additional timing, implementation, simulation, or physical evidence."
        )

    guidance_text = (
        "Guidance: this pattern should be used when the assurance case needs to "
        "argue that an independent Safety System can detect declared safety "
        "triggers, override or block SRAS motion commands, enforce a stopped "
        "state through an independent command path, and maintain the stopped "
        "state until reset or clearance. The generated guidance identifies the "
        "main argument branches, expected evidence types, and limitations that "
        "should be addressed. It does not validate the evidence or prove the "
        "safety claim."
    )

    return EnforcementGuidanceResult(
        route_name="Independent safety enforcement guidance route",
        guidance_text=guidance_text,
        branches=branches,
        expected_evidence=expected_evidence,
        cautions=cautions,
    )