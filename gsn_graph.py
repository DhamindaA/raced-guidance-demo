from html import escape


def dot_escape(text: str) -> str:
    """
    Escapes text for safe insertion into Graphviz DOT labels.
    """
    return (
        str(text)
        .replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
    )


def html_escape(text: str) -> str:
    """
    Escapes text for safe insertion into HTML.
    """
    return escape(str(text)).replace("\n", "<br>")


def shorten(text: str, max_len: int = 260) -> str:
    """
    Shortens long labels for the HTML visualisation.
    """
    text = str(text)
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."


def generate_independent_safety_enforcement_dot(
    params: dict,
    result,
) -> str:
    """
    Generates a selected guidance-level DOT GSN graph for the
    IndependentSafetyEnforcement pattern.

    This DOT is available for download. The on-screen visualisation uses an
    HTML/CSS renderer so users do not need the Graphviz executable installed.
    """

    boundary = dot_escape(params["boundary"])
    trigger = dot_escape(params["trigger"])
    ss = dot_escape(params["ss"])
    sras = dot_escape(params["sras"])
    safe_state = dot_escape(params["safeState"])
    reqs = dot_escape(params["reqs"])
    ss_impl = dot_escape(params["ssImpl"])
    input_topics = dot_escape(params["inputTopics"])
    output_topic = dot_escape(params["outputTopic"])
    geofence_threshold = dot_escape(params["geofenceThreshold"])
    safe_halt_request = dot_escape(params["safeHaltRequest"])
    motion_state_source = dot_escape(params["motionStateSource"])
    reasoning_bound = dot_escape(params["reasoningBound"])
    reasoning_bound_semantics = dot_escape(params["reasoningBoundSemantics"])
    interceptor = dot_escape(params["interceptor"])
    reset_condition = dot_escape(params["resetCondition"])
    formal_req_evidence = dot_escape(params["formalReqEvidence"])
    ajpf_prop_override = dot_escape(params["ajpfProp_override"])
    ajpf_prop_safehalt = dot_escape(params["ajpfProp_safehalt"])
    dafny_prop_interceptor = dot_escape(params["dafnyProp_interceptor"])
    verification_environment = dot_escape(params["verificationEnvironment"])
    sim_evidence = dot_escape(params["simEvidence"])
    phys_evidence = dot_escape(params["physEvidence"])
    arch_evidence = dot_escape(params["archEvidence"])
    integration_evidence = dot_escape(params["integrationEvidence"])
    prism_prop_persist = dot_escape(params["prismProp_persist"])

    cautions_text = (
        "\\n".join(dot_escape(caution) for caution in result.cautions)
        if result.cautions
        else "No additional cautions selected."
    )

    return f'''
digraph IndependentSafetyEnforcement_Guidance {{
  graph [
    rankdir=TB,
    bgcolor="white",
    label="IndependentSafetyEnforcement - Selected Guidance-Level GSN Structure",
    labelloc=t,
    fontsize=20,
    fontname="Arial"
  ];

  node [fontname="Arial", fontsize=10, margin="0.05,0.03"];
  edge [fontname="Arial", fontsize=9];

  G_1 [
    shape=box,
    style="filled,rounded",
    fillcolor="#D9EAF7",
    color="#4F81BD",
    label="G_1\\n{ss} enforces safety-critical stopping for {boundary} under all relevant operating modes by detecting {trigger}, overriding or blocking {sras} motion commands through {interceptor}, and maintaining {safe_state}."
  ];

  C_1_1 [
    shape=box,
    style="filled,rounded,dashed",
    fillcolor="#EDEDED",
    color="#7F7F7F",
    label="C_1_1\\nBoundary/trigger definitions\\nboundary = {boundary}\\ntrigger = {trigger}\\ngeofence/proximity threshold = {geofence_threshold}\\nsafe halt request = {safe_halt_request}"
  ];

  C_1_2 [
    shape=box,
    style="filled,rounded,dashed",
    fillcolor="#EDEDED",
    color="#7F7F7F",
    label="C_1_2\\nSafety System implementation\\n{ss_impl}\\nInputs: {input_topics}\\nMotion-state source: {motion_state_source}\\nStop output/control path: {output_topic}"
  ];

  C_1_3 [
    shape=box,
    style="filled,rounded,dashed",
    fillcolor="#EDEDED",
    color="#7F7F7F",
    label="C_1_3\\nReasoning-bound semantics\\n{reasoning_bound}\\n{reasoning_bound_semantics}"
  ];

  C_1_4 [
    shape=box,
    style="filled,rounded,dashed",
    fillcolor="#EDEDED",
    color="#7F7F7F",
    label="C_1_4\\nFormal verification environment\\n{verification_environment}\\nRaw ROS topics are abstracted into agent percepts/beliefs for verification of Safety System decision logic."
  ];

  S_1 [
    shape=parallelogram,
    style="filled",
    fillcolor="#FFF2CC",
    color="#B8860B",
    label="S_1\\nArgument by trigger detection, override priority, independent enforcement through {interceptor}, formal verification, and persistence of enforced stopping."
  ];

  G_1_1 [
    shape=box,
    style="filled,rounded",
    fillcolor="#D9EAF7",
    color="#4F81BD",
    label="G_1_1\\nTrigger detection and interpretation."
  ];

  G_1_2 [
    shape=box,
    style="filled,rounded",
    fillcolor="#D9EAF7",
    color="#4F81BD",
    label="G_1_2\\nOverride priority."
  ];

  G_1_3 [
    shape=box,
    style="filled,rounded",
    fillcolor="#D9EAF7",
    color="#4F81BD",
    label="G_1_3\\nIndependent enforcement path."
  ];

  G_1_4 [
    shape=box,
    style="filled,rounded",
    fillcolor="#D9EAF7",
    color="#4F81BD",
    label="G_1_4\\nFormal verification of SS and integration logic."
  ];

  G_1_5 [
    shape=box,
    style="filled,rounded",
    fillcolor="#D9EAF7",
    color="#4F81BD",
    label="G_1_5\\nPersistence of stopped state."
  ];

  E_1_1 [
    shape=ellipse,
    style="filled",
    fillcolor="#D9EAD3",
    color="#6AA84F",
    label="E_1_1\\nImplementation/integration evidence\\n{arch_evidence}\\n{integration_evidence}"
  ];

  E_1_2 [
    shape=ellipse,
    style="filled",
    fillcolor="#D9EAD3",
    color="#6AA84F",
    label="E_1_2\\nOverride evidence\\n{ajpf_prop_override}\\n{sim_evidence}\\n{phys_evidence}"
  ];

  E_1_3 [
    shape=ellipse,
    style="filled",
    fillcolor="#D9EAD3",
    color="#6AA84F",
    label="E_1_3\\nIndependent command-path evidence\\n{dafny_prop_interceptor}"
  ];

  E_1_4 [
    shape=ellipse,
    style="filled",
    fillcolor="#D9EAD3",
    color="#6AA84F",
    label="E_1_4\\nFormal verification evidence\\n{formal_req_evidence}\\n{ajpf_prop_safehalt}"
  ];

  E_1_5 [
    shape=ellipse,
    style="filled",
    fillcolor="#D9EAD3",
    color="#6AA84F",
    label="E_1_5\\nPersistence evidence\\n{prism_prop_persist}\\n{sim_evidence}\\n{phys_evidence}"
  ];

  O_2 [
    shape=box,
    style="filled,rounded",
    fillcolor="#FCE4D6",
    color="#C55A11",
    label="Cautions selected\\n{cautions_text}"
  ];

  G_1 -> C_1_1 [style=dashed, arrowhead=onormal, label="InContextOf"];
  G_1 -> C_1_2 [style=dashed, arrowhead=onormal, label="InContextOf"];
  G_1 -> C_1_3 [style=dashed, arrowhead=onormal, label="InContextOf"];
  G_1 -> S_1 [label="SupportedBy"];

  S_1 -> G_1_1 [label="SupportedBy"];
  S_1 -> G_1_2 [label="SupportedBy"];
  S_1 -> G_1_3 [label="SupportedBy"];
  S_1 -> G_1_4 [label="SupportedBy"];
  S_1 -> G_1_5 [label="SupportedBy"];

  G_1_1 -> E_1_1 [label="SupportedBy"];
  G_1_2 -> E_1_2 [label="SupportedBy"];
  G_1_3 -> E_1_3 [label="SupportedBy"];
  G_1_4 -> E_1_4 [label="SupportedBy"];
  G_1_4 -> C_1_4 [style=dashed, arrowhead=onormal, label="InContextOf"];
  G_1_5 -> E_1_5 [label="SupportedBy"];
  G_1_5 -> O_2 [style=dashed, label="Limitations"];
}}
'''


