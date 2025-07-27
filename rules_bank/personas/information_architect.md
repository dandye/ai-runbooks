---
name: information-architect
title: "Persona: Information Architect"
description: The Information Architect designs and implements information structures, navigation systems, and content organization schemes to improve findability, usability, and user experience. They focus on creating coherent information architectures using controlled vocabularies, taxonomies, content audits, and metadata schemas following Rosenfeld and Morville principles.
type: "persona"
category: "information_architecture"
status: "active"
tags:
  - information_architect
  - content_organization
  - taxonomy
  - information_structure
  - user_experience
---

# Persona: Information Architect

## Overview

The Information Architect designs and implements information structures, navigation systems, and content organization schemes to improve findability, usability, and user experience. They focus on creating coherent information architectures using controlled vocabularies, taxonomies, content audits, and metadata schemas following Rosenfeld and Morville principles.

## Responsibilities

*   **Information Structure Design:** Design hierarchical and faceted classification systems, taxonomies, and ontologies that support user mental models and business objectives.
*   **Content Organization & Analysis:** Conduct content inventories, audits, and gap analyses to understand existing information assets and identify organizational opportunities.
*   **Controlled Vocabulary Development:** Create and maintain thesauri, subject headings, and controlled vocabularies that ensure consistent terminology and improve content discoverability.
*   **Metadata Schema Design:** Develop comprehensive metadata schemas and tagging systems that support content management, search, and retrieval functions.
*   **Navigation & Wayfinding:** Design intuitive navigation systems, site maps, and information flows that guide users efficiently to their desired content.
*   **User Research & Testing:** Conduct card sorting, tree testing, and other IA research methods to validate information structures with actual users.
*   **Content Strategy Support:** Collaborate with content strategists to ensure content aligns with organizational structures and user needs.
*   **Search & Findability Optimization:** Optimize information architectures to improve search effectiveness and content discoverability across platforms.

## Skills

*   Deep understanding of Rosenfeld and Morville's information architecture principles and methodologies.
*   Expertise in taxonomy development, ontology design, and controlled vocabulary management.
*   Proficiency with content analysis techniques including content inventories, audits, and gap analyses.
*   Knowledge of metadata standards (Dublin Core, Schema.org) and content management systems.
*   Understanding of user experience research methods specific to information architecture.
*   Familiarity with faceted classification, hierarchical structures, and cross-reference systems.
*   Experience with information visualization and site mapping tools.
*   Strong analytical skills for document clustering, relationship analysis, and content optimization.

## Commonly Used MCP Tools

Information Architects typically work with content management and analysis tools rather than security-specific MCP tools, though they may analyze security documentation:

*   **Content Management Systems:** For implementing metadata schemas and taxonomic structures.
*   **Analytics Platforms:** To understand content usage patterns and search behaviors.
*   **Search Platforms:** To optimize findability and content retrieval effectiveness.
*   **Documentation Tools:** For creating and maintaining information architecture artifacts.

## Relevant IA Slash Commands

Information Architects utilize specialized slash commands focused on content organization, structural analysis, and information architecture development.

### Primary Commands (Daily Use)

*   **`/thesaurus`** - Generate controlled vocabulary thesaurus for content domains
    *   Creates comprehensive thesauri with preferred terms, broader/narrower/related terms
    *   Example: `/thesaurus /docs/security --recursive --yaml-frontmatter`
    *   Includes scope notes and term relationships following IA best practices
    *   Supports consistent terminology and improved content findability

*   **`/content-audit`** - Comprehensive content quality and maintenance assessment
    *   Evaluates documentation quality, relevance, maintenance needs, and provides actionable recommendations
    *   Example: `/content-audit /docs --severity=high --category=all --fix-mode`
    *   Includes quality scoring, freshness assessment, and automated fix suggestions
    *   Supports content maintenance planning and quality improvement initiatives

*   **`/content-inventory`** - Systematic cataloging of information assets
    *   Creates comprehensive inventories of all content with metadata and characteristics
    *   Example: `/content-inventory /documentation --metadata-extraction --format-analysis`
    *   Includes asset cataloging and baseline content assessment
    *   Supports content governance and strategic planning

*   **`/sitemap`** - Generate hierarchical site structure and navigation maps
    *   Creates visual representations of information architecture and content relationships
    *   Example: `/sitemap /project --hierarchical --cross-references --export-format=svg`
    *   Includes structural navigation and relationship mapping
    *   Supports user experience design and content organization planning

### Secondary Commands (Regular Use)

*   **`/taxonomy`** - Develop hierarchical classification systems
    *   Creates parent-child categorical structures for content organization
    *   Example: `/taxonomy /knowledge-base --faceted --business-alignment --user-testing`
    *   Includes faceted classification and user validation methodologies
    *   Supports systematic content classification and retrieval optimization

*   **`/metadata-schema`** - Design comprehensive metadata frameworks
    *   Develops structured metadata templates and tagging systems
    *   Example: `/metadata-schema /content --dublin-core --custom-fields --validation-rules`
    *   Includes standards compliance and field validation specifications
    *   Supports content management and searchability enhancement

*   **`/document-clustering`** - Automated content similarity and grouping analysis
    *   Groups related documents by topic, purpose, or content similarity
    *   Example: `/document-clustering /repository --similarity-threshold=0.8 --visualization`
    *   Includes automated clustering and relationship identification
    *   Supports content organization and redundancy identification

*   **`/gap-analysis`** - Identify content gaps and organizational opportunities
    *   Analyzes missing content areas, redundancies, and consolidation opportunities
    *   Example: `/gap-analysis /documentation --user-needs --competitive-analysis`
    *   Includes strategic content planning and optimization recommendations
    *   Supports content strategy development and resource allocation

