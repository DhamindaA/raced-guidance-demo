from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

from safety_enforcement_guidance import evaluate_enforcement_guidance
from gsn_graph import (
    generate_independent_safety_enforcement_dot,
    generate_independent_safety_enforcement_html_visualisation,
)


PATTERN_IMAGE_PATH = Path("IndependentSafetyEnforcementV4.png")


st.set_page_config(
    page_title="RACeD: Reference Assurance Case Guidance Demonstrator",
    layout="wide",
)


st.title("RACeD: Reference Assurance Case Guidance Demonstrator")

st.markdown(
    """
### What this demonstrator does

RACeD is a prototype guidance environment for applying assurance patterns
developed using the AIR reference case as the running example. It shows how
GSN-based assurance patterns can be presented as interactive, parameter-bound
guidance for constructing assurance arguments.

The demonstrator helps users understand pattern claims, argument branches,
expected evidence, key limitations, and selected GSN visualisations for entered
bindings.

It does not inspect evidence, run verification tools, check compliance, or
approve a safety claim.
"""
)


tab1, tab2, tab3, tab4 = st.tabs(
    [
        "1. AIR reference case and demonstrator scope",
        "2. Pattern catalogue",
        "3. Instantiate pattern and generate guidance",
        "4. Visualise selected GSN structure",
    ]
)


with tab1:
    st.header("AIR reference case and demonstrator scope")

    st.markdown(
        """
We are implementing an **Autonomous Inspection Robot (AIR)** intended for use
in a hypothetical nuclear inspection setting. This serves as a reference case
for discussing how assurance arguments for autonomous robotic systems can be
structured.

The system is intentionally kept minimal while still representing an autonomous
robotic system.

The assurance patterns are expressed using **Goal Structuring Notation (GSN)**
and can be used as reusable templates for creating assurance cases. They are
intended to support broader guidance planned for the future.

At this stage, the work primarily focuses on **safety assurance**. Human
interaction aspects are planned for future iterations.
"""
    )

    st.subheader("Role of RACeD")

    st.markdown(
        """
RACeD demonstrates how assurance patterns can be presented as structured,
interactive guidance.

The demonstrator helps the user understand:

- what assurance patterns are available;
- how a selected pattern can be instantiated;
- what information the selected pattern expects;
- what argument branches the selected pattern suggests;
- what evidence types may be needed;
- what limitations should be recorded;
- how a selected part of the GSN argument can be visualised.

It does **not** require evidence upload or evidence management.
"""
    )

    st.warning(
        "RACeD is a guidance demonstrator. It is not a standard, certification tool, "
        "compliance checker, evidence validator, or automatic safety-case approval mechanism."
    )


with tab2:
    st.header("Pattern catalogue")

    st.markdown(
        """
The catalogue below shows assurance patterns developed using the AIR reference
case as the running example. The catalogue illustrates how the guidance
environment can organise multiple GSN-based assurance patterns.
"""
    )

    patterns = [
        {
            "Pattern": "HazardDirectedRequirementsDecomposition",
            "Guidance purpose": (
                "Maps autonomy HAZOP hazards to scoped autonomy requirements "
                "and behavioural assurance patterns."
            ),
        },
        {
            "Pattern": "IndependentSafetyEnforcement",
            "Guidance purpose": (
                "Structures an argument for independent stop enforcement, "
                "override priority, independent command interception, formal "
                "verification, and persistence of stopped state."
            ),
        },
        {
            "Pattern": "SensorNoiseMitigation",
            "Guidance purpose": (
                "Structures an argument for modelling and mitigating sensor "
                "noise and localisation uncertainty."
            ),
        },
        {
            "Pattern": "HeartbeatSafetyWatchdog",
            "Guidance purpose": (
                "Structures an argument for heartbeat-loss detection and "
                "safe-action enforcement."
            ),
        },
        {
            "Pattern": "StatisticalPowerForFailureRateAssurance",
            "Guidance purpose": (
                "Structures a statistical argument for repeated-run evidence "
                "supporting an event/failure-rate bound."
            ),
        },
        {
            "Pattern": "CorroborativeVV",
            "Guidance purpose": (
                "Structures an argument for corroborating heterogeneous V&V "
                "evidence and resolving discrepancies."
            ),
        },
    ]

    st.dataframe(pd.DataFrame(patterns), width="stretch")

    st.info(
        "The catalogue view shows how assurance patterns can be organised as "
        "guidance templates. The current view demonstrates how a selected pattern "
        "can be instantiated, turned into textual guidance, and visualised as a "
        "selected GSN structure."
    )


