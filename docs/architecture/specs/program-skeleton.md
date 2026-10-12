# First visible program and ordered output

Status: owner-approved revised option A, two short lessons. Supersedes the initial no-output-first proposal.

## Contracts

Hosted C++17 on a computer, ordinary successful output environment. No variables, input, hardware or user-defined helper functions. The first lesson defines main with int result and no parameters, includes iostream, writes Ready followed by newline, then returns zero. A separate valid comparison removes the output action and unused include; it returns zero without writing anything.

The second lesson reuses the same structure: write Program started plus newline, then Program finished plus newline, then return zero. Reverse only the two writes to demonstrate ordering. A final variant writes System followed by a space, then ready followed by newline: two source statements produce one output line.

Each behavior has its own activity source: writes in exact order, then return zero. Scope starts inside main; initial/final UML nodes are not extra C++ statements. Includes and braces are structural, not output actions. Preserve exact text, spaces, case and newline semantics. Output buffering, namespaces in depth and overloads are deferred, not denied. No output success guarantees beyond this example's stated environment.

## Teaching structure

TOOL-01 → programme-minimal → premiers-affichages → CPP-01. Need and expected observations, activity, complete program, exact output, line-by-line reading and comparison. All five programs get the existing UML cards. Describe return status separately from printed text. Explain main's implicit zero return briefly without additional variant. Programs are desktop demonstrations; never present cout as an Arduino Serial replacement.

## Acceptance

Extract labelled complete programs from the lessons; compile C++17 with warnings-as-errors; run each and assert exact stdout, empty stderr and zero exit status. Verify each published SVG equals its generated conception snapshot. Build checks cover links and per-excerpt UML. Browser checks cover both new pages at desktop/mobile widths. Practice remains external; no standalone clone project is published in this change.

## Four-pass review

Requirements: visible result first, structure then ordering/newlines, no variable prerequisite. Dependencies: static content uses existing cards; no runtime feature. Simplicity: five contrasting examples, each answering a distinct question. No design pattern required. Risk: too many new symbols; explain each concrete use without teaching stream internals. Whitespace contrast is moved into actual output rather than a redundant one-line formatting example.

## Sources

https://www.learncpp.com/cpp-tutorial/statements-and-the-structure-of-a-program/
https://www.learncpp.com/cpp-tutorial/introduction-to-iostream-cout-cin-and-endl/
https://eel.is/c++draft/basic.start.main

Original teaching adaptation, not copied lesson text. The formal reference is the current draft; actual examples are checked in C++17 mode.
