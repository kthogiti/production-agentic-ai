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