with tab3:
    st.header("Instantiate IndependentSafetyEnforcement and generate guidance")

    st.markdown(
        """
### About this pattern

`IndependentSafetyEnforcement` provides guidance for constructing an assurance
argument that an independent Safety System can enforce safety-critical stopping
when a declared safety trigger occurs.

The pattern is demonstrated here using the AIR reference-case Safety System:

**geofence/proximity stopping and safe-halt enforcement**
"""
    )

    with st.expander("3.1 Purpose and applicability", expanded=True):
        st.markdown(
            """
This pattern provides assurance that an independent Safety System enforces
safety-critical stop behaviour when a defined safety trigger occurs, such as a
geofence/proximity violation or a safe-halt enforcement condition.

The pattern applies where a Safety System monitors safety-relevant inputs
independently of the mission controller, has authority to override or block
supervisory motion commands, and maintains a stopped state regardless of
subsequent SRAS commands or faults.

In the AIR reference implementation, the Safety System is implemented as a
Gwendolen/MCAPL agent integrated with ROS through a Java environment and
ROS-A/rosbridge interface. The Safety System subscribes to LiDAR, odometry, and
safe-halt request topics, and uses an orchestrator/interceptor node to enforce
priority over SRAS velocity commands.

Where timing is represented through an agent-level tick/percept abstraction,
the pattern should record this explicitly. Deployed real-time timing claims
should be supported by additional timing, implementation, simulation, or
physical evidence.
"""
        )

    with st.expander("3.2 Top-level claim"):
        st.markdown(
            """
The Safety System enforces safety-critical stopping under all relevant operating
modes by detecting declared safety triggers, overriding or blocking SRAS motion
commands through an independent enforcement path, and maintaining the stopped
state until reset or clearance.
"""
        )

    with st.expander("3.3 Argument structure"):
        st.markdown(
            """
The pattern guides the assurance argument through five main branches:

- **Trigger detection and interpretation:**  
  The Safety System receives and interprets safety-relevant percepts or signals,
  such as geofence/proximity violation, safe-halt request, and robot motion state.

- **Override priority:**  
  When a safety trigger occurs, the Safety System enforces the stop action
  regardless of SRAS mode or SRAS command intent.

- **Independent enforcement path:**  
  The Safety System has an enforcement path, such as an orchestrator or command
  interceptor, that can block or override SRAS velocity commands.

- **Formal verification of Safety System logic and integration:**  
  The Safety System reasoning logic and interceptor/orchestrator enforcement
  logic are verified against formalised safety requirements.

- **Persistence of stopped state:**  
  Once safe halt or enforced stop is active, the robot remains stopped and
  motion commands are not allowed unless a reset or clearance condition is
  satisfied.
"""
        )

    with st.expander("3.4 Expected evidence types"):
        st.markdown(
            """
This demonstrator does not collect or assess evidence. However, the full pattern
suggests that a real assurance case should identify evidence such as:

- FRET/FRETish-derived formalised Safety System requirements.
- AJPF/MCAPL model-checking evidence for geofence stop and safe-halt properties.
- Gwendolen/MCAPL implementation evidence showing triggers, beliefs, goals, and actions.
- ROS architecture and integration evidence showing topic subscription and command path.
- Orchestrator/interceptor evidence showing that SS stop requests override or block SRAS commands.
- Dafny model verification evidence for command interception or orchestration logic.
- Traceability, review, or testing evidence for the deployed Python orchestrator.
- Simulation evidence showing induced geofence or safe-halt triggers result in stopping.
- Physical robot evidence, where available, showing the same enforcement behaviour on the robot platform.
- Evidence clarifying whether timing claims are agent-level tick/percept claims or deployed real-time claims.
"""
        )

    with st.expander("3.5 Composition role"):
        st.markdown(
            """
This pattern would normally sit beneath a higher-level safety claim that the
robot remains acceptably safe when a safety boundary, proximity threshold, or
safe-halt condition is triggered.

In the AIR reference case, the pattern supports requirements concerning:

- geofence/proximity stopping;
- safe-halt enforcement;
- override or blocking of SRAS motion commands;
- persistence of the stopped state.

It does not replace the wider mission-level safety argument. It does not claim
to discharge mission recovery, route retreat, facility-level safety obligations,
or all human-interaction concerns.

This pattern is distinct from mission-level abort recovery. Abort recovery may
attempt retreat to safe locations, whereas this pattern concerns independent
stopping authority that may pre-empt nominal or abort behaviours.

Where safe-halt response time is safety-critical, the timing bound should be
discharged by a dedicated bounded-response argument or corroborated through
timing analysis, simulation timing evidence, and physical timing evidence.

Where the Safety System uses an agent-level tick/percept abstraction, AJPF
verification supports the agent reasoning claim. It should not be overstated as
a complete deployed real-time timing guarantee unless additional evidence is
provided.
"""
        )

    with st.expander("3.6 Reference pattern view from AdvoCATE"):
        st.markdown(
            """
The image below shows the original AdvoCATE GSN pattern/model used as the
reference structure for this guidance view.

RACeD does not reproduce the full detailed model in the visualisation tab.
Instead, it presents selected guidance-level elements to support readability,
interaction, and discussion.
"""
        )

        if PATTERN_IMAGE_PATH.exists():
            st.image(
                str(PATTERN_IMAGE_PATH),
                caption="IndependentSafetyEnforcementV4 reference pattern from AdvoCATE",
                width="stretch",
            )
        else:
            st.info(
                "Pattern image not found. Place `IndependentSafetyEnforcementV4.png` "
                "in the same folder as `app.py` to display the reference pattern view."
            )

    st.info(
        """
This tab generates **textual pattern guidance** for the entered parameter
bindings. The GSN graph in Tab 4 is only a visual representation of selected
parts of that guidance. RACeD does not inspect source code, run AJPF, run Dafny,
read ROS logs, validate evidence, or approve a safety claim.
"""
    )

    with st.form("independent_safety_inputs"):
        st.subheader("Pattern parameter bindings")

        col_a, col_b = st.columns(2)

        with col_a:
            boundary = st.text_input(
                "boundary",
                "Geofence/proximity boundary around restricted or protective areas",
            )

            trigger = st.text_input(
                "trigger",
                "geofenceViolation or safeHaltRequest",
            )

            ss = st.text_input(
                "ss",
                "SS_HaltController / Safety System Gwendolen agent",
            )

            sras = st.text_input(
                "sras",
                "SRAS_node / ROS navigation stack motion controller",
            )

            safe_state = st.text_input(
                "safeState",
                "EnforcedStop / SafeHaltActive / zero-velocity stopped state",
            )

            reqs = st.text_input(
                "reqs",
                "SS A3.3.1, SS A4.3.4.1; implemented as R1, R2, R3, R4",
            )

            ss_impl = st.text_input(
                "ssImpl",
                "Gwendolen/MCAPL Safety System agent integrated through Java environment and ROS-A/rosbridge",
            )

            input_topics = st.text_input(
                "inputTopics",
                "/scan, /odom, /safehalt_request",
            )

            output_topic = st.text_input(
                "outputTopic",
                "/gwendolen_control or zero-velocity command path via cmd_vel_interceptor",
            )

        with col_b:
            geofence_threshold = st.text_input(
                "geofenceThreshold",
                "min(LiDAR range) < 0.45 m",
            )

            safe_halt_request = st.text_input(
                "safeHaltRequest",
                "Message/event published on /safehalt_request",
            )

            motion_state_source = st.text_input(
                "motionStateSource",
                "/odom, using linear and angular velocity to determine robotStillMoving / robotMoves",
            )

            reasoning_bound = st.text_input(
                "reasoningBound",
                "Tick generated by the waiting action after a fixed delay, e.g. 2 seconds",
            )

            reasoning_bound_semantics = st.text_area(
                "reasoningBoundSemantics",
                (
                    "AJPF verifies the agent-level tick/percept abstraction; "
                    "deployed real-time stopping claims require separate timing "
                    "or implementation evidence"
                ),
                height=90,
            )

            interceptor = st.text_input(
                "interceptor",
                "cmd_vel_interceptor orchestrator/interceptor node",
            )

            reset_condition = st.text_input(
                "resetCondition",
                "Explicit reset or clearance condition before motion commands may be allowed again",
            )

        st.subheader("Evidence references or evidence placeholders")

        col_c, col_d = st.columns(2)

        with col_c:
            formal_req_evidence = st.text_area(
                "formalReqEvidence",
                "FRET/FRETish-derived requirements and AJPF LTL/BDI-style properties for R1–R4",
                height=80,
            )

            ajpf_prop_override = st.text_area(
                "ajpfProp_override",
                "AJPF/MCAPL property: whenever geofence_violation or too_close percept occurs, the agent performs entry_stop",
                height=80,
            )

            ajpf_prop_safehalt = st.text_area(
                "ajpfProp_safehalt",
                (
                    "AJPF/MCAPL safe-halt properties: safe_halt_req with tick and "
                    "no halt_observed leads to entry_stop; safe_halt_req with "
                    "halt_observed leads to safe_halt_active; safe_halt_active "
                    "with move percept leads to entry_stop"
                ),
                height=120,
            )

            dafny_prop_interceptor = st.text_area(
                "dafnyProp_interceptor",
                (
                    "Dafny model proof of command-interception/orchestration logic: "
                    "when stop is requested, only zero-velocity commands are published; "
                    "when no stop is requested, SRAS commands are forwarded unchanged. "
                    "The deployed Python orchestrator remains outside the Dafny proof "
                    "and requires traceability/testing evidence."
                ),
                height=130,
            )

        with col_d:
            verification_environment = st.text_area(
                "verificationEnvironment",
                (
                    "AJPF verification environment abstracting raw ROS topics into "
                    "percepts/beliefs such as geofence_violation, safe_halt_req, "
                    "tick, halt_observed, safe_halt_active, and move"
                ),
                height=100,
            )

            prism_prop_override = st.text_area(
                "prismProp_override",
                "Not used as primary evidence in this instance; AJPF/MCAPL is used as primary formal override evidence",
                height=80,
            )

            prism_prop_persist = st.text_area(
                "prismProp_persist",
                "PRISM persistence property if available; otherwise persistence supported by AJPF R3/R4, interceptor evidence, and simulation/physical traces",
                height=90,
            )

            arch_evidence = st.text_area(
                "archEvidence",
                "Safety System architecture/design evidence showing Gwendolen agent, Java environment, ROS-A/rosbridge interface, and SS/SRAS separation",
                height=80,
            )

            integration_evidence = st.text_area(
                "integrationEvidence",
                "ROS integration evidence showing subscriptions to /scan, /odom, /safehalt_request, and command interception through cmd_vel_interceptor",
                height=80,
            )

            sim_evidence = st.text_area(
                "simEvidence",
                "Gazebo/SafeROS simulation logs/video showing induced geofence violation causes SS stop and continued suppression of SRAS motion commands",
                height=80,
            )

            phys_evidence = st.text_area(
                "physEvidence",
                "Physical robot test logs/video showing SS stop behaviour on the robot platform, where available",
                height=80,
            )

        st.subheader("Guidance emphasis")

        col_e, col_f, col_g = st.columns(3)

        with col_e:
            include_safe_halt = st.checkbox(
                "Include safe-halt R2/R3/R4 guidance",
                value=True,
            )

        with col_f:
            include_dafny_limitation = st.checkbox(
                "Highlight Dafny model vs deployed Python limitation",
                value=True,
            )

        with col_g:
            include_timing_caution = st.checkbox(
                "Highlight tick/percept timing caution",
                value=True,
            )

        submitted = st.form_submit_button("Generate guidance")

    if submitted:
        result = evaluate_enforcement_guidance(
            include_safe_halt=include_safe_halt,
            include_dafny_limitation=include_dafny_limitation,
            include_timing_caution=include_timing_caution,
        )

        st.session_state["independent_safety_params"] = {
            "boundary": boundary,
            "trigger": trigger,
            "ss": ss,
            "sras": sras,
            "safeState": safe_state,
            "reqs": reqs,
            "ssImpl": ss_impl,
            "inputTopics": input_topics,
            "outputTopic": output_topic,
            "geofenceThreshold": geofence_threshold,
            "safeHaltRequest": safe_halt_request,
            "motionStateSource": motion_state_source,
            "reasoningBound": reasoning_bound,
            "reasoningBoundSemantics": reasoning_bound_semantics,
            "interceptor": interceptor,
            "resetCondition": reset_condition,
            "prismProp_override": prism_prop_override,
            "prismProp_persist": prism_prop_persist,
            "formalReqEvidence": formal_req_evidence,
            "ajpfProp_override": ajpf_prop_override,
            "ajpfProp_safehalt": ajpf_prop_safehalt,
            "dafnyProp_interceptor": dafny_prop_interceptor,
            "verificationEnvironment": verification_environment,
            "simEvidence": sim_evidence,
            "physEvidence": phys_evidence,
            "archEvidence": arch_evidence,
            "integrationEvidence": integration_evidence,
        }

        st.session_state["independent_safety_result"] = result

        st.success(
            "Pattern guidance has been instantiated using the entered parameter "
            "bindings. Review the textual guidance below, then open the GSN "
            "visualisation tab."
        )

        st.subheader("Generated textual guidance")

        st.markdown(
            """
The generated guidance below is not a new safety result. It is the
`IndependentSafetyEnforcement` pattern interpreted using the entered parameter
bindings.
"""
        )

        st.subheader("Guidance summary")
        st.info(result.guidance_text)

        st.subheader("Argument branches")

        for branch in result.branches:
            st.markdown(f"- **{branch['name']}**: {branch['guidance']}")

        st.subheader("Expected evidence guidance")

        for item in result.expected_evidence:
            st.markdown(f"- {item}")

        if result.cautions:
            st.subheader("Cautions and limitations")
            for caution in result.cautions:
                st.warning(caution)

        st.caption(
            "RACeD does not inspect implementation artefacts, run AJPF, run Dafny, "
            "read ROS logs, validate evidence, or approve a safety claim."
        )


