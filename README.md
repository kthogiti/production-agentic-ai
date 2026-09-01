# AI Software Development Team

A production-oriented multi-agent project built using
LangChain, LangGraph, RAG and MCP.

## Goal

Build an AI software development team consisting of:

- 1 Lead / Architect Agent
- 5 Expert Full-Stack Developer Agents

The team will eventually:

- understand software requirements
- define architecture
- break requirements into work items
- assign development tasks
- inspect an existing repository
- implement code
- write tests
- perform code reviews
- execute builds/tests
- resolve implementation conflicts
- work through Git/MCP tools
- request human approval when necessary

## Day 1

Implemented the first Developer Agent.

Current workflow:

START → Developer → END

The Developer produces structured output containing:

- understanding
- plan
- implementation
- assumptions

## Observation

Without architectural context, the Developer Agent may
make implementation assumptions.

Future versions will introduce a Lead/Architect Agent
responsible for architecture and task decomposition.

## Day 2

Added the Lead / Architect Agent.

Current workflow:

START
→ Lead
→ Developer
→ END

The Lead is responsible for:

- understanding requirements
- defining high-level architecture
- defining technical constraints
- creating a work item
- defining acceptance criteria

The Developer receives the Lead's architecture and work item
instead of independently interpreting the original requirement.

### Key observation

Delegation reduces uncontrolled architectural assumptions,
but agent outputs still need verification.

Future versions will introduce review and feedback loops.

## Day 3

Added an implementation review loop.

Current workflow:

START
→ Lead
→ Developer
→ Lead Review

If approved:
→ END

If changes are required:
→ Developer
→ Lead Review
→ END

The Lead now verifies:

- architecture compliance
- technical constraints
- acceptance criteria
- unnecessary design changes
- invented requirements

A maximum review-attempt count prevents uncontrolled loops.

### Key learning

Agent instructions are not guarantees.

Important outputs should be independently verified.

## Day 4

The Lead Agent can now decompose a software requirement
into multiple ordered implementation work items.

The workflow executes each work item independently.

Current flow:

START
→ Lead
→ Select Work Item
→ Developer
→ Review

If revision is required:
→ Developer
→ Review

If approved:
→ Complete Work Item

If more work exists:
→ Select Next Work Item

Otherwise:
→ END

### Key learning

Not every LangGraph node should contain an LLM.

Deterministic workflow operations such as selecting the next
work item and advancing an index should remain normal code.

The AI Lead is responsible for reasoning and decomposition.
LangGraph is responsible for workflow orchestration.

## Day 5

Introduced the first Developer Pool.

The team currently contains:

- Lead / Architect Agent
- Developer 1
- Developer 2

Work items are assigned using deterministic
round-robin assignment.

Current workflow:

START
→ Lead
→ Select Work Item
→ Assign Developer
→ Developer
→ Review

If changes are required:
→ Same Developer
→ Review

If approved:
→ Complete Work Item
→ Next Work Item

### Key learning

Agent selection does not always require an LLM.

Because both Developers currently have similar capabilities,
assignment can remain deterministic.

A new limitation is now visible:

Developers do not yet work against a shared evolving codebase.

Repository access will be required before the team can
behave like real developers.