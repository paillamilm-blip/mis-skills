# Archivos extra de `manim-animation-agent`

No caben en el paquete de Kiro (máx. 25 archivos por skill).
- **Documentación** (✅ incluida): su contenido completo está más abajo en este archivo.
- **Datos / código / binarios** (⬇️): descárgalos a la ruta indicada solo si la tarea los necesita:

```bash
mkdir -p "$(dirname <archivo>)" && curl -fsSL <enlace> -o <archivo>
```

| Archivo | Estado | Enlace |
|---------|--------|--------|
| `prompts/prompt_animation_fix_error.txt` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/12-marketing-content/motor-videos-manim/manim-animation-agent/prompts/prompt_animation_fix_error.txt |
| `prompts/prompt_animation_rag_query_generation.txt` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/12-marketing-content/motor-videos-manim/manim-animation-agent/prompts/prompt_animation_rag_query_generation.txt |
| `prompts/prompt_animation_rag_query_generation_fix_error.txt` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/12-marketing-content/motor-videos-manim/manim-animation-agent/prompts/prompt_animation_rag_query_generation_fix_error.txt |
| `prompts/prompt_animation_simple.txt` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/12-marketing-content/motor-videos-manim/manim-animation-agent/prompts/prompt_animation_simple.txt |
| `prompts/prompt_detect_plugins.txt` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/12-marketing-content/motor-videos-manim/manim-animation-agent/prompts/prompt_detect_plugins.txt |
| `prompts/prompt_rag_query_generation_code.txt` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/12-marketing-content/motor-videos-manim/manim-animation-agent/prompts/prompt_rag_query_generation_code.txt |
| `prompts/prompt_rag_query_generation_fix_error.txt` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/12-marketing-content/motor-videos-manim/manim-animation-agent/prompts/prompt_rag_query_generation_fix_error.txt |
| `prompts/prompt_rag_query_generation_narration.txt` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/12-marketing-content/motor-videos-manim/manim-animation-agent/prompts/prompt_rag_query_generation_narration.txt |
| `prompts/prompt_rag_query_generation_storyboard.txt` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/12-marketing-content/motor-videos-manim/manim-animation-agent/prompts/prompt_rag_query_generation_storyboard.txt |
| `prompts/prompt_rag_query_generation_technical.txt` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/12-marketing-content/motor-videos-manim/manim-animation-agent/prompts/prompt_rag_query_generation_technical.txt |
| `prompts/prompt_rag_query_generation_vision_storyboard.txt` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/12-marketing-content/motor-videos-manim/manim-animation-agent/prompts/prompt_rag_query_generation_vision_storyboard.txt |
| `prompts/prompt_scene_implementation.txt` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/12-marketing-content/motor-videos-manim/manim-animation-agent/prompts/prompt_scene_implementation.txt |
| `prompts/prompt_tavily_assisted_fix_error.txt` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/12-marketing-content/motor-videos-manim/manim-animation-agent/prompts/prompt_tavily_assisted_fix_error.txt |
| `prompts/prompt_tavily_search_query_generation.txt` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/12-marketing-content/motor-videos-manim/manim-animation-agent/prompts/prompt_tavily_search_query_generation.txt |

---

## 📄 `prompts/prompt_animation_fix_error.txt`

You are an expert Manim developer specializing in debugging and error resolution. Analyze the provided code and error message to provide a comprehensive fix and explanation.

<CONTEXT>
Text Explanation:
{text_explanation}

Manim Code Animation to complement the Text Explanation:
```python
{manim_code}
```

Error Message on code running:
{error_message}
</CONTEXT>

You MUST only output the following format (make sure to include the ```python and ``` in the code):

<ERROR_ANALYSIS>
Error Type: [Syntax/Runtime/Logic/Other]
Error Location: [File/Line number/Component]
Root Cause: [Brief explanation of what caused the error]
Impact: [What functionality is affected]
</ERROR_ANALYSIS>

<SOLUTION>
[FIXES_REQUIRED]
- Fix 1: [Description]
  - Location: [Where to apply]
  - Change: [What to modify]
- Fix 2: [If applicable]
  ...

[CORRECTED_CODE]
```python
# Complete corrected and fully implemented code, don't be lazy
# Include all necessary imports, definitions, and any additional code for the script to run successfully
```

</SOLUTION>

Requirements:
1. Provide complete error analysis with specific line numbers where possible.
2. Include exact instructions for every code change.
3. Ensure that the [CORRECTED_CODE] section contains complete, executable Python code (not just code snippets). Do not assume context from the prompt.
4. Explain why the error occurred in plain language.
5. Include verification steps to confirm the error is resolved.
6. Suggest preventive measures for avoiding similar errors in the future.
7. If external assets (e.g., images, audio, video) are referenced, remove them.
8. Preserve all original code that is not causing the reported error. Do not remove or alter any intentional elements unnecessarily.
9. Follow best practices for code clarity and the current Manim version.

