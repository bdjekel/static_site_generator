# Static Site Generator

## Overview
This is a custom static site generator written in Python that converts Markdown files into HTML pages. The project demonstrates a complete implementation of a markdown parser and HTML generator from scratch, showcasing object-oriented design patterns and text processing algorithms.

## Table of Contents

- [Overview](#overview)
- [Architecture & Design Patterns](#architecture--design-patterns)
  - [1. Composite Pattern (HTML Node Hierarchy)](#1-composite-pattern-html-node-hierarchy)
  - [2. Strategy Pattern (Block Type Processing)](#2-strategy-pattern-block-type-processing)
  - [3. Pipeline Pattern (Text Processing)](#3-pipeline-pattern-text-processing)
- [Core Components](#core-components)
  - [Main Entry Point (`main.py`)](#main-entry-point-mainpy)
  - [Page Generation (`generate_pages_recursive.py`, `generate_page.py`)](#page-generation-generate_pages_recursivepy-generate_pagepy)
  - [Markdown Parser (`markdown_to_html_node.py`)](#markdown-parser-markdown_to_html_nodepy)
  - [Text Processing Pipeline](#text-processing-pipeline)


## Architecture & Design Patterns

### 1. **Composite Pattern** (HTML Node Hierarchy)
The system uses a composite pattern with three main node types:
- **`HTMLNode`**: Abstract base class defining the interface for all HTML nodes
- **`LeafNode`**: Terminal nodes that contain text content and render as self-closing or simple tags
- **`ParentNode`**: Container nodes that can hold multiple child nodes and render as opening/closing tag pairs

### 2. **Strategy Pattern** (Block Type Processing)
The `BlockType` enum and `block_to_block_type()` function implement a strategy pattern where different markdown block types are processed using specific algorithms:
- Headings (H1-H6)
- Code blocks
- Blockquotes
- Ordered/Unordered lists
- Paragraphs

### 3. **Pipeline Pattern** (Text Processing)
The markdown-to-HTML conversion follows a multi-stage pipeline:
1. **Block Parsing**: Split markdown into logical blocks
2. **Block Classification**: Identify block types using regex patterns
3. **Inline Processing**: Parse text formatting, links, and images within blocks
4. **Node Construction**: Build HTML node tree
5. **HTML Generation**: Convert node tree to HTML string

## Core Components

### **Main Entry Point** (`main.py`)
- Orchestrates the entire build process
- Accepts optional basepath parameter for deployment
- Cleans and recreates the output directory
- Copies static assets and generates HTML pages

### **Page Generation** (`generate_pages_recursive.py`, `generate_page.py`)
- Recursively processes markdown files in the content directory
- Converts each `.md` file to `.html` using template substitution
- Maintains directory structure in output
- Handles template variable replacement (`{{ Title }}`, `{{ Content }}`)

### **Markdown Parser** (`markdown_to_html_node.py`)
- Core conversion engine that transforms markdown to HTML nodes
- Implements block-level parsing with type-specific handling
- Uses pattern matching for different block types
- Constructs hierarchical HTML node tree

### **Text Processing Pipeline**
1. **`markdown_to_blocks.py`**: Splits markdown into logical blocks by double newlines
2. **`text_to_textnodes.py`**: Orchestrates inline text processing
3. **`split_nodes_delimiter.py`**: Handles bold, italic, strikethrough, and code formatting
4. **`split_nodes_image.py`**: Processes markdown image syntax
5. **`split_nodes_link.py`**: Processes markdown link syntax

### **HTML Node System**
- **`HTMLNode`**: Base class with tag, value, children, and properties
- **`LeafNode`**: Terminal nodes for text content and self-closing tags
- **`ParentNode`**: Container nodes that can hold multiple children
- **`TextNode`**: Intermediate representation for text with formatting metadata

## Algorithms & Data Structures

### **Text Parsing Algorithms**
1. **Delimiter-based Parsing**: Uses state machines to track opening/closing delimiters for bold, italic, etc.
2. **Regex-based Extraction**: Pattern matching for links, images, and block identification
3. **Word-level Processing**: Splits text into words to handle delimiter boundaries correctly
4. **Block Classification**: Uses regex patterns to identify markdown block types

### **Data Structures**
1. **Tree Structure**: HTML nodes form a hierarchical tree representing document structure
2. **Linked Lists**: Text nodes are processed as linked lists during parsing
3. **Enums**: `TextType` and `BlockType` enums for type safety
4. **Dictionaries**: Properties storage for HTML attributes

### **State Management**
- **Delimiter Toggle**: Tracks whether text is inside formatting delimiters
- **Space Transfer**: Maintains whitespace during text processing
- **Block Context**: Determines how to process text based on block type

## Key Features

### **Markdown Support**
- **Headings**: H1-H6 with `#` syntax
- **Code Blocks**: Fenced with triple backticks
- **Blockquotes**: Lines starting with `>`
- **Lists**: Ordered (1. 2. 3.) and unordered (- item)
- **Paragraphs**: Default text blocks
- **Inline Formatting**: Bold (`**text**`), italic (`_text_`), strikethrough (`~~text~~`), code (`text`)
- **Links**: `[text](url)` syntax
- **Images**: `![alt](url)` syntax

### **Template System**
- Simple template substitution with `{{ Title }}` and `{{ Content }}`
- Basepath configuration for deployment flexibility
- CSS and static asset integration

### **Error Handling**
- Validation for required title in markdown files
- Error checking for unclosed delimiters
- Graceful handling of malformed markdown

## Testing
Comprehensive test suite covering:
- Individual component functionality
- Edge cases and error conditions
- Integration testing of the full pipeline
- HTML output validation

## Technologies & Skills

### **Languages**
- Python 3.10.12

### **Core Skills**
- Object-Oriented Programming
- Text Processing & Parsing
- Regular Expressions
- File I/O Operations
- Recursive Algorithms
- Template Systems

### **Design Patterns**
- Composite Pattern (HTML Node Hierarchy)
- Strategy Pattern (Block Type Processing)
- Pipeline Pattern (Text Processing)
- Template Method Pattern (HTML Generation)

### **Algorithms**
- State Machine (Delimiter Parsing)
- Recursive Tree Traversal
- Pattern Matching (Regex)
- Word-level Text Processing
- Block Classification

### **Data Structures**
- Tree Structures (HTML Node Hierarchy)
- Linked Lists (Text Node Processing)
- Enums (Type Safety)
- Dictionaries (HTML Properties)
- Lists (Block Processing)

### **Tools & Concepts**
- Markdown Parsing
- HTML Generation
- Static Site Generation
- File System Operations
- Unit Testing
- Command Line Interface
- Template Substitution