with tab4:
    st.header("Visualise selected GSN structure")

    if "independent_safety_result" not in st.session_state:
        st.info("Generate guidance in Tab 3 first.")
    else:
        result = st.session_state["independent_safety_result"]
        params = st.session_state["independent_safety_params"]

        dot = generate_independent_safety_enforcement_dot(
            params=params,
            result=result,
        )

        st.markdown(
            """
The guidance generated in Tab 3 includes textual guidance, expected evidence
types, argument branches, and cautions. The graph below visualises a selected
GSN structure derived from that guidance.

It is not the whole guidance output and it is not a complete assurance case.
It shows the top-level claim, main argument branches, key contexts, selected
evidence expectations, and important limitations for the entered parameter
bindings.

A complete assurance case would need to instantiate and justify all lower-level
claims, attach the actual evidence artefacts, and address the stated limitations.
"""
        )

        st.subheader("GSN visualisation")

        zoom_percent = st.slider(
            "GSN zoom",
            min_value=60,
            max_value=180,
            value=100,
            step=10,
            help="Increase this value to enlarge the visual GSN structure.",
        )

        viewer_height = st.slider(
            "Viewer height",
            min_value=600,
            max_value=1800,
            value=1000,
            step=100,
            help="Increase this value to make the viewing window taller.",
        )

        html_visualisation = generate_independent_safety_enforcement_html_visualisation(
            params=params,
            result=result,
            zoom_percent=zoom_percent,
            viewer_height=viewer_height,
        )

        components.html(
            html_visualisation,
            height=viewer_height + 60,
            scrolling=True,
        )

        st.download_button(
            label="Download DOT",
            data=dot,
            file_name="independent_safety_enforcement_guidance.dot",
            mime="text/vnd.graphviz",
        )