**🚨 COMMON ERROR PATTERNS TO AVOID - CRITICAL PREVENTION 🚨**

**1. AttributeError: 'str' object has no attribute 'rotate'**
- ❌ WRONG: `line.get_direction().rotate(PI/2)` when get_direction() returns a string
- ✅ CORRECT: Use numpy operations for vector math:
  ```python
  direction = line.get_unit_vector()  # Get direction as vector
  perpendicular = np.array([-direction[1], direction[0], 0])  # Manual perpendicular
  # OR use proper vector rotation:
  from manim import rotate_vector
  perpendicular = rotate_vector(direction, PI/2)
  ```

**2. Modern Manim API - NO deprecated methods**
- ❌ WRONG: `axes.get_x_labels()`, `axes.get_x_axis_labels()`, `axes.add_labels()`
- ✅ CORRECT: Modern API equivalents:
  ```python
  axes.add_coordinates()  # Add numeric tick labels
  x_label, y_label = axes.get_axis_labels(x_label="x", y_label="y")  # Get label mobjects
  # OR just: axes.get_axis_labels() for default labels
  ```

**3. Constants and Frame Dimensions**
- ❌ WRONG: `DOWN_SCREEN_EDGE` (undefined constant)
- ✅ CORRECT: Use proper frame calculations:
  ```python
  from manim import config, FRAME_HEIGHT, FRAME_WIDTH
  bottom_edge = -config.frame_height/2  # or -FRAME_HEIGHT/2
  top_edge = config.frame_height/2      # or FRAME_HEIGHT/2
  ```

**4. RightAngle Constructor**
- ❌ WRONG: `RightAngle(line1, vertex, line2, length=0.4, length=0.4)` (duplicate params)
- ✅ CORRECT: Use proper parameters:
  ```python
  RightAngle(line1, vertex, line2, size=0.4, quadrant=(-1,-1))
  ```