def node_html(
    node_id: str,
    title: str,
    body: str,
    css_class: str,
    x: int,
    y: int,
    w: int,
    h: int,
) -> str:
    return f"""
    <div class="node {css_class}" style="left:{x}px; top:{y}px; width:{w}px; height:{h}px;">
        <div class="node-id">{html_escape(node_id)}</div>
        <div class="node-title">{html_escape(title)}</div>
        <div class="node-body">{html_escape(body)}</div>
    </div>
    """


def generate_independent_safety_enforcement_html_visualisation(
    params: dict,
    result,
    zoom_percent: int = 100,
    viewer_height: int = 1000,
) -> str:
    """
    Generates a zoomable HTML/CSS visualisation of the selected GSN structure.
    This does not require the Graphviz executable.
    """

    scale = zoom_percent / 100
    base_width = 2200
    base_height = 1280
    canvas_width = int(base_width * scale)
    canvas_height = int(base_height * scale)

    boundary = shorten(params["boundary"], 180)
    trigger = shorten(params["trigger"], 160)
    ss = shorten(params["ss"], 160)
    sras = shorten(params["sras"], 160)
    safe_state = shorten(params["safeState"], 160)
    reqs = shorten(params["reqs"], 160)
    ss_impl = shorten(params["ssImpl"], 210)
    input_topics = shorten(params["inputTopics"], 150)
    output_topic = shorten(params["outputTopic"], 170)
    geofence_threshold = shorten(params["geofenceThreshold"], 120)
    safe_halt_request = shorten(params["safeHaltRequest"], 120)
    motion_state_source = shorten(params["motionStateSource"], 160)
    reasoning_bound = shorten(params["reasoningBound"], 170)
    reasoning_bound_semantics = shorten(params["reasoningBoundSemantics"], 210)
    interceptor = shorten(params["interceptor"], 140)
    reset_condition = shorten(params["resetCondition"], 160)
    formal_req_evidence = shorten(params["formalReqEvidence"], 180)
    ajpf_prop_override = shorten(params["ajpfProp_override"], 180)
    ajpf_prop_safehalt = shorten(params["ajpfProp_safehalt"], 210)
    dafny_prop_interceptor = shorten(params["dafnyProp_interceptor"], 220)
    verification_environment = shorten(params["verificationEnvironment"], 200)
    sim_evidence = shorten(params["simEvidence"], 160)
    phys_evidence = shorten(params["physEvidence"], 150)
    arch_evidence = shorten(params["archEvidence"], 160)
    integration_evidence = shorten(params["integrationEvidence"], 160)
    prism_prop_persist = shorten(params["prismProp_persist"], 170)

    cautions_text = (
        "<br>".join(html_escape(caution) for caution in result.cautions)
        if result.cautions
        else "No additional cautions selected."
    )

    nodes = []

    nodes.append(
        node_html(
            "G_1",
            "Safety-critical stopping is enforced",
            f"{ss} enforces stopping for {boundary} by detecting {trigger}, overriding/blocking {sras} through {interceptor}, and maintaining {safe_state}.",
            "goal",
            650,
            40,
            900,
            135,
        )
    )

    nodes.append(
        node_html(
            "C_1_1",
            "Boundary and trigger context",
            f"Boundary: {boundary}<br>Trigger: {trigger}<br>Threshold: {geofence_threshold}<br>Safe halt request: {safe_halt_request}",
            "context",
            40,
            40,
            500,
            150,
        )
    )

    nodes.append(
        node_html(
            "C_1_2",
            "Implementation context",
            f"{ss_impl}<br>Inputs: {input_topics}<br>Motion state: {motion_state_source}<br>Output: {output_topic}",
            "context",
            1660,
            40,
            500,
            170,
        )
    )

    nodes.append(
        node_html(
            "S_1",
            "Argument strategy",
            f"Argument by trigger detection, override priority, independent enforcement through {interceptor}, formal verification, and persistence.",
            "strategy",
            760,
            235,
            680,
            115,
        )
    )

    branch_y = 430
    evidence_y = 650
    branch_w = 380
    evidence_h = 170

    branches = [
        (
            "G_1_1",
            "Trigger detection and interpretation",
            f"{ss} receives and interprets {input_topics}, including motion state from {motion_state_source}.",
            "E_1_1",
            "Implementation and interface evidence",
            f"{arch_evidence}<br>{integration_evidence}",
            40,
        ),
        (
            "G_1_2",
            "Override priority",
            f"If {trigger} occurs, {ss} enforces {safe_state} regardless of {sras} command intent.",
            "E_1_2",
            "Override evidence",
            f"{ajpf_prop_override}<br>{sim_evidence}<br>{phys_evidence}",
            480,
        ),
        (
            "G_1_3",
            "Independent enforcement path",
            f"{ss} uses {interceptor} and does not depend on correct {sras} behaviour.",
            "E_1_3",
            "Command-path evidence",
            f"{dafny_prop_interceptor}",
            920,
        ),
        (
            "G_1_4",
            "Formal verification",
            f"Safety System reasoning and interceptor logic are verified against {reqs}.",
            "E_1_4",
            "Formal verification evidence",
            f"{formal_req_evidence}<br>{ajpf_prop_safehalt}<br>Environment: {verification_environment}",
            1360,
        ),
        (
            "G_1_5",
            "Persistence of stopped state",
            f"Once {safe_state} is active, stopping is maintained until reset or clearance: {reset_condition}.",
            "E_1_5",
            "Persistence evidence",
            f"{prism_prop_persist}<br>{sim_evidence}<br>{phys_evidence}",
            1800,
        ),
    ]

    for g_id, g_title, g_body, e_id, e_title, e_body, x in branches:
        nodes.append(node_html(g_id, g_title, g_body, "goal", x, branch_y, branch_w, 135))
        nodes.append(node_html(e_id, e_title, e_body, "evidence", x, evidence_y, branch_w, evidence_h))

    nodes.append(
        node_html(
            "J_1_4_3",
            "Timing interpretation",
            f"{reasoning_bound}<br>{reasoning_bound_semantics}",
            "context",
            1360,
            875,
            380,
            150,
        )
    )

    nodes.append(
        node_html(
            "O_1",
            "Guidance output",
            "This visualisation shows selected GSN guidance only. It does not validate evidence or approve the safety claim.",
            "output",
            760,
            1040,
            620,
            120,
        )
    )

    nodes.append(
        node_html(
            "O_2",
            "Cautions selected",
            cautions_text,
            "caution",
            1430,
            1040,
            650,
            150,
        )
    )

    # SVG lines are approximate visual connectors for the selected GSN skeleton.
    lines = """
    <svg class="links" width="2200" height="1280" viewBox="0 0 2200 1280">
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L8,3 z" fill="#666" />
            </marker>
            <marker id="arrowDashed" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L8,3 z" fill="#888" />
            </marker>
        </defs>

        <!-- context links to G_1 -->
        <line x1="540" y1="110" x2="650" y2="110" stroke="#888" stroke-width="2" stroke-dasharray="6,4" marker-end="url(#arrowDashed)" />
        <line x1="1660" y1="125" x2="1550" y2="115" stroke="#888" stroke-width="2" stroke-dasharray="6,4" marker-end="url(#arrowDashed)" />

        <!-- G_1 to S_1 -->
        <line x1="1100" y1="175" x2="1100" y2="235" stroke="#555" stroke-width="2.5" marker-end="url(#arrow)" />

        <!-- S_1 to branch goals -->
        <line x1="1100" y1="350" x2="230" y2="430" stroke="#555" stroke-width="2.5" marker-end="url(#arrow)" />
        <line x1="1100" y1="350" x2="670" y2="430" stroke="#555" stroke-width="2.5" marker-end="url(#arrow)" />
        <line x1="1100" y1="350" x2="1110" y2="430" stroke="#555" stroke-width="2.5" marker-end="url(#arrow)" />
        <line x1="1100" y1="350" x2="1550" y2="430" stroke="#555" stroke-width="2.5" marker-end="url(#arrow)" />
        <line x1="1100" y1="350" x2="1990" y2="430" stroke="#555" stroke-width="2.5" marker-end="url(#arrow)" />

        <!-- branch goals to evidence -->
        <line x1="230" y1="565" x2="230" y2="650" stroke="#555" stroke-width="2.5" marker-end="url(#arrow)" />
        <line x1="670" y1="565" x2="670" y2="650" stroke="#555" stroke-width="2.5" marker-end="url(#arrow)" />
        <line x1="1110" y1="565" x2="1110" y2="650" stroke="#555" stroke-width="2.5" marker-end="url(#arrow)" />
        <line x1="1550" y1="565" x2="1550" y2="650" stroke="#555" stroke-width="2.5" marker-end="url(#arrow)" />
        <line x1="1990" y1="565" x2="1990" y2="650" stroke="#555" stroke-width="2.5" marker-end="url(#arrow)" />

        <!-- formal verification branch to timing justification -->
        <line x1="1550" y1="820" x2="1550" y2="875" stroke="#888" stroke-width="2" stroke-dasharray="6,4" marker-end="url(#arrowDashed)" />

        <!-- persistence branch to guidance output -->
        <line x1="1990" y1="820" x2="1370" y2="1040" stroke="#555" stroke-width="2.5" marker-end="url(#arrow)" />

        <!-- guidance output to cautions -->
        <line x1="1380" y1="1100" x2="1430" y2="1100" stroke="#888" stroke-width="2" stroke-dasharray="6,4" marker-end="url(#arrowDashed)" />
    </svg>
    """

    return f"""
    <style>
        body {{
            margin: 0;
            font-family: Arial, sans-serif;
            background: white;
        }}

        .viewer {{
            width: 100%;
            height: {viewer_height}px;
            overflow: auto;
            border: 1px solid #d9d9d9;
            background: white;
        }}

        .canvas {{
            position: relative;
            width: {canvas_width}px;
            height: {canvas_height}px;
            background: white;
        }}

        .diagram {{
            position: relative;
            width: {base_width}px;
            height: {base_height}px;
            transform: scale({scale});
            transform-origin: top left;
        }}

        .links {{
            position: absolute;
            left: 0;
            top: 0;
            z-index: 0;
            pointer-events: none;
        }}

        .node {{
            position: absolute;
            box-sizing: border-box;
            padding: 10px 12px;
            border-radius: 12px;
            overflow: hidden;
            z-index: 2;
            font-size: 14px;
            line-height: 1.25;
            box-shadow: 0 1px 4px rgba(0,0,0,0.10);
        }}

        .node-id {{
            font-weight: bold;
            font-size: 13px;
            margin-bottom: 4px;
        }}

        .node-title {{
            font-weight: bold;
            margin-bottom: 5px;
        }}

        .node-body {{
            font-size: 13px;
        }}

        .goal {{
            background: #D9EAF7;
            border: 2px solid #4F81BD;
        }}

        .strategy {{
            background: #FFF2CC;
            border: 2px solid #B8860B;
            transform: skew(-8deg);
        }}

        .strategy .node-id,
        .strategy .node-title,
        .strategy .node-body {{
            transform: skew(8deg);
        }}

        .context {{
            background: #EDEDED;
            border: 2px dashed #7F7F7F;
        }}

        .evidence {{
            background: #D9EAD3;
            border: 2px solid #6AA84F;
            border-radius: 50px;
        }}

        .output {{
            background: #D9EAD3;
            border: 2px solid #6AA84F;
            border-radius: 50px;
        }}

        .caution {{
            background: #FCE4D6;
            border: 2px solid #C55A11;
        }}
    </style>

    <div class="viewer">
        <div class="canvas">
            <div class="diagram">
                {lines}
                {''.join(nodes)}
            </div>
        </div>
    </div>
    """