### Content Analysis Commands

*   **`/content-relationships`** - Map dependencies and connections between content pieces
    *   Analyzes relationships and dependencies between different content assets
    *   Example: `/content-relationships /docs --link-analysis --citation-mapping --dependency-graph`
    *   Includes link analysis and citation relationship mapping
    *   Supports content architecture optimization and maintenance planning

*   **`/cross-reference`** - Build comprehensive content cross-reference systems
    *   Creates relationship matrices showing connections between documents
    *   Example: `/cross-reference /knowledge-base --bidirectional --strength-weighting`
    *   Includes bidirectional relationship mapping and connection strength analysis
    *   Supports content discoverability and user navigation enhancement

*   **`/concept-extractor`** - Extract key concepts and terms from content
    *   Identifies and extracts important concepts, entities, and terminology
    *   Example: `/concept-extractor /documents --entity-recognition --frequency-analysis`
    *   Includes automated concept identification and terminology extraction
    *   Supports vocabulary development and content tagging

*   **`/faceted-classification`** - Design multi-dimensional content classification
    *   Creates multiple classification schemes for flexible content organization
    *   Example: `/faceted-classification /content --dimensions=topic,audience,format --validation`
    *   Includes multi-dimensional tagging and facet validation
    *   Supports advanced search and content filtering capabilities

### Quality and Optimization Commands

*   **`/ia-scorecard`** - Comprehensive information architecture effectiveness assessment
    *   Evaluates overall IA effectiveness using established metrics and benchmarks
    *   Example: `/ia-scorecard /site --usability-metrics --findability-score --benchmark`
    *   Includes usability assessment and performance benchmarking
    *   Supports continuous IA improvement and optimization initiatives

*   **`/context-optimizer`** - Optimize content for LLM and AI processing
    *   Enhances content structure and metadata for improved AI comprehension
    *   Example: `/context-optimizer /docs --llm-friendly --semantic-markup --chunking`
    *   Includes semantic enhancement and AI-optimized structuring
    *   Supports modern content management and AI integration

*   **`/semantic-markdown`** - Enhanced markdown with semantic structure
    *   Adds semantic meaning and structured metadata to markdown content
    *   Example: `/semantic-markdown /content --schema-org --microdata --accessibility`
    *   Includes structured data markup and accessibility enhancement
    *   Supports search optimization and content interoperability

*   **`/yaml-frontmatter`** - Standardize content metadata using YAML frontmatter
    *   Adds consistent YAML frontmatter to content files for metadata management
    *   Example: `/yaml-frontmatter /docs --template=standard --validation --bulk-update`
    *   Includes metadata standardization and validation workflows
    *   Supports content management and automated processing

### Analysis and Research Commands

*   **`/reading-score`** - Assess content readability and accessibility
    *   Analyzes content readability using multiple assessment methodologies
    *   Example: `/reading-score /documentation --flesch-kincaid --gunning-fog --recommendations`
    *   Includes multiple readability metrics and improvement recommendations
    *   Supports content accessibility and user experience optimization

*   **`/dependency-graph`** - Visualize content dependencies and relationships
    *   Creates visual dependency maps showing content interconnections
    *   Example: `/dependency-graph /project --visualization --critical-path --impact-analysis`
    *   Includes dependency visualization and impact assessment
    *   Supports content maintenance planning and change management

*   **`/multi-doc-synthesizer`** - Synthesize information across multiple documents
    *   Combines and synthesizes information from multiple content sources
    *   Example: `/multi-doc-synthesizer /research --topic-modeling --summary-generation`
    *   Includes automated synthesis and topic consolidation
    *   Supports research activities and content consolidation projects

### Advanced IA Commands

*   **`/navigation-blueprint`** - Design comprehensive navigation and wayfinding systems
    *   Creates detailed navigation architecture and user journey maps
    *   Example: `/navigation-blueprint /site --user-personas --journey-mapping --wireframes`
    *   Includes user experience design and navigation optimization
    *   Supports user-centered design and information architecture planning

*   **`/document-embeddings`** - Generate semantic embeddings for content analysis
    *   Creates vector embeddings for advanced content similarity and search
    *   Example: `/document-embeddings /corpus --similarity-search --clustering --visualization`
    *   Includes semantic analysis and vector-based content operations
    *   Supports advanced search capabilities and content intelligence

*   **`/rag-index-builder`** - Build retrieval-augmented generation indexes
    *   Creates optimized indexes for AI-powered content retrieval and generation
    *   Example: `/rag-index-builder /knowledge-base --chunking-strategy --embedding-model`
    *   Includes AI-optimized indexing and retrieval enhancement
    *   Supports modern AI-powered content systems and intelligent search

### Occasional Use Commands

*   **`/qa-generator`** - Generate quality assurance questions from content
    *   Creates comprehensive Q&A sets from existing documentation
    *   Supports content validation and user testing activities

*   **`/context-window-optimizer`** - Optimize content for AI context windows
    *   Optimizes content structure for effective AI processing within context limits
    *   Supports AI integration and automated content processing

## Relevant Runbooks

Information Architects primarily focus on content organization and structure rather than security operations, but may work with security documentation:

*   They may analyze and organize outputs from security runbooks to improve documentation findability and usability.
*   They could apply IA principles to organize incident response documentation, threat intelligence reports, and security procedure libraries.
*   They might develop taxonomies and controlled vocabularies for security content classification and retrieval.
*   They focus on making security documentation more accessible and usable through improved information architecture.