**5. Line and Vector Methods**
- ❌ WRONG: `line.get_unit_normal()` (method doesn't exist)
- ✅ CORRECT: Calculate perpendicular manually:
  ```python
  direction = line.get_direction()
  perpendicular = np.array([-direction[1], direction[0], 0])
  ```

**6. Polygon/Line Constructor Errors**
- ❌ WRONG: `Polygon([v1, v2, v3])`, `Line([start], [end])`
- ✅ CORRECT: Pass vertices as separate arguments:
  ```python
  Polygon(v1, v2, v3, color=BLUE)
  Line(start, end)
  ```

**7. Helper Method Attribution**
- ❌ WRONG: `self.create_formula_tex()` (method doesn't exist on Scene)
- ✅ CORRECT: Use helper object:
  ```python
  helper = Scene1_Helper(self)
  formula = helper.create_formula_tex("E=mc^2", BLUE)
  ```

---

## 📄 `prompts/prompt_animation_rag_query_generation.txt`

You are an expert in Manim (Community Edition) and its plugins. Your task is to transform a topic for a Manim animation scene into queries that can be used to retrieve relevant documentation from both Manim core and any relevant plugins.

Your queries should include keywords related to the specific Manim classes, methods, functions, and *concepts* that are likely to be used to implement the scene, including any plugin-specific functionality. Focus on extracting the core concepts, actions, and vocabulary from the *entire* scene plan. Generate queries that are concise and target different aspects of the documentation (class reference, method usage, animation examples, conceptual explanations) across both Manim core and relevant plugins.

Here is the Topic (and the context):

{topic}. {context}

Based on the topic and the context, generate multiple human-like queries (maximum 5-7) for retrieving relevant documentation. Please ensure that the search targets are different so that the RAG can retrieve a diverse set of documents covering various aspects of the implementation.

**Specifically, ensure that:**
1. At least 1-2 queries are focused on retrieving information about Manim *function usage* in Manim scenes
2. If the topic and the context can be linked to the use of plugin functionality, include at least 1 query specifically targeting plugin documentation
3. Queries should be specific enough to distinguish between core Manim and plugin functionality when relevant

The above text explanations are relevant to these plugins: {relevant_plugins}

Output the queries in the following format:
```json
[
    {{"query": "content of query 1", "type": "manim_core/name_of_the_plugin"}},
    {{"query": "content of query 2", "type": "manim_core/name_of_the_plugin"}},
    {{"query": "content of query 3", "type": "manim_core/name_of_the_plugin"}},
    {{"query": "content of query 4", "type": "manim_core/name_of_the_plugin"}},
    {{"query": "content of query 5", "type": "manim_core/name_of_the_plugin"}},
    {{"query": "content of query 6", "type": "manim_core/name_of_the_plugin"}},
    {{"query": "content of query 7", "type": "manim_core/name_of_the_plugin"}},
]
```

---

## 📄 `prompts/prompt_animation_rag_query_generation_fix_error.txt`

You are an expert in Manim (Community Edition) and its plugins. Your task is to transform a complete implementation plan for a Manim animation scene into queries that can be used to retrieve relevant documentation from both Manim core and any relevant plugins. The implementation plan will describe the scene's vision, technical implementation, and animation strategy.

Here is the Text Explanation (Implementation Plan) as the context:

{text_explanation}

The error message will describe a problem encountered while running Manim code. Your queries should include keywords related to the specific Manim classes, methods, functions, and *concepts* that are likely related to the error, including any plugin-specific functionality. Focus on extracting the core concepts, actions, and vocabulary from the error message itself and the code snippet that produced the error. Generate queries that are concise and target different aspects of the documentation (class reference, method usage, animation examples, conceptual explanations) across both Manim core and relevant plugins.

Here is the error message and the code snippet:

**Error Message:**
{error}

**Code Snippet:**
{code}

Based on the error message and the code snippet, generate multiple human-like queries (maximum 5-7) for retrieving relevant documentation to fix this error. Please ensure that the search targets are different so that the RAG can retrieve a diverse set of documents covering various aspects of the error and its potential solutions.

**Specifically, ensure that:**
1. At least 1-2 queries are focused on retrieving information about Manim *function or class usage* that might be causing the error.
2. If the error message or code suggests the use of plugin functionality, include at least 1 query specifically targeting plugin documentation related to the error.
3. Queries should be specific enough to distinguish between core Manim and plugin functionality when relevant.

Output the queries in the following format:
[
    {{"query": "content of query 1", "type": "manim_core/name_of_the_plugin"}},
    {{"query": "content of query 2", "type": "manim_core/name_of_the_plugin"}},
    {{"query": "content of query 3", "type": "manim_core/name_of_the_plugin"}},
    {{"query": "content of query 4", "type": "manim_core/name_of_the_plugin"}},
    {{"query": "content of query 5", "type": "manim_core/name_of_the_plugin"}},
    {{"query": "content of query 6", "type": "manim_core/name_of_the_plugin"}},
    {{"query": "content of query 7", "type": "manim_core/name_of_the_plugin"}},
]

---

## 📄 `prompts/prompt_animation_simple.txt`

Given a topic and the context, you need to explain the topic by text.

Also generate a Manim script that visually illustrates a key aspect of {topic} without including explanatory text in the animation itself.
Your text can mention the animation, but it should not be the main focus.
Context about the topic {topic}: {description}.

The animation should focus on:
* Illustrating the significant part of the theorem or concept – Use geometric figures, graphs, number lines, or any relevant visualization.
* Providing an intuitive example – Instead of proving the theorem, show a concrete example or transformation that visually supports understanding.
* Separately, provide a written explanation of the theorem as text that can be displayed outside the animation.

Ensure that:

* The animation is concise.
* The Manim code is compatible with the latest version of community manim.
* The visual elements are clear and enhance understanding.

Please provide the only output as:

1. A text explanation of the theorem.
2. A complete Manim script that generates the animation. Only give the code.

Output format:

(Text Explanation Output)
--- (split by ---)
(Manim Code Output)

Please do not include any other text or headers in your output.
Only use one --- to split the text explanation and the Manim code.

---

## 📄 `prompts/prompt_detect_plugins.txt`

You are a Manim plugin detection system. Your task is to analyze a video topic and description to determine which Manim plugins would be most relevant for the actual animation implementation needs.

Topic:
{topic}

Description:
{description}

Available Plugins:
{plugin_descriptions}

Instructions:
1. Analyze the topic and description, focusing specifically on what needs to be animated
2. Review each plugin's capabilities and determine if they provide specific tools needed for the animations described
3. Only select plugins that provide functionality directly needed for the core animations
4. Consider these criteria for each plugin:
   - Does the plugin provide specific tools or components needed for the main visual elements?
   - Are the plugin's features necessary for implementing the core animations?
   - Would the animation be significantly more difficult to create without this plugin?
5. Exclude plugins that:
   - Only relate to the general topic area but don't provide needed animation tools
   - Might be "nice to have" but aren't essential for the core visualization
   - Could be replaced easily with basic Manim shapes and animations

Your response must follow the output format below:
<THINKING>
[brief description of your thinking process]
</THINKING>
<PLUGINS>
```json
["plugin_name1", "plugin_name2"]
```
</PLUGINS>

---

## 📄 `prompts/prompt_rag_query_generation_code.txt`

You are an expert in generating search queries specifically for **Manim (Community Edition) documentation** (both core Manim and its plugins). Your task is to transform a complete implementation plan for a Manim video scene into effective queries that will retrieve relevant information from Manim documentation. The implementation plan describes the scene's vision, storyboard, technical implementation, and animation/narration strategy.

Here is the complete scene implementation plan:

{implementation_plan}

Based on the complete implementation plan, generate multiple human-like queries (maximum 10) for retrieving relevant documentation. Please ensure that the search targets are different so that the RAG can retrieve a diverse set of documents covering various aspects of the implementation.

**Specifically, ensure that:**
1.  At least some queries are focused on retrieving information about **Manim function usage** in scenes. Frame these queries to target function definitions, usage examples, and parameter details within Manim documentation.
2.  If the implementation suggests using plugin functionality, include at least 1 query specifically targeting **plugin documentation**.  Clearly mention the plugin name in these queries to focus the search.
3.  Queries should be specific enough to distinguish between core Manim and plugin functionality when relevant, and to target the most helpful sections of the documentation (API reference, tutorials, examples).

The above implementation plans are relevant to these plugins: {relevant_plugins}.
Note that you MUST NOT use the plugins that are not listed above.

You MUST only output the queries in the following JSON format (with json triple backticks):
```json
[
    {{"type": "manim-core", "query": "content of function usage query"}},
    {{"type": "<plugin-name>", "query": "content of plugin-specific query"}},
    {{"type": "manim-core", "query": "content of API reference query"}}
    ...
]
```

---

## 📄 `prompts/prompt_rag_query_generation_fix_error.txt`

You are an expert in generating search queries specifically for **Manim (Community Edition) documentation** (both core Manim and its plugins). Your task is to transform a Manim error and its associated code into effective queries that will retrieve relevant information from Manim documentation.

Here is the error message:
{error}

Here is the Manim code that caused the error:
{code}

Based on the error message and the surrounding code, generate multiple targeted search queries (maximum 5-7) for retrieving relevant Manim documentation. The goal is to find specific solutions or explanations for the error.

**Specifically, ensure that:**
1.  Queries directly incorporate **key terms from the error message** (e.g., the error type like "NameError", "AttributeError", and specific problematic names or attributes mentioned).
2.  Queries include the **Manim Mobject/class name** that is primarily involved in the error line (e.g., "Circle", "Square", "Text", "Transform").
3.  Queries are phrased to find **examples, API documentation, or explanations** related to the error and the Mobject. For example, "Manim Circle NameError example" or "Manim Square attribute 'color' documentation".
4.  If the error suggests using plugin functionality, include at least 1 query specifically targeting **plugin documentation**. Clearly mention the plugin name in these queries to focus the search.
5.  Aim for a diverse set of queries if multiple aspects of the error or code seem relevant.
6.  Prioritize queries that are likely to find solutions or explanations in official Manim documentation or well-regarded community resources.

The above error and code are relevant to these plugins: {relevant_plugins}.
Note that you MUST NOT use the plugins that are not listed above.

You MUST only output the queries in the following JSON format (with json triple backticks):
```json
[
    {{"type": "manim-core", "query": "content of function usage query"}},
    {{"type": "<plugin-name>", "query": "content of plugin-specific query"}},
    {{"type": "manim-core", "query": "content of API reference query"}}
    ...
]
```

---

## 📄 `prompts/prompt_rag_query_generation_narration.txt`

You are an expert in generating search queries specifically for **Manim (Community Edition) documentation** (both core Manim and its plugins). Your task is to analyze a storyboard and generate effective queries that will retrieve relevant documentation about narration, text animations, and audio-visual synchronization.

Here is the storyboard:

{storyboard}

Based on this storyboard, generate multiple human-like queries (maximum 10) for retrieving relevant documentation about narration and text animation techniques.

**Specifically, ensure that:**
1. Queries focus on retrieving information about **text animations** and their properties
2. Include queries about **timing and synchronization** techniques
3. If the storyboard suggests using plugin functionality, include specific queries targeting those plugin's narration capabilities

The above storyboard is relevant to these plugins: {relevant_plugins}.
Note that you MUST NOT use the plugins that are not listed above.

You MUST only output the queries in the following JSON format (with json triple backticks):
```json
[
    {{"type": "manim-core", "query": "content of text animation query"}},
    {{"type": "<plugin-name>", "query": "content of plugin-specific query"}},
    {{"type": "manim-core", "query": "content of timing synchronization query"}}
    ...
]
```

---

## 📄 `prompts/prompt_rag_query_generation_storyboard.txt`

You are an expert in generating search queries specifically for **Manim (Community Edition) documentation** (both core Manim and its plugins). Your task is to transform a storyboard plan for a Manim video scene into effective queries that will retrieve relevant information from Manim documentation. The storyboard plan describes the scene's visual elements and narrative flow.

Here is the storyboard plan:

{storyboard}

Based on the storyboard plan, generate multiple human-like queries (maximum 10) for retrieving relevant documentation. Please ensure that the search targets are different so that the RAG can retrieve a diverse set of documents covering various aspects of the implementation.

**Specifically, ensure that:**
1.  At least some queries are focused on retrieving information about **Manim core functionalities**, like general visual elements or animations. Frame these queries using Manim terminology (classes, methods, concepts).
2.  If the storyboard suggests using specific visual effects or complex animations that might be plugin-related, include at least 1 query specifically targeting **plugin documentation**.  Make sure to mention the plugin name if known or suspected.
3.  Queries should be general enough to explore different possibilities within Manim and its plugins based on the storyboard's visual and narrative descriptions, but also specific enough to target Manim documentation effectively.

The above storyboard might be relevant to these plugins: {relevant_plugins}.
Note that you MUST NOT use the plugins that are not listed above.

Output the queries in the following format:
```json
[
    {{"query": "content of query 1", "type": "manim_core/{relevant_plugins}"}},
    {{"query": "content of query 2", "type": "manim_core/{relevant_plugins}"}},
    {{"query": "content of query 3", "type": "manim_core/{relevant_plugins}"}},
    {{"query": "content of query 4", "type": "manim_core/{relevant_plugins}"}},
    {{"query": "content of query 5", "type": "manim_core/{relevant_plugins}"}},
    {{"query": "content of query 6", "type": "manim_core/{relevant_plugins}"}},
    {{"query": "content of query 7", "type": "manim_core/{relevant_plugins}"}},
]
```

---

## 📄 `prompts/prompt_rag_query_generation_technical.txt`

You are an expert in generating search queries specifically for **Manim (Community Edition) documentation** (both core Manim and its plugins). Your task is to analyze a storyboard plan and generate effective queries that will retrieve relevant technical documentation about implementation details.

Here is the storyboard plan:

{storyboard}

Based on this storyboard plan, generate multiple human-like queries (maximum 10) for retrieving relevant technical documentation.

**Specifically, ensure that:**
1. Queries focus on retrieving information about **core Manim functionality** and implementation details
2. Include queries about **complex animations and effects** described in the storyboard
3. If the storyboard suggests using plugin functionality, include specific queries targeting those plugin's technical documentation

The above storyboard plan is relevant to these plugins: {relevant_plugins}
Note that you MUST NOT use the plugins that are not listed above.

You MUST only output the queries in the following JSON format (with json triple backticks):
```json
[
    {{"type": "manim-core", "query": "content of core functionality query"}},
    {{"type": "<plugin-name>", "query": "content of plugin-specific query"}},
    {{"type": "manim-core", "query": "content of animation technique query"}}
    ...
]
```

---

## 📄 `prompts/prompt_rag_query_generation_vision_storyboard.txt`

You are an expert in generating search queries specifically for **Manim (Community Edition) documentation** (both core Manim and its plugins). Your task is to analyze a scene plan for a Manim animation and generate effective queries that will retrieve relevant documentation about visual elements and scene composition.

Here is the scene plan:

{scene_plan}

Based on this scene plan, generate multiple human-like queries (maximum 10) for retrieving relevant documentation about visual elements and scene composition techniques.

**Specifically, ensure that:**
1. Queries focus on retrieving information about **visual elements** like shapes, objects, and their properties
2. Include queries about **scene composition techniques** like layout, positioning, and grouping
3. If the scene plan suggests using plugin functionality, include specific queries targeting those plugin's visual capabilities
4. Queries should be high-level, aiming to discover what Manim features can be used, rather than focusing on low-level implementation details.
    - For example, instead of "how to set the color of a circle", ask "what visual properties of shapes can I control in Manim?".

The above scene plan is relevant to these plugins: {relevant_plugins}.
Note that you MUST NOT use the plugins that are not listed above.

You MUST only output the queries in the following JSON format (with json triple backticks):
```json
[
    {{"type": "manim-core", "query": "content of visual element query"}},
    {{"type": "<plugin-name>", "query": "content of plugin-specific query"}},
    {{"type": "manim-core", "query": "content of composition technique query"}}
    ...
]
```

---

## 📄 `prompts/prompt_scene_implementation.txt`

You are an expert in educational video production and Manim (Community Edition) animation development. Your task is to create a detailed implementation plan for Scene {scene_number}.

<BASE_INFORMATION>
Topic: {topic}
Description: {description}
</BASE_INFORMATION>

<SCENE_CONTEXT>
Scene Overview:
{scene_outline}
</SCENE_CONTEXT>

<IMPLEMENTATION_PLAN>

[SCENE_VISION]
1.  **Overall Narrative**:
    - Describe the overall story or message of the scene. What is the key takeaway for the viewer?
    - How does this scene fit into the larger narrative of the video?
    - What is the desired emotional impact on the viewer?

2.  **Learning Objectives**:
    - What specific knowledge or skills should the viewer gain from this scene?
    - How will the visual elements and animations support these learning objectives?
    - What are the key concepts that need to be emphasized?

[STORYBOARD]
1.  **Visual Flow**:
    - Describe the sequence of visual elements and animations in the scene.
    - Provide a rough sketch or description of the key visual moments.
    - How will the scene transition between different ideas or concepts?
    - What is the pacing of the scene? Are there moments of pause or rapid action?

[TECHNICAL_IMPLEMENTATION]
1.  **High-Level Components (VGroups)**:
    - **Identify the main conceptual sections of the scene.** Think of this like outlining chapters in a story or sections in a presentation.
    - **Define the purpose of each high-level component.** What should the viewer learn or understand from each section?
    - **Describe how these components relate to each other and the overall scene flow.** How will you transition between these sections to create a cohesive narrative?
    - **Provide a brief rationale for your choice of high-level components.** Why did you choose these specific sections?

2.  **VGroup Hierarchy**:
    - **For each high-level component, define a parent VGroup.** This VGroup will act as a container for all elements within that section.
    - **Break down each parent VGroup into nested VGroups for sub-components as needed.** Think about logical groupings of elements.
    - **Specify the relative positioning of these VGroups within the scene using `next_to()`, `align_to()`, and `shift()` where possible.** How will the parent VGroups be arranged on the screen relative to each other? (e.g., stacked vertically, side-by-side, etc.) Prioritize relative positioning using the following references:
        - `ORIGIN`: the center of the scene
        - scene margins (e.g., corners, edges)
        - other VGroups as references.
        - **MUST NOT use absolute coordinates.**
    - **Define the scale relationships between different levels of the VGroup hierarchy.** Will sub-VGroups inherit scale from parent VGroups? How will scaling be managed to maintain visual consistency?
    - **Provide a brief rationale for your VGroup hierarchy.** Why did you choose this specific structure?

    For each VGroup level (from high-level down to sub-components):
    - Name: [Descriptive name for the VGroup, e.g., "TitleSection", "ProblemStatementGroup", "Explanation1Group"]
    - Purpose: [What is the purpose of this VGroup? What should the viewer learn or understand from this VGroup?]
    - Contents: [List all child VGroups and individual elements (Text, MathTex, Shapes, etc.) that belong to this VGroup.]
    - Positioning:
        * Reference: [Specify what this VGroup is positioned relative to. Do not use absolute coordinates.]
        * Alignment: [How is it aligned relative to the reference? Use `align_to()` with options like `UP`, `DOWN`, `LEFT`, `RIGHT`, `ORIGIN`, etc.]
        * Spacing: [Describe any spacing considerations relative to sibling VGroups or elements within the parent. Use `buff` argument in `next_to()` or `arrange()`. Refer to the defined minimum spacing value.]
    - Scale: [Specify the scale of this VGroup relative to its parent VGroup. Use relative scaling factors (e.g., 1.0 for same scale, 0.8 for smaller).]
    - Rationale: [Explain the reasoning behind the structure and organization of this VGroup. Why did you group these elements together?]

3.  **Element Specification**:
    For each individual element (Text, MathTex, Shapes, etc.) within a VGroup:
    - Name: [Descriptive name for the element, e.g., "ProblemTitleText", "Equation1", "HighlightCircle"]
    - Type: [Manim object type. Examples: Text, MathTex, Circle, Rectangle, Arrow, Line, etc.]
    - Parent VGroup: [Specify the VGroup this element belongs to. This establishes the hierarchical relationship.]
    - Positioning:
        * Reference: [Specify what this element is positioned relative to. Use its parent VGroup, other elements, `ORIGIN`, or scene margins as references. Do not use absolute coordinates.]
        * Alignment: [How is it aligned within its parent VGroup? Use `align_to()` or `next_to()` with appropriate directions, e.g. `UP`, `DOWN`, `LEFT`, `RIGHT`, `ORIGIN`, `UL`, `UR`, `DL`, `DR`]
        * Spacing: [If applicable, describe spacing relative to other elements using `buff` in `next_to()`. Refer to the defined minimum spacing value.]
    - Style Properties:
        * Color: [Hex code or named color (e.g., "RED", "BLUE"). Use hex codes for specific colors. e.g., #FF0000 for red]
        * Opacity: [Value between 0 and 1. 1 for fully opaque, 0 for fully transparent.]
        * Stroke Width: [Specify stroke width using levels: `thin`, `medium`, or `thick`.]
        * Font: [Font family name, if applicable.]
        * Font Size: [Specify font size using levels: `heading1`, `heading2`, `heading3`, `heading4`, `heading5`, `heading6`, or `body`. Refer to the defined font size levels.]
        * Fill Color: [Hex code for fill color, if applicable.]
        * ... [Include any other relevant style properties]
    - Z-Index: [Integer value for layering order within the VGroup. Higher values are on top.]
    - Required Imports: [List specific Manim classes that need to be imported to create this element. e.g., `from manim import Text, Circle`]

[ANIMATION_STRATEGY]
1.  **VGroup Transitions**:
    - **Define how parent VGroups will transition onto and off of the scene, and between different sections.** Describe the movement patterns for these high-level groups. Examples: 'Slide in from left', 'Fade in and scale up', 'Move to top of screen'.
    - **Specify the timing and coordination of VGroup transitions.** How long will each transition take? Will transitions overlap or be sequential?
    - **Describe any transformation sequences applied to VGroups during transitions.** Will VGroups rotate, scale, or change shape during transitions?

2.  **Element Animations**:
    - **Define the animations for individual elements within each VGroup.** What animations will bring each element to life? Examples: 'Write in text', 'Draw a circle', 'Highlight an equation', 'Fade in an image'.
    - **Group related element animations using Manim's animation grouping features (e.g., `AnimationGroup`, `Succession`).** Explain how these groups will be used to create cohesive animation sequences.
    - **Coordinate element animations with parent VGroup movements and transitions.** Ensure element animations are synchronized with the overall scene flow.
    - **Specify the timing of element animations relative to VGroup transitions and other element animations.** Create a timeline or sequence of animations.

3.  **Scene Flow**:
    - **Describe the overall animation sequence for the entire scene.** Outline the order in which VGroups and elements will be animated.
    - **Specify transition buffers or pauses between major sections of the scene.** How much time will be left between animations for the viewer to process information?
    - **Consider how the animation timing will coordinate with the narration (if narration is planned).** Animations should complement and reinforce the spoken content.

[NARRATION]
- **Narration Script:** [Provide the full script for the narration, including timing cues or markers for when specific animations should occur. The script should be clear, detailed, and engaging, and should align with the visual elements and animations.]
- **Narration Sync:** [Describe how the narration should be synchronized with the animations. Specify how timing cues in the narration script will be used to trigger animations. Are there specific points where the narration and animations should be perfectly synchronized? Explain how you will achieve this synchronization.]

[VIEWER_EXPERIENCE]
1.  **Cognitive Load**:
    - How will you manage the amount of information presented at any given time?
    - Are there any complex concepts that need to be broken down into smaller steps?
    - How will you use visual cues to guide the viewer's attention?

2.  **Pacing**:
    - Is the pacing of the scene appropriate for the content?
    - Are there moments where the viewer needs time to pause and reflect?
    - How will you use animation timing to control the pace of the scene?

3.  **Accessibility**:
    - How will you ensure that the scene is accessible to viewers with different needs?
    - Are there any specific considerations for color contrast or text readability?

[TECHNICAL_CHECKS]
- **VGroup boundary validation:** Ensure all elements are contained within their intended VGroup boundaries and are not overflowing unexpectedly.
- **Hierarchy scale consistency:** Verify that scaling is applied consistently throughout the VGroup hierarchy and that text and elements remain readable at all scales.
- **Animation coordination between levels:** Check that animations at different VGroup levels are coordinated and do not clash or look disjointed.
- **Performance optimization for nested groups:** Consider the performance implications of deeply nested VGroups and optimize structure and animations for smooth playback.
- **Text readability:** Ensure all text elements are legible in terms of size, color contrast, and positioning.
- **Color contrast:** Verify sufficient color contrast between text and background, and between different visual elements for accessibility.
- **Animation smoothness:** Check for any jerky or abrupt animations and refine timing and easing for smoother transitions.

</IMPLEMENTATION_PLAN>

Requirements:
1. All elements must stay within safe area margins
2. Maintain minimum spacing between objects: [value]  (This value is defined in the project settings)
3. Use relative positioning when possible, leveraging `next_to()`, `align_to()`, and `shift()`. Only reference positions relative to `ORIGIN`, scene margins, or other object reference points. Do not use absolute coordinates.
4. Include transition buffers between animations
5. Specify z-index for overlapping elements
6. All colors must use hex codes or named colors
7. Define scale relative to base unit
8. No external dependencies
9. Currently, there are no images or other assets available locally or remotely for you to use in the scene. Only include elements that can be generated through manim.
10. **Do not generate any code in this plan, except for illustrative examples where necessary. This plan is for outlining the scene and should not include any python code.**
11. **The purpose of this plan is to be a detailed guide for a human to implement the scene in manim.**

---

## 📄 `prompts/prompt_tavily_assisted_fix_error.txt`

You are an expert Manim developer specializing in debugging and error resolution using web search insights. You have access to search results from Tavily that contain relevant information about the error. Use this information to provide a comprehensive fix.

<CONTEXT>
Implementation Plan:
{implementation_plan}

Original Manim Code:
```python
{manim_code}
```

Error Message:
{error_message}

Tavily Search Results:
{tavily_search_results}

Extracted Full Content (from top URLs):
{extracted_content}

Search Query Used: {search_query}
</CONTEXT>

<INSTRUCTIONS>
Using the Tavily search results, extracted full content, and your expertise, analyze the error and provide a comprehensive fix. The search results contain real-world solutions and documentation, and the extracted content provides the complete context from the most relevant sources.

**Priority Order for Solutions:**
1. **Extracted Full Content** - Use the complete pages for detailed implementation guidance
2. Official Manim documentation insights
3. GitHub issues and solutions
4. Stack Overflow community solutions
5. Reddit/Discord community fixes
6. Your expert knowledge as fallback

**Key Requirements:**
- **Prioritize extracted full content** - It contains complete solutions and context
- Extract actionable insights from both search snippets and full content
- Cross-reference information between search results and extracted content
- Apply modern Manim best practices
- Provide complete, executable code
- Explain the fix with reference to specific sources found
- Quote relevant sections from extracted content when applicable
</INSTRUCTIONS>

You MUST output in the following format:

<TAVILY_INSIGHTS>
Key Findings from Search Results:
- [Insight 1 from search snippets]
- [Insight 2 from search snippets]
- [Insight 3 from search snippets]

Key Findings from Extracted Content:
- [Insight 1 from full page content]
- [Insight 2 from full page content]
- [Insight 3 from full page content]

Most Relevant Source: [URL or source that best addresses this error]
Best Extracted Content: [Which extracted page provided the most complete solution]
</TAVILY_INSIGHTS>

<ERROR_ANALYSIS>
Error Type: [Syntax/Runtime/Logic/Other]
Error Location: [File/Line number/Component]
Root Cause: [Brief explanation based on search insights]
Search-Informed Solution: [How the search results inform the fix]
</ERROR_ANALYSIS>

<SOLUTION>
[FIXES_APPLIED]
- Fix 1: [Description with reference to search source]
  - Source: [Which search result provided this insight]
  - Change: [What to modify]
- Fix 2: [If applicable]
  ...

[CORRECTED_CODE]
```python
# Complete corrected code based on Tavily search insights
# Comments explaining fixes with source references
```

[VERIFICATION_STEPS]
1. [Step to verify the fix works]
2. [Additional verification if needed]

[PREVENTION_TIPS]
- [How to avoid this error in future, based on search insights]
- [Best practices learned from search results]
</SOLUTION>

**Requirements:**
1. Reference specific search results when explaining fixes
2. Include source URLs when applicable
3. Ensure corrected code is complete and executable
4. Prioritize solutions from authoritative sources (official docs, maintainers)
5. If search results are insufficient, clearly state limitations

---

## 📄 `prompts/prompt_tavily_search_query_generation.txt`

You are an expert in analyzing Python error tracebacks, specifically for Manim (Community Edition) errors. Your task is to analyze a full, potentially verbose traceback and generate a concise, effective search query under 400 characters that will help find solutions online.

<CONTEXT>
Full Error Traceback:
{traceback}

Original Code Context:
{code_context}

Implementation Plan Context:
{implementation_plan}
</CONTEXT>

<TASK>
Analyze the provided traceback and generate the most effective search query to find a solution. The query **MUST** be targeted at the official Manim documentation.

**Key Requirements for Effective Queries:**
- **ALWAYS** include `"site:docs.manim.community"` to target official documentation. This is not optional.
- Include the specific Manim object or class name (e.g., `Polygon`, `Text`, `Scene`).
- Include the most relevant key phrases from the actual error message (e.g., `"takes 1 positional argument but 2 were given"`).
- Combine these elements into a precise query.

**Important Constraints:**
- Query MUST be under 400 characters.
- Query MUST start with "manim".
- Prioritize technical terms from the traceback.
</TASK>

<OUTPUT_FORMAT>
Search Query: [Your concise search query here - under 400 characters]

Query Rationale: [Brief explanation of why this query will be effective]

Key Error Components:
- Error Type: [The main exception type]
- Failed Component: [The specific Manim object/method that failed]
- Context: [Brief context about what was being attempted]
</OUTPUT_FORMAT>

**Examples of Documentation-Targeted Queries:**
- "manim Polygon ValueError all input arrays must have same number of dimensions site:docs.manim.community"
- "manim Text AttributeError has no attribute font_size site:docs.manim.community"
- "manim Transform TypeError takes positional argument site:docs.manim.community"
- "manim Scene ImportError missing manim community edition site:docs.manim.community"

**How to Construct the Best Query:**
1.  **Start with "manim"**: `manim`
2.  **Add the Class/Object**: `manim Polygon`
3.  **Add the Core Error Message**: `manim Polygon "takes 1 positional argument but 2 were given"`
4.  **Append the Site Specifier**: `manim Polygon "takes 1 positional argument but 2 were given" site:docs.manim.community`

Generate your response following the OUTPUT_FORMAT exactly.
