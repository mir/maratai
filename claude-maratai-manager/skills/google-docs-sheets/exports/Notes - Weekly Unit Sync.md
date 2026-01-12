Notes - Weekly Unit Sync

## Jan 9, 2026 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNTEwMTdUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019286162&usg=AOvVaw2HVXZwNT0iXH9BT4G2VriL)

Attendees: [Analytics Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Paul Kuchin](mailto:pavel.kuchin@semrush.com)  [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* “Data Assets Certification” Project (together with the DG team)

* Completed:

* Implement technical DQ checks for Stage 1 Critical Tables
* Critical tables test coverage metric has been implemented
* Deployed changes related to “criticality\_tier” field alerting logic update

* “DQ observability” Project

* In progress/Next week

* Data Platform Performance Indices and DQ metrics alignment and review

* “Unified DQ” Project (DQ alignment between DI and DO teams)

* Next week

* Sync and planning next steps (common raw data structure required for DQ metrics)

* “AI supported DQ” Project

* In progress/Next week

* In testing under the Data Assets Certification Project: test all generated Cursor commands for different test types generation & compose command for all test types generation in one command

* “Incident Management” Project

* Next week:

* Incidents JIRA project will be updated with requested ticket types and workflows; first Incident Management meeting will take place on 21st of January

* DQ improvements

* Completed:

* Bugfix for “run changed” CI step (skip\_ci\_test is working)

DG

* "Data Ownership" Project (ex-BOTO):

* Completed:

* Aligned with DataOps on System Owner responsibilities
* Updated the Ownership Framework based on received feedback (added examples, links to runbooks and playbooks)

* In Progress/Next week:

* Collect remaining feedback (DParty team)
* Aligned with TLs on the refined framework
* Review and define the technical approach for migrating from the current framework

* Metadata Project:

* Completed

* Updated the new project charter and timeline in Confluence.
* Review of the metadata repository set-up options with Data Integration and Data Ops Team.

* In Progress/Next week:

* Final decision on the metadata repository set-up.
* Set-up metadata marts.

* Other:

* Completed:

* Update the retention mart:

* Added ownership details
* Tested for the upcoming quarterly cycle of the retention policy

* In Progress:

* Current Data Enrichment Process Improvement:

* Alignment with Sales IT, Sales Ops, and Sales Analytics teams to streamline the daily automated enrichment process and eliminate manual enrichment.

                

BI

* “Revenue Site in Unified Tableau” Project

* Next week:

* Finalise the migration

* “Datos Tableau Cloud in Unified Tableau” Project

* In progress:

* Test connection to AWS
* Provide access to users from Datos’ Tableau Cloud to Analytics Site

* Refactoring, Issues & Other:

* Completed:

* New BI intake channel

* In Progress / Next Week:

* Dashboard for Security Compliance team
* Additional views for Ambassador Program Dash
* BQ costs dashboard - Investigate Top 10 Expensive Queries Weekly

WA

* "Events Watchtower" Project

* In Progress/Next Year:

* Investigate Product and Marketing events overlap for possible split (Talk to product team Andrei Lenisahin)
* Adobe Analytics investigation - book a demo with to AA sales

* Digital Marketing Stories

* Completed:

* There was a drop in the MQLs - Lowered budgets

* InProgress/Next Week

* Form\_submit events unification - meeting with Marketing Automation team

* End User Stories

* Backfill events missing due to event overload - confirming necessity of backfill

* Other items

* Completed

* EX team MP data in Trebuchet
* Diego Paz email removed from Cookie Bot (Pavel is watching alerts)

Data Operations

​​

* Support improvements

* Completed:

* Support for release dbt-wrapper (v0.7.7, v0.7.8):

* introduced criticality\_tier metadata field for dbt model alert prioritization.
* bug fix for the CI step "run changed\*\*"\*\*

* Optimized the approach to using the data source for the Content Performing dashboard [BI]

* In Progress:

* Support for changes to the Corporate Service source by the Cobalt team
* new fields to Mongo export dataparadise.listing\_management\_raw\_exports\_analytics\_mongo

* Infrastructure:

* Completed:

* Review PaySol tables for SemPay migration
* [PoV] Vertex AI Workbench instance for dparty (permissions + basic setup)
* Documentations of usage of enterprise-dwh-prod-tf data-marts in DWH
* Research use of Airflow ExternalTaskMarker to improve recovery process
* Analytics Data Platform: Audit

* In Progress

* "Infrastructure Audit" Project. Platforms Infrastructure Inventory
* Optimization of the sandbox creation mechanism in BQ analytics-division-dev-tf

* Next

* Deploy Airflow ExternalTaskMarker to improve recovery process

Data Integrations

* "Implementation of a PII data cleansing process" Project

* Completed:

* Implementation of a PII data cleansing process for Intercom

* Next

* Integrate ZoomCall data and prepare PII cleaned datasets

* Data Sources & Marts Updates:

* Completed:

* IronClad workflow data from N8N to Tableau provided by Security Team [BI]
* Integrated the SFDC Order object into the SSoT SFDC
* New fields from SFDC Task and Event
* Integration Organic Traffic data from GCS
* [Issue] Resolving Ironclad sync issue has been resolved
* Data Subject Access Request from CS
* Analytics Data Platform: Audit

* In Progress

* Add ADs platforms Google Ads and Display & Video 360 data
* Reverse ETL pipeline for Facebook sign-up conversions [WA]

* Next

* Airbyte Upgrade from 1.6 to 2.0

EX

* DataChat

* Completed:

* ❤️ Google Docs, Sheets & BigQuery Resource Integration - Paste links to Google Docs, Sheets, or BigQuery tables and see them as visual chips with automatic validation, sharing guidance, and direct content reading by AI
* 📊 Monitoring Dashboard with Eval Integration - View usage statistics, charts, recent questions with filters, and create evaluation test cases directly from questions (admin feature)
* 🐛 Fixed bugs and internal improvements

* Next week:

* Fix bugs and internal work
* Support users

* Trebuchet

* Completed:

* ❤️ AI-powered Metric Debugging — Users can now debug experiment metrics using AI assistant directly from the metric chart.
* 🐛 Fixed bugs and internal improvements

* Next week:

* Conversion metric GA4 users -> GA4 users who clicked this button using this page
* Debug metric with AI for all users
* Prepare documentation for GitLab feature toggles
* Meet with the Payments solution team to discuss how to integrate with A/B backend tests

## Dec 19, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNTEwMTdUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019299643&usg=AOvVaw2lwEce0b6sXHCB7q0upu_T)

Attendees: [Analytics Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Paul Kuchin](mailto:pavel.kuchin@semrush.com)  [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

#### 

DQ

* “Unified DQ” Project (DQ alignment between DI and DO teams)

* Completed

* DI team capacity for this project has been allocated and approved. Detailed planning has been scheduled to the beginning of next year due to upcoming holidays and PTOs

* “AI supported DQ” Project

* Completed

* Cursor commands for completeness, timeliness, and column data types tests generation

* In progress/Next week

* Test all generated Cursor commands for different test types generation & compose command for all test types generation in one command

* “Data Assets Certification” Project (together with the DG team)

* Completed:

* Update dbt\_wrapper models alerting logic in order to support new “criticality\_tier” metadata field for data assets certification workflows
* Described Test creation workflow for data owners

* In progress/Next week:

* Implement technical DQ checks for Stage 1 Critical Tables
* Deploy changes related to “criticality\_tier” field alerting logic update

* “Incident Management” Project

* Completed:

* Post-mortem incident management workflow has been reviewed with team leads and finalized

* In progress/Next week:

* Incident backlog will be reviewed; regular Incident Management meetings will start in January

* DQ improvements

* Completed:

* “changed files” CI step approaches for merge request and for merge changes into master have been aligned using git diff, instead of GITLAB API to enable all bulk changes to be taken into account and mitigate API limitations (will be deployed together with the new wrapper’s version)

DG

* “Data Assets Certification” Project:

* Completed:

* Certification Progress tracking mart

* In progress/Next week:

* dbt “Contracts” feature testing

* "Data Ownership" Project (ex-BOTO):

* Completed:

* Prepared mart with ownership distribution between teams
* Working version of the Ownership Framework is done and shared with TLs and managers
* Project Charter is updated and timeline reflects upcoming changes.

* In Progress/Next week:

* Alignment with the leadership inside the division
* Finalized version of the Ownership Framework

* Metadata Project:

* Completed

* Creation of the new project charter

* In Progress/Next week:

* Adjustment on the project timeline

* Data Catalog

* Completed

* Bug Fix with expander (SQL and Columns sections)

* In Progress/Next week:

* Prepare a document with improvements proposition (req. by Nikita)

BI

* “Data Platform Metrics” Project

* In Progress/Next Steps:

* Fixing bugs

* “Revenue Site in Unified Tableau” Project

* Completed:

* Setting up users from Revenue Site to Analytics

* In Progress:

* Migration of Retention’s team remaining workbooks

* “Datos Tableau Cloud in Unified Tableau” Project

* No updates

* Refactoring, Issues & Other:

* Completed:

* Pricing Page Dashboard broken Offer ID filter
* Dashboard Certification - Key Metrics
* Refactoring AI SEO Statistics dashboard to move to prod (in testing)
* Vendor Setup - Podstudios Agency

* In Progress / Next Week:

* New Dashboards for Security Compliance team
* Addition of 3 Tableau Expansions
* Dashboard Confluence links updates
* Dashboard Certification - Content Performing
* Investigating Custom SQL sending too many queries for Content Performing

WA

* "Events Watchtower" Project

* In Progress/Next Year:

* Events drop investigation Browser/gtag limits - Placing on hold until we investigate Adobe Analytics to see if this would be solved there
* Adobe Analytics investigation - ChatGPT project for investigation created, (Talk to AA sales)

* Digital Marketing Stories

* Completed

* Integrate the li\_fat\_id value into reverse ETL  model to optimize platform attribution

* InProgress/Next Week

* New paid marketing data monitoring to proactively flag errors on data sent,dashboard ready, to be validated today or early next week.
* Enterprise Forms Submissions Investigation (form\_submit events unification) - provided the  analysis of the data of the form submits - waiting for stakeholders to evaluate

* End User Stories

* Completed

* China/Owox: MR merged, after alignment with insights team the filter is applied on dependent models, not on main model cl\_events\_intraday
* Front end start trial and purchase event drop: after anaylisis and recommendation, we agreed on a fix with Ivory team who will implement it in January.

* Other items

* Completed

* Keywordmagic data provided to the team

* In Progress/Next Week:

* KPIs/Metrics discussion

 

Data Operations

* Support improvements

* Completed:

* Release dbt-wrapper v0.7.6:

* Added a check to ensure that a new pseudo model does not duplicate existing dbt model.

* Airflow update:

* Fixed Slack alert notifications with missing compiled query issue

* [Incident Support] Supported restarting missed tasks in downstream after the data incident with “ISO Countries” dictionary
* Agreement: dbt-wrapper freeze period after release v0.7.7 on Monday, December 22th till Jan, 6th

* In Progress:

* [Issue] secure.transaction with empty PK led to long, “never-ending” queries in BQ

* Next:

* Optimize the approach to using the data source for the Content Performing dashboard [BI]

* Infrastructure:

* Completed:

* Added Alert for peak load occurrence on the BQ side

* In Progress:

* [PoV] Vertex AI Workbench instance for dparty (permissions + basic setup)
* Review PaySol tables for SemPay migration
* Research use of Airflow ExternalTaskMarker to improve recovery process

* Operational process changes

* In Progress:

* For the #analytics-data-engineering-support channel, we plan to automatically create Jira tickets for all incoming requests.

Data Integrations

* "Implementation of a PII data cleansing process" Project

* In progress:

* Implementation of a PII data cleansing process for Intercom

* "Raw Data handover to DI" SalesForce data Project

* In progress:

* Add history data from ADP Platform to SSoT SDFC SCD2 data-marts

* Data Sources & Marts Updates:

* Completed:

* Integrate data from GBP AI Agent [PG,MongoDB] [Analytics] [[DDWH-2333](https://www.google.com/url?q=https://semrush.atlassian.net/browse/DDWH-2333&sa=D&source=editors&ust=1768225019317490&usg=AOvVaw17hjxT0SOrwpEJ59LFc77C)]
* Integrate data from es-lakehouse-prod-tf: semrush\_static\_data\_pages, semrush\_static\_data\_workflows
* Integrated Intercom Conversations data for subsequent PII data cleansing process [Intercom migrated from Monil’s side]
* Zoominfo Data Enrichment process for Marketo [Marketing Automation]

* In Progress

* Integrate the SFDC Order object into the SSoT SFDC
* New fields from SFDC Task and Event
* Integration Organic Traffic data from GCS
* [Issue] Resolving Ironclad sync issue - we are still working with Fivetran & Ironclad support.

* Next:

* Add ADs platforms Google Ads and Display & Video 360 data
* Reverse ETL pipeline for Facebook sign-up conversions [WA]
* IronClad/SFDC workflows data from N8N to Tableau provided by Security Compliance Team [BI]

EX

Datachat

* This week

* 🎅 Added GPT-5.2 model
* ☃️ UX/UI: Updated Export button
* 🧦 Fixed compaction bugs, fixed charts, and next-steps

* Next week

* 🎄
* 🎄
* 🎄
* 🎄
* ☃️Test gpt 5.2
* 🧦Evals

Trebuchet

* This week

* 🎅 Conversion metric
* ☃️ Fix Slack integration bugs
* 🎁 Fix [incidents.io](https://www.google.com/url?q=http://incidents.io&sa=D&source=editors&ust=1768225019322196&usg=AOvVaw2gHMzHQqbSaUgOYCXPmNe8) alerts
* 🔧 Update frontend dependencies

* Next week

* 🎄
* 🎄
* 🎄
* 🦌Improve debug metric with AI
* ❄️Fix the conversion metric

## Dec 12, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNTEwMTdUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019322779&usg=AOvVaw1F6R-RvbqIqmdmgbvBTjrW)

Attendees: [Analytics Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Paul Kuchin](mailto:pavel.kuchin@semrush.com)  [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* “Unified DQ” Project (DQ alignment between DI and DO teams)

* Completed

* Review & update project charter with DQ team lead

* Next week:

* Final review and sharing planned efforts with DI team

* “AI supported DQ” Project

* Completed

* Uniqueness test generation has been improved with more supplementary python scripts to make it more precise

* In progress/Next week

* Multiply uniqueness test generation approach for other test types & compose command for all test types generation in one command

* “Data Assets Certification” Project (together with the DG team)

* In progress/Next week:

* Update dbt\_wrapper models alerting logic in order to support new “criticality\_tier” metadata field for data assets certification workflows
* Implement basic technical DQ checks for Stage 1 Critical Tables

* “DQ observability” Project

* Next week:

* Define key DQ metrics (test coverage, test reporting, data health and their segmentation)

* “Incident Management” Project

* Completed:

* Existed incident management workflow has been reviewed and its resurrection with improvements is ready to be shared and clarified

* In progress/Next week:

* Define convenient workflow for all parties, prepare playbook, prepare JIRA and respective Slack channel for the workflow to be active

* DQ improvements

* Completed:

* CI steps “run changed” and “validate owners” have been updated with new dbt wrapper release - now all changed tests will be triggered for their verification and there should be no problems with many changes in one MR (for example, update metadata fields for all dbt tests/models)
* Update dbt configs with “analytics-dq” and “test\_description” (instead of deprecated “analytics-qa” and “allure\_description”)
* Tests for zombie/deprecated models have been deleted

DG

* “Data Assets Certification” Project:

* Completed:

* Certification Project Stage 1 announced and kicked off
* Criticality\_tier now assigned for all dbt models
* Mart with critical models’ metadata

* In progress/Next week:

* Develop CI/CD controls for critical tables and default
* dbt “Contracts” feature testing

* "BOTO" Project:

* Completed:

* Defined problem statements and proposed solutions.

* In Progress/Next week:

* Update the Project Charter and timeline to reflect upcoming changes, including implementation approach and deadlines.
* Finalize a working version of the Ownership Framework to share with the Analytics division

* Metadata Project:

* Completed
* In Progress/Next week:

* Creation of the new project charter and architecture specification for the Metadata Inventory & Transparency Project.

* DG Strategy

* Completed:

* DG Strategy 2026 is updated

BI

* “Data Platform Metrics” Project

* In Progress/Next Steps:

* Additional Data Governance metrics
* Finishing plan for 2026 metrics addition

* “Revenue Site in Unified Tableau” Project

* In Progress:

* Setting up users from Revenue Site to Analytics
* Migration of Retention’s team remaining workbooks

* “Datos Tableau Cloud in Unified Tableau” Project

* In Progress:

* Accesses to Tableau Cloud and AWS
* AWS connection to Tableau Server test
* Migration Plan

* Refactoring, Issues & Other:

* Completed:

* Update of process for deleting tables
* Addition of dynamic disclaimer to Content Performing dash
* Vendor Setup - Topic Ranker (SERP Gap Analyzer app)

* In Progress / Next Week:

* New Dashboards for Security Compliance team
* Addition of 3 Tableau Expansions
* Dashboard Confluence links updates
* Vendor Setup - Podstudios Agency (4 vendors remaining)
* Dashboard Certification - Key Metrics
* Dashboard Certification - Content Performing
* Refactoring AI SEO Statistics dashboard to move to prod
* Investigating Custom SQL sending too many queries for Content Performing

WA

* "Events Watchtower" Project

* In Progress/Next Week:

* Events drop investigation Browser/gtag limits - discussion

* "Streaming Strategy" Project

* Completed

* Review current UA usage and establish next steps for table owners

* InProgress/Next Step

* Contact table owners and developers and discuss changes propositions

* Digital Marketing Stories

* InProgress/Next Week

* Create new dashboard for paid traffic data quality
* Create reverse ETL pipelines to Meta
* Optimize the data quality sent to Linkedin and Google now that we have emails and ads identifiers
* Enterprise Forms Submissions Investigation (form\_submit events unification)

* End User Stories

* Completed

* Identified the problem with divergence between frontend and backend data for start trial and purchases - fix will be discussed with ginger team

* InProgress/Next Week

* China/Owox: MR pending from dparty team to confirm the fix

* Other items

* Completed

* n8n for weekly watcher and assignee (#analytics-helpdesk)
* Add tracking of right mouse clicks (open in the new tab tracking - TEST)
* Structure and plan for WAE (Epics + Tickets priority)

* In Progress/Next Week:

* KPIs/Metrics discussion

Data Operations

* Support improvements

* Completed:

* Support release for dbt-wrapper v0.7.5

* Infrastructure:

* Completed:

* Change host for Berush DB Ingestion process
* Bunch of support requests:

* Airflow tasks alerts with no logs → moved to the following discussions

* In Progress:

* [PoV] Vertex AI Workbench instance for dparty (permissions + basic setup)
* Monitor too frequent queries to BigQuery
* [Issue] Compiled query is absent in test alert notifications
* Add a check of pseudo-models integrity to prevent dbt models duplications

* Next:

* Joint brainstorming sessions with DI to identify problems that we can solve in the best possible way

Data Integrations

* "Raw Data handover to DI" Project

* Completed:

* [Source Deprecation] DataOps task dataparadise.neon\_changemn is failing
* [Source Deprecation] DataOps task dataparadise.chorus\_engagements is failing
* [Issue] DataOps task dataparadise.listing\_management\_raw\_exports\_analytics\_mongo is failing

* "Raw Data handover to DI" SalesForce data Project

* In progress:

* Add history data from ADP Platform to SSoT SDFC SCD2 data-marts

* Infrastructure & Toolset

* Completed:

* Cloud Composer Instance upgraded to 2.15.3 (Airflow 2.9.3)

* Data Sources & Marts Updates:

* Completed

* Create data-mart mart\_monolith\_\_billing\_report - for financial reports and discontinuation of FinDWH [[DDWH-2514](https://www.google.com/url?q=https://semrush.atlassian.net/browse/DDWH-2514&sa=D&source=editors&ust=1768225019335377&usg=AOvVaw1MlbvoparPc3PnwLngZhUE)]
* Change Data Integration Team Metrics (Jira KPI)

* In Progress

* Integrate the SFDC Order object into the SSoT SFDC
* Integrate data from es-lakehouse-prod-tf: semrush\_static\_data\_pages, semrush\_static\_data\_workflows
* Resolve Ironclad sync issue

* Blocked

* Integrate data from GBP AI Agent [PG,MongoDB] [Analytics] [[DDWH-2333](https://www.google.com/url?q=https://semrush.atlassian.net/browse/DDWH-2333&sa=D&source=editors&ust=1768225019336143&usg=AOvVaw38RosxAzCRh_y8jg0ACHf7)]

* PostgreSQL source is OK
* With MongoDB as the source, we still have network connection issue.

EX

DataChat

        This week

* Add evals for Trebuchet MCP and improve GA4 agent
* Add ability to filter threads by tool calls
* Search threads/evals by usecase
* export dialog
* improved Confluence search
* Bugfixes

Next week

* Improve UI of exporting data
* Debug the langchain supervisor
* Try gpt-5.2

Trebuchet

        This week

* Add toolkit in Trebuchet experiment
* Add filter by toolkit and team on the Trebuchet dashboard
* Gathered initial feature requests from VP of product
* Helped to debug 0’s in the metrics of experiments

        Next week

* Planning
* Bugfixing

## Dec 5, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNTEwMTdUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019338017&usg=AOvVaw1tT_YMNB-rAoZTZsIQEwK4)

Attendees: [Analytics Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Paul Kuchin](mailto:pavel.kuchin@semrush.com)  [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Unified DQ (DQ alignment between DI and DO teams)

* Completed

* Project charter for DI & DO DQ alignment has been created
* DQ roadmap has been updated with planned activities for this project

* Next week:

* Review project charter with DQ team lead
* Share planned and required efforts with DI team

* AI supported DQ

* Completed

* dbt-repo-related documentation has been migrated from Confluence to dbt repo markdown documentation (with implemented supplementary migration script that supports recursive Confluence pages migration)

* In progress/Next week

* Implementing Cursor commands for dbt tests creation workflows

* Data Assets Certification (together with the DG team)

* Completed:

* Agreed on required models metadata changes and functionality related to alerting

* Next week:

* Update dbt\_wrapper models alerting logic in order to support new “criticality\_tier” metadata field for data assets certification workflows

* DQ observability

* Next week:

* Define key DQ metrics (test coverage, test reporting, data health and their segmentation)

* Incident Management

* Next week:

* We are going to start resurrection of the previously existed incident management workflow (review, discussion and required changes to be defined)

* DQ improvements

* Completed:

* DQ strategy has been updated & DQ roadmap has been confirmed
* Volume anomaly test macro has been updated
* dbt tests referencing missing or outdated nodes have been deleted
* Monthly highlights report has been shared

* Blocked:

* Update dbt configs with “analytics-dq” and “test\_description” (instead of deprecated “analytics-qa” and “allure\_description”)

* CI issues have been found and investigated, improvements suggestions have been shared

DG

* “Data Assets Certification” Project:

* Completed:

* Certification Framework for Dashboards
* Classification Framework for Tables confirmed between teams
* List of candidate tables for Certification confirmed by Leads

* In progress/Next week:

* Develop CI/CD controls for critical tables
* Data Contracts Testing – essential DQ check for Critical tables
* Can start certification

* "BOTO" Project:

* Completed:

* Feedback on the current Ownership Framework (BOTO) collected

* In Progress/Next week:

* Drafting the new version of the Ownership framework

* Metadata Project:

* Completed
* In Progress/Next week:

* Develop a new approach to deliver a metadata solution that is tool-agnostic and can easily integrate to a new platform (e.g., Adobe Experience Platform) but still ensures searchability, transparency, lineage, and observability.

* DG Strategy

* Completed:

* Roadmap re-prioritised; some projects were descoped

* In Progress/Next week:

* Update Strategy document and announce

BI

* “Data Platform Metrics” Project

* Done:

* Bug fixes
* Additional Data Operations metrics (Avg Execution Time per Ticket, Airflow Pipleline Success Rate)

* “Revenue Site in Unified Tableau” Project

* In Progress:

* Migration of Retention’s team remaining workbooks

* “Datos Tableau Cloud in Unified Tableau” Project

* In Progress:

* Accesses to Tableau Cloud and AWS

* Refactoring, Issues & Other:

* Completed:

* Enterprise Solution Business Overview dashboard
* Vendor Setup - Podstudios Agency (2 vendors ready)
* [Registrations Dash] Expand history to more than 2 years and add Total category
* Add jobstories and features into Activity dash
* Daily Report - Handling Issues with Zero Numbers (in test)
* Fix bugs in Stork 4.0 dashboard

* In Progress / Next Week:

* New Dashboards for Security Compliance team
* Addition of 3 Tableau Expansions
* Dashboard Confluence links updates
* Automatic license provisioning process
* Vendor Setup - Podstudios Agency (4 vendors remaining)
* Vendor Setup - Topic Ranker (SERP Gap Analyzer app)

---

WA

* "Streaming Strategy" Project

* Completed

* Testing gtag/browser limitations - discussion will follow
* Specification for PaySol Devs (sent purchase event to OWOX/GA4)

* In Progress/Next Week:

* Discontinued syncing for UA-only source tables while preserving the code and structures for dependencies. Next steps: separate tables with UA and non-UA sources.
* China/Owox: tests and discussions about best way to exclude the spam

* Other items

* In Progress/Next Week:

* Upsell audiences - proposing client side solution, waiting for requestors (triggering definition)
* Improve backend tracking for Meta ⇒ created 2 tables for reverse etl and created ticket with integrations team to work on the process under data platform (currently under bsai team)
* Workflow for analytics-helpdesk watchers - n8n integration - waiting for some clarifications from stakeholders

Data Operations

* Support improvements

* Completed:

* ​​dbt-wrapper released v0.7.3, v0.7.4

* bugfix: Changed models incorrectly added to copy list in CI/CD test runner [dparty]
* bugfix: search\_tables function bug in custom\_dev\_run\_list for ml models [dparty]
* Update ownership validation to enable analytics-dq new alias and allow analytics-bi team to be set up as an owner of tests.
* Increased the character limit to 70 characters for test slack notifications.

* Next week/In Progress:

* Change host for Berush DB Ingestion process

* Infrastructure:

* Completed:

* Fixed data-paradise-20.infrastructure.bq.tables\_info\_history script failure (after changing finance\_unit in GOST)
* Change Airflow retry strategy for hyper tasks (exponential backoff retry introduced)
* Bunch of support request

* Next week/In Progress:

* Vertex AI Workbench instance for dparty (permissions + basic setup)

Data Integrations

* "Raw Data handover to DI" Project

* Completed:

* [Issue] DataOps task dataparadise.listing\_management\_raw\_exports\_analytics\_mongo is failing
* [Source Deprecation] Delete Yahoo integration from DataOps DP

* In progress

* [Source Deprecation] DataOps task dataparadise.neon\_changemn is failing
* [Source Deprecation] DataOps task dataparadise.chorus\_engagements is failing

* "Raw Data handover to DI" SalesForce data Project

* Completed

* Implement SFDC SCD2 marts - in preparation for the replacement SFDC Ingest Analytics Platform processes

* Next:

* Add history data from ADP Platform to SSoT SDFC SCD2 data-marts

* Infrastructure

* In progress:

* Cloud Composer Instance upgrade [[DDWH-1941]](https://www.google.com/url?q=https://semrush.atlassian.net/jira/software/c/projects/DDWH/boards/281?selectedIssue%3DDDWH-1941&sa=D&source=editors&ust=1768225019350935&usg=AOvVaw3Dg_vdg8KGHQffAwtuvgvX)

* Data Sources & Marts Updates:

* Completed

* Added user\_id to api\_query\_report from Limit Service [[DDWH-2494](https://www.google.com/url?q=https://semrush.atlassian.net/browse/DDWH-2494&sa=D&source=editors&ust=1768225019351391&usg=AOvVaw04ZMSgzeOaF0SH4VLNSQUO)]
* Added new field from Marketo Leads: mql\_source\_detail, mql\_source, last\_program\_touchpoint

* In Progress

* Change Data Integration Team Metrics (Jira KPI) [[DDWH-2438](https://www.google.com/url?q=https://semrush.atlassian.net/browse/DDWH-2438&sa=D&source=editors&ust=1768225019352064&usg=AOvVaw2AyyqBdyorbitCIys0CcLT)][[a]](#cmnt1)[[b]](#cmnt2)

* Blocked

* Integrate data from GBP AI Agent [PG,MongoDB] [Analytics] [[DDWH-2333](https://www.google.com/url?q=https://semrush.atlassian.net/browse/DDWH-2333&sa=D&source=editors&ust=1768225019352610&usg=AOvVaw1pKkR7lCSeyDu00IEePZvy)]

EX

DataChat

        This week

* Updated UX/UI
* Export conversation to google docs
* Slack Bot
* Fix send feedback to Slack
* Setup Renovate

Next week

* Bugs
* Better slack bot

Trebuchet

        This week

* Requests from experiment owners
* UPDATE no WHERE clause
* Bug with select date

        Next week

* Talk to VPs of product to form roadmap for next 4-6 months
* Update the DB to Postgres18
* Fix backups

## Nov 28, 2025[Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNTEwMTdUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019355031&usg=AOvVaw3p2JS2nZe1LLnowA9n3qNm)

Attendees: [Analytics Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Paul Kuchin](mailto:pavel.kuchin@semrush.com)  [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* 💰SemPay migration

* Completed:

* Verified test cases provided by PaySol team, based on this list they will prepare real data for further testing.

* DQ improvements

* Completed:

* DQ strategy review with Mike
* Updated and aligned all Confluence pages related to the DBT QA section.
* Cursor command for uniqueness test generation with required supplementary scripts

* In Progress/Next week:

* Implementing Cursor commands for other dbt test types
* Implementation of dbt test template for rows count anomaly detection
* Data Integrations & Data Operations DQ alignment planning

DG

* “Data Assets Certification” Project:

* Completed:

* Tables Classification scoring algorithm is ready
* Dashboard Certification Priority reaffirmed with Mike and Stefan; To start in ~Dec

* In progress/Next week:

* Confirm the tables classification workflow with TLs – Nikita confirmed, Danil’s on the way
* Design-document for CI/CD controls is under review by [Aleksandr Gritsenko](mailto:a.gritsenko@semrush.com)

* "BOTO" Project:

* Completed:
* In Progress/Next week:

* Collecting feedback

* Metadata Platform Project:

* Completed
* In Progress/Next week:

* Metadata Platform priority and scope is being reassessed by leadership
* Strategic roadmap, refined implementation plan, project charter (Review in progress)
* Cost-benefit analysis draft and metadata architecture for Phase 1

BI

* “Data Platform Metrics” Project

* In Progress:

* Bug fixes
* Additional Data Operations metrics

* “Revenue Site in Unified Tableau” Project

* In Progress:

* Migration of Retention’s team remaining workbooks

* Refactoring, Issues & Other:

* Completed:

* Enterprise Solution Business Overview dashboard(in test)
* Daily Report extract fix

* In Progress / Next Week:

* Daily Report - Handling Issues with Zero Numbers
* Automatic license provisioning process
* [Registrations Dash] Expand history to more than 2 years and add Total category
* Multiple vendor setups

WA

* "Streaming Strategy" Project

* In Progress/Next Week:

* Discontinued syncing for UA-only source tables while preserving the code and structures for dependencies. Next steps: separate tables with UA and non-UA sources.
* Improving data collection and streaming to platforms (phase 1 - identification)

* Other items

* Completed:

* Fix GA4 tracking for Exploding Topics - additional analysis requested
* Drop on show events on /home - agreement with sky team on workaround (merge multiple event to one event)

* In Progress/Next Week:

* Upsell audiences - proposing client side solution, waiting for requestors (triggering definition)
* is\_first parameter - definition on payload structure (mandatory and optional params)
* Spike of traffic - contacted OWOX to understand streaming data in China vs GA4 - full data refresh soon (removing spam data)
* Purchase event drop explanation - change in tracking by product teams (event name: purchase => show) - waiting for additional data (1st Nov)
* Workflow for analytics-helpdesk watchers - n8n integration - in testing

Data Operations

* Support improvements

* Completed:

* New service account for n8n
* Reloaded the missing data in google\_campaign manager table.
* Prepared and tested a new dbt-wrapper release.

* Next week/In Progress:

* Deploy a new dbt-wrapper image.
* Working on the new cl\_ga4\_events\_intraday(data directly from GA) and creating new field on the current cl\_events\_intraday

* Infrastructure:

* Completed:

* Bunch of support request

* Next week/In Progress:

* Review and purpose image tagging and deployment in key Data Operations repos

Data Integrations

* "Implementation of a PII data cleansing process" Project

* Completed

* PII-cleaned data-mart: mart\_sfdc\_\_task, mart\_cancellation\_\_cancellation\_reason

* In progress:

* Integrate Conversations data from Intercom with PII cleansing [sot\_intercom\_ai]
* Integrate ZoomCalls info data with PII-cleaned cleansing: src\_int\_zoomCalls.

* "Migration technical test to DBT". Project

* In progress:

* Implement technical test for mart\_marketo tables

* With alerts to[incident.io](https://www.google.com/url?q=http://incident.io&sa=D&source=editors&ust=1768225019366484&usg=AOvVaw1y0wqLWy0XeHYQSgCTNyQg)

* Infrastructure

* In progress:

* Cloud Composer Instance upgrade

* Data Sources & Marts Updates:

* Completed

* Integrate data from Limit Server [Pub/Sub] [Analytics] [[DDWH-2145](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2145&sa=D&source=editors&ust=1768225019367009&usg=AOvVaw07mG7zIpxNfEkt3aKcbgSs)]
* Add recurring\_trigger\_attempts to PaySol extraction pipeline [Analytics] [[DDWH-2480](https://www.google.com/url?q=https://semrush.atlassian.net/browse/DDWH-2480&sa=D&source=editors&ust=1768225019367216&usg=AOvVaw0372TTg4J8f6uE8LvcmSjG)]
* Add new activities from Marketo: activities\_addto\_paid\_subscriptionv2 [MarTech] [[DDWH-2465](https://www.google.com/url?q=https://semrush.atlassian.net/browse/DDWH-2465&sa=D&source=editors&ust=1768225019367425&usg=AOvVaw1HQf9e4NuhqC_178snIske)]
* Add new tables from EntSol: Usermanager.segments, Usermanager.benchmarks [[DDWH-2485](https://www.google.com/url?q=https://semrush.atlassian.net/browse/DDWH-2485&sa=D&source=editors&ust=1768225019367610&usg=AOvVaw38ck03LxYqfgP1UWrgIbTy)]

* In progress

* Integrate data from GBP AI Agent [PG,MongoDB] [Analytics] [[DDWH-2333](https://www.google.com/url?q=https://semrush.atlassian.net/browse/DDWH-2333&sa=D&source=editors&ust=1768225019367871&usg=AOvVaw0HI5TlzBvOyqJWV70VlJPi)]
* Change Data Integration Team Metrics (Jira KPI) [[DDWH-2438](https://www.google.com/url?q=https://semrush.atlassian.net/browse/DDWH-2438&sa=D&source=editors&ust=1768225019368028&usg=AOvVaw3idDCPLvkzizgwPPuxu-qg)]

EX

Datachat

* This week

* Usecase and evals ownership
* Delete (hide) threads
* Remove leaderboard
* Deploy force reload
* Bugs

* Next week

* Integration with Slack
* Improve evals
* GPT-5.1
* Bugs

Trebuchet

* This week

* Fix bugs with AI Analysis and AI design validation and move to GPT-5.1
* Finish exp -> Create report
* Upgrade to Python 3.13
* Migrate to pnpm
* Removed AI Chat
* Removed unused libs
* Stopped old unused DataBase instances

* Next week

* Toolkits dimension for experiments

## Nov 21, 2025[Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNTEwMTdUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019369516&usg=AOvVaw3uKnd3y-f5vAn4Wl88kJQy)

Attendees: [Analytics Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Paul Kuchin](mailto:pavel.kuchin@semrush.com)  [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

 

DQ

* SemPay migration

* Completed:

* Migration testing planning completed. Preliminary list of automated tests has also been prepared. We are now waiting for the test data from the PaySol team and for the finalization of the mapping logic from the Analytics team.

* DQ improvements

* Completed:

* gitlab CI step “run tests on changed models” has been improved with the “warn” dbt test severity warning result
* DQ strategy and project charters documents have been updated.

* In Progress/Next week:

* AI supported dbt tests generation plan and required supplementary scripts creation.

DG

* “Data Assets Certification” Project

* Completed:

* Critical Dashboards identified, workflow for dashboards classification confirmed and now live

* In progress/Next week:

* Finish Tables Classification scoring algorithm; Improved this week to >85% accuracy
* Confirm the tables classification workflow with TLs
* Design-document for CI/CD controls

* Metadata Platform Project:

* Completed

* Feedback gathering to identify priorities, pain points, and benefits.

* In Progress/Next week:

* Strategic roadmap and refined implementation plan - For Review
* Cost-benefit analysis model - For Review
* Project Charter and Metadata Architecture - For Review

BI

* “Data Platform Metrics” Project

* Completed / In Testing:

* [Data Governance]

* Number / Volume of Deprecated Legacy Data Assets
* Number of Data Assets segmented by Retention Policy Tiers

* [BI]

* Tableau # of licenses (by type and total)
* Tableau Number of workbooks (Analytics Site without Test)
* Tableau: Storage in Gb

* “Revenue Site in Unified Tableau” Project

* Completed / In Testing:

* Migration script completed (without hyper or separate extract)

* In Progress:

* Migration of Retention’s team workbooks

* Refactoring, Issues & Other:

* Completed:

* Refund Dashboard
* Renewal metric adjustment for C-level Scorecards

* In Progress / Next Week:

* Enterprise Solution Business Overview dashboard
* Daily Report - Handling Issues with Zero Numbers
* Automatic license provisioning process

Data Chat

* Features

* New JIRAs submitted about new features:

* Export Questions
* Add Ownership to Use Cases
* Accuracy Dashboard
* Scheduled Prompts to BigQuery
* Use Case Certification
* Slack integrations

* Use Cases

* Definition of use cases with Team Leads next week

* Other

* Set up new JIRA project for DataChat

WA

* "Streaming Strategy" Project

* In Progress/Next Week:

* Identifying dbt models and their owners using UA data to determine whether they can be removed or replaced with a GA4 source. => deprioritized from this sprint

* Other items

* Completed:

* Dashboard - Marketing e-book launch
* Drop on show events on /home - recommended changes in AJST

* In Progress/Next Week:

* Spike of traffic - contacted OWOX to understand streaming data in China vs GA4 - apply the filter to OWOX - ready to filter the spam out
* Purchase event drop explanation - change in tracking by product teams (event name: purchase => show) - updating downstream tables
* Fix GA4 tracking for Exploding Topics - additional analysis requested
* Workflow for analytics-helpdesk watchers - n8n integration, app approval…
* Google Ads API - Cooperation with Marketing Automation team to get the right data from forms submitted - solution in deployment
* Is\_first param - Purchase event param removal - agreed with Marketing team to use only back end events for tracking start trials and purchase conversions. - creating the new tables, workflows and alerts
* Table fixes (incremental table refresh fix) and upgrades (ad hoc request on new marketing page)

Data Operations

* Support improvements

* Completed:

* Fixed issue with Airflow scheduler by upgrading python version
* Included health-check for Airflow Scheduler to prevent incidents like the one we got during weekend
* Ensuring alerting system for infrastructure is set
* Tableau-helper now supports numeric values(it cast it to floats to prevent issues with hypers)
* Now its already possible to use –empty parameter on custom\_dev\_run\_list command for models with not function dependency

* SemPay migration

* Next week/In Progress:

* Clarify current state of the models from the migration scope

* Infrastructure:

* Completed:

* Bunch of support requests
* Replace deprecated Slack API for notifications with a new one

Data Integrations

* "Implementation of a PII data cleansing process" Project

* In progress:

* Integrate Conversations data from Intercom with PII cleansing [sot\_intercom\_ai]
* PII-cleaned data-mart: mart\_sfdc\_\_task, mart\_cancellation\_\_cancellation\_reason

* “Metadata Platform” Project

* In progress:

* Production instance OpenMetadata

* “Data Platform Metrics” Project

* In progress:

* Change Data Integration Team Metrics (Jira KPI) [[DDWH-2438](https://www.google.com/url?q=https://semrush.atlassian.net/browse/DDWH-2438&sa=D&source=editors&ust=1768225019379634&usg=AOvVaw2MVdL-e7DlbNcEK686Ch6i)]

* Infrastructure

* In progress:

* Cloud Composer Instance upgrade

* Data Sources & Marts Updates:

* Completed

* Ownership of the data preparation process for Impact (Affiliate Marketing) has been transferred to MarTech (mart\_impact\_first\_trial\_payment)

* In progress

* Integrate data from Limit Server [Pub/Sub] [Analytics] [[DDWH-2145](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2145&sa=D&source=editors&ust=1768225019380408&usg=AOvVaw3ioz0AcsvwLPsK9vo8FHbS)]
* Integrate data from £ GBP AI Agent [PG,MongoDB] [Analytics] [[DDWH-2333](https://www.google.com/url?q=https://semrush.atlassian.net/browse/DDWH-2333&sa=D&source=editors&ust=1768225019380609&usg=AOvVaw36el4Q_6mA6CwI-9ErAhCs)]

EX  
  
-        Datachat

* This week done

* Export to Google Sheet a.k.a. Download Button right below tables in DataChat answer
* Move to PostgreSQL 18, eliminate storage issue, save 825 GB of storage
* Dynamic chart bug
* Clean and Refactor backend code
* Refactor GA4 agent prompt to align with the new GA4 table schema

* Next week

* Slack bot data-chat “agent” (trigger DataChatBot in thread for help)
* Version control
* Planning

* Trebuchet

* This week

* Refactor Trebuchet MCP tools

* Next week

* Planning

## Nov 14, 2025[Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNTEwMTdUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019381924&usg=AOvVaw2Kp6PUHAM-q53qum5diEW3)

Attendees: [Analytics Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Paul Kuchin](mailto:pavel.kuchin@semrush.com)  [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* SemPay migration

* In Progress/Next week:

* Testing efforts clarification and evaluation.

* Zombie data deletion

* Tests and tests related data have been deleted for not deprecated by DPARTY team models.

* DQ improvements

* Completed:

* Cursor documentation generation command for dbt models has been updated in accordance with the recent [documentation guide](https://www.google.com/url?q=https://semrush.slack.com/archives/C011Q58AZKR/p1762530552973709?thread_ts%3D1762524060.286089%26cid%3DC011Q58AZKR&sa=D&source=editors&ust=1768225019383244&usg=AOvVaw3Vp8-bO9CucsebAk7cjEYy) posted by the DPARTY team.
* DQ strategy and project charters documents have been updated.
* DQ Questionnaire has been shared in [#prj-analytics-data-quality](https://www.google.com/url?q=https://semrush.slack.com/archives/C09JHJ09MNZ&sa=D&source=editors&ust=1768225019383601&usg=AOvVaw1O33R3X-yIGPkC0_kVCbCK) with analytics leads for DQ plans further prioritization.

* In Progress/Next week:

* AI supported dbt tests generation plan and required supplementary scripts creation.

BI

* “Data Platform Metrics” Project

* In Progress / Next Week:

* Continuing metric expansions

* “Revenue Site in Unified Tableau” Project

* In Progress:

* Revenue Site migration pilot using script

* Refactoring, Issues & Other:

* Completed:

* Finalise Refund dashboard
* C-level Scorecard Renewal adjustment to 3-month window (in testing)

* In Progress / Next Week:

* Analysis - Hypers vs Extracs vs ClickHouse vs BiqQuery
* Automatic license provisioning for Tableau
* Refactor Enterprise Website Metrics dash
* Daily Reports - Handling Issues with Zero Numbers
* Enterprise Solution Business Overview to prod
* New vendor setup - New MRR Impact & Content Performing

WA

* "Adoption of Amplitude" Project - No news - Stakeholders silent

* In Progress/Next Week:

* Access - WIP access management solution

* "Streaming Strategy" Project

* In Progress/Next Week:

* Identifying dbt models and their owners using UA data to determine whether they can be removed or replaced with a GA4 source.

* Other items

* Completed:

* Aligned with paid marketing and implemented tag for upsell campaign.
* Fix GA4 tracking for Exploding Topics
* Workflow for analytics-helpdesk watchers

* In Progress/Next Week:

* Intake channel - playing with automation (slack, n8n. AI)
* Google Ads API - Cooperation with Marketing Automation team to get the right data from forms submitted - solution in sandbox environment
* Is\_first param - Purchase event param removal - agreed with Marketing team to use only back end events for tracking start trials and purchase conversions. Cleaning GTM ongoing.

DE (Data Operations)

* ETL Workflows 2.0:

* Next week/In Progress:

* Cloud Run Job operators have been deployed

* Streamline infrastructure:

* Completed:

* Got rid of a deprecated slack api and introduced a new one for Airflow notifications.
* Updated domain crawler to stop storing raw web pages to gcp bucket.

* Next week/In Progress:

* Still working on slack alerts bug
* Set up automatic refresh of business categories predicted from the pistachio team.

* Support improvements

* Next week/In Progress:

* Next tableau-helper release will cast numeric types to floats during hyper creation to avoid type issues
* Deploy of –empty command on DBT local environment

* SemPay migration

* Next week/In Progress:

* Clarify current state of the models from the migration scope

* Other:

* Next Week/In progress

* Manuel Knowledge transfer to Data Integrations team

Data Integrations

* "Implementation of a PII data cleansing process" Project

* Completed

* PII-cleaned data-mart: mart\_sfdc\_\_case

* In progress:

* sot\_intercom\_ai

* Integrate Conversations data from Intercom

* “Metadata Platform” Project

* Completed

* Metadata Platform Requirements Gathering

* Data Sources & Marts Updates:

* Completed

* Integrate Position Tracking: Campaign Management data-source [Analytics] [[DDWH-2225](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2225&sa=D&source=editors&ust=1768225019390731&usg=AOvVaw0bgMSyrTKP3ZO6J_Ya_KiP)]
* Integrate Enterprise Solutions PG Databases [Analytics] [[DDWH-2393](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2393&sa=D&source=editors&ust=1768225019390965&usg=AOvVaw08Yus2-DR93OH8rEOJj3eP)]

* In progress

* Integrate data from Limit Server [Pub/Sub] [Analytics] [[DDWH-2145](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2145&sa=D&source=editors&ust=1768225019391204&usg=AOvVaw1qo5ldbZD1yLcWlZbvc1pf)]
* Integrate data from GBP AI Agent [PG,MongoDB] [Analytics] [[DDWH-2333](https://www.google.com/url?q=https://semrush.atlassian.net/browse/DDWH-2333&sa=D&source=editors&ust=1768225019391373&usg=AOvVaw0jWHLzui9JesVwYtpId82t)]

EX  
  
-        Datachat

* This week done

* Export to Google Sheet a.k.a. Download Button right below tables in DataChat answer
* Move to PostgreSQL 18, eliminate storage issue, save 825 GB of storage
* Dynamic chart bug
* Clean and Refactor backend code
* Refactor GA4 agent prompt to align with the new GA4 table schema

* Next week

* Slack bot data-chat “agent” (trigger DataChatBot in thread for help)
* Version control
* Planning

* Trebuchet

* This week

* Refactor Trebuchet MCP tools

* Next week

* Planning

## Nov 7, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNTEwMTdUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019392829&usg=AOvVaw28BoFIc4TgBlvG7KisSTPx)

Attendees: [Analytics Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Paul Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* SemPay migration

* Testing approach has been discussed and requested from the SemPay team to provide test data for verification.

* DQ improvements

* Completed:

* Create a prompt for model description generation
* DQ vision has been discussed with Nikita Kudryavtsev and vision roadmap has been optimized for required goals
* Update DQ operational roadmap

* In Progress/Next week:

* Share dbt models description generation with Analytics team for testing
* Update project charters in the Data Platform KB page

DG

* “Data Assets Certification” Project

* Completed:

* Scoring system for Table Criticality Classification: ~75% Recall of SLA tables. Showtime!

* In progress/Next week:

* Define Scoring model for Dashboard Criticality Classification and Align with Analytics TLs
* Analytics TL’s review of Dashboards Criticality Classification

* "BOTO" Project:

* Completed:
* In Progress/Next week:

* Collecting feedback on the framework
* Refining the ownership framework based on the inputs

* Metadata Platform Project:

* In Progress/Next week:

* Strategic Roadmap and refined implementation plan to better show the target state of the metadata platform project.
* Feedback gathering to identify feature priorities, pain points, and benefits.

BI

* “Data Platform Metrics” Project

* In Progress / Next Week:

* Continuing metric expansions

* “Revenue Site in Unified Tableau” Project

* In Progress:

* Revenue Site migration pilot using script

* Refactoring, Issues & Other:

* Completed:

* Email statistics date filters issues
* Archived Churn Pinguin
* Pricing Page funnel dashboard (In Test)

* In Progress / Next Week:

* Analysis - Hypers vs Extracs vs ClickHouse vs BiqQuery
* Automatic license provisioning for Tableau
* Refactor Enterprise Website Metrics dash
* C-level Scorecards Renewal adjustment to 3-month window
* Daily Reports - Handling Issues with Zero Numbers

WA

* "Adoption of Amplitude" Project - No news - Stakeholders silent

* In Progress/Next Week:

* Access - WIP access management solution

* "Streaming Strategy" Project

* In Progress/Next Week:

* Researching data streaming setups (directly GA4, directly OWOX, server-side GTM)
* Price and implementation costs comparisons

* Other items

* Completed:

* Helped HR IT team implement an experimentation
* Fixing exploding topics GTM - updated setup - waiting for data
* [semrush.com/home](https://www.google.com/url?q=http://semrush.com/home&sa=D&source=editors&ust=1768225019397841&usg=AOvVaw370sL8d-EzUS-Isz9hyOAF) Tracking issues - sky team has limited events - waiting for data

* In Progress/Next Week:

* Meta - reviewed warnings and errors, started fixing them
* Intake channel - playing with automation (slack, n8n. AI)
* Google Ads API - Cooperation with Marketing Automation team to get the right data from forms submitted - blocked - waiting for marketing automation team’s implementation
* Is\_first param - Purchase event param removal - discussions with DM team and Diamond team

DE (Data Operations)

* ETL Workflows 2.0:

Next week/In Progress:

* Make current production compatible with using Cloud Run for airflow jobs (via feature flags)

* Streamline infrastructure:

* Completed:

* Now on team tiger data pipelines we are connecting directly on their DB, so we are deactivating two MongoDB machines that we have with no other usage.
* Evaluate the usage of “--empty” on DBT (Dry run)

* Next week/In Progress:

* Deploy of new DBT image with the capability of running commands with –empty for models without function dependency
* Fixing slack alerts in the failures channel
* Migrate tables copied from DI DWH to dbt staging models (95% completed).

* Support improvements

* Completed:

* Manage voyantis access to our data through Service Account

* Next week/In Progress:

* Update tableau helper to avoid issues with numeric type

* Other:

* Completed
* Next Week/In progress

* Prepare MRs for Jira Cloud migration
* Updating airflow deployment scripts

Data Integrations

* "Implementation of a PII data cleansing process" Project

* Completed

* PII-cleaned data-mart: mart\_sfdc\_\_email\_message

* In progress:

* mart\_sfdc\_\_case

* "Raw Data handover" Project

* Completed

* Incident: Airflow task failed: dataparadise.listing\_management\_raw\_exports\_analytics\_mongo

* Data Sources & Marts Updates:

* Completed

* SSoT SFDC: Pipeline cost and performance optimisations.

* In progress

* Integrate data from Limit Server [Analytics] [[DDWH-2145](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2145&sa=D&source=editors&ust=1768225019401477&usg=AOvVaw2ussy8wX5jsJVwIHYcJoam)]
* Integrate Position Tracking: Campaign Management data-source [Analytics] [[DDWH-2225](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2225&sa=D&source=editors&ust=1768225019401671&usg=AOvVaw0cwR7DaDONAjlieaPahuIq)]
* Integrate Enterprise Solutions PG Databases [Analytics] [[DDWH-2393](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2393&sa=D&source=editors&ust=1768225019401843&usg=AOvVaw3Zp4plkl7qhQXnshyJn91g)]

EX

Datachat

        This week        

* Review responses and improve evals
* Output confluence search as a tool call after response
* Improve semrush\_company\_info\_agent with better prompts and searching approach
* Little Confluence SEO with hidden phrases on pages
* Improved confluence agent searching approach
* Create ratings system for DataChat responses to store all reviews in one place (Data Base)
* Add CI job for check random 5 evals on RC and send results to a Slack

        Next week

* Fix code\_interpereter\_tool

Trebuchet

        This week

* Fix dynamic metrics form
* End-to-end testing: (Create / Edit experiments, Create / Edit metrics within an experiment)
* Add SRM check for experiments
* [Dashboard](https://www.google.com/url?q=https://lookerstudio.google.com/reporting/4451d45f-083b-4c5b-b36a-856eb5b84a1e/page/qDYeF&sa=D&source=editors&ust=1768225019403193&usg=AOvVaw0s-DhqED6ELm-mBvVtx43y) for Trebuchet experiments in Looker studio

        Next week

* Improve end-to-end tests: add checks, make run on CI

Topics:

* Jira/Confluence Cloud Migration, what to expect?

## Oct 31, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNTEwMTdUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019403788&usg=AOvVaw3ABYDxNVo8K78SHhxDn-SE)

Attendees: [Analytics Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Paul Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* MRR metrics monitoring

* Completed:

* Target and Source level test coverage enrichment for all MRR types

* In-progress:

* Core and Product level test coverage enrichment for all MRR types

* PaySol multiple currencies payments

* Completed:

* Creating alerting whenever a currency outside the predefined list appears in the payment data table.

* DQ improvements

* Completed:

* [DBT tests WARN severity](https://www.google.com/url?q=https://docs.getdbt.com/reference/resource-configs/severity&sa=D&source=editors&ust=1768225019405080&usg=AOvVaw2mU80KqvIuhfNqZud5c0aQ) alerts functionality has been enabled

* In Progress/Next week:

* Create a prompt for model description generation
* Update DQ operational roadmap
* Add the project charters in the Data Platform KB page

DG

* Project “Data Assets Certification”

* Completed:

* Dashboards classification by BI team completed – thanks to [Stefan Stošić](mailto:stefan.stosic@semrush.com)and [Alyona Kotovich](mailto:alena.kotovich@semrush.com)!
* First results for the scoring system for Table Criticality Classification: 50% Recall of SLA tables. WIP

* In progress/Next week:

* Criticality Classification scoring mode is under development
* Reconcile the Dashes Classification results for the Analytics TL’s review

* "BOTO" Project:

* Completed:
* In Progress/Next week:

* Collecting feedback on the framework
* Refining the ownership framework based on the inputs

* Metadata Platform Project:

* In Progress/Next week:

* Project Charter refinement
* Architecture specifications discussion

* Other

* Lead to Renew Program (L2R)

* In progress/Next week:

* Provide needed support on the SFDC Account Cleanup Pilot.
* Provide support on the onboarding of the new SFDC consulting and implementation partner (Coastal Cloud) to help optimize our SFDC ecosystem - collaboration plan & timeline still waiting to be announced by the Business Transformation Team.

BI

* “Data Platform Metrics” Project

* In Progress / Next Week:

* Agreed on plan for Data Operations, Integration and Governance teams
* Continuing metric expansions

* “Revenue Site in Unified Tableau” Project

* In Progress:

* Revenue Site migration pilot using script

* Refactoring, Issues & Other:

* Completed:

* Dashboard Classification document
* LTV/CAC Dashboard adjustments

* In Progress / Next Week:

* Pricing Page funnel dashboard
* Analysis - Hypers vs Extracs vs ClickHouse vs BiqQuery
* Automatic license provisioning for Tableau

---

WA

* “Back on Track” Project - DONE

* "Adoption of Amplitude" Project

* In Progress/Next Week:

* Event taxonomy discussions - no news - waiting for Andrei
* Access - licenses will be provided automatically (IT)

* "Streaming Strategy" Project

* In Progress/Next Week:

* Prepared model to switch to GA4 data instead of Owox. Tests will be based on this from now on.

* Other items

* Completed:

* Spike of traffic - Explained by Owox, done
* Intake channel - existing channel renamed, redirected users from other channels and closed them

* In Progress/Next Week:

* Meta - reviewed warnings and errors, started fixing them
* Google Ads API - Cooperation with Marketing Automation team to get the right data from forms submitted
* Fixing exploding topics GTM - meeting with stakeholders, agreed on fixes
* Helped HR IT team implement an experimentation
* [semrush.com/home](https://www.google.com/url?q=http://semrush.com/home&sa=D&source=editors&ust=1768225019415464&usg=AOvVaw0pI8wsWXEX5DqM18uGXGzc) Tracking issues

DE (Data Operations)

* ETL Workflows 2.0:

* Completed:

* Cloud run jobs are fully implemented in terraform

* Next week/In Progress:

* Make current production compatible with using Cloud Run for airflow jobs (via feature flags)

* Streamline infrastructure:

* Completed:

* Prepare terragrunt instructions for composer deployment on dev/stage/prod
* Deploy of new DBT Image fixing CI Issues and new useful commands on dbt wrapper
* Deploy of new airflow image removing last committer

* Next week/In Progress:

* Deploy of a new airflow image, removing bug on slack alerts when sending messages to the script-failures channel
* Working on the tiger team mongo db replica issue
* Migrate tables copied from DI DWH to dbt staging models (50% migrated).

* Support improvements

* Completed:

* Add sqlfluff to more folders
* Fixed drive credentials issues when modifying a model with external table as dependency
* Found root cause of user\_documents data discrepancy
* Update dbt model check  for scd columns at non-scd tables

* Next week/In Progress:



* Other:

* Completed

* Analysed user-segments API performance, identified a root cause, and implemented fixes that significantly reduced request latency.

* Next Week/In progress



Data Integration

* "Implementation of a PII data cleansing process" Project

* In progress:

* Continuing to prepare the cleansing process for mart\_sfdc\_\_email\_message
* Excluded the mart\_marketo\_\_email\_activities table from the scope

* "CLEAR" Project. Data Integrations data

* Completed:

* We’ve completed the removal of the datasets and tables that were marked for deletion during the review.

* "Reverse ETL Tool implementation" Project: Census & Fivetran

* The Fivetran contract renewal date is approaching
* We’ll try to establish a joint contract that also includes the use of Census

* Data Sources & Marts Updates:

* Completed

* Implement Reverse ETL for Intercom with user data [[DDWH-2067](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2067&sa=D&source=editors&ust=1768225019422608&usg=AOvVaw2g-nBLprumU2JBYi6mPGpV)]
* LinkedIn Conversions API RETL [Web Analytics] [[DDWH-2203](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2203&sa=D&source=editors&ust=1768225019422964&usg=AOvVaw0KdFykDadGMLRJIz5yHH7w)]
* Swoogo: Authentication issue [[DDWH-2399](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2399&sa=D&source=editors&ust=1768225019423244&usg=AOvVaw0ZBlQZLfczIFmBVOdFoS-y)]

EX

Datachat

        This week        

* Sunset universal search, redo the confluence search (show AI sub responses)
* Implement features e2e with claude
* Improved evals filtering
* Fixed various UI bugs (eval expansion, test case rows, trailing dashes)
* Update libraries: langchain 1.0 and langgraph 1.0 and OpenAI 2.6

        Next week

                Evals, bugs, UI enhancements

Trebuchet

        This week

                Implemented end-to-end testing for Trebuchet: experiment and metrics creation.

                Migrate all metrics to DB

        Next week

                Create more e2e tests

                Create Dashboard

## Oct 24, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNTEwMTdUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019426342&usg=AOvVaw0oOxvxZ0IzN2NGiw2ZciNy)

Attendees: [Analytics Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Paul Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* MRR metrics monitoring

* In progress:

* SOURCE level test coverage enrichment for all MRR types

* Rockerbox & Voyantis tests alerts

* Completed:

* Tuning and adjusting the logic of Rockerbox tests

* DQ improvements

* Completed:

* Defining criteria for table prioritization within the data lineage to support future table certification.
* Jira Cloud UAT testing

DG

* Project “Data Assets Certification”

* Completed:

* Prototype for Table Criticality Classification: Scoring System based on graph, code complexity, and downstream authority signals  – thanks to[Ekaterina Esina](mailto:ekaterina.esina@semrush.com)for collaboration

* In progress/Next week:

* Initial classification of dashboards

* Customer Engagement Data Access Policy

* Completed:

* Communication with stakeholders on access policy initiated

* In progress/Next week:

* "BOTO" Project:

* Completed:

* Refined the Project Charter and aligned with Roadmap Timeline

* In Progress/Next week:

* Collecting feedback on the current framework
* Refining the framework based on the inputs

* Metadata Platform Project:

* In Progress/Next week:

* Project Charter and architecture specifications update

* Other

* Lead to Renew Program (L2R)

* Completed

* High-Level process flow of Customer Journey from Lead Generation to Customer Churned (in collaboration with Sales IT).

* In progress/Next week:

* Provide support on the onboarding of the new SFDC consulting and implementation partner (Coastal Cloud) to help optimize our SFDC ecosystem.

BI

* “Data Platform Metrics” Project

* In Progress / Next Week:

* Continuing metric expansions

* “Revenue Site in Unified Tableau” Project

* In Progress:

* Retention pilot using migration script

* Refactoring, Issues & Other:

* Completed:

* Churn Penguin sunsetting (announcement)
* Holding MRR for Exploding Topics Vendor
* MRRhawk 2.0 Advanced with Limits sunsetting
* Aligned JIRA status & priority workflows between BI and WAE

* In Progress / Next Week:

* Analysis - Hypers vs Extracs vs ClickHouse vs BiqQuery
* Dashboard Classification
* AI Enhanced Subscriptions
* New intake channels

---

WA

* “Back on Track” Project

* Completed:

* [Bug]: GA4 events not published in their datasource :

* Self-corrected and metrics are back to normal.
* Proposed future improvement, implement throttling at the AJST level instead

* "Adoption of Amplitude" Project

* In Progress/Next Week:

* Event taxonomy discussions - no news - waiting for Andrei

* "Streaming Strategy" Project

* In Progress/Next Week:

* Compare and explore other options of streaming web data

* Other items

* Completed:

* Corporate registrations (waiting for DM to provide pixels)

* In Progress/Next Week:

* Meta - reviewed warnings and errors, started fixing them
* Google Ads API - research and start building table to be pushed
* Spike of traffic - contacted Owox to understand streaming data in China vs GA4
* Fixing exploding topics GTM

DE (Data Operations)

* ETL Workflows 2.0:

* Completed:

* Create evaluation criteria for dbt-core/dbt-cloud

* Next week/In Progress:

* Evaluate using Cloud Run for airflow jobs
* Evaluate using kubernetes for airflow jobs

* Streamline infrastructure:

* Completed:

* Prepare terragrunt instructions for composer deployment on dev/stage/prod
* Deploy of new DBT Image fixing CI Issues and new useful commands on dbt wrapper

* Next week/In Progress:

* Deploy of a new airflow image, removing the last commiters and a bug on slack alerts when sending messages to the script-failures channel

* Support improvements

* Completed:

* Created custom ls command which reads models from GCS manifest
* Reviewed pseud\_user\_id logic
* Add etl to collect metadata about gcs buckets, buckets permissions and bucket content for centring-land-727 project

* Next week/In Progress:

* Add sqlfluff to more folders

* Other:

* Completed

* Tested our systems work with Jira Cloud and prepare migration task
* Reviewed and updated stability data metrics

* Next Week/In progress

* Write the Vision for Data Engineering
* Investigating user-segment api performance

Data Integration

* "Implementation of a PII data cleansing process" Project

* In progress:

* We are continuing the implementation of the PII cleansing mechanism for the mart\_sfdc\_\_email\_message table.
* We encountered an issue with the large data volume, so the algorithms for sending data to GCP DLP will need to be refined.

* “Evaluation of Metadata Tools” Project

* In progress:

* Production Environment

* "Incident Management Framework" Project

* In progress:

* Project charter & Project kick-off
* Phase 1: Process design Q4’25
* Phase 2: Implementation Q1’26

* "Raw Data handover to BDP" Project

* In progress:

* Decommissioning Quora Source:[[](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2301&sa=D&source=editors&ust=1768225019437199&usg=AOvVaw1_coCo2F9ryJd-waGWp74b)[DDWH-2301](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2301&sa=D&source=editors&ust=1768225019437283&usg=AOvVaw3JaEuneEHY3a0PFmobxjoS)]

* Data Sources & Marts Updates:

* Completed

* SSoT SFDC. Add the Renewal\_Likelihood\_c and Renewal\_Risk\_Factorsc fields to enterprise-dwh-prod-tf.mart\_sfdc.mart\_sfdc\_opportunity [[DDWH-2329](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2329&sa=D&source=editors&ust=1768225019437779&usg=AOvVaw31snEeguE2uAATEc-zm2Cs)]
* Implement exporting process Manual Leads Data from GCS (MarTech) [[DDWH-2315](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2315&sa=D&source=editors&ust=1768225019437966&usg=AOvVaw2MrH45fN4KK1WvXZNF_dp_)]

* In Progress

* Integrate data from GBP AI Agent: gbp\_location and orchestrator\_job [[DDWH-2333](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2333&sa=D&source=editors&ust=1768225019438198&usg=AOvVaw2XuFN0EeLEYdVoquooDJz0)]
* Implement Reverse ETL for Intercom with user data [[DDWH-2067](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2067&sa=D&source=editors&ust=1768225019438354&usg=AOvVaw1QY5349EA6UzxZALCGURG3)]
* LinkedIn Conversions API RETL [Web Analytics] [[DDWH-2203](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2203&sa=D&source=editors&ust=1768225019438504&usg=AOvVaw3EBLaE4flADgSBsvQIgjc5)]

EX

Datachat

        This week        

* Sunset universal search, redo the confluence search
* Implement features e2e with claude
* Improved evals filtering
* Fixed various UI bugs (eval expansion, test case rows, trailing dashes)

        Next week

                PTOs

                Update libs

                Evals, bugs, UI enhancements

Trebuchet

        This week

                Big refactor of metrics

        Next week

                Push refactored logic to prod

E2e testing with AI

                New metrics

                

## Oct 17, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNTEwMTdUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019439704&usg=AOvVaw2u2LbESnLH8felvuW4FOAO)

Attendees: [Analytics Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Paul Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* MRR metrics monitoring

* Completed:

* New MRR models inclusion into test coverage (backlog MRR, holding\_mrr\_monthly, holding\_mrr\_weekly)

* Next week:

* SOURCE level test coverage enrichment for Committed MRR and Booking Events data

* Rockerbox & Voyantis tests alerts

* Completed:

* Test coverage for the Rockerbox data and Slack alerts redirection to dedicated channel
* Voyantis team tests update for new owox data source semrush-com.owox\_streaming\_ga4

* DQ improvements

* Completed:

* [DBT tests WARN severity](https://www.google.com/url?q=https://docs.getdbt.com/reference/resource-configs/severity&sa=D&source=editors&ust=1768225019441100&usg=AOvVaw2_If4AEg4QyHuNe9rpPe9U) alerts functionality has been enabled (the release is planned on October 27 due to other changes to be released for dbt\_wrapper) the announcement with all changes will be shared next week

DG

* Project “CLEAR”

* Completed:

* [Retention Policy](https://www.google.com/url?q=https://kb.semrush.net/pages/viewpage.action?pageId%3D256781643&sa=D&source=editors&ust=1768225019441649&usg=AOvVaw25_s_if6wfddDe5C1mRWHv) completed and soon will be announced Division-wide, marking the project-end 🎉

* Project “Data Assets Certification”

* Completed:

* Dashboard Criticality Classification Framework drafted—to be confirmed by [Stefan Stošić](mailto:stefan.stosic@semrush.com);

* In progress/Next week:

* Initial classification of dashboards
* Design criticality classification system for tables: AI approach

* Customer Engagement Data Access Policy

* Completed:

* Confirmed Access Policy implementation timelines internally

* In progress/Next week:

* Communicate with stakeholders on access policy rollout purpose and timelines

* "BOTO" Project:

* In Progress/Next week:

* Refining the Project Charter and alignment with Roadmap Timeline

* Other

* Lead to Renew Program (L2R)

* Completed

* SFDC Data Dictionary Template and document guide

* In progress/Next week:

* SFDC Account Merge Impact Analysis on data enrichment - dependencies and suggested mitigations are pending for approval by Sales IT
* High-Level process flow of Customer Journey from Lead Generation to Customer Churned - additional adjustment has been done and pending review by Sales IT

BI

* “Data Platform Metrics” Project

* Completed:

* Created source to track Stale Content and Quality labels history
* Adjusted BI metric sources for daily scale

* In Progress / Next Week:

* Continuing metric expansions

* “Revenue Site in Unified Tableau” Project

* In Progress:

* Retention pilot using migration script

* Refactoring, Issues & Other:

* Completed:

* LTV/CAC Dashboard
* MRR hawk2.0 sunsetting (questionnaire)
* JIRA Cloud testing
* Remove user persona filter from all dashboards
* Hyper files cleaning (32 removed)

* In Progress / Next Week:

* Analysis - Hypers vs Extracs vs ClickHouse vs BiqQuery
* MRRhawk 2.0 Advanced with Limits sunsetting
* Holding MRR for Exploding Topics Vendor

WA

* “Back on Track” Project

* In Progress/Next Week:

* [Bug]: GA4 events not published in their datasource - Published but failed - probably race condition issue - cannot test on RC

* "Streamline WA Infrastructure" Project

* Completed:

* Marketing Pixels cleaning - done for all GTMs (results [here](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1X_Z9sq9xx-_HgH-2vNIQpSJukSodB1ps6foRsNVUegU/edit?usp%3Dsharing&sa=D&source=editors&ust=1768225019445890&usg=AOvVaw1iullp1Mn1hZTnuZiuEQjq))
* Deprecation of Unused GTM Events (ivory-team)

* "Adoption of Amplitude" Project

* Establish the process for removing license inactive employees
* In Progress/Next Week:

* Event taxonomy discussions - no news - waiting for Andrei
* Inactive employees

* "Streaming Strategy" Project

* Completed:

* Comparison between OWOX and free GA4 (found discrepancies)

* In Progress/Next Week:

* Compare and explore other options of streaming web data

* Other items

* Completed:

* Linkedin Conversion API - table built, data being streamed

* In Progress/Next Week:

* Corporate registrations (waiting for DM to provide pixels)

Data Integration

* "Implementation of a PII data cleansing process" Project

* In progress:

* Prepared a roadmap. Implementation all tables will be finished approximately in mid-November.

* “Firmographic Enrichment Service” Project

* Inherits the results of the “Data Enrichment Optimizations” project
* The goal is to replace the existing enrichment solution for SFDC to simplify its maintenance

* “Evaluation of Metadata Tools” Project

* OpenMetadata won as a result of a thorough comparison.
* The details will be announced later today.

* Reverse ETL for Intercom

* In progress:

* Implement Reverse ETL for Intercom with user data [[DDWH-2067](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2067&sa=D&source=editors&ust=1768225019448355&usg=AOvVaw3XO7hFozWp60ZqqQP1YzGd)]: Final stages of preparing the requirements and data for delivery.

* Data Sources & Marts Updates:

* Completed

* Resume process & reload program\_members data (Marketo) [[DDWH-1741](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-1741&sa=D&source=editors&ust=1768225019448816&usg=AOvVaw1kb3IKkEYH6EFoR9y5Dv8z)]
* Change source SFTP to GCS for Oracle MRR data-mart [[DDWH-2152](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2152&sa=D&source=editors&ust=1768225019449008&usg=AOvVaw0_wBZboqTfM2FDtoeAxg0r)]: to minimisation of using SFTP infra
* Bug: Broken formula check\_formula\_failures\_sbqq\_quote\_c [[DDWH-2221](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2221&sa=D&source=editors&ust=1768225019449315&usg=AOvVaw0HX7gdosKoGSbDURDF-feY)]
* Bug: Model stg\_entsol\_\_product\_analytics\_static\_data\_customers is failing [[DDWH-2299](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2299&sa=D&source=editors&ust=1768225019449558&usg=AOvVaw0xDh_fnE0e9Er7ThlNKQOZ)]
* Issue: BigQuery costs jumped significantly since Sep 23rd [[DDWH-2316](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2316&sa=D&source=editors&ust=1768225019449772&usg=AOvVaw2sY6PVTbvvxz2WatfBPhed)]
* Issue: Failed Semrush Monolith DB data integration [[DDWH-2318](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2318&sa=D&source=editors&ust=1768225019449962&usg=AOvVaw3VUlcFhtjc-s0qxvDKNpsa)]

* In Progress

* Implement exporting process Manual Leads Data from GCS (MarTech) [[DDWH-2315](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2315&sa=D&source=editors&ust=1768225019450193&usg=AOvVaw2Q4hLsxR9HMQXUvVRG7aWD)]
* Integrate data from Limit Server [Analytics] [[DDWH-2145](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2145&sa=D&source=editors&ust=1768225019450365&usg=AOvVaw22B6ozuMbZXRBDFZ9lFvud)]
* Integrate Zuora Revenue data [Business Units Partnership] [[DDWH-2061](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2061&sa=D&source=editors&ust=1768225019450555&usg=AOvVaw2c8LSYliw1E7rcK26lPd3-)]
* LinkedIn Conversions API RETL [Web Analytics] [[DDWH-2203](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2203&sa=D&source=editors&ust=1768225019450716&usg=AOvVaw1CckvDbnQ_0J1M0DDpfy5O)]

* Next (new major requests):

* New Source: Integrate data from GBP AI Agent: gbp\_location and orchestrator\_job [[DDWH-2333](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2333&sa=D&source=editors&ust=1768225019450979&usg=AOvVaw0qZPAPJXaA_27g_u4rgtFz)]
* Change: SSoT SFDC. Add the Renewal\_Likelihood\_c and Renewal\_Risk\_Factorsc fields to enterprise-dwh-prod-tf.mart\_sfdc.mart\_sfdc\_opportunity [[DDWH-2329](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2329&sa=D&source=editors&ust=1768225019451406&usg=AOvVaw1CwFPCip2t5Q-i2Gi9i1VV)]

DE (Data Operations)

* Infrastructure 2.0:

* Completed:

* Deprecate useless pseudo models at data-paradise
* Expose metadata about buckets and Cloud Storage buckets permissions

* Next week/In Progress:

* Explore using google cloud run for airflow tasks instead of VM
* Create Airflow staging
* Collect metadata about objects in production Cloud Storage buckets

* Streamline infrastructure:

* Completed:

* Sunset the sellzone project
* Next week/In Progress:

* Migrate tables from Data Integration DWH to staging DBT models. 30% migrated.
* Update stability data metrics.
* Fixing a bug in CI, the update hyper step runs during run changed prod even when the changes aren’t hyper-related, causing the pipeline to fail.

* Support improvements

* Completed:

* Test our systems work with the new Jira Cloud environment
* Groom our backlog, filter some outdated tasks

EX

Trebuchet

* This week

* Markdown editor for descriptions of the experiment
* CI/CD pipeline - 3x faster
* Improved error handling and Sentry error storage
* Updated dependencies to latest versions
* Enhanced Slack API integration with improved image upload and better text block formatting
* Fixed dependencies and configuration issues
* Added SAST security scanning to CI workflow

* Next week

* Reach out to dev. teams on how to properly setup exp.

Datachat

This week

* Bug fixes, evals

Next week

* Bug fixes, evals

Notes



Action items

## <testing\_tableau\_embeddings>

## 

## </testing\_tableau\_embeddings>

---

## Oct 10, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019455157&usg=AOvVaw28Le25Crc3HHLbd0HkRypN)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* MRR metrics monitoring

* In progress / Next week:

* SOURCE level test coverage enrichment for Committed MRR and Booking Events data
* New MRR models inclusion into test coverage (backlog MRR, holding\_mrr\_monthly, holding\_mrr\_weekly)

* Rockerbox & Voyantis tests alerts

* In progress:

* Test coverage for the Rockerbox data and Slack alerts redirection to dedicated external channel
* Voyantis team tests update for new owox data source semrush-com.owox\_streaming\_ga4

* GA4 Streaming Data Health Checks

* Completed:

* Update GA4 Streaming tests to apply monitoring checks only to jobstories with sufficient history

* DQ improvements

* Completed:

* DBT tests and models alerts severity logic and appearance have been updated (we will release updates in the beginning of the next week)

* Next week / In progress:

* DQ vision interviews with stakeholders and strategy feedback collection
* DBT tests warnings enablement

DG

* Project “CLEAR”

* Completed:

* GCS buckets Clearing done - [report results](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1dRuEhv49u4kBVBwvUI2mX4_tjQQ3TwizioHb5XjCcbI/edit?gid%3D288335546%23gid%3D288335546&sa=D&source=editors&ust=1768225019457360&usg=AOvVaw25CUVraKKQLNpC6JNgIDLg)
* Quarterly Notification live

* In progress/Next week:

* Automation of the retention policy
* Adjustments to the Retention & Archival Policy

* Project “Data Assets Certification”

* Completed:

* New Project Charter

* In progress/Next week:

* Design criticality classification system
* Discuss Project Charter with TLs

* Customer Engagement Data Access Policy

* Completed:

* Project Charter and Scope confirmed with Data Integrations and Monil

* In progress/Next week:

* Confirm access cut-off timelines and Communicate with stakeholders on it

* Other

* Lead to Renew Program (L2R)

* Completed
* In progress/Next week:

* High-Level process flow of Customer Journey from Lead Generation to Customer Churned - pending review with Sales IT
* Adjustments on the SFDC Data Dictionary Template - pending review with Sales IT

BI

* “Data Platform Metrics” Project

* Completed:

* Created source to track Stale Content and Quality labels history
* Adjusted BI metric sources for daily scale

* In Progress / Next Week:

* Continuing metric expansions

* “Revenue Site in Unified Tableau” Project

* Completed:

* Proposed merge structure
* Kickoff with Retention and Sales BI

* In Progress/Next Week:

* Retention pilot using migration script

* Refactoring, Issues & Other:

* Completed:

* Tableau Add-On for Google Docs Guide
* RoR Churn Dashboard wireframe

* In Progress / Next Week:

* Analysis - Hypers vs Extracs vs ClickHouse vs BiqQuery
* JIRA Cloud testing
* MRR hawk2.0 sunsetting (questionnaire)
* MRRhawk 2.0 Advanced with Limits sunsetting
* LTV/CAC Dashboard - additional development

WA

* “Back on Track” Project

* In Progress/Next Week:

* [Bug]: GA4 events not published in their datasource - ready for production test next week

* "Streamline WA Infrastructure" Project

* Completed:

* Marketing Pixels cleaning - semrush.com container - Final result: Reduced GTM size: From 91% to 67% (24% reduction)

* In Progress/Next Week:

* Continuing with Marketing Pixels cleaning - searchengineland.com and backlinko.com containers

* "Adoption of Amplitude" Project

* In Progress/Next Week:

* Event taxonomy discussions

* "Streaming Strategy" Project

* In Progress/Next Week:

* Comparison between OWOX and GA4

* Other items

* Completed:

* Linkedin Conversion API - table built, ready to be pushed
* Traffic spike investigation : spam traffic

Data Integrations

* "Raw Data handover to BDP" Project

* Completed

* Incident: DataOps DP job dataparadise.listing\_management\_raw\_exports\_analytics\_mongo is failing [[DDWH-2223](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2223&sa=D&source=editors&ust=1768225019462529&usg=AOvVaw0tGoIHhvvqcBvO33m0O5PT)]

* In progress:

* DataOps DP job dataparadise.QuoraAds is failing [[DDWH-2198](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2198&sa=D&source=editors&ust=1768225019462777&usg=AOvVaw3AE3_6UW4G_YTCp7VsKFvi)]: We are preparing this process for decommissioning.
* DataOps DP job dataparadise.e2e\_tests\_acquisition\_quora is failing [[DDWH-2199](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2199&sa=D&source=editors&ust=1768225019463038&usg=AOvVaw3VZkz2Qe91gZQcH8EqaFWZ)]: We are preparing this process for decommissioning.

* On hold

* Incident: DataOps DP job dataparadise.osm\_data\_loader is failing [[DDWH-2109](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2109&sa=D&source=editors&ust=1768225019463461&usg=AOvVaw3XGUL7DumdpwXyagfs9gCb)]

* "Implementation of a PII data cleansing process" Project

* In progress:

* We received a prioritized list of tables that need to be cleaned of PII next. And began analyzing and planning the work.

* Reverse ETL for Intercom

* In progress:

* Implement Reverse ETL for Intercom with user data [[DDWH-2067](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2067&sa=D&source=editors&ust=1768225019464078&usg=AOvVaw0G8Ktcta5I7avdfBK950D8)]: Still in the process of analyzing implementation options

* Data Sources & Marts Updates:

* Completed

* New Source: Data Mart for Enterprise Users [MarTech] [[DDWH-2187](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2187&sa=D&source=editors&ust=1768225019464441&usg=AOvVaw1pVI39F2Qxf9pkYAU62BvJ)]: Source from Enterprise Users to send to Marketo.
* New Source: Integrate Airtable data [Analytics] [[DDWH-2171](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2171&sa=D&source=editors&ust=1768225019464672&usg=AOvVaw09gqQxb2nkAXvdLabP4Y1r)]: Customer Onboarding data from Marketing Airtable
* New Source: Oracle Report data integration (Prowly's CAC) [Analytics] [[DDWH-1753](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-1753&sa=D&source=editors&ust=1768225019464931&usg=AOvVaw2u1Yh79Jy4zdZyZQu4P_Jx)]: Data from the report is delivered daily to the PROD data mart.
* New Source: Reporting Solution trials extraction [Analytics] [[DDWH-2202](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2202&sa=D&source=editors&ust=1768225019465414&usg=AOvVaw3f8ctnRm_MS8bZbysoAJk1)]
* Updated Source: Add a new field eligible\_for\_the\_lifecycle in workato recipe Lead Export from Marketo [MarTech] [[DDWH-2209](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2209&sa=D&source=editors&ust=1768225019465849&usg=AOvVaw0XZwiMeit548zAcixtc2H-)]
* Review the "CLEAR": Projects for review by BDP [[DDWH-2019](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2019&sa=D&source=editors&ust=1768225019466054&usg=AOvVaw3n2h8SqLjlc2f1vZqq1TBH)]: We have completed the review of BigQuery related to the Clear project. For tables that require additional work before deletion, we have created separate tasks.
* Clean decommissioned Salesforce processes and data [[DDWH-2119](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2119&sa=D&source=editors&ust=1768225019466393&usg=AOvVaw0m0BfHg4tKXmqGfchxYTS6)]: After completely disabling the old SFDC exports we removed over 2k tables from BQ, GCP infrastructure, and Fivetran artifacts.
* Incident: Ironclad source authentication failure [[DDWH-2196](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2196&sa=D&source=editors&ust=1768225019466738&usg=AOvVaw3Wmr057RYKg9j22PRgq7Pw)]: The configuration on the Fivetran side has changed.
* Incident: Fix a missing column in stg\_entsol\_\_product\_analytics\_static\_data\_customers [[DDWH-2204](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2204&sa=D&source=editors&ust=1768225019467003&usg=AOvVaw0iePedLzkhQeYERnhdHC9F)]: The field in the source has been deleted.

* Next:

* New Source: Integrate data from Limit Server [Analytics] [[DDWH-2145](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2145&sa=D&source=editors&ust=1768225019467329&usg=AOvVaw3TqhqdQ8cienw66leXhcEd)]
* New Source: Integrate data from Oracle ERP for Procurement Team [[DDWH-2205](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2205&sa=D&source=editors&ust=1768225019467531&usg=AOvVaw3-ZClvfeDURnKOrKoUdy6q)]
* New Source: Integrate Position Tracking: Campaign Management data-source [Analytics] [[DDWH-2225](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2225&sa=D&source=editors&ust=1768225019467792&usg=AOvVaw1ZEK8hApQCnCfD0Rd2NLA4)]
* New Source: Integrate Zuora Revenue data [Business Units Partnership] [[DDWH-2061](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2061&sa=D&source=editors&ust=1768225019468004&usg=AOvVaw2f1h4dVKDT9EEHeowOiiDl)]
* New Reverse RETL: LinkedIn Conversions API RETL [Web Analytics] [[DDWH-2203](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2203&sa=D&source=editors&ust=1768225019468244&usg=AOvVaw3XRcrzFMTF5CXqbCG--Ncr)]

DE Function (Data Operations)

* Infrastructure 2.0:

* Completed:

* Working with admin team on using kubernetes for airflow tasks
* Created terraform deployment for cloud composer on dev environment
* Explore Airflow 3 deployment in Cloud Composer

* Next week/In Progress:

* Explore using google cloud run for airflow tasks instead

* Streamline infrastructure:

* Completed:



* Next week/In Progress:

* Migrate tables from Data Integration DWH to staging DBT models. 30% migrated.
* Update stability data metrics.

* Support improvements

* New quarterly script that send a message on internal channel with the next targets tables of project CLEAR

* Other:

* We collected data from our script failure channel for future analysis

EX  
Trebuchet  
        This week

A library to split users into groups is in prod and already used now  
Next week  
        Plan refactoring for automatic metrics creation

DataChat

This week

* Maintenance: Added SAST to CI pipeline for enhanced security scanning  
  Implemented NotFound page
* Evals: Enhanced evals page with better functionality and UI
* Bugs: Scheduled prompts in prod
* Bugs: k8s configs still hard to do
* Bugs: Upgraded PostgreSQL to version 17
* Bugs: Fixed BigQuery schema refresh to properly update field

Next week

* Fix Bugs
* Create Evals
* Fix prompts

Notes:

* Please don't forget to complete your self-evaluations in WD today!

## Oct 3, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019471494&usg=AOvVaw1lqBEAec0godmZac5AfnoT)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* MRR metrics monitoring

* Completed:

* PRODUCT layer test coverage of the Committed MRR and Bookings has been improved

* Next week:

* SOURCE level test coverage enrichment for Committed MRR and Booking Events data
* New MRR models inclusion into test coverage (backlog MRR, holding\_mrr\_monthly, holding\_mrr\_weekly)

* Rockerbox tests (request from Eugeniy Sobolev)

* Next week:

* Test coverage for the Rockerbox data and Slack alerts redirection to dedicated external channel

* DQ improvements

* Completed:

* DQ Strategy Vision roadmap

* In progress:

* DBT tests and models severity testing

* Next week:

* DQ vision interviews with stakeholders and strategy feedback collection
* DBT tests warnings enablement

DG

* Project “CLEAR”

* Completed:

* GCS buckets Clearing done (27 buckets); report results next week

* In progress/Next week:

* Automation of the retention policy
* Adjustments to the Retention & Archival Policy

* Project “Data Enrichment Optimization”

* Completed
* In progress/Next week:

* Initial Data Enrichment Optimization effort will now be focused on the tech solution to Firmographics enrichment service into Analytics & Marketing. Data Integration team will be responsible for the implementation in the DWH.
* The wider data enrichment effort (not just firmographics but also commercial, engagement, and behavioral data) will be a core part of the L2R (Lead to Renew) program.

* Project “Data Assets Certification”

* Completed:

* Staged rollout approach confirmed, with quality stages TBD later

* In progress/Next week:

* Design criticality classification system

* Customer Engagement Data Access Policy

* Completed:

* Policy confirmed with Data Integrations and Monil

* In progress/Next week:

* Communicate with stakeholders on the access change
* Scope extension: PII-cleaned versions now required for all customer domain tables, not chorus only as planned before; Timeline to be aligned with Data Ints

BI

* “Tableau Cloud Migration” Project

* Completed:

* Folder Structure & Permission Matrix

* In progress / Next Week:

* Costing Analysis

* “Data Platform Metrics” Project

* Completed:

* Rearranging dashboard layout
* Added DQ metrics from BI Alert

* In Progress / Next Week:

* Expanding BI metrics

* “Revenue Site in Unified Tableau” Project

* Completed:

* Proposed merge structure

* In Progress/Next Week:

* Kickoff with Retention and Sales BI

* Refactoring, Issues & Other:

* Completed:

* Scorecards Sales Rep source adjustment
* Redesign New/Active/Lost Users dashboard

* In Progress / Next Week:

* RoR Churn Dashboard wireframe
* Tableau Add-On for Google Docs Guide
* Analysis - Hypers vs Extracs vs ClickHouse vs BiqQuery

WA

* Completed:

* Owox vs ga4 comparison done for page views, and 3 main conversions

* In Progress/Next Week:

* Linkedin Conversion API - building table with the right table : investigation, development
* [Bug]: GA4 events not published in their datasource: 90% there
* Marketing Pixels cleaning - Continue with other containers
* Amplitude integration project - discussions about taxonomy

Data Integrations

* "Raw Data handover to BDP" Project

* On hold

* DataOps DP job dataparadise.osm\_data\_loader is failing. [[DDWH-2109](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2109&sa=D&source=editors&ust=1768225019478652&usg=AOvVaw27fBlgcKPDmup46-Ra8uH7)]

* In progress:

* DataOps DP job dataparadise.QuoraAds is failing [[DDWH-2198](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2198&sa=D&source=editors&ust=1768225019478931&usg=AOvVaw1PT4LQgcVzAHd6l0hIpzSf)]
* DataOps DP job dataparadise.e2e\_tests\_acquisition\_quora is failing [[DDWH-2199](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2199&sa=D&source=editors&ust=1768225019479133&usg=AOvVaw2dmHYNr_hDusYZc8A63_xO)].

* "Implementation of a PII data cleansing process" Project

* Completed:

* Defined data agnostic approach for clearing PII data. Implementation of a PII data cleansing process for Chorus data [[DDWH-2168](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2168&sa=D&source=editors&ust=1768225019479689&usg=AOvVaw11gGwjwOG8jGbgh9LKU2h9)]

* Reverse ETL for Intercom

* In progress:

* Implement Reverse ETL for Intercom with user data. In the process of analyzing implementation options and developing requirements [[DDWH-2067](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2067&sa=D&source=editors&ust=1768225019480113&usg=AOvVaw399ebTZJxAxFNlwZoSopci)]

* Jira Cloud UAT

* Completed: We tested the Jira Cloud instance with our project and prepared a report for IT Support

* Sources and data-marts updates / business-requests:

* Completed

* Integrate crawler data from Black Team Pub/Sub topic [[DDWH-2166](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2166&sa=D&source=editors&ust=1768225019480782&usg=AOvVaw3vTwuagU4OsN9oAM8yxjSn)]
* Revenue report (September 2025 revenue, FinDWH)

* In progress

* Data Mart for Enterprise Users [[DDWH-2187](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2187&sa=D&source=editors&ust=1768225019481089&usg=AOvVaw1GHeweN7jKB3GKGhsMdFdB)]
* Integrate Airtable data [[DDWH-2171](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2171&sa=D&source=editors&ust=1768225019481227&usg=AOvVaw3i5tQc6RBcyffEufz8nth7)]
* Oracle Report data integration (Prowly's CAC). We’re ready with RC and waiting for Production data from Oracle [[DDWH-1753](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-1753&sa=D&source=editors&ust=1768225019481529&usg=AOvVaw2xSnELUDQnJ8WKlVP9QKaw)]

* Next:

* Data integrations: Integrate Limit Server (Analytics) [[DDWH-2145](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2145&sa=D&source=editors&ust=1768225019481845&usg=AOvVaw3QJzAMfclDEnwVBfvWGmOe)]
* New: Reporting Solution trials extraction (Analytics) [[DDWH-2202](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2202&sa=D&source=editors&ust=1768225019482017&usg=AOvVaw2tX44noOTAZddnMwrFyGXn)]
* New: LinkedIn Conversions API RETL [[DDWH-2203](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2203&sa=D&source=editors&ust=1768225019482169&usg=AOvVaw14dzMyaLkP5Ts6yghRimlN)]

DE Function (Data Operations)

* Infrastructure 2.0:

* Completed:

* Added a new Gitlab ci step to ensure Gitlab dbt datasets are cleared when CI starts
* Disabled automatic views removing process

* Next week/In Progress:

* Explore running airflow jobs in kubernetes

* Streamline infrastructure:

* Completed:

* Migrated Slack API to the new API.
* Materialization table\_copy was released, existed table copies was migrated to use this new option

* Next week/In Progress:

* Migration of tables which we copy from Data Integration dwh to dbt staging models.

* DBT-wrapper

* Completed:

* Fix pseudo models integration on CI

* Next week/In Progress:



* Support improvements

* Completed:

* Clear dataset script created to be able to clear personal datasets
* Manually created gsheets external tables are completely migrated into dbt projects as external materializations
* Created new prowly staging tables from dwh-prod-tf

* Next week/In Progress:

* Sqlfluff will be completely applied for analytics-projects-prod

* Other:

* Completed:



* Next week/In Progress:

* Performance evaluations in progress

EX

* Trebuchet

* Helped with incoming requests “Why I see this data”
* Made announcements for devs about migration to new events structure next week

* DataChat

* This week

* Optimized CI/CD.
* Migrated evaluations to database
* Fixed UI bugs including table overflows, tool call formatting, and result visibility issues.
* Enhanced eval system with batch processing.
* Restricted access by division.
* Refactored compaction logic and fixed heartbeat streaming.

* Next week

* Fix bugs
* Improve UI for evals
* Revisit evals, get back to Analysts
* Add more evals

## Sep 26, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019486372&usg=AOvVaw2pmDA4_c7Sn1gYSxAQ2H8N)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* MRR metrics monitoring

* Completed:

* Implementation of automated tests for CORE layer of the Committed MRR and Bookings
* Brand24 tests have been switched to new daily data sources

* Rockerbox tests (request from Eugeniy Sobolev)

* Next week:

* Test coverage for the Rockerbox data
* Rockerbox Slack alerts redirection to external channel

* DQ metrics

* Completed:

* Pass and failure dbt tests counts & rates have been implemented
* Descriptions have been added to all DQ metrics models

* Next week:

* DBT tests Slack alerts metric

* DQ improvements

* In progress / Next week:

* DQ Strategy Vision roadmap

* Next week:

* DBT tests and models severity testing
* DBT tests warnings enablement

DG

Project “CLEAR”

* Completed:

* Compute Costs reported

* In progress/Next week:

* GCS buckets Clearing (16 / 27 completed)
* Automation of the retention policy
* Adjustments to the Retention & Archival Policy

Project “Data Enrichment Optimization”

* Completed
* In progress/Next week

* Alignment with the Growth Analytics Team on the usage of CompanyEnrich credits.
* Alignment with Business IT on lead enrichment and enrichment latency.

Project “Data Assets Certification”

* Completed:

* Alternative approach to certification, to be approved reviewed by [Sam Bishop](mailto:lynne.bishop@semrush.com)

* In progress/Next week

Customer Engagement Data Access Policy

* Completed:

* Confirmed scope of data, draft policy and list of stakeholders with Monil

* In progress/Next week

* Refine policy and communicate with stakeholders on the access change

BI

* “Tableau Cloud Migration” Project

* Completed:

* Folder Structure & Permission Matrix

* In progress / Next Week:

* Costing Analysis

* “Data Platform Metrics” Project

* Completed:

* Fixes and visual improvements
* Modifying sources for daily & weekly views
* Adding Data Operation metrics

* In Progress / Next Week:

* Expanding BI metrics
* Rearranging dashboard layout

* “Revenue Site in Unified Tableau” Project

* Completed:

* Proposed merge structure

* In Progress/Next Week:

* Kickoff with Retention and Sales BI

* Refactoring, Issues & Other:

* Completed:

* LTV/CAC dashboard

* In Progress / Next Week:

* RoR Churn Dashboard wireframe
* Redesign New/Active/Lost Users dashboard
* Scorecards Sales Rep source adjustment

WA

* Completed:

* Marketing Pixels cleaning - [semrush.com](https://www.google.com/url?q=http://semrush.com&sa=D&source=editors&ust=1768225019492496&usg=AOvVaw2Ir1wiTYfAUTaX51aHxz5n) container cleaned (12 % drop)

* In Progress/Next Week:

* Marketing Pixels cleaning - Continue with other containers
* OWOX Utilization & Necessity Review - comparison running
* Amplitude integration project
* [Bug]: GA4 events not published in their datasource: Solution fix ⇒ unexpected roadblock searching for fix
* Linkedin Conversion API - meeting with Linkedin, next steps defined, building table to be pushed

Data Integrations

* "Raw Data handover to BDP" Project

* On hold

* DataOps DP job dataparadise.osm\_data\_loader is failing. [[DDWH-2109](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2109&sa=D&source=editors&ust=1768225019493716&usg=AOvVaw2j5DkOJLTuHe4SRj5yaeHj)]

* In progress:

* DataOps DP job dataparadise.QuoraAds is failing [[DDWH-2198](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2198&sa=D&source=editors&ust=1768225019493967&usg=AOvVaw15rRuIZRIoafmVvfxKUUwc)]
* DataOps DP job dataparadise.e2e\_tests\_acquisition\_quora is failing [[DDWH-2199](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2199&sa=D&source=editors&ust=1768225019494164&usg=AOvVaw19ookHQgyJvmMrI7i4IOq2)].

* "Implementation of a PII data cleansing process" Project

* In progress:

* Defined data agnostic approach for clearing PII data. Finalizing implementation for Chorus [[DDWH-2168](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2168&sa=D&source=editors&ust=1768225019494651&usg=AOvVaw1Fn-7PZ4YwGzp42HV8b9kn)]

* "Data Enrichment Optimization" Project

* Completed

* Re-enrichment of the rest of accounts [[DDWH-2182](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2182&sa=D&source=editors&ust=1768225019494936&usg=AOvVaw1KbQA811LmVddHLRYb6ver)]

* In progress:

* Domain checker process design [[DDWH-1991](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-1991&sa=D&source=editors&ust=1768225019495158&usg=AOvVaw06NPVQB8rPwEsvmIcONUk8)]

* Reverse ETL for Intercom

* In progress:

* Continuing communication with Intercom customer support to resolve missing data issue. [[DDWH-2067](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2067&sa=D&source=editors&ust=1768225019495491&usg=AOvVaw38Q8ymvd8zIT7smYe5QX1U)]

* Sources and data-marts updates / business-requests:

* Completed

* PaySol data-mart for SFDC Opportunities: Implementing outbound data-mart for SFDC Reverse ETL - SFDC Opportunity Refinement (IT Division request) [[DDWH-2169](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2169&sa=D&source=editors&ust=1768225019495885&usg=AOvVaw24PNF-AR8K7-EjTwyUMRDs)]
* Data integrations from PR toolkit trials [[DDWH-2102](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2102&sa=D&source=editors&ust=1768225019496105&usg=AOvVaw0PzzDGc5ttpQifPzK6P4m2)]
* Revise mart\_zuora\_\_product [[DDWH-2165](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2165&sa=D&source=editors&ust=1768225019496283&usg=AOvVaw0l7zw6Q2fiCaqKXGgr2wTV)]
* Data Subject Access Request [[DDWH-2191](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2191&sa=D&source=editors&ust=1768225019496427&usg=AOvVaw1Xv-mT4BxODdfn7HsSJF6s)]

* In progress

* Integrate crawler data from Black Team Pub/Sub topic [[DDWH-2166](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2166&sa=D&source=editors&ust=1768225019496656&usg=AOvVaw05nX851nPaA_vBFyTGk1BM)]

DE Function (Data Operations)

* Infrastructure 2.0:

* Completed:

* Removed UDFs which were not defined in dbt.
* Fixed datasets and tables metadata collection process

* Next week/In Progress:

* Ensure Gitlab dbt datasets are cleared when CI starts
* Terraform deployment for Airflow

* DBT-wrapper

* Completed:



* Next week/In Progress:



* Support improvements

* Completed:



* Next week/In Progress:

* Migrate manually created external tables to external materializations
* Pause developing of dbt external package until we have staging environment, due to inability to proper test changes before moving to production
* Release table\_copy materialization

* Other:

* Completed:



* Next week/In Progress:

* Migrate Slack API

EX

Trebuchet

* This week

* Testing new script for dividing users into groups in prod together with [Ondra Šubrt](mailto:ondra.subrt@semrush.com)

* Next week

* Break all the experiments on production

DataChat

* This week

* Share chat revamped
* Automatic request retry system
* Context overflow protection
* Network timeout issues
* Evals for retention team

* Next week

* Bugs, network issues
* Advanced sharing permissions and controls

Notes:

* DataChat – now public
* DataEng – helps on holidays
* Meet up with inDrive
* Performance Review starts on Sept 29
* Our Goals for H2

 

## Sep 19, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019500253&usg=AOvVaw0BSugVKZkH50TNwmfpsML7)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Elementary Data POC

* Accounting blessed the opportunity to sign the contract this year
* Next week:

* Procurement team to discuss with ED final price
* Procurement team to discuss with Sam and CFO the business case
* Preliminary approval request support and facilitation

* DBT Cloud POC

* Answered questions from the dbt Cloud regarding DQ.

* MRR metrics monitoring

* In Progress/Next week:

* Implementation of automated tests for CORE layer of the Committed MRR and Bookings

* DQ improvements

* Completed:

* Count of issues identified by data tests metric has been implemented
* DBT tests number and MRR test coverage metrics have been updated with daily values
* DQ Strategy rework into DQ vision for the end of 2026

* Next week:

* DQ metrics implementation for the Data Platform Performance Dashboard

* Alerts statistics

* DQ Strategy Vision roadmap
* DBT tests and models severity testing

DG

Project “CLEAR”

* Completed:

* GCS candidate lists - review

* In progress/Next week:

* GCS files deletion
* Automation of the retention policy
* 8 EDW BQ projects - monitoring for retention & archival

Project “Data Enrichment Optimization”

* Completed
* In progress/Next week

* Updated workflow to include lead/non-paying users enrichment & adjustment on the enrichment latency period.
* Exploring collaboration options that data providers offered in light of the funding constraints:

* Infobel

* Approval from Legal & Marketing for the joint success story in exchange for free 3317 credits for a year.

* D&B

* Evaluate the possibility of using unused Google Cloud commit credits in exchange for enriched data

* CompanyEnrich

* Alignment with Growth Analytics Team on the credit usage

Project “Data Assets Certification”

* Completed:

* Meta-analysis of industry best practices

* In progress/Next week

* Alternative Certification Approach

BI

* “Tableau Cloud Migration” Project

* In progress / Next Week:

* Folder Structure & Permission Matrix
* Costing Analysis

* “Data Platform Metrics” Project

* Completed:

* Fixes and visual improvements

* In Progress / Next Week:

* Modifying sources for daily & weekly views
* Expanding BI & Data Operations metrics

* “Revenue Site in Unified Tableau” Project

* In Progress/Next Week:

* Plan

* Refactoring, Issues & Other:

* Completed:

* Enterprise Renewal Rate dashboard

* In Progress / Next Week:

* LTV/CAC dashboard
* RoR Churn Dashboard
* Redesign New/Active/Lost Users dashboard

WA

* Completed:

* Implement Anura Script (block spam traffic for affiliates)
* Review triggers and tags setup for Enterprise
* GA4 success page events / form submissions for Enterprise
* AJST event validation : new ai products and Experimentation events

* In Progress/Next Week:

* Marketing Pixels cleaning - Stakeholders alerted again (hard stop today) - deletion and pausing next week (lowering the size of semrush GTM by at least 26% probably more)
* OWOX Utilization & Necessity Review - first steps 👶
* Amplitude integration project
* [Bug]: GA4 events not published in their datasource: Solution prepared ⇒ Waiting for Makering pixels cleaning task to be completed to free up some GTM size
* GA4 testing monitoring - conversion events (sign\_up, trial…)
* Investigation on best approach for Reverse ETL to Linkedin (conversion API)

Data Integrations

* "Raw Data handover to BDP" Project

* On hold

* DataOps DP job dataparadise.osm\_data\_loader is failing. [[DDWH-2109](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2109&sa=D&source=editors&ust=1768225019508659&usg=AOvVaw2QfrGxD_Vjp3pNOf3gCqH6)]  
  The process is too resource intensive and needs to be optimized.

* Completed:

* DataOps DP Rockerbox export reconfiguration [[DDWH-2179](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2179&sa=D&source=editors&ust=1768225019509032&usg=AOvVaw2hZDesqKwgCWNKXaoSGSay)]
* DataOps DP job dataparadise.yahoo\_costs\_daily is failing. [[DDWH-2110](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2110&sa=D&source=editors&ust=1768225019509302&usg=AOvVaw2zIuVRo-kVPdItZwMDrMiF)]  
  Muted and conserved, to be replaced downstream [[DDWH-2189](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2189&sa=D&source=editors&ust=1768225019509521&usg=AOvVaw2e05gl3vE5Tdv16Q80C7TL)].

* "Raw Data handover to BDP" SalesForce Project

* Completed:

* DataOps DP SFDC: Final field Last\_Primary\_Country\_Change\_Date\_\_c have been added to target table. [[DDWH-2094](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2094?atlOrigin%3DeyJpIjoiYjM0MTA4MzUyYTYxNDVkY2IwMzVjOGQ3ZWQ3NzMwM2QiLCJwIjoianN3LWdpdGxhYlNNLWludCJ9&sa=D&source=editors&ust=1768225019510243&usg=AOvVaw2TNvyiVJgVhr-YAvsdXr14)]

* "Implementation of a PII data cleansing process" Project

* In progress:

* Got preliminary requirements. Started prototyping [[DDWH-2168](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2168&sa=D&source=editors&ust=1768225019510816&usg=AOvVaw2WWog08Td_uNzSm85VdE3T)]

* "Data Enrichment Optimization" Project

* In progress

* Re-enrichment of the rest of accounts [[DDWH-2182](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2182&sa=D&source=editors&ust=1768225019511345&usg=AOvVaw0ddnGYXLY7_7AK5dLf6KvY)]

* Reverse ETL for Intercom

* In progress:

* We’ve sent a test batch of data which was received but is not displaying in the UI. Communicating with Intercom customer support to resolve this issue. [[DDWH-2067](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2067&sa=D&source=editors&ust=1768225019512047&usg=AOvVaw3Q93y5NEXGZFxzwo5jFHL8)]

* Sources and data-marts updates / business-requests:

* Completed

* Add new fields to mart\_impact\_first\_trial\_payment (Affiliate Marketing) [[DDWH-2172](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2172&sa=D&source=editors&ust=1768225019512634&usg=AOvVaw2Yn3vkj6RCPdNtOf1A15AR)]
* Adjust billing\_subs\_addons date timezone [[DDWH-2155](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2155&sa=D&source=editors&ust=1768225019512909&usg=AOvVaw3BzaJjFWKUcLgsyUbt_cgg)]
* Clean raw\_salesforce processes [[DDWH-2119](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2119&sa=D&source=editors&ust=1768225019513170&usg=AOvVaw21gJVmtQx-42NDL03KxYjq)]
* Extend mart\_oracle\_\_mrr [[DDWH-2074](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2074&sa=D&source=editors&ust=1768225019513413&usg=AOvVaw3eNUZVwXrdLJdGiztdN0cg)]

* In progress

* PaySol data-mart for SFDC Opportunities: Implementing outbound data-mart for SFDC Reverse ETL - SFDC Opportunity Refinement (IT Division request) [[DDWH-2169](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2169&sa=D&source=editors&ust=1768225019513957&usg=AOvVaw1TwB-g_6HdZwNgZJ21ftpW)]
* Data integrations from PR toolkit trials [[DDWH-2102](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2102&sa=D&source=editors&ust=1768225019514239&usg=AOvVaw36zOQjR3RVnPBYeAT6wLsI)]
* Revise mart\_zuora\_\_product [[DDWH-2165](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2165&sa=D&source=editors&ust=1768225019514482&usg=AOvVaw2F_oRIvgyOMIF_IibXqUv0)]  
  Mart have been split into three to allow more flexible querying
* Data Subject Access Request [[DDWH-2191](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2191&sa=D&source=editors&ust=1768225019514841&usg=AOvVaw2wyv0tsQd-3WLL6goupf_H)]

DE Function (Data Operations)

* Infrastructure 2.0:

* Completed:

* Set up BigQuery dataset with Google Cloud Storage Audit Logs for all buckets in centering-land-727 project.
* Got approval for airflow 3 usage in composer (took a long time)
* Setup infrastructure repository structure
* Set up audit logs collection for google sheet integrations at centering-land-727 project
* Update metadata stats metrics collection

* Next week/In Progress:

* Start work (hopefully!) on RC environment
* Prepare list of existed google sheet integrations to review and clean up
* Requirements gathering for ETL Workflow 2.0

* DBT-wrapper

* Completed:

* Release external tables official package to allow creation of external tables as sources
* Deploy CI check for pseudo dbt models integrity (as optional step)
* Allowed to run multiple branches in local dbt environment
* Fix issue with dbt tests not copying source views properly

* Next week/In Progress:

* Migrate external materializations to the new external tables packages and deprecate external materializations

* Support improvements

* Completed:

* Included sqlfluff in duap, rup, stork30 and stork40 folders

* Next week/In Progress:

* More dbt folders added to sqlfluff
* Clear BQ datasets at start of CI run (deterministic CI builds)
* Make CI check for pseudo dbt models integrity mandatory

* Other:

* Completed:

* Fix property in google analytics events database (for API service)
* Project charters added to the Group’s confluence page.

* Next week/In Progress:

* Add requester email  to support requests BQ table

EX

Trebuchet

* Next week

* Check Frontend events are working with new version of WTE (thanks [Ondra Šubrt](mailto:ondra.subrt@semrush.com))

DataChat

* This week

* New evals added
* Helping Retention Analysis team to adopt DataChat
* Added evals to RC environment
* DataChat can tell who are the owners of the tables (thanks [Paul Kuchin](mailto:pavel.kuchin@semrush.com))

* Next week

* Scheduled analysis for people
* Share chat feature
* Smoother error handling: better message and retry button
* Context overflow handling
* More evals

## 

## Sep 12, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019522379&usg=AOvVaw0bLoDHlUrsamviKqrHkvYT)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Elementary Data POC

* No updates this week, waiting for the procurement team
* In Progress/Next week:

* Procurement Team to discuss the best price with ED and clarify our eligibility to sign the contract this year with accounting
* Preliminary approval request support and facilitation

* DBT Cloud POC

* Had a sync with the dbt cloud team reviewing the DQ capabilities
* Composed [a comparison document for Elementary Data and dbt Cloud DQ capabilities](https://www.google.com/url?q=https://docs.google.com/document/d/1XoQWA884hdncfFWrZelFJWglXGlI0fH3ynaJW_gChJo/edit?usp%3Dsharing&sa=D&source=editors&ust=1768225019524467&usg=AOvVaw3-lqx-oQnoykgYvgLma9AH) (The maturity of dbt Cloud in terms of DQ is much lower than Elementary Data but they have different aims, but dbt Cloud will definitely easy tests implementation and data observability)
* We will share with dbt Cloud DQ use cases in order to receive approaches from their perspective even if the dbt Cloud doesn’t provide some capabilities

* MRR metrics monitoring

* Completed:

* Implementation of automated tests for TARGET layer in Committed MRR lineage

* In Progress/Next week:

* Implementation of automated tests for CORE layer of the Committed MRR and Bookings

* DQ improvements

* Completed:

* Review traffic test approach with Web Analytics team
* DQ roadmap update
* DQ engineering use cases for the new infra 2.0 document
* DBT tests number and MRR test coverage metrics have been implemented and passed to BI team for adding them into the DP Performance Dashboard
* Created DBT Data Quality Issues Log to collect and track issues, to be visualized in the dashboard later

* In Progress/Next week:

* DQ metrics implementation for the Data Platform Performance Dashboard

* Alerts statistics
* Data Issues/Incidents log statistics

* DQ strategy rework into DQ vision for the end of 2026, and its strategy supported with a quarterly roadmap

DG

Project “CLEAR”

* Completed:

* Completed CLEARing of DataOps BQ projects, kudos [Ana Milasinovic](mailto:ana.milasinovic@semrush.com)
* Report is ready ([SHOW](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1dRuEhv49u4kBVBwvUI2mX4_tjQQ3TwizioHb5XjCcbI/edit?gid%3D1720422899%23gid%3D1720422899&sa=D&source=editors&ust=1768225019528730&usg=AOvVaw3sirPqU4gmjxVNG86o_Q6u))
* 27 GCS candidate lists

* In progress/Next week:

* GCS candidate lists - review
* 8 EDW BQ projects - monitoring for retention & archival
* Automation of the retention policy

Project “Data Enrichment Optimization”

* Completed

* SFDC Data Dictionary Template and document guide

* In progress/Next week

* Alignment with Sales IT and Sales Ops for the below action items:

* Inclusion of leads/non-paying customer in our unified enrichment workflow
* Latency Strategy. Current latency is 15–60 min; moving to real-time requires Sales IT and SalesOps/RevOps alignment on which use cases truly need it, acceptable staleness, and cost/architecture trade-offs.

Project “Data Assets Certification”

* Completed:

* Configurable Certification Efforts Calculator: understand what it really takes to certify

* In progress/Next week

* Prepare Certification repositioning proposition

Project “Metadata Platform”

No updates.

BI

* “Tableau Cloud Migration” Project

* In progress / Next Week:

* Folder Structure & Permission Matrix
* Costing Analysis

* “Data Platform Metrics” Project

* In Progress / Next Week:

* Fixes and improvements
* Expanding BI metrics
* Expanding DQ metrics

* “Revenue Site in Unified Tableau” Project

* In Progress/Next Week:

* Plan

* Refactoring, Issues & Other:

* Completed:

* Fix User Lists Dashboard

* In Progress / Next Week:

* LTV/CAC dashboard
* RoR Churn Dashboard
* Spotlight Event reporting
* Redesign New/Active/Lost Users dashboard

WA

* BACKLOG

* Completed:

* Experimentation platform event data validation - Just waiting for MR approval from DE

* In Progress/Next Week:

* GA4 testing monitoring - first test prepared (page\_view)
* Reverse engineering of current backend tracking functionality (Meta)
* Marketing Pixels cleaning - Stakeholders alerted again (T - 1 week)
* [Bug]: GA4 events not published in their datasource: preparing the MVP solution in GTM ⇒ locally testing MVP

* Other tasks :

* Data discrepancy for AB tests  resolved with Growth Analytics Team
* Data validation updates
* Anura (checking spam traffic from affiliates) - release next Monday

Data Integrations

* "Raw Data handover to BDP" Project

* In Progress

* ADP job dataparadise.yahoo\_costs\_daily is failing [[DDWH-2110](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2110&sa=D&source=editors&ust=1768225019537153&usg=AOvVaw076WoUrf12177Gnsu4niOs)]
* ADP job dataparadise.osm\_data\_loader is failing. It looks like the problem is in the ADP infrastructure as there is no access to the source from ADP CI/CD [[DDWH-2109](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2109&sa=D&source=editors&ust=1768225019537668&usg=AOvVaw0PzQfNp72p1COTng8-XjSM)]

* Completed

* ADP job dataparadise.dcm\_costs is failing [[DDWH-2108](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2108&sa=D&source=editors&ust=1768225019538045&usg=AOvVaw0tPZPoopL1ViF6t-0h7iE8)]

* "Raw Data handover to BDP" SalesForce Project

* In progress:

* ADP SFDC: We got access to the field Last\_Primary\_Country\_Change\_Date\_\_c and are ready to update the target table. Due to the incident with sf\_opportunity on Wednesday, we decided not to push this task [[DDWH-2094](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2094?atlOrigin%3DeyJpIjoiYjM0MTA4MzUyYTYxNDVkY2IwMzVjOGQ3ZWQ3NzMwM2QiLCJwIjoianN3LWdpdGxhYlNNLWludCJ9&sa=D&source=editors&ust=1768225019539022&usg=AOvVaw2KBgWaAmvN5vARr4j5zoxv)]

* "Implementation of a PII data cleansing process" Project

* In progress:

* Started gathering requirements and analyzing the task [[DDWH-2168](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2168&sa=D&source=editors&ust=1768225019539595&usg=AOvVaw0hWKuLkIHE9g-7WAwS_gag)]

* "Data Enrichment Optimization" Project

* Completed

* Prepared the creation of Account enriched Golden Records based on two providers: ZI and OpenAI [[DDWH-2112](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2112&sa=D&source=editors&ust=1768225019540096&usg=AOvVaw2I3eoYwaBsMNXirU0R_5_V)]

* Reverse ETL for Intercom

* In progress:

* Started gathering requirements and analyzing the task [[DDWH-2067](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2067&sa=D&source=editors&ust=1768225019540400&usg=AOvVaw0GzCnTOCoR6xQJSbR8o7j9)]

* Sources and data-marts updates / business-requests:

* Completed

* Corporate API [Incident]: The normal data export process from the source has been restored. [[DDWH-2137](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2137&sa=D&source=editors&ust=1768225019540771&usg=AOvVaw1EHDQ6Gt5CagFitZj9aD51)]
* SSoT SFDC: Email Messages. New source data-mart mart\_sfdc\_\_email\_message [[DDWH-2101](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2101&sa=D&source=editors&ust=1768225019541027&usg=AOvVaw0DKWMmPtTVZnQ-_0hKAvIu)]
* SSoT SFDC: OpportunityTeamMember. New source data-mart mart\_sfdc\_\_opportunity\_team\_member [[DDWH-2141](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2141&sa=D&source=editors&ust=1768225019541381&usg=AOvVaw3bBLN2KTwsiJCCqGkZEEu9)]
* Chorus Data: Loaded historical data since 2023 for the data mart mart\_chorus\_\_conversations [[DDWH-2139](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2139&sa=D&source=editors&ust=1768225019541621&usg=AOvVaw0pB8wy0yrjQwhOWlC7HoIB)]

* In progress

* PaySol data-mart for SFDC Opportunities: Implementing outbound data-mart for SFDC Reverse ETL - SFDC Opportunity Refinement (IT Division request) [[DDWH-2169](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2169&sa=D&source=editors&ust=1768225019541941&usg=AOvVaw0YlpYHTNgV8xmoj7s99u-R)]
* Data integrations from PR toolkit trials [[DDWH-2102](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2102&sa=D&source=editors&ust=1768225019542113&usg=AOvVaw2jKMQt5mSCXb_EV5WvQOpe)]

* New data Requests

* Revise mart\_zuora\_\_product. DParty has updated the requirements for the previously prepared data mart [[DDWH-2165](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2165&sa=D&source=editors&ust=1768225019542409&usg=AOvVaw058CBnujWRMpSmM4FseLy5)]
* Integrate data from Black Team Pub/Sub (Insight Analyst request) [[DDWH-2166](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2166&sa=D&source=editors&ust=1768225019542613&usg=AOvVaw0dpYLezTjNUeHAFA5n8BzU)]
* Integrate Airtable data (Insight Analyst request, Source from Brand experience marketing team) [[DDWH-2171](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2171&sa=D&source=editors&ust=1768225019542849&usg=AOvVaw2gDSDNdICGgYd6MiZbdqhq)]
* Integrate Limit Server data (Insight Analyst request) [[DDWH-2145](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2145&sa=D&source=editors&ust=1768225019543065&usg=AOvVaw2-nX3V9Hep5dqiB6iAAKNA)]
* Add new fields to mart\_impact\_first\_trial\_payment (Affiliate Marketing) [[DDWH-2172](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2172&sa=D&source=editors&ust=1768225019543375&usg=AOvVaw1P-MrDezCgslTJpgLlU_6b)]

* Blocked

* Extend mart\_oracle\_\_mrr: still waiting for missing required bu\_id and bu\_name fields in delivery flow from Oracle PROD [[DDWH-2074](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2074&sa=D&source=editors&ust=1768225019543782&usg=AOvVaw2JFjPnpJtpGzGsifAtgxMu)]

DE (Data Operations)

* Infrastructure 2.0:

* Completed:

* Deployed of dbt wrapper that turns analytics-division-dev project usage on

* Next week/In Progress:

* Start implementation of Airflow in RC environment
* Work on requirements gathering for project “Design the analytics ETL workflow 2.0”

* DBT

* Completed:

* Implemented a step in ci to check pseudo model integrity

* Next week/In Progress:

* Deploy step to ci to check pseudo model integrity
* Continue sqlfluff code quality improvements
* Testing dbt external package to substitute external materialization
* Removing unused marketing models
* Support "Branching" in local env

* Support improvements

* Completed:

* Added a new field to SF.Opportunity table
* Improved documentation of customdep\_replace\_refs

* Next week/In Progress:

EX

* Trebuchet

* Setting up backend tests
* Fix docs thanks [Paul Kuchin](mailto:pavel.kuchin@semrush.com)
* Helping POs and Analysts with their experiments and metrics

* Datachat

* Python interpreter tool
* Memory
* Roadmaps, discussions, prioritizations

Notes:

* Performance Review Cycle – starting soon (to cover everybody “older” than Apr 1, 2025)
* Ryan team – some of Analysts mover there, so now we have “two Danils + Nikita”
* Budget 2026 – prop prepared / to be discussed b/w Sam and CFO ~next week
* OWOX – would be good to optimize it if possible

## Sep 5, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019547096&usg=AOvVaw26ghyIgKqmgSEruOiaD7D3)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Elementary Data POC

* Completed

* Sync with ED Sales team and our procurement team with process clarification
* Pricing options were discussed internally and confirmed, and shared with the procurement team (detailed roles assignment across Analytics Division, several adoption scenarios were composed)
* ED Business Case has been prepared in addition to pricing options with scenarios description

* In Progress/Next week:

* Procurement Team to discuss the best price with ED and clarify our eligibility to sign the contract this year
* Preliminary approval request support and facilitation

* Executive Scorecards dashboard

* Completed:

* Adding tests for Google Sheets sources

* MRR metrics monitoring

* In Progress:

* Implementation of automated tests for target and core layers in Committed MRR lineage

* DQ improvements

* Completed:

* DQ strategy first version has been shared and discussed internally

* Next week:

* DQ metrics implementation for the Data Platform Performance Dashboard
* DQ strategy rework into DQ vision for the end of 2026, and its strategy supported with a quarterly roadmap

DG

Project “CLEAR”

* Completed:

* Archived:  analytics-internal-prod-tf, analytics-projects-prod-tf

* In progress/Next week:

* CLEAR GCS files: retention criteria and candidate lists – lightweight approach
* Pending few tables for the archival: analytics-external-prod-tf
* 8 EDW projects for review by BDP

Project “Data Enrichment Optimization”

* Completed

* Formal project presentation to stakeholders.

* In progress/Next week

* Continue alignment and coordination with Business IT for the interconnected efforts between L2R (Lead to Renew program) and data enrichment.
* D&B and Infobel pricing negotiations with the procurement team. Arranging POC with CompanyEnrich.

Project “Data Assets Certification”

* In progress/Next week

* Prepare configurable estimates of the certification efforts: framework and pilot

Project “Metadata Platform”

No updates.

Other

* Completed

* Data Governance Strategy & Roadmap; Presentation scheduled for Today

BI

* Refactoring, Issues & Other

* Completed:

* Spotlight event reporting (add GA4 data)

* In Progress:

* LTV/CAC dashboard

* “Tableau Cloud Migration” Project

* In progress:

* Folder Structure & Permission Matrix

WA

* BACKLOG

* Completed:

* Meta - Trial Event Merging FE and BE: mapped the pixel data, under investigation for the conversion api data and possible modification of tables in sight. ⇒ solution implemented, no errors flagged
* Retargeting: Create upsell and convert audiences in GA4: splitted it in 2 tickets: one is finished, one is closed and will be recreated as a project

* In Progress/Next Week:

* Marketing Pixels cleaning : file shared with marketing teams, still 2 weeks left for their feedback on what can be deleted.
* [Bug]: GA4 events not published in their datasource: preparing the MVP solution in GTM ⇒ locally testing MVP
* Experimentation platform event data validation

* ADHOC

* Completed

* Enterprise pixel implementation and discussions
* Other tasks :

* Data validation updates
* Spotlight conference tagging and tracking
* GA4 testing monitoring

BDP

* "Raw Data handover to BDP" Project

* In progress:

* ADP job dataparadise.osm\_data\_loader is failing [[DDWH-2109](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2109&sa=D&source=editors&ust=1768225019554921&usg=AOvVaw2VL_w6YpRdzk6HriTtagVk)]
* ADP job dataparadise.yahoo\_costs\_daily is failing [[DDWH-2110](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2110&sa=D&source=editors&ust=1768225019555111&usg=AOvVaw2I6dndoPijzd3Mgh54eHch)]
* ADP job dataparadise.dcm\_costs is failing [[DDWH-2108](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2108&sa=D&source=editors&ust=1768225019555271&usg=AOvVaw1BKmzx9L_AdNBL6eN7YAH9)]

* Completed

* ADP job dataparadise.slack is failing [[DDWH-2095](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2095&sa=D&source=editors&ust=1768225019555480&usg=AOvVaw1Uhs2vvLP69sSnxpGahzSK)]
* Analysed duplicated App Center source extraction. Only one table in ADP requires migration. [[DDWH-2029](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2029&sa=D&source=editors&ust=1768225019555683&usg=AOvVaw12nAzm8nnTsYpJHzQ9Sp6e)]

* "Raw Data handover to BDP" SalesForce Project

* In progress:

* ADP SFDC: New fields for SF entities Account and Contact. 2 out of 3 fields have been added, but we are waiting for Sales IT to grant access to export for one field. [[DDWH-2094](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2094?atlOrigin%3DeyJpIjoiYjM0MTA4MzUyYTYxNDVkY2IwMzVjOGQ3ZWQ3NzMwM2QiLCJwIjoianN3LWdpdGxhYlNNLWludCJ9&sa=D&source=editors&ust=1768225019556180&usg=AOvVaw2rrraNcAp4ipjEmpQh2QC1)]

* "Data Enrichment Optimization" Project

* Completed

* We presented our solution to stakeholders. And it seems that a request for real-time enrichment has appeared.

* In progress

* Design & implementation re-enrichment process

* "Adapting of multi-currency in Payment Solution" Project

* Completed

* Prepared changes to our financial reporting process for FP&A

* “Evaluation of Metadata Tools” Project

* In progress

* OpenMetadata ([https://openmetadata.rc-k2.semrush.net/\*\*](https://www.google.com/url?q=https://openmetadata.rc-k2.semrush.net/**&sa=D&source=editors&ust=1768225019557322&usg=AOvVaw1icOJp--PSRX6o__flY9uH)): We continue testing
* DataHub ([https://datahub.rc-k2.semrush.net/\*\*](https://www.google.com/url?q=https://datahub.rc-k2.semrush.net/**&sa=D&source=editors&ust=1768225019557495&usg=AOvVaw1d1vK6ZUvgAb5_JDep-GEg)):\*\* Configured BDP data ingest. Next ADP.

* Reverse ETL for Intercom

* On Hold:

* Still on hold. But a new stakeholder has been found.

* CLEAR Project result Review

* In progress

* ~80% completed. Remaining tables for review have been distributed between engineers

* Sources and data-marts updates:

* Completed

* Non GAAP metrics (Acquired companies sources): Add extra validations for the startDate and endDate for API Resellers
* Winback Campaign Data (for Marketo): The source that had been decommissioned was preserved.
* Data marts update schedule change to 1:00 AM:

* mart\_dict\_public\_\_free\_domains

* In progress:

* Corporate API [Incident]: The load was temporarily suspended to resolve issues with the load on the source.
* Chorus Data: We have received a request for reverse filling to provide all available data from this source.
* Data marts update schedule change ([ADP requirements](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1eloTWnZe0TX1QyrobQfJEQGiCQoZwST_rEtdIcejglI/edit?gid%3D0%23gid%3D0&sa=D&source=editors&ust=1768225019559135&usg=AOvVaw0UomfzGFxoaD2h4iq54SmQ)):

* mart\_data\_enrichment\_account\_location\_zoominfo
* mart\_marketo\_\_\*

* New data Requests:

* Data integrations from PR toolkit trials [[DDWH-2102](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2102&sa=D&source=editors&ust=1768225019559498&usg=AOvVaw1uFqeXsfjI8t3yM_O-mEmG)]
* Data Enrichment for Marketo [[DDWH-2127](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2127&sa=D&source=editors&ust=1768225019559640&usg=AOvVaw3b5_d55mmc75D4VgMrOHtf)]
* SSoT SFDC: Email Messages [[DDWH-2101](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2101&sa=D&source=editors&ust=1768225019559803&usg=AOvVaw21kOg6AjlOmXIsrn7B5XQX)]
* SSoT SFDC: OpportunityTeamMember [[DDWH-2141](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2141&sa=D&source=editors&ust=1768225019560009&usg=AOvVaw375N3tyEeZWBtCwHnHhAky)]

* On Hold

* Extend Oracle mart: mart\_oracle\_\_mrr due to missing required fields in Oracle on PROD.

DE

* Infrastructure 2.0:

* Completed:

* Development and testing of dbt wrapper that will turn analytics-division-dev usage on

* Next week/In Progress:

* Deployment of dbt wrapper that will turn analytics-division-dev usage on

* Infrastructure improvements / Tech debt

* Completed:

* Fixed multiple issues with docker timing out (this will reduce the number of retries for tasks)
* Fixed an issue where sometimes the sync with google components failed silently

* Next week/In Progress:

* Improve code quality by adding sqlfluff checks to analytics-projects-prod-tf
* Start building RC environment
* Researching new IaC repository structure
* Check with kind team using k8s for jobs instead of google batch
* Start requirements for realistic POC for SDLC lifecycle 2.0

* Support improvements

* Completed:

* Added requestor field support ticket table to associated jira ticket.
* Updated fire reaction in AnalyticsDivisionBot to avoid an error message appearing for non-DE users.

* Next Week/In progress:



EX

Trebuchet

* This week

* Setting up AB tests Backend and Frontend
* Reviewing all the docs from all Semrush dev. Teams
* New event tracking with analytics js tool (thanks to [Ondra Šubrt](mailto:ondra.subrt@semrush.com))

* Next week

* Test new experiments tracking tool
* Prepare to deploy in to prod

DataChat

* This week

* token prices on the evals
* scroll down button
* context compaction
* tracing tool calls
* [Table](https://www.google.com/url?q=http://data-chat-prod-tf.analytics.daily_usage&sa=D&source=editors&ust=1768225019563709&usg=AOvVaw0-67kIhrm-yO8vph3yTNuq) with daily metric
* [docs](https://www.google.com/url?q=https://gitlab.semrush.net/analytics-team/datachat/-/tree/master/docs?ref_type%3Dheads&sa=D&source=editors&ust=1768225019563873&usg=AOvVaw1d3rDHXKKDbLTpPDwBbXMQ)/ with roadmaps, diagrams, strategy, todos, …

* Next week

* Adding evals
* API, Scheduled analysis

Notes:

* “Distributed Offsite” – Sam would like to do it in the 1st half of Dec
* Invite you to check the recent Bill’s Coffe Talks – abt recent org changes & plans (see #analytics-internal)
* Asking you to pass the AI training (see #analytics-data-platform)

## Aug 29, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019564788&usg=AOvVaw0gKPX2E4tJHRQvc1EyXGM9)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Elementary Data POC

* Completed

* Procurement team sync (we will provide required ED features, ED team will prepare an offer for different options, procurement team assists negotiations and NDA)
* BDP Data scope for the POC has been defined (next steps will be only after the CFO decision)

* In Progress/Next week:

* ED team sync regarding available options and flexibility of features
* Prepare and justify required Elementary Data features (Business Case)

* MRR metrics monitoring

* Completed:

* Committed MRR test coverage discussed and aligned with DPARTY team

* In Progress/Next week:

* Starting implementation of automated tests for target and core layers in Committed MRR lineage (DPARTY will create business checks and some basic checks with our support)

* GA4 streaming events data health

* Completed:

* Improved logic of thresholds calculation for GA4 data events monitoring tests

* DQ improvements

* Next week:

* DQ vision preparation (adapt current board with the ideal DQ image)
* Alerts criticality investigation (we have received critical alerts for not critical tests but related to critical models)

DG  
  
Project “CLEAR”

* Completed:

* Candidate lists that are done with review: analytics-projects-prod-tf
* Archived: analytics-tableau-prod-tf, analytics-tests-prod-tf, trebuchet-rc-tf, trebuchet-prod-tf

* In progress/Next week:

* Candidate list for review by BDP: enterprise-dwh-prod-tf, enterprise-dwh-rc-tf, enterprise-dwh-raw-prod-tf, enterprise-dwh-raw-rc-tf, enterprise-dwh-ftran-prod, enterprise-dwh-ftran-rc-tf, enterprise-dwh-airbyte-prod-tf
* To Be Archived: analytics-internal-prod-tf, analytics-external-prod-tf, analytics-projects-prod-tf
* CLEAR GCS files: retention criteria and candidate lists

Project “Data Enrichment Optimization”

* In progress/Next week

* D&B and Infobel business case analysis doc has been prepared and discussion about the pricing is ongoing.
* Alignment with Business IT between L2O and data enrichment projects.
* Presentation to stakeholders of the unified enrichment workflow.

Project “Data Assets Certification”

* In progress/Next week

* Refine Framework and Pilot plan according to Sam’s feedback

Project “Metadata Platform”

No updates.

Other

* In progress/Next week

* Refine Data Governance Strategy, Roadmap & Presentation

BI

* “C-level Scorecards” Project

* Completed

* Sent Email to stakeholders

* “Tableau Cloud Migration” Project

* No updates

* Refactoring, Issues & Other

* Completed:

* Fix daily report subscription
* Enterprise Renewals Rate dashboard
* Redesign new/active/lost dashboard

* In testing:

* CMO dashboard (WBR)

* In Progress:

* Spotlight event reporting (add GA4 data)

WA

* BACKLOG

* Completed:

* Search Engine Land and Backlinko remarketing and conversion pixels for CTAs : pixels are published - waiting for confirmation form stakeholders
* Cross-Domain Conversion Tracking - waiting for confirmation form stakeholders

* In Progress/Next Week:

* Meta - Trial Event Merging FE and BE: mapped the pixel data, under investigation for the conversion api data and possible modification of tables in sight. ⇒ final changes in process
* Retargeting: Create upsell and convert audiences in GA4
* Marketing Pixels cleaning : file shared with marketing teams, given them 2 weeks for their feedback on what can be deleted.
* [Bug]: GA4 events not published in their datasource: preparing the MVP solution in GTM

* ADHOC

* Completed

* Dbt local set up
* Other tasks :

* Implement web tracking in [ai-visibility-index.semrush.com](https://www.google.com/url?q=http://ai-visibility-index.semrush.com&sa=D&source=editors&ust=1768225019572441&usg=AOvVaw2gXKUcsoluhtLuBdUP1Kyf) + event validation
* Implement pixel in [https://www.semrush.com/lp/enterprise-aio-a/en/](https://www.google.com/url?q=https://www.semrush.com/lp/enterprise-aio-a/en/&sa=D&source=editors&ust=1768225019572669&usg=AOvVaw05AhNOt9clKm660f9m_H9z)
* Fix Cookiehub issue in Datos
* Brainstorm with DM team about the best remarketing set up ⇒ topics: consent, cookies, data available

BDP

* "Raw Data handover to BDP" Project

* In progress:

* ADP SFDC: New fields for SF entities Account and Contact [[DDWH-2094](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2094?atlOrigin%3DeyJpIjoiYjM0MTA4MzUyYTYxNDVkY2IwMzVjOGQ3ZWQ3NzMwM2QiLCJwIjoianN3LWdpdGxhYlNNLWludCJ9&sa=D&source=editors&ust=1768225019573370&usg=AOvVaw1u_7LQG2GP926bvqptpGFF)]
* ADP job dataparadise.slack is failing [[DDWH-2095](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2095&sa=D&source=editors&ust=1768225019573529&usg=AOvVaw354sD46ph9CzBsG7mx1nrY)]
* Analyse and deprecate duplicated App Center source extraction [[DDWH-2029](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2029&sa=D&source=editors&ust=1768225019573732&usg=AOvVaw3H_KUiuXWKbS6vkMz7P9n9),[DDWH-2031](https://www.google.com/url?q=https://jira.semrush.net/browse/DDWH-2031&sa=D&source=editors&ust=1768225019573894&usg=AOvVaw1jn8A8S7j13PTnt44IPK0Q)]

* "Data Enrichment Optimization" Project

* In progress

* Design & implementation re-enrichment process

* “Evaluation of Metadata Tools” Project

* In progress

* OpenMetadata ([https://openmetadata.rc-k2.semrush.net/](https://www.google.com/url?q=https://openmetadata.rc-k2.semrush.net/**&sa=D&source=editors&ust=1768225019574507&usg=AOvVaw1oggWjDw9TUaKY8uXAaTcq)): We continue testing
* DataHub ([https://datahub.rc-k2.semrush.net/](https://www.google.com/url?q=https://datahub.rc-k2.semrush.net/**&sa=D&source=editors&ust=1768225019574699&usg=AOvVaw2eAL3q_CcXsWG9Bmx5Cs54)): we’ve started configuring metadata ingestion

* "Adapting of multi-currency in Payment Solution" Project

* In progress:

* Adapting multi-currency for financial ARR report (aka FinDWH)

* SSoT SFDC

* Completed

* Helping the MarTech team migrate to the SFDC SSoT. Outdated process of loading Salesforce data via Fivetran has been disabled (Savings ~$1K per month)

* Reverse ETL for Intercom

* On Hold:

* We lost the main stakeholder because he is no longer with the company

* Sources and data-marts updates:

* Completed

* SSoT SFDC: new Opportunity.CurrencyIsoCode field
* SSoT SFDC: new Opportunity.Sales\_Engineer\_Notes\_c field

* In progress / Next week

* Oracle Report data integration (Prowly's CAC)
* Data marts update schedule change ([ADP requirements](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1eloTWnZe0TX1QyrobQfJEQGiCQoZwST_rEtdIcejglI/edit?gid%3D0%23gid%3D0&sa=D&source=editors&ust=1768225019576361&usg=AOvVaw3f5f0WjJf0auQCNq_6TDTN)):

* mart\_data\_enrichment\_account\_location\_zoominfo
* mart\_dict\_public\_\_free\_domains
* mart\_marketo\_\_\*

* On Hold

* Extend Oracle mart: mart\_oracle\_\_mrr due to missing required fields in Oracle on PROD.

DE

* Infrastructure 2.0:

* Completed:

* Under the hood preparation to run DBT on new dev environment
* Creation of code to maintain the new dev environment and access

* Next week/In Progress:

* Begin deployment of Staging environment
* Final testing of dbt dev environment updates

* Infrastructure improvements / Tech debt

* Completed:

* Make install now update your gcloud version (Old one presented some failures)
* Updated dbt workers and added some magical settings to hopefully avoid dbt worker dying
* Excluded rule CV02 in sqlfluff, which replaces ifnull by coalesce
* Included macro incrementsl\_date in sqlfluff
* Applied sqlfluff to data-paradise-20/marketing folder
* Created a new version of bq-helper to support python >= 3.12

* Next week/In Progress:

* Continue researching how we can fix the issue with dbt worker sometimes losing connection
* Make all models in analytics-projects-prod-tf to be linted by sqlfluff

* Support improvements

* Completed:



* Next Week/In progress:

* Improve slack-bot:

* Add requestor field support ticket table to associated jira ticket.
* Update fire reaction in AnalyticsDivisionBot.

* Other:

* Completed

EX

Trebuchet

* Copy metrics in trebuchet, .md descriptions
* Docs for developers for trebuchet
* DatePicker bug

DataChat

* New evals
* Tokens counting, cost control
* Peek into users requests

## Aug 22, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019579940&usg=AOvVaw2dN0xBK0gNOeUjfDhO4zb0)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Elementary Data POC

* Completed

* POC tracker template and general plan has been received and discussed with ED team
* Software request has been submitted for approvals

* In Progress/Next week:

* POC Project Charter (use cases, POC tracker enrichment)
* POC & POV data scope definition
* Tasks decomposition and planning

* MRR metrics monitoring

* In progress/Next week:

* Committed MRR & New holding\_mrr\_monthly test coverage together with DPARTY team

* GA4 streaming events data health

* In Progress/Next week:

* Tune and improve thresholds for GA4 data events monitoring tests

* DQ improvements

* Completed:

* Take DE tests ownership
* DQ current state description document
* MRR and SLA models and tests have been enhanced with additional severity metadata to improve visibility of critical and major alerts

* Next week:

* DQ vision preparation (adapt current board with the ideal DQ image)

DG

Project “CLEAR”



Project “Data Enrichment Optimization”

* Completed

* Established CoE (set-up CoE structure & roles & responsibilities)

* In progress/Next week

* Business case analysis for supplementary enrichment data providers.
* Alignment with Business IT between L2O and data enrichment projects.
* Presentation to stakeholders of the unified enrichment workflow.

Project “Data Assets Certification”

No updates.

Project “Metadata Platform”

No updates.

BI

* “C-level Scorecards” Project

* In Progress:

* Handling issue with data delay for Exploding Topics, Brand24, SplitSignal, Exploding Topics, Insights24, Datos

* “Data Platform Metrics” Project

* Completed

* Dashboard redesigned

* “Tableau Cloud Migration” Project

* Completed:

* Run Migration Readiness Assessment

* In Progress

* POV Testing plan

* Refactoring, Issues & Other

* In Progress:

* Spotlight event reporting (add GA4 data)
* Enterprise Renewals Rate dashboard
* Redesign new/active/lost dashboard

  ---

WA

* BACKLOG

* Completed:

* Daily table of users with no frontend events
* DV360 Migration to gtag & Enhanced Conversions Setup
* Investigate and implement CMP event tracking in GTM
* [Bug]: GA4 events not published in their datasource: Looking for the right place to apply the change.

* In Progress/Next Week:

* Cross-Domain Conversion Tracking (Problem with redirects reported to requestor)
* Search Engine Land and Backlinko remarketing and conversion pixels for CTAs (Confirming details with requestor)
* [Bug]: GA4 events not published in their datasource: Waiting for Violeta’s opinion, prepare the MVP solution in GTM
* Meta - Trial Event Merging FE and BE: mapped the pixel data, under investigation for the conversion api data and possible modification of tables in sight.

* ADHOC

* Completed

* Implement events for Sponsors of Spotlight campaigns
* Send data to OWOX from BE (Prowly team/ Marat)

* In Progress/Next Week:

* Check the implementation of the CookieHub trigger in the SEL - DONE - still waiting for the feedback, got message from CookieHub
* [Bug]: GA4 events not published in their datasource: Looking for the right place to apply the change.
* Audit and Deprecation of Unused GTM Events (Billing Upgrade and Billing Payment): under investigation, billing payment and upgrade are used as triggers for paid marketing purposes. - Moved back to backlog - reopen after Marketing Pixels cleanup

* NEW

* In Progress/Next Week

* Marketing Pixels cleaning (announced automation, prepared, waiting for access FO SA to Datos)
* Marketing Efforts accuracy (Brainstorms with teams we are supporting)

BDP

* "Raw Data handover to BDP" Project

* Completed

* MaxMind DB Source: new credentials have been obtained and replaced. The pipeline can only be tested in Prod on Monday. At the same time, we are analyzing the feasibility of migrating this process to the BDP platform.
* CRM Source: the integration has been archived

* SSoT SFDC

* In progress

* Helping the MarTech team migrate to the SFDC SSoT. The work on our side has been completed. After the final checks by the MarTech team next week, we will disable the old Salesforce data ingestion process in Fivetran.

* Savings: ~$1K per month.

* “Evaluation of Metadata Tools” Project:

* In progress

* OpenMetadata: We continue testing OpenMetadata. The version has been upgraded to 1.9, bringing a slightly updated UI and new data contract management features.
* DataHub: we finally received approval from the Security Team to use DataHub in our infrastructure, and the SysOps Team has started the installation of the tool.

* Implement Reverse ETL for Intercom with user data

* In progress

* ​​Requirements gathering and design

* Sources and data-marts updates:

* Completed

* GKT Team data (metrics from search\_volume, organic\_traffic, backlinks)

* enterprise-dwh-prod-tf.mart\_backlinks.\* (6 tables)
* enterprise-dwh-prod-tf.mart\_search\_volume.\* (7 tables)
* enterprise-dwh-prod-tf.mart\_organic\_traffic.\* (3 tables)

* Swoogo: new field from source mart\_swoogo\_\_transaction.registrant\_id

* In progress / Next week

* Oracle Report data integration (Prowly's CAC):

* The report has been prepared by the Fin IT team.
* Next steps — the Business Integration team should prepare an export from Oracle for us. In turn, we will prepare the data mart.

DE

* Infrastructure 2.0:

* Completed:

* Set up accounts and permissions for new dev and rc projects
* Deprecate analytics-data-prod

* Next week/In Progress:

* Implement change to dbt-wrapper to run on analytics-division-dev
* Create code to maintain the analytics-division-dev env

* Infrastructure improvements / Tech debt

* Completed:



* Next week/In Progress:



* Support improvements

* Completed:

* Granted permissions for data governance team to be able to archive data in several projects
* Enable Severity aware alert notifications for dbt tests

* Next Week/In progress:



* Other:

* Completed



EX

* Project “Trebuchet - Experimentation”

* Completed

* Screenshots order

* In progress / Next week

* GraphQL requests are hard task for the AI
* Docs for owox endpoint custom events tracking in trebuchet

* Project “DataChat”

* Done

* Redesigned prompt expansion
* New visual next steps
* Evals

* In progress / Next week

* Dashboards integration
* Evals
* Bugs

## Aug 14, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019593918&usg=AOvVaw28uW4lrlCYcx4wS2E256H3)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Elementary Data POC

* Next week:

* POC Project Charter (use cases, POC tracker)

* MRR metrics monitoring

* Completed:

* Sync with Dparty team to discuss further steps related to C-level data support

* In progress/Next week:

* Tuning created sensitive tests for holding MRR daily
* Committed MRR test coverage
* New holding\_mrr\_monthly model test coverage

* Executive Scorecards dashboard

* In Progress:

* Basic DBT tests implementation

* GA4 streaming events data health

* In Progress/Next week:

* Tune and improve thresholds for GA4 data events monitoring tests

* DQ improvements

* In progress/Next week:

* Take DE tests ownership

DG

Project “CLEAR”

* Completed:

* Candidate lists that are under review: Analytics-external, Analytics-tableau-prod, analytics-internal-prod-tf, enterprise-dwh-raw-prod, enterprise-dwh-raw-rc, analytics-projects-prod-tf, analytics-tests-prod-tf,

* In progress/Next week:

* Drafting candidate lists for enterprise-dwh-prod
* Archive/Deletion: data-paradise-20
* Archival and Retention Policy - Draft version

Project “Data Assets Certification”

No updates.

Project “Data Enrichment Optimization”

* Completed
* In progress/Next week

* Center of Excellence Structure, Roles & Responsibilities, and Governance model for decision making and escalations - Under Review
* Infobel POC -Additional review on the POC results is needed. And Business Case analysis will be prepared.
* Business Case Analysis for D&B - In progress.
* CompanyEnrich - under coordination with procurement team for the NDA.

Project “Metadata Platform”

No updates.

BI

* “C-level Scorecards” Project

* In Progress:

* Handling issue with data delay for Exploding Topics, Brand24, SplitSignal, Exploding Topics, Insights24, Datos

* “Data Platform Metrics” Project

* Completed - Additional BI Metrics

* “Tableau Cloud Migration” Project

* In Progress - POV Testing plan

* Refactoring, Issues & Other

* Completed:

* Advanced Emailing (Workshop) - testing & template creation

* In Progress:

* Spotlight event reporting (+ Swoogo)
* Paid Toolkits Activity - enhancements

WA

* Completed:

* Data validation error - CD error is fixed and changes deployed to prod
* Retargeting: Implement a ToolKit u-variable in GTM
* Some GTMs approval
* Meeting with stakeholders (gathering requirements)

* Cross-Domain Conversion Tracking
* Search Engine Land and Backlinko remarketing

---

* In Progress/Next Week:

* Check the implementation of the CookieHub trigger in the SEL - DONE - waiting for feedback
* Daily table of users with no frontend events : query logic validated, preparing the table with daily BE only users
* [Bug]: GA4 events not published in their datasource: Looking for the right place to apply the change.
* DV360 Migration to gtag & Enhanced Conversions Setup - will close this/next week (Waiting for Change on DM side)
* Intake process - discussion about merging support channels into one, tested a taskBot and workflows in slack - will continue after backlog is handled
* Audit and Deprecation of Unused GTM Events (Billing Upgrade and Billing Payment): under investigation, billing payment and upgrade are used as triggers for paid marketing purposes. - Moved back to backlog - reopen after Marketing Pixels cleanup

BDP

* "Raw Data handover to BDP" Project

* In progress

* MaxMind DB Source: still waiting for new credentials
* CRM Source: Decommissioning

* SSoT SFDC

* In progress

* We are helping the MarTech team migrate to the SFDC SSoT in processes related to Marketo.

* "Data Enrichment Optimizations" Project. PoC

* Completed

* We added the ability to obtain enriched data via OpenAI to our PoC.

* In progress

* Present the proposed approach to stakeholders (demo) and continue onboarding more providers into the enrichment cascade.

* “Evaluation of Metadata Tools” Project:

* In progress

* We continue to test OpenMetadata. Unfortunately, we were unable to prepare the DataHub instance this week, so it has been postponed until next week.

* Sources and data-marts updates:

* Completed

* Extended SSoT SFDC:

* Contract -> mart\_sfdc.mart\_sfdc\_\_contract
* Product2 -> mart\_sfdc.mart\_sfdc\_\_product\_2

* Enterprise Solutions data

* mart\_entsol.mart\_entsol\_\_product\_analytics\_static\_data\_customers
* mart\_entsol.mart\_entsol\_\_semrush\_static\_data\_workspace\_limits
* mart\_entsol.mart\_entsol\_\_semrush\_static\_data\_workspace\_stats
* mart\_entsol.mart\_entsol\_\_semrush\_static\_data\_workspaces

* In progress / Next week

* GKT Team data (metrics from search\_volume, organic\_traffic, backlinks)
* Oracle Report data integration (Prowly's CAC): Fin IT has returned to preparing the report in Oracle. We will integrate the report once they have finished.

DE

* Infrastructure improvements / Tech debt

* Completed:

* Connected data-paradise-20 with semrush-analytics-data-prod-us-east4(postgres) to run federated queries
* Created new GCP projects for infrastructure 2.0

* Next week/In Progress:

* Exploring switching Gitlab runners from VMs to instance groups.
* Begin work to migrate local dbt development to analytics-division-dev GCP project’
* Begin work to set up staging environment

* Support improvements

* Completed:

* Git hooks updated to allow comments mentioning internal database
* Fixed dbt custom\_dev\_run\_list command to allow copying views to local environment
* Solved bug with scd materialization to allow alter table parameter

* Next Week/In progress:

* Enable Severity aware alert notifications for dbt tests
* Fix “table\_copy” materialization to allow copying test table instead of production table to cicd dataset.

* Other:

* Completed

* New How-to: [How to mark files for full refresh](https://www.google.com/url?q=https://kb.semrush.net/display/ATI/How-to%253A%2BMark%2Bmodels%2Bto%2Bfull%2Brefresh%2Bautomatically&sa=D&source=editors&ust=1768225019606079&usg=AOvVaw0j2O2W9EJ-kHfTQJWW4stM)

EX

* Project “Trebuchet - Experimentation”

* Completed

* Rewritten AI prompts, updated AI analysis

* In progress / Next week

* Integration of backend tests: gathering information, planning, discussing
* Announce AI analysis updates, datachat-trebuchet integration

* Project “DataChat”

* Done

* UI for editing table access levels

* In progress / Next week

* Bug with limited number of tool calls
* Checking out various EVAL tools
* Tableau integration
* Prompts improvements based on the users requests

## Aug 8, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019608431&usg=AOvVaw0tsw-5bS3rvRk6JwNbGY9V)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Monte Carlo

        Project Charter is ready for review. Waiting for the contract decision to define next steps.

* Elementary Data

* Next week:

* Prepare MC and ED compatibility justifications or just POC justifications (depends on the management decision and budgeting).

* MRR metrics monitoring

* Completed:

* Box plot tests for MRR, users and customers number by limits and units
* MRR crucial tests metadata has been updated to notify Dparty team leadership

* Next week:

* Sync with Dparty team to discuss further steps related to C-level data support

* Executive Scorecards dashboard

* Next week:

* Basic DBT tests implementation
* Box plot tests

* GA4 streaming events data health

* Completed:

* Box plot tests for events number as a part of GA4 data monitoring

* Next week:

* Tune and improve thresholds for GA4 data events monitoring tests

* Dormant\_users\_monthly model test coverage

* Completed:

* DQ checks have been implemented for the dormant\_users\_monthly model

* DQ improvements

* In progress/Next week:

* DQ Framework description (to add clarity and transparency)

DG

Project “CLEAR”

* Completed:

* Candidate lists that is under review: Analytics-external, Analytics-tableau-prod, enterprise-dwh-raw-prod, enterprise-dwh-raw-rc, semrush-com , analytics-projects-prod-tf
* Archive/Deletion - analytics-datamart-prod-tf

* In progress/Next week:

* Drafting candidate lists for analytics-tests-prod-tf, enterprise-dwh-prod
* Archive/Deletion: data-paradise-20
* Ready for the review (will be shared soon): analytics-internal-prod-tf

Project “Data Assets Certification”

Project “Data Enrichment Optimization”

* Completed

* Revised Project Charter

* In progress/Next week

* Infobel POC - Results under review
* Business Case Analysis for D&B - to update ROI computation
* CompanyEnrich - to start exploration stage

Project “Metadata Platform”

* In progress/Next week

* Metadata Req’s from Data Governance

BI

* “C-level Scorecards” Project

* Completed:

* Enterprise Gross MRR Renewal %
* Visual changes to better align with company branding

* In Progress:

* Handling issue with data delay for Exploding Topics, Brand24, SplitSignal, Exploding Topics, Insights24, Datos

* “Data Platform Metrics” Project

* In Progress - Additional BI Metrics

* “Tableau Cloud Migration” Project

* In Progress - POV Testing plan

* Refactoring, Issues & Other

* Completed:

* Salvage Offers - data fix
* New MRR Impact - enhancements
* Upgrade PLG per Users

* In Progress:

* Advanced Emailing (Workshop) - testing & template creation
* CMO Dashboard refactoring (WBR view)
* Spotlight event reporting (+ Swoogo)
* Paid Toolkits Activity - enhancements

WA

* Completed:

* QA Meta Tracking – Pixel + API - issue identified,solution presented and deployed - ticket closed
* Datos Live configuration with CookieHub - changes deployed, ticket closed.
* Mouseflow issue (CI Toolkit team) - during investigation found out it is already fixed =o)

* In Progress/Next Week:

* Daily table of users with no frontend events : first results presented, waiting for feedback
* Audit and Deprecation of Unused GTM Events (Billing Upgrade and Billing Payment): under investigation, billing payment and upgrade are used as triggers for paid marketing purposes. Tbd if we can delete them.
* Data validation :

* Fix CD error - Approver review pending
* add tracking\_wizard as new semrush\_product\_name - then we can close this one

* [Bug]: GA4 events not published in their datasource - suggested two possible solutions,  waiting for help from ajst dev
* DV360 Migration to gtag & Enhanced Conversions Setup - performing a test with DM before we make permanent changes
* Intake process - discussion about merging support channels into one, tested a taskBot and workflows in slack

BDP

* "Raw Data handover to BDP" Project

* In progress / Next week

* MaxMind DB Source: The pipeline is broken due to a blocked account. We’re currently working on resolving the issue together with the Slide Team.
* Merge old data from Facebook Ads, LinkedIn Ads with the new Fivetran provided data: As part of this task, we developed a unified approach for managing archived and static data. We’re planning to test this approach in the context of this project.
* We’re continuing to collect information about the data sources and how the ingested data is being used.

* "Data Enrichment Optimizations" Project. PoC

* Completed

* We’ve completed the main work on the PoC.

* In progress / Next week

* Demo for stakeholders and get approval to proceed with further development.

* “Evaluation of Metadata Tools” Project:

* OpenMetadata

* We’ve set up a test instance, and we’re now actively testing its capabilities ([https://openmetadata.rc-k2.semrush.net/](https://www.google.com/url?q=https://openmetadata.rc-k2.semrush.net/&sa=D&source=editors&ust=1768225019626452&usg=AOvVaw2BeRoKEJUq5BK3xtOxI89O)).

* DataHub

* Infrastructure setup is in progress.

* Sources and data-marts updates:

* Completed

* Swoogo API data (15 8 data-marts)
* Marketo Activity Trials data-mart: mart\_marketo\_\_activities\_addto\_trial\_subscription\_v2
* Extended SSoT SFDC: mart\_sfdc\_\_account

* In progress / Next week

* GKT Team data (metrics from search\_volume, organic\_traffic, backlinks)
* Enterprise Solutions data
* Extended SSoT SFDC: Add new “Contract” entity

DE

* Infrastructure improvements / Tech debt

* Completed:

* New command to help analysts to full refresh model and downstreams
* Introduced a new parameter `skip\_ci\_test` allowing selective exclusion of specific tests execution in the `run\_tests\_on changed\_models` cicd step.
* “Folders” data update by production dump

* Next week/In Progress:

* Exploring switching Gitlab runners from VMs to instance groups.
* Starting new local development environment setup
* Updating gitlab airflow-read-api token that is about to expire

* Support improvements

* Completed:

* Access for Bigquery restricted operations (dangerous operations that can be run by leads)
* Git hooks updated to allow comments mentioning internal database

* Next Week/In progress:



* Other:

* Completed:

* H2 Goals definition

EX

* Project “Trebuchet - Experimentation”

* Completed

* Updated GPT-models to version 5
* Upgraded Django to 5.2

* In progress / Next week

* Rewrite the prompts for gpt-5

* Project “DataChat”

* Completed

* Feedback button
* Environmental banner
* Page to edit agent’s prompts, common MCP and supervisor
* Button to share prompts across all colleagues
* Updated GPT-models to version 5

* In progress / Next week

* Common problems gathering, categorization, planning
* UI for editing table access levels
* Re-discuss integration with BI
* Add more tables, rewrite prompts for GPT-5
* Fix bugs with silent answers and sudden stops

## Aug 1, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019632620&usg=AOvVaw2VMWzZtCtKC4wYuj1Pgr1k)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Monte Carlo

        The MC platform access has been blocked today due to the contract to be signed.

* Completed

* MC ML monitor for holding MRR daily has been created and evaluated for credit units consumption (verification logic requires changes due to the high cost of the test)
* Unmonitored intermediate and staging tables have been filtered out from the MRR product lineage
* Committed MRR dashboard tables have been added to MRR data product

* Next week (only after the contract is signed and the access is back):

* DBT tests migration preparation step (namings, templates, rules, tags)

* MRR metrics monitoring

* In progress:

* Quantitative tests for MRR and users number grouped by limits and units

* Next week:

* Update crucial tests metadata to notify Dparty team leadership

* Executive Scorecards dashboard

* Next week:

* Basic DBT tests implementation
* Box plot tests

* GA4 streaming events data health

* In progress/Next week:

* Creating tests for monitoring of the quality of the GA4 data

* Marketing tests

* Completed:

* Creating tests for new facebook, bing and linkedIn sources

* DQ improvements

* In progress/Next week:

* DQ Framework description (to add clarity and transparency)

DG

Project “CLEAR”

* Completed:

* Candidate lists that is under review: Analytics-external, Analytics-tableau-prod, enterprise-dwh-raw-prod, enterprise-dwh-raw-rc
* Ready for the review (will be shared soon): semrush-com, analytics-projects-prod
* Revisited and updated Tier system

* In progress/Next week:

* Drafting candidate lists for analytics-tests-prod-tf, enterprise-dwh-prod

Project “Data Assets Certification”

* Completed:

* Pilot Plan approved by analytical TLs;

* In progress/Next week:

* Pilot plan to be reviewed by Sam next week;

Project “Data Enrichment Optimization”

* Completed

* SMB match rate improvement: Additional 6% overall match rate increase after enabling additional company data

* In progress/Next week

* Infobel POC - pending on Infobel’s side
* Business Case Analysis for D&B - pending review
* Revised Project Charter - pending review

Project “Metadata Platform”

* In progress/Next week

* Metadata Req’s from Data Governance: to be used in PoC performed by BDP

Other

* Completed

* Critical Data Alerts – developed, handed over the deployment to the DE Team
* Table descriptions from dbt to Data Catalog

BI

* “C-level Scorecards” Project

* Completed:

* DS creation

* In Progress:

* Enterprise Gross MRR Renewal %

* “Data Platform Metrics” Project

* Completed:

* Dashboard creation

* “Tableau Cloud Migration” Project

* In Progress:

* Tableau Next investigation
* Features/current pain points discussion with Tableau

* Refactoring, Issues & Other

* Completed:

* Advanced Emailing System (access to Workshop was granted)  
  Next step: create test announcement

* In Progress:

* CMO Dashboard refactoring (WBR view)
* Spotlight event reporting (+ Swoogo)

WA

* Completed:

* Add script to staging GTM
* Modify event parameters validations
* Update semrush\_product\_name Validation to Accept ai\_vo
* Remove required parameter status form\_submit\_text in the form\_submit event

* In Progress/Next Week:

* Datos Live configuration with CookieHub - waiting for confirmation to close this issue
* QA Meta Tracking – Pixel + API - issue identified, present solution next week to prevent duplicated triggering
* Missing events for domain overview tool - Root cause identified, solution in progress
* DV360 Migration to gtag & Enhanced Conversions Setup - met with the team, solution proposed and waiting for confirmation from Google
* Set-up Consent mode for Ryte - not started, after discussion with stakeholders it is not a priority, back to backlog

BDP

* "Raw Data handover to BDP" Project

* In progress

* MaxMind migrate: analytics-external-prod-tf.maxmind\_com source (it’s in a non-functional state currently)
* Analytics SFDC: This integration is being analyzed separately - we have started planning the migration process to SSoT SFDC.

* Completed:

* Analytics SFDC export: From ADP SFDC removed several columns that will soon be removed from the SFDC source

* Evaluation of Metadata Tools:

* OpenMetadata – expected by the end of the day (by BDP)
* DataHub – expected next week (by the SysOps Team)

* Sources and data-marts updates:

* In progress / Next week

* Swoogo API data: The data samples have been analyzed. We received a list of entities from stakeholders whose data needs to be provided. Next week, we’ll begin preparing the PROD processes.
* GKT Team data (metrics from search\_volume, organic\_traffic, backlinks):
* New request: Enterprise Solutions data (es-lakehouse-prod-tf):

* Platform

* Completed:

* Upgrade Airbyte from v1.4 to v1.6 (with SysOps team)

* In progress / Next weeks

* Upgrade Cloud Composer (Airflow) to composer-2.13.6-airflow-2.9.3
* Review the "CLEAR" project result for enterprise-dwh-raw-prod

DE

* Infrastructure improvements / Tech debt

* Completed:

* First study about google colab - Study done to see how it fits inside our dev environment, and if it have all we need to implement it, so we can remove our jupyterhub. Next stage is to make some experiences with it.
* Fixed airflow sensor that was running out if disk (again)
* Created design for analytics internal reorganization

* Next week/In Progress:

* Fixing the issue where our metrics exporter machines are getting high memory usage
* Validate the full refresh tables and their downstreams script
* Adding owner files in all repos that we own
* Migrating table copies from dataparadise to DBT repo
* Explore switching Gitlab runners from virtual machines to instance Groups
* Decommission of analytics-data-prod-tf project
* Researching Recursion error on Gitlab for dbt repo
* Improve “run tests on changed models” CICD step to introduce a new meta parameter which will allow us to exclude tests we don’t want to be run on changed models.
* Researching possible ways of datamart optimization

* GA lite

* Completed:

* Deploy cl\_events\_intraday table.

* Support improvements

* Next Week/In progress:

* Implementing Bigquery restricted operations (dangerous operations that can be run by leads)

EX

* Project “Trebuchet - Experimentation”

* Completed

* Prepare the Toolkit Activation and Onboarding metric together with Alla
* Add the eventTrafficSource parameter to the GA4 and GA4Users metrics
* Fix screenshot upload issues
* Fix charts and tables for deprecated metrics and improve UX across all metrics
* Update the UI of the main page
* Add link to the KB report from the experiment page

* In progress / Next week

* Project “DataChat”

* Completed

* Moved all prompts and configuration settings for Supervisor, Agents, and MCP servers to the database
* Change a Confluence search agent to a Universal search
* Add MCPs through the interface

* In progress / Next week

## Jul 25, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019649569&usg=AOvVaw2zhaWN5XGyf3XRhxxpoJ_8)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Monte Carlo

* Completed

* MC MRR project scoping ([current consumption](https://www.google.com/url?q=https://getmontecarlo.com/settings/billing&sa=D&source=editors&ust=1768225019650090&usg=AOvVaw0_cmx1UJlliK0f3tq3QQsU) is 600 credit units per day with the limit of 712 credit units per day)
* [Project Charter](https://www.google.com/url?q=https://docs.google.com/document/d/1IiHtB-IIBebEYRHXBjuCZTGjDfIJ06sMYY2tTeujG8c/edit?usp%3Dsharing&sa=D&source=editors&ust=1768225019650429&usg=AOvVaw1WVdwk34S3jIZajeqxtdqM) is ready for a review and feedback

* Next week:

* DBT tests migration preparation step (namings, templates, rules, tags)

* MRR metrics monitoring

* Completed:

* Monitoring workflow improvements have been discussed with Dparty team, respective action items have been [documented](https://www.google.com/url?q=https://docs.google.com/document/d/1M-dvCVTWOG_4GMu8l_nG06qd9dt5RqN_GxLK3uUZDN4/edit?usp%3Dsharing&sa=D&source=editors&ust=1768225019651003&usg=AOvVaw2s6DWc9lalZi9yPeLqSgtG) to track the status

* In progress/Next week:

* Quantitative tests for MRR and users number grouped by limits and units
* Update crucial tests metadata to notify Dparty team leadership

* DQ improvements

* Completed

* Project “CLEAR”: data-paradise-20 has been reviewed for the deletion purposes of the not used tables
* DBT tests alerts for the Voyantis team have been updated with the dedicated external channel to notify and people to be tagged within these tests

* In progress/Next week:

* DQ Framework description (to add clarity and transparency)
* GA4 streaming events data health checks

DG

Project “CLEAR”

* Completed:

* Candidate lists done and under review: DP-20, Analytics-external, Analytics-tableau-prod, Analytics-datamart
* 1st wave of Archive/Deletion CL727 tables (434 tables deleted)

* In progress/Next week:

* Drafting candidate lists for semrush-com, analytics-projects-prod, enterprise-dwh-raw-prod, enterprise-dwh-raw-rc
* Revisit and update of Tier system

Project “Data Assets Certification”

* Completed:

* Pilot Plan for Regs Dash ready, to be reviewed today

Project “Data Enrichment Optimization”

* In progress/Next week

* Infobel POC
* Business Case Analysis for D&B

Project “Metadata Platform”

* In progress/Next week

* Metadata Architecture – PoC of OMD / DataHub

Other

* Completed

* Data Governance Strategy, Roadmap

* In progress/Next week

* Critical Data Alerts – under development

BI

* “C-level Scorecards” Project

* In Progress:

* Enterprise Gross MRR Renewal %

* “Data Platform Metrics” Project

* In Testing:

* Dashboard creation

* Daily Reports - 7D Rolling Metrics Redesign

* Completed - User Interviews
* In Progress - Dashboard update after source redesign

* “Tableau Cloud Migration” Project

* In Progress:

* Tableau Next investigation
* Features/current pain points discussion with Tableau

* Refactoring, Issues & Other

* Completed:

* New MRR Impact dash fixes (Add NUMRRPPU metric, add new dimension)
* Monthly Dashboard Quality Labeling
* Bug in Cohort size in Toolkits Activity dash

* In Progress:

* Advanced Emailing System
* CMO Dashboard refactoring (WBR view)

WA

* Completed:

* Screen flickering for signup page
* QA TikTok Pixel Events

* In Progress/Next Week:

* QA Meta Tracking – Pixel + API
* Add script to staging GTM - prepared, waiting for CORS update from devs
* Missing events for domain overview tool - Investigation
* DV360 Migration to gtag & Enhanced Conversions Setup - meeting with stakeholders next week
* Set-up Consent mode for Ryte & Datos - not started

BDP

* "Raw Data handover to BDP" Project

* In progress

* Analytics SFDC export: Several columns will soon be removed from the SFDC source, but we’ve received approval to remove them from the export process as they are no longer used. We’re preparing the code to remove them from analytics-external-prod.

* "Reverse ETL Tool implementation" Project

* In progress / Next week

* We are preparing a comparative report

* Sources and data-marts updates:

* Completed:

* New: Corporate API data-marts (MarTech):

* enterprise-dwh-prod-tf.mart\_corporate.mart\_corporate\_\_accounts
* enterprise-dwh-prod-tf.mart\_corporate.mart\_corporate\_\_users

* New: APP Center gRPC data-marts (Business Systems Integration):

* enterprise-dwh-prod-tf.mart\_appcenter.mart\_appcenter\_\_trials
* enterprise-dwh-prod-tf.mart\_appcenter.mart\_appcenter\_\_product\_trials

* In progress / Next week

* Swoogo API data extraction - at the beginning of the week, we handed over the raw data to the Insight Analytics team for review. We’re waiting for their feedback
* New request: Bring raw data from GKT Team (16 tables)
* Upgrade Airbyte from v1.4 to v1.6 (with SysOps team)

* New initiatives teaser:

* Evaluation of Metadata Tools: OpenMetadata & DataHub as a part of the project “Metadata Platform”
* "Pilot of an incident management tool" Project: Testing the feasibility of using the incident management tool incident.io, which will soon replace the currently used Opsgenie.

DE

* Infrastructure improvements / Tech debt

* Completed:

* Added protections to gitlab. We added branch protection to internal repositories to ensure code is reviewed by DE team before being merged. We have also added managers in GOST to ensure nobody can create infrastructure or change GCP permissions without DE approval
* Machine cleanup. Thanks to our alert system, we found out some machines related to airflow and gitlab were dangerously close to breaking. The cause was that the machines were set up without proper way of cleaning their local disks , and because they have been running non stop for a long time, their disks (inodes to be more specific) were almost reaching a limit.
* Remove/fix failing scripts. Decommissioned old redundant pipelines so today script-failures channel is empty (at least for now).
* Optimized big failing models (From 8Tb to 143 Gb of used resources per each run)

* Next week/In Progress:

* Discuss updates to GCP projects for local development with Tech leads
* Start work on DE roadmap updates
* Investigate about google colab vs our internal jupyterhub
* Introduce a button in GitLab for full refresh tables with their downstreams
* Migrate basic table copy to datamart from dataparadise to dbt

* GA lite

* In progress:

* Deploy cl\_events\_intraday table on Jul 29.

* Support:

* Completed:

* New table - Cost Metrics for Data Platform

EX

* Project “Trebuchet - Experimentation”

* Completed

* Moved custom metric to the deprecated section and removed unused form
* Fixed image export in KB reports
* Updated authentication to use Google OAuth
* Added Cursor rules

* In progress / Next week

* Preparing Toolkit Activation and Onboarding metric with Alla

* Project “DataChat”

* Completed

* Enabled tools in message history
* Migrated frontend to Feature-Sliced Design architecture  
  Implemented automated DataChat usage metrics collection in BigQuery
* Added Leaderboard page
* Updated Ruff rules
* Added Cursor rules

* In progress / Next week

* Moved all prompts and configuration settings for Supervisor, Agents, and MCP servers to the database
* Change a Confluence search agent to a Universal search

## Jul 18, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019663365&usg=AOvVaw1C0Dx5FmVaVKwNeWKt-C3_)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Monte Carlo

* In progress

* MC MRR project scoping (target: 712 MC credit units per day)

* Next week:

* MRR project charter
* MC fixes verification

* Holding MRR Test Coverage

* Completed:

* Overall MRR test coverage metric (Holding MRR, MRR 2.0) has been added
* Main calculation models lineage and test coverage metric for Bookings and Committed MRR have been added

* In progress:

* Monitoring workflow with Dparty team

* DQ improvements

* Completed

* Updated timeliness and completeness DBT test macros with SCD active partition parameter
* DBT test alerts for the external Voyantis team have been enriched with required metadata to be posted in the external Slack channel

* In progress/Next week:

* DQ Framework description (to add clarity and transparency)

DG

Project “CLEAR”

* Completed:

* Candidate list for DP20; Now is under review
* Candidate list for analytics-external-prod-tf; Now is under review
* 1st wave of  CL727 tables reviewed; Now is in archiving process

* In progress/Next week:

* Drafting candidate lists for analytics-datamart-prod-tf, analytics-projects-prod-tf

Project “Data Assets Certification”

* Completed:

* Pilot Plan reviewed with all involved parties

* In progress/Next week

* Estimate Pilot plan for 2 more Dashes

Other

* Completed

* “Metadata Platform” Charter completed

* In progress/Next week

* Data Governance 6Q Strategy under development
* Metadata Architecture Specification under review by [Aleksandr Gritsenko](mailto:a.gritsenko@semrush.com) and [Manuel Garrido](mailto:manuel.garridopena@semrush.com)
* Critical Data Alerts under development

DE

* Infrastructure improvements

* Completed:

* Removing several unused tasks, models and tests from dbt - backlinko\_aweber and DoubleClick.
* Fixed “run tests on changed models” cicd step to prevent updating changed models in previous step from production
* Created a google group for external data viewers
* Fixed timestamp overflow error in analytics-tableau-prod-tf\_\_innovation\_hub\_\_collaboration job
* Tested and deployed additional slack notification channels (used for voyantis)
* Added dbt options document to dbt repo

* In progress/Next week:

* Recalculation of the cl\_events\_intraday table after revision with division teammates
* Fixing potential\_bots task (replace javascript api which stopped working with python api)
* Update custom\_dev\_run\_list dbt command to allow cloning a model with materialization=”google\_sheet\_external” to local environment
* Update hyper ci action on gitlab which does not work
* Check automated removal date for analytics-internal-prod-tf.dbt\_gitlab\_% datasets
* Decommission analytics-tableau-prod-tf\_\_internal\_analytics task
* Spike/research terraform deployment for airflow
* Populate airflow task metadata to BigQuery labels

* Support:

* Completed:

* New how-to : [Copy data from BQ to Clickhouse](https://www.google.com/url?q=https://kb.semrush.net/display/ATI/How-to%253A%2BCopy%2Bfrom%2BBigQuery%2Bto%2BClickhouse&sa=D&source=editors&ust=1768225019669487&usg=AOvVaw3TEUbKhR_FaBa7l79XGXl_)
* In progress/Next week:

* Give read permissions on ga-roster tables in Postgres for new web analysts

* Others:

* New team member onboarding

BI

* “C-level Scorecards” Project

* In Progress:

* Enterprise Gross MRR Renewal %

* Data Platform Metrics Dashboard

* In Progress:

* Dashboard

* Daily Reports - 7D Rolling Metrics Redesign

* In Progress:

* Requirements Gathering

* “Tableau Cloud Migration” Project

* In Progress:

* Discussions with IT team on scope of their support
* Tableau Next investigation

* Refactoring, Issues & Other

* Completed:

* Add costs data into CMO and New MRR Impact dashes
* Tableau Add-on for Google Workspace

* In Progress:

* Advanced Subscriptions - Delivering Tableau Views to user email

WA

* Completed:

* Screen flickering for signup page

* In Progress/Next Week:

* QA Meta Tracking – Pixel + API
* QA TikTok Pixel Events
* Add script to staging GTM
* DV360 Migration to gtag & Enhanced Conversions Setup
* Set-up Consent mode for Ryte & Datos

BDP

* "Raw Data handover to BDP" Project

* Completed

* Migration AppHub source is not required as the download source is no longer used (we previously reported on the process of decommissioning the AppHub service, that data we are downloading)

* "Data Enrichment Optimizations" Project

* Completed:

* Last week we shared our architectural approach with the team at Zoominfo and received confirmation that we don't deviate from best-practice when developing services like this.
* We connected Zoominfo to our data enrichment pipeline

* In progress / Next week

* Next week, we will begin the design of the last phase, which involves collecting all enriched data into standardized Golden Records
* Connect OpenAI as a data-provider

* "Reverse ETL Tool implementation" Project

* Completed:

* We tested the capabilities of Census and Hightouch for use with Marketo

* In progress / Next week

* Preparation of a comparative report. Analyzing the value according to the requirements
* Checking other possible destinations (SFDC, GA4)

* Sources and data-marts updates:

* In progress / Next week

* Corporate API data extraction
* Swoogo API data extraction (Marketing & Expansion Analytics Team, Brand Marketing)
* Upgrade Airbyte from v1.4 to v1.6 (with SysOps team)

EX

* Project “Trebuchet - Experimentation”

* Completed

* Update shift data logic for all metrics
* Extend trials users metric to include app\_name, trial\_type, and tier fields
* Stop calculation of user metrics, disable the Prefect service and remove integration with it from Trebuchet
* Update MCP to fetch full graphql schema

* In progress / Next week

* Update calculating date
* Add notification in slack for successful and unsuccessful calculations

* Project “DataChat”

* Completed

* Improve UI / UX
* Fix bugs and connect logs service (Sentry) to collect errors
* Add the user guide on Datachat
* Present Datachat to different teams:  
  - Retention team  
  - Design team (Aleksandra Shcherbakova)  
  - Business Process Transformation team (Saeid Nobakht - Carly Patterson)

* In progress / Next week

* Improve message history by including tools and other metadata
* Onboard the Revenue team on how to use DataChat
* Add ability to connect multiple MCP servers in DataChat
* Improve the GA4 agent based on the Design team recommendation

## Jul 11, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019676486&usg=AOvVaw1MVlwcFivurrezp7ed59zk)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Monte Carlo

* In progress/Next week:

* MRR project charter
* MC project limitations clarification
* MC fixes verification

* Holding MRR & MRR 2.0 Test Coverage

* Completed:

* MRR 2.0 tests have been added as a CORE level for Holding MRR metric

* Next week:

* Discuss with the D-party monitoring workflow
* MRR dashboards and charts scope definition
* MRR final metrics checks definition

* Test coverage for Marketing transition to Toolkits

* Completed:

* Business rules tests for the following models:

calculations\_cpt\_cpt\_touches

* DQ improvements

* In progress/Next week:

* DQ Framework description (to add clarity and transparency)
* H1 summary goals status refactoring

DG

Project “CLEAR”

* Completed:

* Candidate list for DP20; Now is under review
* 1st wave of  CL727 tables reviewed; Now is in archiving process

* In progress/Next week:

* Drafting candidate lists for analytics-external-prod-tf, enterprise-dwh-raw-prod, enterprise-dwh-raw-rc
* Archiving Policy draft

Project “Data Enrichment Optimization”

* 🌴

Project “Data Assets Certification”

* Completed:

* Reviewed and approved Pilot plan with DE/DQ

* In progress/Next week

* Review Pilot plan with BI and analytics team leads

Other

* Completed

* CODEOWNERS [race condition](https://www.google.com/url?q=https://semrush.slack.com/archives/C011Q58AZKR/p1750257806856729?thread_ts%3D1750252481.757689%26cid%3DC011Q58AZKR&sa=D&source=editors&ust=1768225019679982&usg=AOvVaw2AH2ZVLQIvz9smqE7UERPX) fixed

* In progress/Next week

* Data Governance 6Q Strategy under development
* Metadata Management: Project Charter & Architecture Specification under review
* Critical Data Alerts – enhance slack alerts visual format – under development

DE

* Infrastructure improvements

* Completed:

* Deploy with new DBT image where DBT tests just run once
* Removed e2e\_tests\_aquisition\_fb and all related tests/models, since they are not used anymore

* In progress/Next week:

* Fixing/Removing script tasks that have had errors from a long time, but with no complains
* Test and deploy additional slack notification channels (used for voyantis)

* Support:

* Completed:

* DE support bot is online, it will allow DE to streamline ticket management and enable metrics collection
* Change source for clickhouse marketing\_numrr\_unique\_visitors\_monthly\_stork\_40

BI

* "Tableau Collections & Folders" Project

* (Completed) - Folders’ reorganisation

* “C-level Scorecards” Project

* In Progress:

* Enterprise Gross MRR Renewal %

* Data Platform Metrics Dashboard

* In Progress:

* Gathering Q2 Metrics
* Dashboard

* Completed:

* Metrics for BI, BDP, DG

* Daily Reports - 7D Rolling Metrics Redesign

* In Progress:

* Requirements Gathering

* Refactoring, Issues & Other

* Completed:

* Upgrade PLG KPIs Dashboard for Growth Team

* In Progress:

* Advanced Subscriptions - Delivering Tableau Views to user email
* Tableau Add-on for Google Workspace
* Add costs data into CMO and New MRR Impact dashes

WA

* In Progress:

* Ondra & Alberto -  onboarding
* Screen flickering for signup page
* QA Meta Tracking – Pixel + API
* QA TikTok Pixel Events

BDP

* "Raw Data handover to BDP" Project

* In progress

* We’ve started analyzing existing integrations in analytics-external. We plan to formalize the work as an official project.
* Also, checking how we collect data from SFDC and moving everything to the new SFDC source of truth will be split off as its own separate project activity.
* Analyse migration AppHub data integration to Inventory/Bakery source

* Reverse ETL tools testing

* In progress / Next weeks (till the end of July)

* Continue evaluating HighTouch and Census capabilities.

* Sources and data-marts updates:

* Completed:

* new Source: Trends API unit consumption: mart\_api\_limiter\_\_products,

* enterprise-dwh-prod-tf.mart\_api\_limiter.mart\_api\_limiter\_\_products
* enterprise-dwh-prod-tf.mart\_api\_limiter.mart\_api\_limiter\_\_request\_limits
* enterprise-dwh-prod-tf.mart\_api\_limiter.mart\_api\_limiter\_\_subscription\_types
* enterprise-dwh-prod-tf.mart\_api\_limiter.mart\_api\_limiter\_\_users

* new fields to SFDC SSoT Opportunity: Added 35 new fields to enterprise-dwh-prod-tf.mart\_sfdc.mart\_sfdc\_\_opportunity
* new entity to SFDC SSoT: DOZISF\_\_ZoomInfo\_\_c
* Added new Zoominfo field employeeCountByDepartment to current data-enrichment data-mart

* In progress / Next week

* Upgrade Airbyte from v1.4 to v1.6 (with SysOps team)
* We plan to upgrade GCP Cloud Composer (Airflow) as part of our planned maintenance process.

EX

* Project “Trebuchet - Experimentation”

* Completed

* Migrate trials\_users metric to `data-paradise-20.product.toolkits\_beta\_trials\_by\_toolkit`
* Remove create init custom metric by default and also remove it from existing Draft, Planned and possible Running experiments

* In progress / Next week

* Preparing to switch off the Prefect service

* There are only 3 experiments with old user metrics, after their completion we turn off the Prefect service

* Trebuchet MCP

* Expose graphql schema to the LLM in description of the tool, so it can properly run the request to edit the metrics
* Add the ability to edit the description (experiment design)

* Onboarding Maxim

* Project “DataChat”

* Completed

* Update and reorganise the UI
* Synchronize your table with the original Bigquery table after adding or deleting columns.
* Create the alpha version of the users guide

* In progress / Next week

* Run sql queries on the user’s account in order to reduce cost on our infrastructure
* Onboard the Retention and Revenue teams on how to use DataChat
* Fix bugs with message streaming

## Jul 4, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019688259&usg=AOvVaw1osTkdFTXZ4PuX733i8lU8)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Monte Carlo

* Completed

* Clarified next steps with MC

* In progress/next week:

* MRR probation project - project charter and planning
* MC project limitations clarification
* MC fixes verification

* Holding MRR Test Coverage

* Completed:

* Holding MRR test coverage for product and source (source tables for critical dashboards) data layer
* Holding MRR Daily test coverage for product layer with additional box plot test for the final metric

* Next week:

* MRR dashboards and charts scope definition
* Discuss with the D-party monitoring workflow
* MRR final metrics checks definition

* Test coverage for Marketing transition to Toolkits

* Completed:

* Created basic technical and business logic tests for toolkit\_attribution

and dashboards\_content\_performing\_dash

* In progress:

* Business rules tests for the following models:

calculations\_cpt\_cpt\_touches

* DQ improvements

* Completed:

* [H1 summary & goals status](https://www.google.com/url?q=https://docs.google.com/presentation/d/1Hk8mZmsucndgbNbCZNWPHr0GogZp7sl4gVvSU4hglPc/edit?usp%3Dsharing&sa=D&source=editors&ust=1768225019690746&usg=AOvVaw1RhyOmBDOusrmETVDlzvEV)
* [June highlights summary](https://www.google.com/url?q=https://docs.google.com/document/d/1QVLz0rcVx5xIYLK9zqwQ2X8d-oCpW01c0Yz9b0O5-Go/edit?tab%3Dt.0&sa=D&source=editors&ust=1768225019690927&usg=AOvVaw35_6ZIShakCJnaPrron8IE)
* [DQ vision has been reviewed and finalized](https://www.google.com/url?q=https://miro.com/app/board/uXjVInR4XDs%3D/?share_link_id%3D500513059749&sa=D&source=editors&ust=1768225019691096&usg=AOvVaw2cCBqLjxzGu9FtC9Wggt4C)

* Next week:

* DQ Framework MIRO board (to add clarity and transparency)

DG

Project “CLEAR”

* In progress/Next week:

* Review of candidate lists for CL727
* Finilazing candidate list for DP20
* Drafting candidate lists for analytics-external-prod-tf, enterprise-dwh-raw-prod, enterprise-dwh-raw-rc

Project “Data Enrichment Optimization”

* Completed:

* Manual → Semi-Automated Enrichment: Retired the full-manual workflow and switched to ZoomInfo Enhance. Time-to-Delivery dropped from 2-3 days to <1 hour.
* Revised Business Requirements.

* In progress/Next week

* SMB match rate improvement: Awaiting Sales Ops sign-off to enable “Additional Data” in ZoomInfo Sales
* Revised Project Charter

Project “Data Assets Certification”

* In progress/Next week

* Review Pilot plan with DE/DQ, and analytics team leads

Other

* Completed

* Metadata Strategy draft ready, under review with [Mike Trifonov](mailto:mike.trifonov@semrush.com)

* In progress/Next week

* “Metadata Architecture Development” Project Charter and Specification under review
* Critical Data Alerts – enhance slack alerts visual format

BI

* "Tableau Collections & Folders" Project

* (In Progress) - Folders’ reorganisation

* “C-level Scorecards” Project

* Completed:

* Coloring in Table View
* Finished "zoom" views for all metrics
* Loaded Sales Reps history 2024
* Added quarter views
* Documentation

* In Progress:

* Enterprise Gross MRR Renewal %

* Data Platform Metrics Dashboard

* In Progress:

* Gathering Q2 Metrics
* Dashboard prototype

* Refactoring, Issues & Other

* Completed:

* New version of Registrations dashboard

* In Progress:

* Advanced Subscriptions - Delivering Tableau Views to user email
* Tableau Add-on for Google Workspace
* CMO Dashboard refactoring

WA

* In Progress:

* Ondra Subrt - onboarding
* Alberto Mendez Ceniga - starting 07/07

BDP

* “Salesforce Source Data Centralization (SSoT)” Project.

* Completed

* We’ve completed the setup of the SSoT data storage from SFDC [and closed the project](https://www.google.com/url?q=https://rhythm.semrush.net/bet/42824&sa=D&source=editors&ust=1768225019695785&usg=AOvVaw1rMl4iGkVEsuloiAXcdpXu). A total of 44 entities are currently being synchronized on an ongoing basis. SSoT data marts are being generated for 38 of them. The remaining 6 entities are synchronized to populate related formula fields and do not require separate SSoT data marts.

* Next steps

* The migration of RevOps processes to the prepared SFDC will follow their internal schedule, and we will phase out the Workato-based SFDC data collection process accordingly. The decommissioning will be coordinated to ensure a smooth and controlled transition without disrupting existing workflows.
* The MarTech team will migrate their processes to the new SFDC by the end of August, after which we will decommission the outdated and duplicate SFDC data collection process.
* We are starting to analyze the third duplicate process — “SFDC data collection for the Analytics team” — and plan to gradually decommission it.

* "Data Enrichment Optimization" Project. Plan, Architecture & PoC

* In progress / Next week

* We’ve received the API keys for ZoomInfo and are setting up the integration to enable the enrichment process in our PoC service.
* We’re also in the process of finalizing access to an OpenAI API key to incorporate it into the enrichment workflow.

* “Data Platform Metrics Dashboard" Project. BDP Metrics

* Completed

* We’ve set up data collection from Jira
* and prepared daily-based metrics for reporting: “Created Tasks Total”, “Closed Tasks Total”, “Created Tasks Support”, and “Closed Tasks Support”.

* "Raw Data handover to BDP" Project

* In progress / Next months

* We’ve started analyzing the data sources and source-integrations that were transferred to our ownership this month from Manuel’s team.

* Reverse ETL tools testing

* In progress / Next week

* We’ve received approval from Security and Legal for test usage of Reverse ETL tools (HighTouch and Census).
* Next week, together with the MarTech team, we’ll begin evaluating their capabilities.

* Sources and data-marts updates:

* Completed:

* Extended Marketo Leads mart: mart\_marketo.mart\_marketo\_\_leads

* new fields have been added: Mql\_last\_datetime, new\_business\_lead\_score, LeadSource, selfReportedCompanySize, Phone, Company, Lead\_lifecycle\_status, Country, person\_source\_detail

* In progress / Next week

* We’re planning to integrate a new PostgreSQL source with Trends API unit consumption data (requested by the Obsidian Team).

DE

* General

* Completed:

* Fix access for couple JupyterHub users
* Bunch of infrastructural updates (secret keys, table management)

* In progress/Next week:

* Changing source table for analytics-tableau-ch.marketing\_numrr\_unique\_visitors\_monthly\_stork\_40 table on clickhouse
* Two big problems with recursion
* Removing retries on dbt tests

* Highlighted:

* We deprecated ~700 tables with experiments data on our side, and started to use this data from the source project (trebuchet-prod)

EX

* Project “DataChat”

* Completed

* Add the ability to search confluence in DataChat
* Improve prompts for existing tools
* Increase SQL limits up to 2Tb
* Update tools design

* In progress / Next week

* Connect minimum number of their tables
* Collect feedback
* Fix bugs with message history and tools

* Project “Experimentation”

* Completed

* Block the button to create custom metric

* In progress / Next week

* For running experiments

* Add monitoring metrics similar to custom metrics
* Ask if it is ok to delete custom metrics

* Migrate trials\_users metric to `data-paradise-20.product.toolkits\_beta\_trials\_by\_toolkit`
* Onboarding a new team member

Notes:

* [Mike] Next Week – AMA session with Sam – pls feel free to add your q’s
* [Mike] Next Week – SLT meeting (Senior Leadership Team = C Levels), all the company is working to prep for this and we hope to hear some news from there

## Jun 27, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019702283&usg=AOvVaw2o3tXbekxGnI2Wzm0JHsVu)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) 

DQ

* Monte Carlo PoC

This week we focused on the Monte Carlo POC

* Completed

* POV state has been summarized and communicated to Mike

* In progress/next week:

* Next steps clarification
* MC fixes verification

* Holding MRR Test Coverage

* In progress:

* Holding MRR test coverage for product and source (source tables for critical dashboards) data layer

* Test coverage for Marketing transition to Toolkits

* Completed:

* Created basic technical and business logic tests for marketing\_toolkit\_metrics and marketing\_toolkit\_metrics\_week models

* In progress:

* coverage with basic and business rules tests is being implemented for the following models:

calculations\_tk\_attribution\_toolkit\_attribution

dashboards\_content\_performing\_dash

calculations\_cpt\_cpt\_touches

* DQ improvements

* Completed:

* DQ vision adding Monte Carlo capabilities as enablers

* Next week:

* H1 summary & goals status

* Test coverage for the Holding MRR – as a percentage
* Number of Data Issues in Production – as it shows direct business impact

* June highlights summary

DE

* General

* Completed:

* Market segment column on salesforce buying signal table
* Tasks from the weekly support

* In progress/Next week:

* Make tests run only once even if they fail
* Extract certain limits
* Fix access to JupyterHub for several users
* Migrate datamart tables from dataparadise to dbt

* Monte Carlo PoC

* In progress/Next week:

* Verify amount of requests on our side against MonteCarlo API

 DG

Project “CLEAR”

* In progress/Next week:

* Drafting candidate lists for data-paradise-20, enterprise-dwh-raw-prod, enterprise-dwh-raw-rc

Project “Data Enrichment Optimization”

* Completed
* In progress/Next week

* Revised draft of Business Requirements and Project Charter Doc
* SMB match rate improvement

Other

* Completed

* Metadata Project Charter and Architecture specification
* Finished the solution design and implemented technical aspects (i.e., unit test) for the Voyantis Data Alerts.

* In progress/Next week

* Metadata Project Charter and Architecture Specification review with DE and DP leads
* Voyantis Data Alerts Integration testing and deployment (℅ DE)

BI

* "Tableau Collections & Folders" Project

* (In Progress) - Folders’ reorganisation

* “C-level Scorecards” Project

* In Progress:

* Additional features
* History for Total & Tenured Sales Reps
* Enterprise Gross MRR Renewal %
* Documentation

* Data Platform Metrics Dashboard

* In Progress:

* Gathering Q2 Metrics
* Dashboard prototype

* Refactoring, Issues & Other

* (Completed) - [MC PoV] Tableau integration  
  (In testing) - New version of Registrations dashboard
* In Progress:

* Advanced Subscriptions - Delivering Tableau Views to user email
* Tableau Add-on for Google Workspace
* CMO Dashboard refactoring

WA

* In Progress:

* Onboarding plan for new Web Engineers

* Ondra Subrt - starting 07/01
* Alberto Mendez Ceniga - starting 07/07

EX

* Project Trebuchet

* Improve ga4\_users metrics to count unregistered users too
* Multiple bugifxes
* Deprecate inactive teams

* Project “DataChat”

* Completed

* Limiting access to added tables
* Confluence search
* Search semrush website
* Multiple prompt improvements

* Add your datachat questions and ideas how to answer them to the [doc](https://www.google.com/url?q=https://docs.google.com/document/d/1Ee0npl9hIsWK4AqMnm3b8WWVdpchok5rI3kgPpzYBFc/edit?tab%3Dt.0%23heading%3Dh.fbbn27hlf51m&sa=D&source=editors&ust=1768225019711901&usg=AOvVaw11DotCEBHOhCm5FZOELjts)

## 

## Jun 20, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019712321&usg=AOvVaw0MDwsYd0Vz5pg19OArafx5)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Monte Carlo PoC

This week we focused on the Monte Carlo POC

* Completed

* Analyzing the centralized Data Quality Dashboard
* Defining a hierarchy for grouping tests in dashboards
* Reviewing the Test Results View for alerts and monitors
* Drafting a strategy for migrating and optimizing DBT tests

* In progress/next week:

* Enable and configure ML-based monitors (box plot test for payments)
* Evaluate Slack notifications from both alerts and monitors (severity and prioritization of the alerts, alerts customization)
* MC RBAC exploration (we could leverage RBAC until we do not have monitors as a code to control MC changes)
* Incident management framework review
* MC templates for DBT tests migration as a part of the DQ framework
* Costs & billing exploration
* Summarizing PoV

* Holding MRR Test Coverage

* Next week:

* Holding MRR test coverage for product (source tables for critical dashboards) data layer

* DQ improvements

* Next week:

* DQ vision adding Monte Carlo capabilities as enablers

DG

Project “CLEAR”

* Completed:

* Candidate list for CL727 Project

* In progress/Next week:

* Drafting candidate lists for data-paradise-20, enterprise-dwh-raw-prod

Project “Data Assets Certification”

* Completed

* Cost-Effective Optimisation [pending on Mike’s review]

* In progress/Next week

Project “Data Enrichment Optimization”

* Completed
* In progress/Next week

* Revised Business Requirements and Project Charter Doc
* SMB match rate improvement

Project “BOTO” (stage: BOTO for dbt tests)

* Completed

* Rolled out BOTO for dbt tests 🎉
* Update BOTO to the new PLG structure

* In progress/Next week

Other

* Completed

* Collected requirements for  “Metadata Architecture” Project

* In progress/Next week

* Voyantis Data Alerts - testing

BI

* "Tableau Collections & Folders" Project

* (Completed) - Creating Collections for Retention [analytics site]
* (Next week) - Folders’ reorganisation

* “C-level Scorecards” Project

* Completed:

* Dashboard 1st version

* In Progress:

* Additional features
* Enterprise Gross MRR Renewal %
* Documentation

* Data Platform Metrics Dashboard

* In Progress:

* Gathering Q2 Metrics
* Dashboard prototype

* Refactoring, Issues & Other

* Completed:

* Fix Custom SQL in Self-service dash

* In Progress:

* Advanced Subscriptions - Delivering Tableau Views to user email
* New version of Registrations dashboard
* Tableau Add-on for Google Workspace
* [MC PoV] Tableau integration

WA

* In Progress:

* Onboarding plan for new Web Engineers
* [Bug]: GA4 events not published in their datasource
* Mouseflow issue (CI Toolkit team)
* QA TikTok Pixel Events

DE

* “Infrastructure improvements”

* Completed:
* In progress/Next week:

* ExternalSensor replacement
* Switch on dbt-tests execution on CI/CD

* “GA4 Streaming Light” (or Lite?)

* Completed:

* Data and structure validation
* Necessary changes on models

* In progress/Next week:

* Deploy aligned with team - since its highly used table

* Monte Carlo PoC

* Completed:

* Data performance logs for integration in DBT

* In progress/Next week:

* Log integration with DBT

BDP

* "Monte Carlo PoV" Project. Feature testing by BDP

* In progress / Next week

* We’re continuing to explore MC’s capabilities and are also preparing a summary report on what we find useful.

* "Data Enrichment Optimization" Project. Plan, Architecture & PoC

* In progress / Next week

* We’ve started implementing the second phase, specifically the process that performs enrichment based on the previously prepared emails and domains.

* Transcripts data from Chorus API

* Completed

* We prepared the production pipeline and handed over the data source to the stakeholders.

* “Salesforce Source Data Centralization (SSoT)” Project.

* Completed

* We received positive feedback from RevOps confirming that the format and volume of the prepared data meet their needs. They are ready to begin the migration to the highest-priority table, Opportunity.

* In progress / Next week

* We continue validation of the collected data.

* Oracle Report data integration (Prowly's CAC)

* On Hold

* The task is currently on hold, as Finance IT has paused work on the Oracle report. Due to other higher-priority initiatives on their side, the report preparation has been postponed until the end of July.

* Sources and data-marts updates:

* Completed:

* We migrated the data loading process from Brand24 (used in HoldingMRR) from Fivetran to Airbyte, resulting in an estimated monthly savings of around $1K in the Fivetran budget.
* We expanded the data collection from Marketo Leads at the request of RevOps (mart\_marketo.mart\_marketo\_\_leads).

EX

* Project “DataChat”

* Completed

* Download CSV
* Temp tables
* Full refactor

* In progress / Next week

* Charts and plots
* Daily MRR, charts, UI for adding tables, move prompts to internal DB, fix trebuchet MCP network issue

* Project “Experimentation”

* Completed

* New Colors in charts!
* Improve MCP to copy the metrics
* Rewrite of GA4, UA events metrics

* In progress / Next week

* Integrate AI helper to create metrics in trebuchet

Topics:

* [Mike] Monte Carlo PoV – to be finished on Jun 27th (in a week)
* [Mike] DWH 2.0 → will be transformed into “Unified Data Platform” Project

* First step – is  a handover of all integrations / raw data to BDP team as of July 1
* Manuel, Alex and Mike are working on the long-term plan how plan / to make this unification efficient

* [Mike] Don’t forget to visit today’s DEMO (Alex’s team presentation)
* [Mike] FYI: PaySol plans to re-implement a “new” payment solution in Q4
* [Mike] FYI: Next will be “short” for many of us

* Spain is on Holiday on Jun 24
* Manuel, Alex, Natalia (and probably Mike) to be on PTO in the end of the week

## Jun 13, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019728065&usg=AOvVaw1UEP9rBkQi90K2ALyv1FNb)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Holding MRR Test Coverage

* Completed:

* Holding MRR test coverage for core (key upstream tables) data layer

* In progress / Next week:

* Holding MRR test coverage for product (source tables for critical dashboards) data layer

* Monte Carlo PoC

* Completed

* Custom monitors for HoldingMRR have been created

* Next week:

* Strategy session with MC team for Migrating and Optimizing existing DBT tests to Monte Carlo monitors:

* What stays in DBT
* What migrates to Monte Carlo
* What is auto-covered by MC monitors

* Enable and configure ML-based monitors
* Evaluate Slack notifications from both alerts and monitors
* Build and review DQ dashboards with grouping by tags/test types

* DQ improvements

* Next week:

* DBT yaml tests grouping and scheduling investigation (wrapper)

DG

Project “CLEAR”

* Completed
* In progress/Next week:

* Developing approach for analysis and drafting candidate list (centering-land-727, enterprise-dwh-raw-prod)

Project “Data Assets Certification”

* Completed
* In progress/Next week

* Cost-Effective Optimisation

Project “Data Enrichment Optimization”

* Completed
* In progress/Next week

* Cross-collaboration with business stakeholders on the business requirements (Done: Sales/RevOps, Retention, Finance; To do: Marketing)
* Discussion on enrichment architecture solution with ZI

Project “BOTO” (stage: BOTO for dbt tests)

* Completed
* In progress/Next week

* Pending on DE

Other

* Completed

* Project “Metadata Architecture” has been officially kicked off

* In progress/Next week

* Voyantis Data Alerts

BI

* "Tableau Collections & Folders" Project

* (Completed) - Creating Collections for Expansion and Finance
* (In Progress) - Creating Collections for Retention

* “C-level Scorecards” Project

* Completed:

* Dashboard 1st version

* In Progress:

* Releasing the workbook (Final adjustments, UAT & Go-Live)
* Enterprise Gross MRR Renewal % (On hold currently)
* Documentation

* Data Platform Metrics Dashboard

* In Progress:

* Gathering Q2 Metrics
* Dashboard prototype

* Refactoring, Issues & Other

* Completed:

* Fix Custom SQL in Self-service dash

* In Progress:

* Tableau Add-on for Google Workspace
* [MC PoV] Tableau integration

WA

* In Progress:

* [Bug]: GA4 events not published in their datasource
* Mouseflow issue (CI Toolkit team)
* QA TikTok Pixel Events

BDP

* "Monte Carlo PoV" Project. Feature testing by BDP

* In progress / Next week

* Connected BQ's PROD instances and continue to test the tool.

* "Data Enrichment Optimization" Project. Plan, Architecture & PoC

* In progress / Next week

* We continue with the implementation of the first phase, “Collection and preparation of identifying data”, which consists of preparing and normalizing the data that will be the main input data for enrichment.

* Transcripts data from Chorus API

* In progress / Next week

* We’ve received confirmation from the RevOps team that the previously provided test data is exactly what they needed. The next step is to prepare a production-grade data mart.

* “Salesforce Source Data Centralization (SSoT)” Project.

* Completed

* After verifying the accuracy of the collected data (SFDC formula fields), we identified shortcomings in the data collection algorithm, which were resolved without affecting the final data marts.

* In progress / Next week

* We continue validation of the collected data.
* We are still waiting for feedback from the RevOps team after sharing the 12 tables with them.

* Oracle Report data integration (Prowly's CAC)

* In progress / Next week

* Gathering requirements and preparing the specification is ongoing

* Sources and data-marts updates:

* In progress / Next week:

* Migrate Brand24 source integration from Fivetran to Airbyte: The nature of the data generated by the Brand24 source indicated that using Fivetran for export is not economically viable. Therefore, we decided to migrate this process to a more cost-effective tool.
* UBS “User Activities” new source integration

DE

* “Infrastructure improvements”

* Completed:

* Removed deprecated legacy columns from `users` table as part of schema cleanup.
* Upgraded googleapis version to resolve pipeline issues.
* Added a new field to `Opportunity` table
* Fix folders info ingestion
* Share access to data (for monte carlo user, for N.Grushin)

* In progress/Next week:

* ExternalSensor replacement
* Airflow version update (required for ExternalSensor update)
* Plans to back up Google Secrets
* Monte Carlo and DBT performance data integration
* Fix app\_payments downstream - child updates first than parent
* Review gcp quotas and add alerts for main projects

* “GA4 Streaming Light”

* Completed:
* In progress/Next week:

* Implement new GA4 streaming table with unnested fields

* Monte Carlo DE Support
* “Fire fighting”

EX

* Project “DataChat”

* Completed

* Bugfixes, access fixes, Improving prompts
* GA4 added
* Backend refactoring

* In progress / Next week

* UI for adding more tables

* Project “Experimentation”

* Completed

* Bugfixes, metrics improvements

* In progress / Next week

* Demo for analysts about new things in trebuchet

Topics:

* Collab with Insight Analysts – let’s pls pay attention to a “soft” collab with them. In case you notice any “agressive” communication from them – pls let Mike know
* Engagement Survey – plan
* Roundtable – will share a pack with you today

## Jun 6, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019750634&usg=AOvVaw0CnWhKjUC-yoq-55b-10iq)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

Let’s continue our practice – let’s try to share only the high-level info relevant to others,  in super-simple terms. Thanks!

DQ

* Holding MRR Test Coverage

* In progress / Next week:

* Holding MRR test coverage for core data layer

* Monte Carlo PoC

* Completed

* Slack integration
* Analytics DP BQ projects integration

* In progress / Next week:

* MC platform use cases & evaluation planning
* MC monitors exploration

* DQ improvements

* Completed:

* Cleaning deleted fake models refs for e2e\_tests schema
* Unit overview dashboard tests pause (waiting for fixes and recreation
* Implemented tests for the collection\_apps model (now renamed to collection\_items) following the recent refactoring

* Registration SSoT

* Completed:

* Tested the new mart\_users\_scd model and implemented automated tests

DG

Project “BOTO” (stage: BOTO for dbt tests)

* Completed

* Thoroughly tested BOTO update

* In progress/Next week

* Pending on DE to merge BOTO update

Project “Data Assets Certification”

* Completed

* Collected time estimates on pilot: data sources and dashboard certification

* In progress/Next week

* Pending on Metrics Definition team for time estimates on BL certification

Project “Data Enrichment Optimization”

* Completed
* In progress/Next week

* Cross-collaboration with business stakeholders on the business requirements
* Architecture review in collaboration with ZI

Other

* Completed

* Project “CLEAR” has been officially kicked off 🧹

* In progress/Next week

* Voyantis Data Alerts
* Metadata Architecture v.2

BI

* "Tableau Collections & Folders" Project

* (In Progress) - Creating Collections for Expansion, Retention and Finance

* “C-level Scorecards” Project

* Completed:

* Metrics added to unified data source

* SEMR New MRR (Total Company)
* EntSol+Ryte+Insight24 ARR
* EntSol+Ryte+Insight24 Net New ARR
* Total Company Gross MRR Churn %
* Total Gross Sales (Incl. winback <90 days)

* In Progress:

* Dashboard Design
* Metrics in progress of being added

* Total Reps – Sales Capacity
* # of Tenured Reps – Sales Capacity
* Sales-Influenced Incremental MRR
* Enterprise Gross MRR Renewal % (On hold currently)

* Refactoring, Issues & Other

* Completed:

* Create new view in New MRR Impact dash for toolkits
* CookieHub dashboard refactoring

* In Progress:

* Tableau Add-on for Google Workspace
* [MC PoV] Tableau integration

WA

* (Completed) - VWO Script Paused Due to Pages Reloading
* In Progress:

* [Bug]: GA4 events not published in their datasource
* Mouseflow issue (CI Toolkit team)
* QA TikTok Pixel Events

BDP

* "Owox pipelines replacement" Project. Data Integration

* Completed

* GA4 Data Import: Finally we’ve got the production pipeline BQ -> SFTP -> GA4.
* All in all, GA4 Data Imports, Facebook Ads, and LinkedIn Ads were migrated from the OWOX Pipeline as part of this activity for May.

* Microsoft Ads (ex Bing Ads) - migrated from old implementation with the others but this was not in OWOX

* "Data Enrichment Optimization" Project. Plan, Architecture & PoC

* Completed

* Prepared a draft enrichment Pipeline based on existing requirements

* In progress / Next week

* We have started implementing the first stage, “Collection and preparation of identifying data”, which consists of preparing and normalizing the data that will be the main input data for enrichment.

* "Monte Carlo PoV" Project. Feature testing by BDP

* Completed

* We’ve set up MC integrations with our RC environment (BQ, dbd, and Airflow). And started evaluating the capabilities of MC for our tasks.

* In progress / Next week

* We plan to combine our DQ checks with MC monitoring to evaluate the value for us and the possibility of expansion.
* We also plan to test the integration of MC with our Incident Management System - Incident.io

* Transcripts data from Chorus API

* Completed

* Connected Airbyte to the source and collected data samples for the stakeholder

* In progress / Next week

* What remains to be done is: get confirmation of the value of the data we have access to, agree on the final data format, and prepare the Production-grade pipeline.

* “Salesforce Source Data Centralization (SSoT)” Project.

* In progress / Next week

* We continue to verify the correctness and completeness of the data collected from SFDC
* We are still waiting for feedback from the RevOps team after sharing the 12 tables with them last week.

* Oracle Report data integration (Prowly's CAC)

* In progress / Next week

* Gathering requirements and preparing the specification continues

* Sources and data-marts updates:

* Change: Cancellation Reason Source. Adapted the data collection process after the Proto schema change for Pubsub on the source side

DE

* “Infrastructure improvements”

* Completed:

* Removed duplicates from my\_reports tables

* In progress/Next week:

* ExternalSensor replacement
* Airflow version update (required for ExternalSensor update)
* Plans to back up Google Secrets
* Research how to move all analytics-team subscriptions to pythons script

* “GA4 Streaming Light”

* Completed:

* Cost estimation and table designed finalised

* In progress/Next week:

* Implement new GA4 streaming light table

* Monte Carlo DE Support
* “Fire fighting”

EX

* Project “DataChat”

* Completed

* Trebuchet MCP
* Registrations, Holding MRR, trials

* In progress / Next week

* New users table from Violetta
* GA4 users journey

* Project “Experimentation”

* Completed

* New metrics (trials with filter limits)
* Bugfixes

* In progress / Next week

* Limits filter for first payments, MRR

## May 30, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019762462&usg=AOvVaw3RPPTnq4lRLudvsZ7zOO8g)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

As an experiment – let’s try to explain our progress in super-simple terms, like event a newcomer can understand the idea? Probably it could make it more transparent to the whole team as well

DQ

* Holding MRR Test Coverage

* Completed:

* Defined and estimated core data-level test coverage
* Updated SCD models for the data layers

* In progress / Next week:

* Holding MRR test coverage for core data layer

* Monte Carlo PoC

* Completed

* Scope of integration has been created and discussed

* In progress / Next week:

* MC integration

* DQ improvements

* Completed:

* Prepared full set of materials for Analytics Tech How-To demo (presentation, checklists, test templates)

* In progress:

* Tech Demo for analysts (how to write and not to write tests right now in our dbt project)

* Next week:

* DBT yaml tests grouping and scheduling investigation (wrapper)

* Registration SSoT

* Next week:

* Test the new mart\_users\_scd model

DG

Project “BOTO” (stage: BOTO for dbt tests)

* Completed
* Next week

* Announcement & Full Rollout

Project “Data Assets Certification”

* Completed

* Pilot Plan draft

* In progress/Next week

Project “Data Enrichment Optimization”

* Completed
* In progress/Next week

* Requirements doc (review in progress)

Other

* Completed

* Cognism PoC reviewed and eliminated from enrichment vendors
* Ana completed onboarding 🎉

* In progress/Next week

* Project “CLEAR” Kickoff 🧹

BI

* "Tableau Collections & Folders" Project

* (Completed) - Released Collections for Advertising Toolkit, Content Toolkit, Essential Workbooks, Growth Division, Local Toolkit, Marketing Division, Payment Solution, PLG Leadership, Product Division and Social Toolkit

* In Progress / Next Week:

* Creating Collections for Expansion, Retention and Finance

* “C-level Scorecards” Project

* Completed:

* Detailed Requirements & Project Charter
* Color blind palette investigation

* In Progress / Next Week:

* Data Source(s) plan
* Dashboard Design

* (Completed) SMB Impact Dashboard

* (Completed) Metrics Monitoring for PaySol

* Refactoring, Issues & Other

* (In Progress) Create new view in New MRR Impact dash for toolkits

WA

* (Completed) - Microsoft Ads Consent Mode compliance warning
* In Progress:

* [Bug]: GA4 events not published in their datasource
* Mouseflow issue (CI Toolkit team)
* QA TikTok Pixel Events

EX

* Project “DataChat”

* Completed

* Trebuchet MCP running locally
* VertexAI and Gemini keys are approved

* In progress / Next week

* Business metrics automation
* Vertex AI POC
* MCP -> prod. Bugfixes.
* Start working on analog of [ux.semrush.com](https://www.google.com/url?q=http://ux.semrush.com&sa=D&source=editors&ust=1768225019768710&usg=AOvVaw2WfGij5zWQQcLgC3S-yO9M) (GA4 data extractor) with vertex AI keys

* Project “Experimentation”

* Completed

* First team deployed to prod user splits based on GA4 events
* Custom metrics are deprecated
* New limits filter already in UI, Bugfixes

* In progress / Next week

* Business metrics automation
* Do presentation for analysts
* Limits filter on experiments

BDP

* "Owox pipelines replacement" Project. Data Integration

* Completed

* GA4 Data Import: We have achieved a working test configuration for the GA4 ← SFTP data upload process.

* In progress / Next week

* GA4 Data Import: The activation of the new process in PROD will be done simultaneously with disabling Data Import in OWOX, as the import cannot operate in two systems at the same time. This stage will be completed early next week.

* “Salesforce Source Data Centralization (SSoT)” Project.

* Completed

* We have prepared the loading of all 41 required tables into the MART layer (there were 47 entities initially, but 6 of them were excluded from the scope).

* In progress / Next week

* We continue to stabilize SSoT, add DQ checks and check the availability of all required fields and data.
* We are still waiting for feedback from the RevOps team after sharing the 12 tables with them last week.

* Setting up the Filonov tool for Digital Marketing

* Completed

* We have obtained a result that is suitable for analysis by the Digital Marketing team. Support from Google has confirmed that our current result is the full extent of what the Filonov tool can provide at this time. The result is currently under review by the DM team.

* Page views from Prowly HubSpot data (Prowly HubSpot CRM)

* No significant progress
* In progress / Next week

* Still checking the uploaded data, estimating the volume, and possibly to use loaded data.

* Oracle Report data integration (Prowly's CAC)

* Completed

* After several discussion sessions with the Finance IT and Business Systems Integration teams, we concluded that we won’t be able to extract reports directly from Oracle due to the relative complexity of implementation. It was decided to continue the integration with the involvement of the Business Systems Integration team.

* In progress / Next week

* We will start preparing the technical specification for BSI.

* Sources and data-marts updates:

* New Source: PySol Subscription-Intents: mart\_subscription\_intents\_\_recurring\_trigger\_attempts
* Change: Zuora source data-mart: Add new order\_id field into mart\_zuora\_\_subscription
* Bugfix: affiliate team data-mart “mart\_impact\_first\_trial\_payment”: Resolved data inconsistency issue and cleaned up deprecated fields.

DE

-Infrastructure improvements:

* In progress/Next week:

* ExternalSensor replacement
* Airflow version update (required for ExternalSensor update)

- SMB Migration

* Completed:

* Folder info gathering

* In progress/Next week

* Gathering of folders configurations (and deprecation of projects\_configurations)

- DE support

* Tasks from the channel
* Still checking the keys erased by sysadmin - we are still missing one
* Migration of collection\_apps table

* Highlighted

* Our approach to Big query quota limiting is now company-wide.

## May 23, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019774255&usg=AOvVaw1s4uihVzlAlVdDBKFb8wOn)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

As an experiment – let’s try to explain our progress in super-simple terms, like event a newcomer can understand the idea? Probably it could make it more transparent to the whole team as well

DQ

* Holding MRR Test Coverage

* Completed:

* DBT tests grouping for holding\_mrr (all tests have been grouped)
* New SCD models for test coverage metrics with models data layers classification (target, source, product, core) - done for holding\_mrr and for holding\_mrr\_daily

* In progress / Next week:

* Holding MRR test coverage for product and core data layers

* Monte Carlo PoC

* In progress / Next week:

* Holding MRR and Marketing Channels lineage evaluation for the Monte Carlo PoC

* DQ improvements

* Next week:

* DBT yaml tests grouping and scheduling investigation (wrapper)
* Tech Demo for analysts (how to write and not to write tests right now in our dbt project)

* Registration SSoT

* Completed:

* Implemented automated test coverage for the users\_registrations model (Registration SSoT)
* Developed a standardized framework for testing metrics and transformations

DG

Project “BOTO” (stage: BOTO for dbt tests)

* Completed
* In progress

* Announcement & Full Rollout (pending on TLs feedback)

* Next week

Project “Data Assets Certification”

* Completed

* Certification Criteria List

* In progress

* Pilot Planning
* Certified Data Assets Lifecycle (re-certification&de-certification)

* Next week

Project “Data Enrichment Optimization”

* Completed
* In progress/Next week

* Requirements documentation and review

Other

* Completed
* In progress/Next week

* Manual Enrichment ao May 20 (Pending on ZI side)
* Cognism POC file review (final review)
* Manual enrichment process enhancement with ZI
* Onboarding Ana

DE

-Infrastructure improvements:

* In progress/Next week:

* ExternalSensor replacement
* Airflow version update (required for ExternalSensor update)
* DWH 2.0 alignment with DPE team

- GA4 streaming light:

* In progress/Next week:

- Cost estimation for GA4 streaming re-processing

- SMB Migration

* In progress/Next week

* Solar Api migration

* Prepare data extraction for “Folder” via PubSub

-Other

* Completed

* Bring fresher data on google search console

* In progress/Next week



BI

* "Tableau Collections & Folders" Project

* (Completed) - Creating Collections for (PaySol, Growth Division, Product Division, Marketing Division)
* In Progress / Next Week:

* Internal & External communication
* Creating Collections for (Expansion Division, User Adoption)

* “C-level Scorecards” Project

* (Completed) - Basic Requirements
* In Progress / Next Week:

* Detailed Requirements & Project Charter
* Data Source(s) plan
* Dashboard Design

* SMB Impact Dashboard

* (Completed) - Dashboard development
* In Progress / Next Week:

* Documentation

* Metrics Monitoring for PaySol

* (In Progress) - Resolving remaining issues & UAT

* Refactoring, Issues & Other

* Completed:

* CookieHub dashboard refactoring
* Vendor access setting - Creating vendor specific dashboards for Exploding Topics
* Monthly Dashboard Quality Labeling
* Signup dashboard improvements

* In Progress / Next Week:

* CMO dashboard refactoring

WA

* (Completed) - Provide the number of FE & BE events for Core Trial
* In Progress:

* Microsoft Ads Consent Mode compliance warning
* [Bug]: GA4 events not published in their datasource
* Mouseflow issue (CI Toolkit team)
* QA TikTok Pixel Events

EX

* Project “DataChat”

* Completed

* Bugfixes, refactoring, small UI tweeks

* In progress / Next week

* Still no experiments in the context
* Start working on analog of [ux.semrush.com](https://www.google.com/url?q=http://ux.semrush.com&sa=D&source=editors&ust=1768225019782851&usg=AOvVaw2F1gl78Q2zQ7EJYV2LpCpj) (GA4 data extractor)
* Wait for VertexAI and Gemini keys for data extraction POC

* Project “Experimentation”

* Completed

* Feedback from POs, improve UX
* GA4 related metrics computed for 30-50 minutes and timed-out. Optimized it should solve the problem for some time.

* In progress / Next week

* Splitting users based on GA4 events

* If no feedback from dev. Teams, we will deploy to production

* Make analysts feel better:

* Add a couple of new metrics
* Improve AI analysis
* Make a tutorial

BDP

* Owox Pipelines Sunsetting

* Completed

* The final data-marts have been prepared in the following data-sets:

* enterprise-dwh-prod-tf.mart\_facebook\_ads - Facebook Ads
* enterprise-dwh-prod-tf.mart\_linkedin\_ads - LinkedIn Ads
* enterprise-dwh-prod-tf.mart\_microsoft\_ads - Microsoft Ads (ex Bing Ads)

* In progress / Next week

* GA4 Data Import: SFTP is prepared on the test environment (RC), next week we will start testing. And also we will prepare the process of saving CSV files from BQ to SFTP. At the same time, the SysOps team will be finalizing the PROD SFTP settings.

* Project “Salesforce Source Data Centralization (SSoT)”

* Completed

* We have prepared the first set of 12 tables and submitted them to the RevOps team for review

* In progress / Next week

* We continue to stabilize SSoT and prepare the remaining tables. There are 47 tables in the scope (12 of them are prepared)

* Page views from Prowly HubSpot data (Prowly HubSpot CRM)

* Completed

* Connected Fivetran and Airbyte to Prowly Hubspot. Started test data collection.

* In progress / Next week

* We will check the uploaded data together with analysts, estimate the volume and load, and possibly start preparing the Prod-grade pipeline.

* Oracle Report data integration (Prowly's CAC)

* In progress / Next week

* On May 27, the report prepared on Oracle's side will be provided for testing

* Marketo Data Mart Backfill:

* In progress / Next week

* Program Members Backfill: we will continue to recover data. Since there are restrictions on the daily loading volume, the backfilling process will be lengthy

* Source from PySol Subscription-Intents

* Completed

* Got access to the source and configured Airbyte

* In progress / Next week

* We are planning to connect a new source to provide new data to the analytics team.

* Setting up the Filonov tool for Digital Marketing

* In progress / Next week

* Together with support from Google, we are trying to get a working tool

* Sources and data-marts updates:

* mart\_oracle\_\_semrush\_items\_list\_mrr: launch time shifted to 1:30 AM UTC
* \*[raw|stg|mart]\_zuora\_\*\*: changed launch time to 12:30 AM UTC

## May 16, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019788463&usg=AOvVaw2djXaPBADTQRdR5JzvqUlS)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Completed

* Investigated dbt\_project.yml and tests groups for the dbt project, holding\_mrr tests have been grouped
* Holding MRR source and target models have been covered with tests (w/o business tests)
* DBT cleaning related to all DBT project tests “warnings”
* stg\_users layer validation and automation test coverage (as part of Registration SSoT)

* In progress

* DBT tests grouping for the dbt project
* users\_registrations validation and test automation coverage

* Next week

* New SCD models for test coverage metrics with models data layers classification (target, source, product, core)
* Holding MRR test coverage for product and core data layers
* DBT tests grouping for the dbt project
* Holding MRR and Marketing Channels lineage evaluation for the Monte Carlo PoC

DG

Project “BOTO” (stage: BOTO for dbt tests)

* Completed
* In progress

* Announcement & Full Rollout (pending on TLs feedback)

* Next week

Project “Data Assets Certification”

* Completed

* Certification criteria checklists for all levels (Business Logic, Data Sources, Dashboard)

* In progress

* Gather feedback & approve on checklists from stakeholders

* Next week

* Finalise framework, plan next steps

Project “Data Enrichment Optimization”

* Completed
* In progress/Next week

* Requirements documentation and review

Other

* Completed

* Project CLEAR charter

* In progress

* Weekly Manual Enrichment (Pending on ZI side)
* Cognism POC file review (Data reconciliation has been completed but identified issues on the Cognism matching process).

* Next week

* Onboarding Ana

DE

* Completed

* Cleaned SSH Keys Access from VMs
* Fixed MongoDB failing job
* Dparty team right now is admin of gitlab/dashboards
* Fixed oracle data ingestion desynchronization
* Gathered user permissions data from api
* Added DPA raw data from Analytics Hub to our external project
* DE support workflow design

* In progress

* Add parameters to bring newest data to GoogleSearchConsole ETL
* Research reasons of data inconsistency between product and analytics data
* Research flattening event\_params values in cl\_events\_intraday table
* (slowly) Airflow ExternalSensors Replacement

* Next week

* Airflow ExternalSensors Replacement

* Highlighted



BI

* SMB Impact Dashboard

* Completed:

* SMB Impact Dashboard (Requirements & Source)

* In Progress / Next Week:

* SMB Impact Dashboard (Dashboard)

* Tableau Structure Optimization

* Completed:

* New Tableau folder structure and mapping to workbooks is ready

* In Progress / Next Week:

* Populating Collections as a way of organizing user content
* Internal & External communication

* Executive reporting (Scorecards)

* In Progress / Next Week:

* Requirements
* Dashboard Design

* Metrics Monitoring for PaySol

* In Progress / Next Week:

* Finishing dashboard & UAT

* Refactoring & Issues

* Completed:

* Toolkit Paid Activity Dashboard – Issues

* In Progress / Next Week:

* CMO dashboard refactoring
* CookieHub dashboard refactoring

WA

* Completed

* Rockerbox Customer Support Users Flag

* In progress/Next week

* Discrepancy analysis of FE & BE events for Core Trial
* QA TikTok Pixel Events

EX

* Project “DataChat”

* Completed

* Context + redesign

* In progress / Next week

* Add experiments to the context
* Wait for VertexAI and Gemini keys for data extraction POC

* Project “Experimentation”

* Completed

* Splitting users based on GA4 events

* Calculations in dbt
* JS library modification

* In progress / Next week

* Splitting users based on GA4 events

* Test with dev. Teams on rc
* Maybe deploy to prod

* Collect feedback from POs, discuss improvements
* Deploy UX changes to prod

BDP (business data platform)

* Owox Pipelines Sunsetting

* Completed

* Data verified: Facebook Ads, Bing Ads and LinkedIn Ads: We may use data collected through Fivetran
* Fivetran will provide analyst-approved dbt models with reports for these sources.

* In progress / Next week

* Transfer the process into production and adopt Fivetran-dbt model.
* GA4 Data Import: SFTP for sending data is still being configured. Delays are due to receiving approval from the Security Team to create SFTP with access without IP restrictions

* Setting up the Filonov tool for Digital Marketing

* In progress / Next week

* We are still trying to get the configuration with credentials suitable for this tool.

* Oracle Report data integration (Prowly's CAC)

* In progress / Next week

* We plan to set up direct data-integration with Oracle reports to collect data without involving the Business System Integration team in the future.

* Marketo Data Mart Backfill:

* Completed:

* Email Activity Backfill: Data-mart is filled with April data and updated after the Marketo API limitation issue last month

* In progress / Next week

* Program Members Backfill: we will continue to recover data

* New/updated sources and data-marts:

* Completed:

* Source & Data Mart: CMP Content Shake
* Source & Data Mart: CMP Advertising Toolkit
* Data Mart: with employee PTO data for RevOps (Workday source)

## May 9, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019799009&usg=AOvVaw0uhtXX3Kx9o-BR5omZmKDU)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

DQ

* Completed

* Test coverage metric scope definition including business requirements (dedicated Confluence page has been created)
* Paysol tables test coverage - cancelled due to the migration freeze

* In progress

* DBT cleaning related to all DBT project tests “warnings”
* Holding MRR source and target models test coverage (70% accomplished)
* Sources validation for Registration SSoT (dev has been validated)

* Next week

* Holding MRR and MRR 2.0 source and target models test coverage
* Business sources (dashboard sources as a final product data sources for business level)  for MRR test coverage scope definition
* Holding MRR and Marketing Channels lineage evaluation for the Monte Carlo PoC
* Sources validation for Registration SSoT (prod tables + autotests)

DG

Project “BOTO” (stage: BOTO for dbt tests)

* Completed

* Guidelines, Runbooks, Framework updated
* Code Merged (except CI validation)

* In progress

* Announcement & Full Rollout

* Next week

Project “DAC”

* [Mike] let’s write the naming in a more explicit way?
* Completed

* Certification Criteria Conceptual List

* In progress

* Certification Criteria Validation

* Next week

Manual Enrichment

* Completed

* Semi-automated enrichment through ZI Sales application for this week’s unenriched accounts. In parallel, the manual process is still in progress.

* In progress
* Next week

Project “Data Enrichment Optimization”

* Completed
* In progress/Next week

* Architecture Review

Other

* Completed
* In progress

* Cognism POC file review

* Next week

* Draft “Housekeeping” Project Charter

DE

* Completed

* Added paysol table - fraud\_status (SP)
* Made transactions\_trimmed incremental (SP)
* Fixed a DBT wrapper bug
* Fixed CMP Trials (Thanks Aleksandr Gritsenko team)
* Usual support tasks

* In progress

* SMB: Folders pub-sub integration (SP)
* SMB: Solar api migration (SP) (may go to the next week)
* Extract prowly\_ror\_admin\_production database to BQ (SP)

* Next week

* Explore replacing Airflow sensors

* Highlighted

* Paysol migration was postponed (or even canceled)

BI

* SMB Impact Dash

* Completed:

* SMB Impact Dashboard (Requirements & Source)

* In Progress / Next Week:

* SMB Impact Dashboard (Dashboard)

* Tableau Structure Optimization

* Completed:

* New Tableau folder structure and mapping to workbooks is ready

* In Progress / Next Week:

* Populating Collections as a way of organizing user content
* Internal & External communication

* Executive reporting (Scorecards)

* In Progress / Next Week:

* Requirements
* Design

* Metrics Monitoring for PaySol

* In Progress / Next Week:

* Finishing dashboard & UAT

* Refactoring & Issues

* In Progress / Next Week:

* CMO dashboard refactoring
* Toolkit Paid Activity Dashboard – Issues

WA

* Completed

* Backend Events Health Check
* Frontend Events Health Check

* In progress/Next week

* Rockerbox Customer Support Users Flag

EX

* Project “DataChat”

* Completed

* Google Auth

* In progress / Next week

* Fix “forgetting” context

* Project “Experimentation”

* Completed

* AI calculations of experiments

* In progress / Next week

* UI Fixes, refactoring, remove Canary deploy
* Splitting users based on GA4 events

BD (business data)

* “Data Certification” “Certified Data Program”

* [Mike] NB! It’s different project vs “Data Assets Certification” project, run by DG. Pls highlight abt the goal of project.
* Completed

* Brand24 source: source export automation for Holding MRR

* Owox Pipelines Sunsetting”

* Completed

* Supermetrics → Fivetran/Airbyte. We decided to use the existing toolset and kept Digital Marketing from purchasing Supermetrics Warehouse.
* We collected data from Facebook Ads, Bing Ads and LinkedIn Ads via Fivetran.

* In progress / Next week

* Verification of collected data in collaboration with Insight Analysts
* Building ETL to obtain table structures similar to those produced by OWOX

* Setting up the Filonov tool for Digital Marketing

* Completed

* We have set up a server to run the tool. Stakeholders will be able to use it independently.

* In progress / Next week

* Finish configuring the tool. Requires obtaining specific Google Ads parameters and Credentials

* Project “Salesforce Source Data Centralization (SoT)”

* In progress / Next week

* We’ve resumed work on the project and will now gradually transfer the tables for use by the RevOps and MarTech teams.

* Project “Data Enrichment Optimization”

* In progress / Next week

* We’re planning to start designing a new architecture for Semrush user data enrichment processes

* New/updated sources and data-marts:

* Completed

* Advertising Toolkit trials: Integrated new source for Marketo
* Cancellation Reasons Form: Implemented changes to the Cancellation Form source as part of the transition to the new SMB platform
* Data Mart: For CMP Trials source

* In progress / Next week

* Data Mart: with employee PTO data for RevOps (Workday source).

Sync Topics:

* [Mike] Analytics DE Review – next Friday, pls block your calendar if willing to hear more
* [Mike] Engagement Survey – thanks for active participation, Manuel’s team is the leader completing 100% already! Would still appreciate inputs of all of you)
* [BD] Business Data Platform Reivew (right?)

## 

## 

## May 2, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019816495&usg=AOvVaw0lfl9LZdCKEYuQed1so7Ny)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* Test coverage Confluence documentation
* Pageviews count tests for MACH project

* In progress

* Sources validation for Registration SSoT

* Next week

* MRR test coverage improvement (metric alignment with business requirements)
* Currency\_exchange\_rates source freshness test
* Sources validation for Registration SSoT

DG

* Completed

* Semi-automated enrichment through ZI Sales application. In parallel, still performed manual enrichment with ZI to have point of comparison.
* Data Enrichment Optimization project charter document

* Audit of existing data quality issues document
* Audit of existing match rate issues document

* DG JIRA project sync
* Certification Framework

* Aligned on Business Logic

* Tech implementation of BOTO for dbt test

* In progress

* Audit of existing enrichment workflows document
* Cognism POC file review
* Certification Framework

* Criteria for BL and DS

* BOTO for dbt tests

* Essential Guidelines and Team Announcements

* Next week

* Review of the enriched file from ZI and request manual update to SFDC IT.
* Data Enrichment Architecture review
* Prepare Metadata for DataChat

DE

* Completed

* Ingest table with fraud data (paysol migration)
* Develop a way to generate airflow dags safely locally from dbt project
* Fires were fixed

* In progress

* Update dbt to newer version (and fix local issues as well)
* Find replacement of owox BQ<>GA4 connection
* Solar Api migration
* Paysol migration
* Gathering user permissions data

* Next week

* Rollover from current week (short week with End of the world Blackout on Monday, airflow fire tuesday, thursday Spanish holiday.

BI

* Completed



* In progress



* Next week



WA

* Completed
* In progress
* Next week

EX

* Project “DataChat”

* Completed

* Project setup, CI/CD, k8s, docker
* Gitlab repo [https://gitlab.semrush.net/analytics-team/datachat](https://www.google.com/url?q=https://gitlab.semrush.net/analytics-team/datachat&sa=D&source=editors&ust=1768225019825983&usg=AOvVaw17UBReLLKITHvNzMXd_HUH)
* Internal hosting [https://data-chat.rc-k2.semrush.net/](https://www.google.com/url?q=https://data-chat.rc-k2.semrush.net/&sa=D&source=editors&ust=1768225019826341&usg=AOvVaw2m-LzT3D4aZm3mT4o5fyhO)

* In progress / Next week

* Make UI better
* Add experiments to context
* Develop MCP for trebuchet

* Project “Experimentation”

* Completed

* POs requests
* Bugfixing

* In progress / Next week

* Adhock DBT metrics
* Automatic cleaning and archiving of old experiments
* AI Calculation of stopped experiments

BD (business data)

* Completed



* In progress



* Next week/weeks



## 

## Apr 25, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019828923&usg=AOvVaw1s0ZdM8KYGYiA1FKUIjYCv)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* Test coverage estimation for all SLA sources including MRR tables
* dbt\_project.yml grouped tests without airflow tasks reanimation
* Voyantis data test coverage
* Test automation for the source tables of the Toolkit Paid Activity dashboard

* In progress

* Test coverage estimation Confluence documentation
* ​​Monte Carlo use case scenarios collection

* Next week

* MRR test coverage improvement (metric alignment with business requirements)
* Paysol tables test coverage
* Currency\_exchange\_rates source freshness test
* Sources validation for Registration SSoT

DG

* Completed

* Performed manual extract and file preparation for manual ZI enrichment.
* Provided SFDC segmentation match rate status to Sales IT.
* Assisted Sales IT investigation on an account missed to be unenriched.

* In progress

* Mind Map for Business Logic Certification (Certification Project)
* Data Enrichment Optimization project charter
* Audit of the current enrichment workflows. (Enrich Essential, Manual enrichment, manual GTM coverage update, and DWH enrichment).
* Review of the enriched file from ZI and request manual update to Sales IT.

* Next week

* Run through with ZI on list upload process and how to use Enhance functionality in ZI Sales application.

DE

* Completed

Upgraded SQL Cloud Postgres instances, added a read-only replica, analytics api switched to the new replica.

Added monitoring and alerting for Airflow Redis virtual machine.

* In progress

Gathering user permissions data

* Next week

BI

* Completed

* Spotlight Budget dashboard fix
* Local Unit Overview improvements
* Upgrade Sign-up dashboard [dash development]

* In progress

* Tableau Collections implementation
* CMO dashboard refactoring
* Executive reporting (Scorecards)

* Next week

* Dashboard certification design

WA

* Completed
* In progress
* Next week

EX

* Completed
* In progress  
  [https://gitlab.semrush.net/analytics-team/datachat](https://www.google.com/url?q=https://gitlab.semrush.net/analytics-team/datachat&sa=D&source=editors&ust=1768225019834667&usg=AOvVaw1GEh7fipUpDfJizJXvy59t)
* Next week  
  Testing, Bugfixes, Refactoring

BD (business data)

* Completed

* Documentation: [Data Extraction Policy: Selection Guide for Data Engineers](https://www.google.com/url?q=https://kb.semrush.net/display/EDWH/Data%2BExtraction%2BPolicy%253A%2BSelection%2BGuide%2Bfor%2BData%2BEngineers&sa=D&source=editors&ust=1768225019835178&usg=AOvVaw1giSbebqRim0o4a5aWW6MA)
* Integrate new source for Marketo: Content Paywall Advertising Toolkit trials

* In progress

* New Source: AppCenterMonetizationInternalService (gRPC service)
* New Source: Brand24: source export automation
* Data Mart: with employee PTO data for RevOps (Workday source).
* Data Quality: Setting up generic technical DQ checks for RAW, STG layers
* Data Migrations: Recruitee data migration assistance

* Next week/weeks

* Resume the [Salesforce data centralization project](https://www.google.com/url?q=https://rhythm.semrush.net/bet/42824&sa=D&source=editors&ust=1768225019836037&usg=AOvVaw2a7Vpr2nsVe1bdzBqibLJS) (we have to make a decision)
* Data Mart: For CMP Trials source
* Supermetrics

## Apr 11, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019836435&usg=AOvVaw2HbxBZ4Pkj8hXlgMTShpCP)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* holding\_mrr new tables test coverage
* Monte Carlo questionnaire for the next session
* dbt\_project.yml grouped tests airflow tasks verification
* Toolkit Paid Activity dashboard testing
* Basic tests for Pre-MRR test (MRR 2.0 source tables testing)

* In progress

* dbt\_project.yml grouped tests without airflow tasks ungrouping and enabling
* Test coverage estimation approach using DG metadata tables
* Business Rule Tests for Pre-MRR Tables

* Next week

* Test coverage estimation approach using DG metadata tables
* Paysol tables test coverage
* Monte Carlo monitors number evaluation
* Voyantis data test coverage
* Test automation for the source tables of the Toolkit Paid Activity dashboard

DG

* Completed

* Weekly manual enrichment activity with ZI

* In progress

* Data Enrichment Optimization Project Charter
* Data review with D&B and Cognism
* Manual enrichment update with SFDC

* Next week

* Data Advisory session with ZI

DE

* Completed

* Write documentation on future staging infrastructure proposal (costs + repository structure)
* Added a new feature to send domains via PubSub to java domain crawler.
* Created a new corporate\_minions\_scd table after several columns were removed from the old one by the developer team.
* Now EL tool supports new versions of Mysql with new driver
* New Table ala\_spending\_by\_campaign

* In progress

* Setting up staging environment for POC
* Upgrade SQL Cloud Postgres 12 instances
* Update dbt version
* Populate airflow metadata to BigQuery table description

* Next week

* Setting up staging environment for POC
* Gather user permissions data from nexus team API

BI

* Completed

* Creating Collections recommendation
* Transfer All Monthly Metrics view (NUMRR) to new source

* In progress

* CMO dashboard refactoring
* Overview for Sign-up dashboard [requirements gathering + prototype]
* Improvements for Sign-up dashboard

* Next week

* Executive Reporting Design
* Metric Monitoring dash for PaySol
* Dashboard certification design

WA

* Completed
* In progress
* Next week

EX

* Completed
* In progress

SECRET PROJECT IS COOKING

* Next week

BD (business data)

* Completed

* Upgraded Airbyte from version 0.63.8 to 1.4
* Moved Airbyte configuration to Terraform
* Adaptation of source changes:

* Semrush Content Paywall - API changes
* Payment Solution Services: is\_first flag

* In progress

* Migration of Legacy processes related to Marketo into the data platform
* Setting up generic technical DQ checks for RAW, STG layers

* Next week

* Brand24 source: source export automation
* Data Mart with employee PTO data for RevOps (Workday source).
* Integrate new source for Marketo: Advertising Toolkit trials
* Quote to Cash Data Integrations: Zuora refunds data

## 

## Apr 4, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019843080&usg=AOvVaw3RB29x7ppgDzsgLtK5oM11)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* Implemented recency test for transactions
* Created DQ Template for Tables Certification
* data-paradise-20 tests with no airflow tasks fix
* Marketing, stork40, daily report, holding\_mrr tests fixes

* In progress

* Monte Carlo demo session review and highlights for the next session preparation
* holding\_mrr new tables test coverage
* Pre-MRR test (MRR 2.0 source tables testing)

* Next week

* Elementary Data comparison with Monte Carlo
* Grouped tests review for respective airflow tasks
* Toolkit Paid Activity dashboard testing
* Test coverage data collection

DG

* Completed

* Dbt tests metadata

* In BQ datamart
* In Data Catalog

* Safe-deleted CL727 sharded tables

* In progress

* Certification Framework

* Next week

* BOTO for dbt tests

DE

* Completed

* Fake dbt models have full refresh disabled by default
* Foursquare ingestion
* Deployed a new cl\_events\_intraday table without bot users
* Set up integration BigQuery to Airtable

* In progress

* Permissions cleaning (almost completed)

* Next week

* Start work on staging environment

* (optional: if any help from other functions needed)
* Highlighted

BI

* Completed

* Communication template & process

* In progress

* Creating Collections recommendation
* CMO dashboard refactoring
* CookieHub dashboard refactoring
* Metrics Monitoring Dash for Pay Sol

* Next week

* Sign-up Executive Overview
* Executive reporting template for Daily Reports

WA

* Completed
* In progress
* Next week

EX

* Completed  
  B
* In progress
* Next week

Business Data Platform Team

Transition period: April

* Completed

* We've moved

* In progress

* Changing the operating model
* Reconfigure the infrastructure to be able to continue working with colleagues who have not moved with us
* Migration of Legacy processes related to Marketo into the data platform
* Recruitee data migration
* Quote to Cash: Data Integrations (SFDC, Zuora, IronClad)

* Next week

* Continuing to migrate legacy Marketo processes to the data platform
* Continuing to change the operating model

Topics to discuss:



## 

## Mar 28, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019848717&usg=AOvVaw0MNuyEt04YS_JWv_lEYZMj)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* Testing of new table `semrush-com.owox\_streaming\_ga4.intraday\_temp` filtered from bots
* Initial version of evaluation of Monte Carlo for Data Quality
* Marketing, stork40 tests fixes
* Units overview dash

* In progress

* Pre-MRR test (MRR 2.0 source tables testing)
* Create DQ Template for Tables Certification

* Next week

* Pre-MRR test (MRR 2.0 source tables testing)
* Elementary data: owners, tags and test types simulation

DG

* Completed

* Archived 500+ tables in CL727

* In progress

* Certification Project
* Collecting dbt tests metadata

* Next week

DE

* Completed

* External sources were described
* Start to collect logs of removed tables (will collect other table usage logs too)
* Fix jira etl
* Streamline Data Engineering request process (new channel and bot)
* Disable dbt.sh run command

* In progress

* Research of paysol tables downstreams
* Big query permissions adjustment to avoid accidental table destruction

* Next week



* (optional: if any help from other functions needed)

* Highlighted

* Find a way how to detect connected google sheets

BI

* Completed

* Archive Stale Content
* Change Seamless purchase dash sources
* BI Jira cleanup and setup for Sprints
* Testing and fixing new page for Units Overview dash(from BI side)

* In progress

* Metric Monitoring Dash for PaySol
* CMO Dashboard refactoring
* CookieHub dashboard refactoring

* Next week

* Creating Collections Recommendation
* Executive Scorecards requirements

WA

* Completed
* In progress
* Next week

EX

* Completed

* In progress
* Next week

Topics to discuss:



## 

## Mar 21, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019853880&usg=AOvVaw2N-R4S-f4a-mSJrpCAlxLB)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* Units Overview dashboard (new tabs) testing (UI + data sources autotests)
* Marketing new tests:

* MACH new channels rows count monitoring tests
* data absence tests in marketing tables with costs
* weekly unit metrics - new users MRR box plot tests

* Transaction tables (in data-paradise-20.finance), discussed during the incident review meeting, have been covered with timeliness tests
* Marketing, stork40, churn tests fixes

* In progress

* Pre-MRR test (MRR 2.0 source tables testing)
* Elementary data: owners, tags and test types simulation

* Next week

* Pre-MRR test (MRR 2.0 source tables testing)
* Create DQ Template for Tables Certification

DG

* Completed

* Slack Alert Update
* Certification Project and Framework Outlined
* Confirmed certification criteria for dash level

* In progress

* Discuss & Confirm criteria for Data Sources and Business Logic

* Next week

* Tests in dbt - metadata collection

DE

* Completed

* Static page for linting sql is [up](https://www.google.com/url?q=https://analytics-team.pages.semrush.net/dbt/linter.html&sa=D&source=editors&ust=1768225019856657&usg=AOvVaw2TWoBDbDUo1t4w_J88nrRl)!
* Created a new table for stork40 in Clickhouse

* In progress

* Ads collection plan is in progress
* Filtering GA4 streaming table from bots.

* Next week

* Reload yahoo daily report from scratch
* Update java crawler to send domains via PubSub

* (optional: if any help from other functions needed)

* We are under a lot of fire

* Highlighted

BI

* Completed

* Toolkit Activity Dashboard(will be on production on Monday)
* Spotlight 2025 Event Budget Dash
* Workbook to new folder structure mapping
* Transfer All Monthly Metrics view (NUMRR) to new source (Now in testing)

* In progress

* CMO Dashboard refactoring
* CookieHub dashboard refactoring
* Metric Monitoring Dash for PaySol

* Next week

* Archive Stale Content
* Deploy new Tableau structure

WA

* Completed
* In progress
* Next week

EX

* Completed
* In progress
* Next week

Topics to discuss:

* Not only 2 newcomers – let’s discuss more!

## Mar 14, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019859193&usg=AOvVaw0_AIwRQmdqlOucwMkOWnou)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* MACH new channels timeliness tests
* Opportunity Id NULLs test (this week [incident](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2499&sa=D&source=editors&ust=1768225019859963&usg=AOvVaw1BvV5vr-rnwqkw3EYuc8YB) with daily report)
* MRR limit attribution tests (related to the last week [incident](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2697&sa=D&source=editors&ust=1768225019860156&usg=AOvVaw0Zka2LWj16GRy8aSM871zk) with duplicates in MRR)
* holding\_mrr, finance and marketing, finance, stork40 tests fixes

* In progress

* MACH new channels rows count monitoring tests
* Elementary data: owners, tags and test types simulation

* Next week

* MACH New channels test coverage
* Units overview dashboard testing
* pre-MRR calculations test coverage
* Marketing unit metrics - new users box plot tests

DG

* Completed

* Updated KB autodocumentation to allow publishing documentation for datamart tables created in dbt using “table\_copy” materialization.
* Updated on-boarding process to include DG processes.

* In progress

* Certification Framework - discussing criteria w/ teams

* Next week

---

DE

* Completed

* Updated java domain crawler to save raw html pages on bucket.
* Disabled duplicated loading of billing\_invoice\_custom
* Added bank\_identification\_number\_black\_list extraction from paysol

* In progress

* Update ga4 clustered streaming for filtering out bot users.
* Upgrade version of old Cloud SQL Postgres instances.
* Research and document all external sources of our dwh
* Figuring out how to replace Owox Pipelines (they are being discontinued)

* Next week

* Copy Rockerbox tables to datamart
* Update java domain crawler to send additional domains for scraping via PubSub topic.
* Figuring out how to replace Owox Pipelines (its going to take some time 🙁)
* Figure out how to revoke permissions for analytics-external prod project
* Create plan for paysol migration

* (optional: if any help from other functions needed)
* Highlighted

BI

* Completed

* Audit of C-level subscribed reports
* Sign up flow dashboard refactor(Growth team)

* In progress

* KB describing current distribution process
* Process for vendors accessing Tableau
* New Tableau structure - Top Level folders recommendation
* Spotlight Budget Dash (Nadine)
* Transfer All Monthly Metrics view (NUMRR) to new source (Marketing team)
* Toolkit Activity dashboard(Product team)
* Metric Monitoring Dash  (PaySol)

* Next week

* New Tableau structure - testing by matching with workbooks
* Onboarding vendor to Tableau

WA

* Completed
* In progress
* Next week

EX

* Completed

* In progress

* Next week

Topics to discuss:

## Mar 7, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019865501&usg=AOvVaw3Uq0rnWcOFhM8U5rEQPHV6)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* Test for duplicates in numrr calculation
* Daily metadata collection into SCD models for rows count and updates monitoring (covered: data-paradise-20, analytics-external-prod-tf)
* Timeliness tests approach and macros for regular, scd, partitioned by date, and sharded by date tables (tests + docs, shared with Dparty for a feedback)
* Timeliness tests for data-paradise-20.acquisition.GoogleSearchConsole\_

* In progress

* New channels test coverage
* Timeliness tests for MACH and recent requests about external data updates monitoring (voyantis, olaf\_prod)

* Next week

* mrrHawk, applications, holding\_mrr limit attribution tests (related to the last incident with duplicates in MRR)
* MRR 2.0 pre-calculation tests to verify data sources before new MRR models run (as a part of mrr20 test coverage)
* Elementary Data package POC: different test types setup
* New channels test coverage

DG

* Completed

* Created task for Admins to improve MR notification bot
* Collected requirements for CertFramework from various teams

* In progress

* Certification Framework outline document

* Next week

* Agree upon Certification Approach

---

DE

* Completed

* Added new fields to Datos Hubspot tables
* Fixed and optimised the domain loading job for better performance.

* In progress

* Paysol data sources research
* Upgrade root domains java crawler to allow saving raw pages on gcp bucket.
* Look for the best solution for ga4 streaming to get rid of bot users and add usability.
* Upgrade Cloud SQL Postgres instance
* Fix infrastructure after Anna’s last day

* Next week
* (optional: if any help from other functions needed)

* What is our part in [Salesforce source data centralization](https://www.google.com/url?q=https://rhythm.semrush.net/bet/42824&sa=D&source=editors&ust=1768225019869154&usg=AOvVaw01WGE7tOYfnj58KAYeoEKN)? ([Slack discussion](https://www.google.com/url?q=https://semrush.slack.com/archives/C011Q58AZKR/p1741175155227029&sa=D&source=editors&ust=1768225019869271&usg=AOvVaw39pZozqn59j2dCSKH2Hvnb))

* Highlighted

BI

* Completed

* Add new charts into Jira Tickets Dash(Kostya and Danil)

* In progress

* Spotlight Budget Dash (Nadine Drognitz)
* Transfer All Monthly Metrics view (NUMRR) to new source (Marketing)
* Sign up flow dashboard refactor (Growth)
* New structure for Tableau Server
* Toolkit Activity dashboard (Product)

* Next week

* QA Testing Toolkit Activity dashboard (~12.03 )
* Vendor access to Tableau (with IT support)

WA

* Completed
* In progress
* Next week

EX

* Completed

* Add time window explanation
* Fixed bug with user count on UI
* Integrate copy data from PostgreSQL to BigQuery with Celery
* Fix sentry auth token

* In progress

* Add two new metrics UA events and UA users
* Migration from Webpack to Vite

* Next week

Topics to discuss:

## Feb 28, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019871386&usg=AOvVaw2No9UZ-0Brj_r0NBagBaCQ)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) 

DQ

* Completed

* holding\_nrr\_grr generic tests & holding\_mrr rows count tests have been fixed
* olaf data yml tests have been moved to sql tests due to wrapper logic
* all models with BOTO changes & models with yml tests have been reviewed for airflow tasks existence and execution
* MRR backlog tasks have been reviewed and groomed
* Additional Plot box tests have been added for New marketing channels project and entire test coverage plan created.

* In progress

* mrr20 test coverage
* analytics-externa-prod-tf daily metadata scd models for timeliness tests due to recent complaints about data updates

* Next week

* Elementary Data package POC: different test types setup
* Timeliness tests for data-paradise-20.acquisition.GoogleSearchConsole\_ and analytics-external-prod-tf.voyantis
* mrr20 test coverage
* Tests creation for New marketing channels project

DG

* Completed

* BOTO for all dbt models configured
* Slack Alerts (part 1)
* Updates to DC

* In progress

* Certification Framework

* Next week

DE

* Completed

Fixed Airflow issue that made it impossible to remove any pipeline.

* In progress

Upgrade Cloud SQL Postgres 12 instances

Fix logic of the new domain crawler

Implement local airflow for testing

GCP cost increases exploration

* Next week
* (optional: if any help from other functions needed)
* Highlighted

BI

* Completed

* Funnel dashboard for Social
* Damage Control view for Reliability Overview

* In progress

* Toolkit Activity dashboard
* Sign up flow dashboard refactor
* Spotlight Budget Dashboard
* Distribution of dashboards according to the new folder structure

* Next week

WA

* Skipped for this week

EX

* Completed
* In progress
* Next week

* Transfer metric UA Events (GA3, old Streaming) events to DBT

Topics to discuss:

* [Mike] CEO change

## 

## Feb 21, 2025 |

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* [MD\_NRR] Source table and dashboard testing
* Marketing tests update & support (stork40, unit\_costs, md holding\_nrr\_grr)
* Elementary Data package graveyard setup for its further DQ needs review

* In progress

* [MACH] Creating test for monitoring "unknown" campaigns
* mrr20 test coverage

* Next week

* [MACH] Test new channels
* MRR related backlog tasks grooming
* Elementary Data package POC: different test types setup

DG

* Completed

* Configured BOTO for CL727 and Export
* Fixed searchability bug in Data Catalog and deprecated old system\_info pages

* In progress

* BOTO Alerts (DEAID required 😀)
* BOTO for Semrush-com

* Next week

* Certification Framework

DE

* Completed

* Get Ironclad tables from SF (for dparty)

* In progress

* Create a new GA4 streaming table with event params as separate columns
* Pipeline to push data to GA (for Violetta)

* Next week

* Upgrade SQL Cloud for user segments service (upgrade version, increase memory, add replica)
* Updated Jupyterhub deployment to us-region

* (optional: if any help from other functions needed)
* Highlighted



BI

* Completed

* Switch marketing dashboards to permanent sources based on stork 4.0
* Funnel dashboard for Social(BI test)

* In progress

* Damage Control view for Reliability Overview
* Spotlight Budget Dash
* Toolkit Activity dashboard
* New Tableau Structure

* Next week

WA

* Completed



* In progress



* Next week



Blocked:

EX

* Completed



* In progress

* Fix bugs with 3+ groups for users (edit + charts)

* Next week

* Add another metric (Events) to dbt

Topics to discuss:



## 

## Feb 14, 2025 |

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* MRR metric test coverage

* holding\_mrr (fully covered but for incident excluded 4 models tests out of 20)
* mrr20 in prod projects (daily metadata + generic tests)

* Elementary package for testing purposes is reviewed and enabled by DE team (many thanx to Anya) + manifest parsing script draft has been tested
* cu\_short and pseudoid\_userid\_short tables comparison research (Marketing team request)

* In progress

* mrr20 test coverage
* MACH project (new channels collection based on GA4 owox streaming) testing

* Next week

* mrr20 test coverage & mrr related backlog tasks grooming
* Elementary package audit data review
* Update marketing calculation tests

DG

* Completed

* Configured MR approval workflow & BOTO validation job (big one)
* Configured BOTO for Tableau and Analytics-tests

* In progress

* BOTO for CL727, Export and Semrush-com
* Slack Alerts using BOTO

* Next week

* Finish w/ BOTO (dbt)

DE

* Completed

* Created a new potential bot user function with updatable list of bot patterns
* Created service account for elementary (for Pasha S.  and Nikita Kot.)
* Fixed owox pipeline for facebook
* Updated wire event-messages pipelines with new fields (for Agata)
* Fix holding\_mrr

* In progress

* Create a new GA4 streaming derived table with event params as columns dynamically adding

* Creating pipeline for sending data to owox (for Violetta)
* Copying ironclad tables from sf (for Nikita Kud.)
* RockerBox: store reports before sending

* Next week

* Requests from DQ

* (optional: if any help from other functions needed)
* Highlighted

* Multiple issues with Airflow dag creation

BI

* Completed

* Refactoring Feature Adoptionted
* Monthly Dashboard Quality Labeling

* In progress

* Damage Control view for Reliability Overview
* Funnel dashboard for Social
* Activity dashboard with new DS for Local Unit
* Renaming of daily reports

* Next week

WA

* Completed

* CookieHub Add Canada // PIPEDA to GTM config

* In progress

* Set up tracking for DemandGen LPs on different platforms

* Next week

* Send BE Events for Trials & Payments
* Send Social Unit - FE Events

Blocked: Send LBPM flag of users to GA4

EX

* Completed

* In progress

* Next week

* Test linear graphics instead of bars
* More metrics in airflow + dbt

Topics to discuss:

* [Mike] Oleg’s comments on Tableau / Daily Rep

* Oleg is a bit lost

* [Mike] UX.semrush.com

## Feb 7, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019886364&usg=AOvVaw1QLe6Eq32PoZwxc5h5LfI_)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* DQ/QA improvements roadmap update (decomposition for testing framework)
* Holding MRR timeliness tests (for Holding MRR models update monitoring)
* 'Holding Daily Report' Dashboard testing
* Salesforce outdated tasks clarification (backlog grooming)
* Create an article for Stork4.0 test in KB

* In progress

* MRR metric test coverage
* Correctness comparison: UA (cu\_short) vs GA4 (pseudoid\_userid\_short) tables

* Next week

* MRR metric test coverage
* Investigate DBT test coverage approaches
* Investigate test coverage for [MACH] Marketing Channels project

DG

* Completed

* Configured & Announced BOTO for External, Projects, Datamart and Trebuchet
* Approved BOTO for Tableau

* In progress

* Configure & Announce BOTO for Tableau
* Configure MR Approval Workflow

* DE Help Required!

* Next week

* Find Owners for Analytics-Tests, Export, Semrush-com, CL727
* BOTO Alerts

DE

* Completed

* Reload historical data of RockerBox ([AAI-2614](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2614&sa=D&source=editors&ust=1768225019888828&usg=AOvVaw1rsTVoKRO8CmHEEKqMMl9D), Simon Putnikov)
* Archive table data-paradise-20.finance.additional\_payments\_limits ([AAI-2612](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2612&sa=D&source=editors&ust=1768225019889038&usg=AOvVaw2I9md7gv8qZzkAKME96A40), Simon Putnikov)
* Update users list at bq\_jobs  ([AAI-2623](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2623&sa=D&source=editors&ust=1768225019889214&usg=AOvVaw24JHRHwj6Wu5Qw_OXZpzsE), Simon Putnikov)
* Fix/Reload data-paradise-20.product.activities\_ table due to api issue ([AAI-2596](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2596&sa=D&source=editors&ust=1768225019889413&usg=AOvVaw0ayrT28DjnmrgwhZJjSn_6), Natalia Karpova)
* Export data from Datos Hubspot ([AAI-2584](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2584&sa=D&source=editors&ust=1768225019889575&usg=AOvVaw2KCudIANjWyw4cV5cNsuRm), Natalia Karpova)
* Extract contact properties from Prowly Hubspot ([AAI-2512](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2512&sa=D&source=editors&ust=1768225019889743&usg=AOvVaw2gT8NkWQ8IFf5da-vSMmXY), Natalia Karpova)
* Fix dataparadise.payments2021 ([AAI-2608](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2608&sa=D&source=editors&ust=1768225019889894&usg=AOvVaw0MVYWy8dZGY1KJePrEDyoL), Manuel Garrido)
* Fix task data-paradise-20.slack.deploy\_log\_messages ([AAI-2615](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2615&sa=D&source=editors&ust=1768225019890079&usg=AOvVaw2HD7GOptS9kRgi_m2yl3B6), Manuel Garrido)
* Fix dataparadise.listing\_management\_raw\_exports ([AAI-2607](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2607&sa=D&source=editors&ust=1768225019890268&usg=AOvVaw3MX8-YU2esos7civTRW3jQ), Manuel Garrido)
* Fix task listing\_management\_raw\_exports\_analytics\_mongo ([AAI-2620](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2620&sa=D&source=editors&ust=1768225019890451&usg=AOvVaw3rdWMiNCt1Z3BE1qt7cLmB), Manuel Garrido)

* In progress

* Automate DE weekly worklog summary ([AAI-2613](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2613&sa=D&source=editors&ust=1768225019890675&usg=AOvVaw3HBi1izVgCM88YUQILC_qd), Simon Putnikov)
* RockerBox: change sql logic and reload data ([AAI-2634](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2634&sa=D&source=editors&ust=1768225019890845&usg=AOvVaw3-TGi55J0Xyn_yvNxNu-gK), Simon Putnikov)
* add field ZI\_Employee\_Count\_2\_\_c and ZI\_Parent\_Employee\_Count\_2\_\_c to Account ([AAI-2618](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2618&sa=D&source=editors&ust=1768225019891069&usg=AOvVaw2DiRjRqiKIhEQ41DwO3zXC), Anna Obyskalova)
* hotfix pipeline dbt ([AAI-2622](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2622&sa=D&source=editors&ust=1768225019891216&usg=AOvVaw0Z0_dKub_iGZ6M__e57Zqq), Anna Obyskalova)
* R&D: dbt\_wrapper ([AAI-2581](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2581&sa=D&source=editors&ust=1768225019891353&usg=AOvVaw0OF3gnvY7pVXpjRlgANmoZ), Simon Putnikov)
* Deprecate airflow task centering-land-727\_\_Marketplace ([AAI-2621](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2621&sa=D&source=editors&ust=1768225019891521&usg=AOvVaw1HRm2PKa8wPfJZjNCEAW2B), Manuel Garrido)
* Deprecate airflow task small-dashboards.ImpactHero  ([AAI-2619](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2619&sa=D&source=editors&ust=1768225019891709&usg=AOvVaw1cyjmyoEnvjvFErY6qZ179), Manuel Garrido)
* Investigate DBT dependencies  ([AAI-2577](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2577&sa=D&source=editors&ust=1768225019891860&usg=AOvVaw2e0JVC_nOUFI6mpZqZncrd), Simon Putnikov)

* Next week

* Reduce the number of unique metrics with unique IDs ([AAI-2567](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2567&sa=D&source=editors&ust=1768225019892090&usg=AOvVaw0oQus-8ByOJmjjL04eGSHZ), Simon Putnikov)

* (optional: if any help from other functions needed)
* Highlighted

* Interviewed two candidates (tech)

BI

* Completed

* Refactoring Feature Adoption(BI testing )
* Limits intersections for Churn Penguin (BI - testing)
* Holding MRR Daily Report dashboard

* In progress

* Reliability Overview
* Funnel dashboard for Social

* Next week

WA

* Completed

* [WAE-20](https://www.google.com/url?q=https://jira.semrush.net/browse/WAE-20&sa=D&source=editors&ust=1768225019893114&usg=AOvVaw1zYZnO7Ox-3yI9uJyptd02) CookieHub setup for new assets

* In progress

* GA4 Data Import setup for is\_local\_business parameter
* [WAE-19](https://www.google.com/url?q=https://jira.semrush.net/browse/WAE-19&sa=D&source=editors&ust=1768225019893475&usg=AOvVaw0J89ayEb2JFxrJ7Czl0Cto) Add Triggers for Standalone CI purchase
* [WAE-2](https://www.google.com/url?q=https://jira.semrush.net/browse/WAE-2&sa=D&source=editors&ust=1768225019893666&usg=AOvVaw35YS7kVwsSWryzbLH9hgL5)  Provide the number of FE & BE events for Core Trial
* Troubleshooting Mousflouf pages

* Next week

* CookieHub Update Template and Canada setup

EX

* Completed  
  [Released GA4](https://www.google.com/url?q=https://semrush.slack.com/archives/C02NHM9GCKG/p1738840901220999&sa=D&source=editors&ust=1768225019894127&usg=AOvVaw35M2fnejGaHAsUqiRfgsKJ) metric for trebuchet AB testing tool  
  Bugs appeared, fixed them
* In progress

Interviews, meta-analysis, discussions of roadmaps

* Next week

* Add page\_path parameter to GA4 metric
* Add a new metric to track number of users in experiment with certain event (GA4\_users)
* Add a new metric to compute conversions from users with certain GA4 event to trials (cr\_ga4\_trials)

Topics to discuss:

## 

## Jan 31, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019895228&usg=AOvVaw3B2IX0A91TlG4QvG8mF2WL)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* Holding MRR & Holding MRR daily test coverage
* Marketing automated tests update (transition to Stork 4.0)
* Daily Weekly Report alerts monitoring
* Backlog Review

* In progress

* 'Holding Daily Report' Dashboard testing
* Salesforce outdated tasks clarification
* MRR\_20 test coverage
* DQ/QA improvements roadmap update (decomposition for testing framework)

* Next week

* MRR\_20 test coverage
* MRR\_hawk20 test coverage

* Postponed

* DQ Sandbox setup (dbt\_expectations has been included into main dbt project, other tools review will be included in the improvements as a part of testing framework)

DG

* Completed

* Approved BOTO for External
* Replaced CL727 Users reference in dbt models

* In progress

* BOTO for Tableau & CL727
* Announce & Configure BOTO for Projects, Datamart (and External?)
* MR Workflow:

* Awaiting Mike for approval
* Tech Task is ready

* Next week

* Rollout MR Workflow (dep’s on DE capability)

DE

* Completed

* Updated cookiehub data
* added permissions for shared queries in bq
* Fixed failing dataparadise etl scripts (graphql, chorus)

* In progress

* Export data from Datos Hubspot

* Next week
* (optional: if any help from other functions needed)

* Make a good description for DEs in tasks, preferably merge requests. It will make it faster, easier, and remove communication problems. Be as specific as possible.

BI

* Completed

* Transfer CTA Stork Dashboard to Stork 4.0
* CMO Dashboard: added First Payments block and rearranged other blocks.
* Fix DS for Datasource dash (internal analytics)
* Refactoring Feature Adoption (in test with Unit)
* Daily Holding MRR Report (QA testing)

* In progress

* Limit intersections in Churn Penguin

* Next week

WA

* Completed

* [WAE-3](https://www.google.com/url?q=https://jira.semrush.net/browse/WAE-3&sa=D&source=editors&ust=1768225019899514&usg=AOvVaw3nOE4lD4sbxhG-HgvUmBoV) Provide the number of FE & BE events for .Trends
* [WAE-1](https://www.google.com/url?q=https://jira.semrush.net/browse/WAE-1&sa=D&source=editors&ust=1768225019899707&usg=AOvVaw1aCRtFacpKq9tL_Kx6ET8L) Prepare for the Local campaign launch
* [WAE-18](https://www.google.com/url?q=https://jira.semrush.net/browse/WAE-18&sa=D&source=editors&ust=1768225019899869&usg=AOvVaw1L3MHvIjzXyRR8q-N0zJiP) DemandGen tracking setup

* In progress

* [WAE-20](https://www.google.com/url?q=https://jira.semrush.net/browse/WAE-20&sa=D&source=editors&ust=1768225019900100&usg=AOvVaw3Vxl_KD06QpjEYIYu2cU4-) CookieHub setup for new assets
* [WAE-19](https://www.google.com/url?q=https://jira.semrush.net/browse/WAE-19&sa=D&source=editors&ust=1768225019900270&usg=AOvVaw0tqXsOzAZ13PP7GfyUr3D3) Add Triggers for Standalone CI purchase
* [WAE-2](https://www.google.com/url?q=https://jira.semrush.net/browse/WAE-2&sa=D&source=editors&ust=1768225019900440&usg=AOvVaw1TvvbQbVkaF01ytcu_VoqW)  Provide the number of FE & BE events for Core Trial
* Troubleshooting Mousflouf pages

* Next week

* [WAE-4](https://www.google.com/url?q=https://jira.semrush.net/browse/WAE-4&sa=D&source=editors&ust=1768225019900749&usg=AOvVaw3a0wjKiQ2mbZyrL70_k7Hl)  Careers site identify users by utms
* (Most Likely) Requested by cross domain setup between careers and workday

EX

* Completed

* Trebuchet: data transfer pipeline BigQuery -> Postrgres in prod
* Dbt: Learned how to handle JSON nulls properly in BigQuery

* In progress

* Trebuchet: new bugs for the GA4 metric. It didn’t showed up

* Next week

* Mon and Tue Marat is on PTO.
* Trebuchet: fix the UX bug - unable to edit dates in experiments
* Update backend libs and deps

Topics to discuss:

-        NO

## Jan 24, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019901937&usg=AOvVaw0RPE7vXAFCtCRpLY-Bm1we)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* Stork 4.0 testing (marketing\_unit\_metrics, CPDash, CMO dashboard tables)
* Daily Weekly Report box plot tests thresholds have been updated
* Marketing Unit Costs Daily test output has been fixed
* Holding MRR snapshots tests are on prod
* Backlog has been partially reviewed

* In progress

* Marketing automated tests update (transition to Stork 4.0)

* Next week

* MRR metrics tasks from backlog (MRR test coverage improvements)
* Salesforce tasks from backlog clarification with insights team
* Marketing automated tests update (transition to Stork 4.0)
* Rest of the backlog review
* DQ/QA improvements roadmap update (decomposition for testing framework)

* Postponed

* DQ Sandbox setup (next week we are going to prepare requirements for dbt test project for new tooling review)

DG

* Completed

* Approved BOTO MR Workflow
* List of CL727 Users dependencies to deprecate
* Bugfix in DC: tables w/ no configs are now not documented

* In progress

* Deprecate CL727 Users dependencies (in models DG own)
* Deprecate 4 columns in DP20 users: communicate w/ BOs
* BOTO for dbt projects 📈

* Next week

* Design MR approval mechanism

DE

* Completed

* Rockerbox update (SP)
* Schedule vendor\_commissions google sheet export (SP)
* Create how-to-do: Export table to google sheet (SP)
* Acquire admin rights on Analytics Division Internal kb space (SP)
* “Fix” issue with MR pipelines getting stuck (Manuel)

* In progress

* Update cookieHub tables for 3 months
* Creating hypers tables from branch and maybe create instruction (SP)

* Next week
* (optional: if any help from other functions needed)

BI

* Completed

* Dashboard Transfer from Violetta
* CookieHub Overview: fixed alert settings so it’s not falsely triggered, added new domains

* In progress

* Transfer CTA Stork Dashboard to Stork 4.0
* CMO Dashboard: added First Payments block and rearranged other blocks.

* Next week

WA

* Completed

* Help Rita to investigate issues w/ traffic on 3d media tools
* Mousflow setup for Backlink Analytics

* In progress

* Prepare for the Local campaign launch

* Next week

* Provide the number of FE & BE events for Core Trial
* Provide the number of FE & BE events for .Trends

EX

* Completed

* Fixing postgresql -> BigQuery pipeline
* Added new metric to production experiment. Bugs appeared)

* In progress

* Fixing Prefect conflict with new metric GA
* Adding GA4 -> trials conversion metric
* Fullstack interviews
* Keep updating frontend libraries and fixing conflicts

* Next week

* Fixing Prefect conflict with new metric GA
* Adding GA4 -> trials conversion metric

* Problems

Sync topics:



## Jan 17, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019908838&usg=AOvVaw3mNBL3rXt5X0L_Aw4Cjx8F)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ(team is on PTO)

* Completed



* In progress



* Next week



* Postponed



DG

* Completed

* Downstream deps for Users table

* In progress

* BOTO:

* CL727 - 70%
* External, Tableau - approving owners with teams

* BOTO in MR Workflow

* Next week

* Continue BOTO
* Deprecate old users table

DE

* Completed

* Prowly tables enrichment (under Igor’s request)
* Tables restoration (dbt local run incident)
* Fix poetry version in our auto-generated DockerFiles (SP)
* Add fields to Account SalesForce pipeline (SP)
* Reschedule Google Campaign Manager pipeline (SP)

* In progress

* Create potential bot users table
* Trebuchet postgres-BQ pipeline
* Create pipeline for RockerBox data export (SP)

* Next week
* (optional: if any help from other functions needed)

BI

* Completed

* Certified Dashboard UX Upgrade
* Added filter Subscription  Period to Sempay dash
* GTM Monitoring dash fixes

* In progress

* Dashboard Transfer from Violetta
* Transfer Dashboard to Stork 4.0
* Refactoring dashboard for Local Unit

* Next week

WA

* Completed

* Completed the setup for acquired media and verified that data is being collected properly.
* Researched why data is underestimated in reports and proposed ways to address the issue: Use raw data in BigQuery. Avoid excluding unconsented users, as the key metric is the number of visits to pages
* Move Berush script to the Necessary.

* In progress

* Check [discrepancies](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1pjf7As3n45GkweRRCKbdSKo_Y1AJvvpPzWQtNem1YHc/edit?gid%3D51035811%23gid%3D51035811&sa=D&source=editors&ust=1768225019915279&usg=AOvVaw08ipy181YUKDDZJaysRFWo) b/w backhand and frontend trials for Rafael Casas

* Next week

* Setup Conversions per request in GTM

---

EX

* Completed

* Update Node.js, React, npm, ui-kit
* GA4 metrics for trebuchet prototype is ready and in production

* In progress

* Interviews for Fullstack dev

* Next week

* Fix the integration bigquery <-> postgresql
* Add GA4 metric to one running ab-test in production
* Meta analysis of ab-tests in 2024

* Problems

Sync topics:



## 

## Jan 10, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019918215&usg=AOvVaw3arF4VI7ZUKJRpbkw702dE)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* Daily Weekly Report thresholds tuning (together with Ilnur)
* Holding MRR tests are ready, waiting for SCD model to be deployed, results have been shared with Alexandra Dumchenko for minor testing rules clarification
* Holding MRR dashboard [updates](https://www.google.com/url?q=https://jira.semrush.net/browse/BI-445&sa=D&source=editors&ust=1768225019919835&usg=AOvVaw2yzLvjhX6k73TEg1zWBiG0) have been reviewed, currently there are no other changes to expect there (Violetta did a great job. She fixed some parts and explained why we should not expect other changes)

* In progress

* Holding MRR tests implementation

* Next week

* DQ team is on vacation (we will try to avoid it in the future)
* Feedback for holding MRR tests
* Daily Weekly Report alerts monitoring to return them into showstoppers after one week of monitoring
* GCS data inconsistency feedback from Maria Andreikovich

* Postponed

* Stork 4.0 testing (since Kate will be on vacation)
* DQ Sandbox setup (with Nikita Kotlyarov’s help)
* Holding MRR tests inclusion
* Holding MRR dashboard golden state requirements compliance review (it’s live now)

DG

* Completed
* In progress

* BOTO for Tableau, External projects
* BOTO workflow for production of marts in dbt and incident mngmnt

* Next week

DE

* Completed

* Table email\_all\_events\_actions\_aggregated was recalculated
* Permissions for Sergei Rogulin were granted
* Google sheets were added as a source

* In progress

* Grant permissions for [georgii.atoian@semrush.com](mailto:georgii.atoian@semrush.com)
* Response analytics requestes

* Next week
* (optional: if any help from other functions needed)

BI

* Completed

* Finished the first iteration of Research how to visualize Gold Labelled Dashboards
* Fixed Holding MRR dash after QA testing

* In progress

* Refactoring Feature Adoption dash (Local Unit)
* Add filter Period to Sempay dash (Paysol)
* Creating documentation and how-to for Holding MRR

* Next week

WA

* Completed

* Verify setup for new assets and fix issues

* In progress

* Check [discrepancies](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1pjf7As3n45GkweRRCKbdSKo_Y1AJvvpPzWQtNem1YHc/edit?gid%3D51035811%23gid%3D51035811&sa=D&source=editors&ust=1768225019926577&usg=AOvVaw2dghga_OuGXKSu6kn1ltSG) b/w backhand and frontend trials for Rafael Casas

* Next week

* N/A

EX

* Completed
* In progress

* [Ga4 metrics](https://www.google.com/url?q=https://gitlab.semrush.net/analytics-team/dbt/-/tree/experiments/ga4-metrics&sa=D&source=editors&ust=1768225019927487&usg=AOvVaw2qBuRPnOsA-KZ6hL5lSx27) for trebuchet in dbt
* [New UX](https://www.google.com/url?q=https://gitlab.semrush.net/analytics-team/dbt/-/tree/experiments/ga4-metrics&sa=D&source=editors&ust=1768225019927768&usg=AOvVaw0OKUm3JhYY0bod4fIdcajB) for new ga4 metrics in trebuchet
* 2 candidates matched for final interview fullstack dev

* Next week

* Release ga4 metrics
* Meta analysis of ab-tests in 2024

* Problems

* postgres -> bq -> postgres

Sync topics:

* No DQ folks next week
* Usage quotas are in force!

## Jan 3, 2025 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019929551&usg=AOvVaw1LRr61xAEnaDtzvUnfgfnI)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* Marketing\_unit\_metrics to Stork 4.0 testing
* Channels\_targets\_plot\_box\_tests update

* In progress

* CMO dashboard to Stork 4.0 testing
* Holding MRR snapshots test implementation

* Next week

* TBD
* Holding MRR additional tests
* GSC daily and monthly data review after fixes
* Daily Weekly Report thresholds tuning with Ilnur Ismagilov

* Postponed

* DQ Sandbox setup (with Nikita Kotlyarov’s help)
* Holding MRR dashboard review after [updates](https://www.google.com/url?q=https://jira.semrush.net/browse/BI-445&sa=D&source=editors&ust=1768225019932321&usg=AOvVaw3Ck5O3_Vu1JeuUyPCpfgC9) + golden state verification

DG

* Completed
* In progress
* Next week

DE

* Completed

* Add 2 external tables from Google drive
* Request quotas for analytics projects
* Update scd table

* In progress

* Schedule vendor\_commissions
* Support external requests

* Next week
* (optional: if any help from other functions needed)

BI

* Completed

* [BI-443](https://www.google.com/url?q=https://jira.semrush.net/browse/BI-443&sa=D&source=editors&ust=1768225019934496&usg=AOvVaw0_rIhKfSu_hIXsc_X0GBrr) Added MRR user tier breakdown to the MRRHawk dashboard

* In progress

* [BI-447](https://www.google.com/url?q=https://jira.semrush.net/browse/BI-447&sa=D&source=editors&ust=1768225019934923&usg=AOvVaw0Z45m1SOxuXWtJqtTCnqFQ) CookieHub Overview dashboard update and alerting
* MRR Holding fixes after QA and Sam’s request
* GTM monitoring leveling up and documentation
* Visual Refactoring Local Unit Overview

* Next week

WA

* Completed

* Zoominfo Setup for Low/Medium/High interest pages

* In progress

* PSNB campaign issue w tracking

* Next week

* Check [discrepancies](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1pjf7As3n45GkweRRCKbdSKo_Y1AJvvpPzWQtNem1YHc/edit?gid%3D51035811%23gid%3D51035811&sa=D&source=editors&ust=1768225019936714&usg=AOvVaw3au8RkmakNXXjsqm4UWyJz) b/w backhand and frontend trials for Rafael Casas

EX

* Completed
* In progress

* Developing GA4 metrics for monitoring AB tests
* Fullstack Interviews, 3 promising candidates

* Next week

* Developing GA4 metrics for monitoring AB tests (1-2 weeks)

* Problems

* Prefect [https://trebuchet-prefect.k1.semrush.net/flow-runs](https://www.google.com/url?q=https://trebuchet-prefect.k1.semrush.net/flow-runs&sa=D&source=editors&ust=1768225019938236&usg=AOvVaw2uQAlEjeSdKBU7eYFzrkrK), which is used for metrics calculations in AB tests, has problems with CPU throttling  
  [https://semrush.slack.com/archives/C073DEF55DY/p1735893124246629](https://www.google.com/url?q=https://semrush.slack.com/archives/C073DEF55DY/p1735893124246629&sa=D&source=editors&ust=1768225019938725&usg=AOvVaw3gsaWjzKhuxPip2cOSjYMq)  
  Can we bump up the CPU and Memory resources for it?  
  Also we cannot deploy to it, probably container is throttling now  
  [https://gitlab.semrush.net/white/trebufect/-/jobs/31303159](https://www.google.com/url?q=https://gitlab.semrush.net/white/trebufect/-/jobs/31303159&sa=D&source=editors&ust=1768225019939264&usg=AOvVaw3QUbYYQ5_0DL6dnJHt0REm)

Sync topics:

* Next Week – we do have a New BI Engineer Alina + Data Team Lead Manuel
* Dbt 1.6 update? [https://jira.semrush.net/browse/AAI-2557](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2557&sa=D&source=editors&ust=1768225019939930&usg=AOvVaw3enK9VRcYMckjd06k2LuRX)
* Streaming data loss
* If you’re getting an access somewhere – pls use the google group instead of personal (it will help to share accesses with your teammates)

## 

## Dec 27, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019940461&usg=AOvVaw1PEuGf8o0FqEZERQOCuHCj)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* Registration tests updates for New Daily Weekly report (end of year decrease case)
* Other tests fixes and updates ([regs.final\_result](https://www.google.com/url?q=https://jira.semrush.net/browse/ADQA-92&sa=D&source=editors&ust=1768225019941190&usg=AOvVaw3yBiuklFR_IarHeixSyC9Z), [regs daily report weekly](https://www.google.com/url?q=https://jira.semrush.net/browse/ADQA-93&sa=D&source=editors&ust=1768225019941300&usg=AOvVaw2bYszqHACo8QjK8n7a_vzi),[finance additional limits payments](https://www.google.com/url?q=https://jira.semrush.net/browse/ADQA-94&sa=D&source=editors&ust=1768225019941412&usg=AOvVaw1PF3M_D-8Z9_eGUte1-TwQ), [CAC\_units\_costs\_daily](https://www.google.com/url?q=https://jira.semrush.net/browse/ADQA-91&sa=D&source=editors&ust=1768225019941509&usg=AOvVaw3Z26fMk2UF0Uis7aQD973k), [New Daily Weekly trials and regs](https://www.google.com/url?q=https://jira.semrush.net/browse/AAR-1971&sa=D&source=editors&ust=1768225019941638&usg=AOvVaw0bD-6xJy0Q_VXBDOFp35V7), [cta32\_sub\_channel\_full\_source\_regrouped](https://www.google.com/url?q=https://jira.semrush.net/browse/AAR-1970&sa=D&source=editors&ust=1768225019941781&usg=AOvVaw1tXqAmV3AI-cQQtIeWm65K))
* Historical GSC daily and monthly data testing

* In progress

* Holding MRR snapshots test implementation
* Marketing\_unit\_metrics to Stork 4.0 testing

* Next week

* Holding MRR tests
* (optional: if any help from other functions needed)

* Postponed

* DQ Sandbox setup (with Nikita Kotlyarov’s help)
* Holding MRR dashboard review after [updates](https://www.google.com/url?q=https://jira.semrush.net/browse/BI-445&sa=D&source=editors&ust=1768225019942592&usg=AOvVaw1rG5UhdtMEF15R7M0UyzOr) + golden state verification

DG

* Completed
* In progress
* Next week

DE

* Completed

* Added recommendation\_system value for GA4 event
* Loaded google search console data for new domains.
* Add BigQuery usage quotas to analytics-team-prod
* Calculate usage quotas
* Resolve incoming requests

* In progress

* Request quotas for other our projects
* Update scd table

* Next week
* (optional: if any help from other functions needed)

BI

* Completed

* Fixed Units Overview

* In progress

* Visual Refactoring Local Unit Overview
* Research how to visualize Gold Labelled Dashboards

* Next week

EX

* Completed

* New feature Canary deploy should be released today
* Thanks [Anna Obyskalova](mailto:anna.obyskalova@semrush.com) for adding access to trebuchet dbt!

* In progress
* Next week

* Prototype metrics calculation for ab tests in dbt
* Add visuals for dbt metrics in trebuchet

## Dec 20, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019944959&usg=AOvVaw2uT8bsY-Ajc5qAh0Nc0F03)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* BU\_Attribution to Stork 4.0 testing
* Cac\_contacts to Stork 4.0 testing
* Daily\_report\_weekly tests
* Marketing CAC unit costs test
* Holding MRR dashboard testing (waiting for a feedback)
* GCM historical data verification version 2

* In progress

* Marketing\_unit\_metrics to Stork 4.0 testing
* Registrations test for New Daily Weekly report enhancement

* Next week

* DQ Sandbox setup (with Nikita Kotlyarov’s help)
* Holding MRR dashboard review after the feedback/status + golden state verification
* Stork 4.0 testing
* GCM historical data re-verification version 2
* (optional: if any help from other functions needed)

DG

* Completed

* Corrected update\_codeowners CI job + Data Catalog script
* Bug fixes in CI, usage stats for datamart

* In progress

* BOTO for Tableau, External projects
* BOTO workflow for production of marts in dbt and incident mngmnt

* Next week

* PTO!

DE

* Completed

* Change GCM pipelines and dbt models

* In progress

* Potential bot users table
* Collecting historical data from GSC
* Patch GCM data (SP)
* JupiterHub migration?

* Next week
* (optional: if any help from other functions needed)

BI

* Completed

* Monthly Dashboard labeling
* Complited Tableau Webinar
* Moved to prod Local PMF Dash
* Minor changes for Local Unit Marketing dash

* In progress

* Fix DS for Datasource dash

* Next week

EX

* Completed

* Thanks [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) for keeping this doc organized
* New features and bug fixes are announced by [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) in [channel](https://www.google.com/url?q=https://semrush.slack.com/archives/C02NHM9GCKG&sa=D&source=editors&ust=1768225019949076&usg=AOvVaw0xXtoIl5rubRg_mq3vi17j)

* UX improvements in trebuchet
* Useful slack notifications
* Screenshot uploading bug

* In progress

* AB test metrics computation service (Prefect) approached team limits of the kubernetis pods.
* Thanks [Mike Trifonov](mailto:mike.trifonov@semrush.com) for helping with experimentation roadmap
* Interviews for fullstack (backend)

* Next week

* Dobby is free to code and refactor

Schedule for the Festive Season (dates are preliminary):

* [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) – will be out starting tomorrow – and till Jan XX
* [Anna Obyskalova](mailto:anna.obyskalova@semrush.com) – will be out and till Jan 12 for a week, then again 2 weeks PTO
* [Natalia Karpova](mailto:natalia.karpova@semrush.com) – will be out starting Dec 30, for 2,5 weeks
* [Simon Putnikov](mailto:simon.putnikov@semrush.com) – no PTO, will cover us during Dec-Jan, thank you, Simon!
* [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) – PTO Jan 6, for 2 weeks
* [Pavel Skladnev](mailto:pavel.skladnev@semrush.com) – PTO Jan 12, 1 week
* CZ/CY employees – are out for Dec 24-26
* ES employees – are out for Dec 25-26

## Dec 13, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019951073&usg=AOvVaw2q2SbwXkI6nTSImLFbpzhy)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

DQ

* Completed

* Daily Report tests exploration & traceability matrix updates
* Daily Report test for Spikes
* All Daily Report MRR box plot test has been added

* In progress

* BU\_Attribution to Stork 4.0 testing
* Daily Report Weekly tests for registrations (tables system\_time snapshots comparison)

* Next week

* Cac\_contacts to Stork 4.0 testing
* Marketing calculations CAC daily unit costs tests
* (optional: if any help from other functions needed)

DE

* Completed

* Collecting historical data from GCM (SP)
* Add new websites to GA4 extraction (SP)
* Analytics\_dept\_tickets bug fix
* New field to SalesForce.Account

* In progress

* Potential bot users table
* Collecting historical data from GSC
* Migrate GCM etl to new pipeline (SP)
* Test CI job for BOTO validation
* Trebuchet related tasks

* Next week
* (optional: if any help from other functions needed)

BI

* Completed

* Monthly Dashboard labeling
* Complited Tableau Webinar
* Moved to prod Local PMF Dash
* Minor changes for Local Unit Marketing dash

* In progress

* Fix DS for Datasource dash

* Next week

DG

* Completed

* Defined BOTO for Datamart & Projects
* Completed Audit of Datamart tables:

* listed potential tables for deprecation (for Q2)
* proposed dbt migration workflow

* In progress

* BOTO for Tableau
* Correct update\_codeowners CI job + Data Catalog script

* Next week

* BOTO for other projects

WA

* Completed

* Added Trends and Local payment / trial conversions (MP by EEADA) [Rafael Casas de las Peñas Risi](mailto:rafael.casas@semrush.com)

* In progress

* PSNB campaign research [Evgeniy Sobolev](mailto:e.sobolev@semrush.com)
* RockerBox Implementation
* Missing events bug on marketing lps w/ [Dima Parshin](mailto:dmitry.parshin@semrush.com)

EX

* Completed

* [Fixed bug](https://www.google.com/url?q=https://semrush.slack.com/archives/C02NHM9GCKG/p1733914128756659&sa=D&source=editors&ust=1768225019955826&usg=AOvVaw1syKiRQPN0BBJTdL-1aN0E) with images not uploading
* Created the easy to use [design doc template](https://www.google.com/url?q=https://gitlab.semrush.net/white/trebuchet/-/merge_requests/700&sa=D&source=editors&ust=1768225019956026&usg=AOvVaw1nvr5AFta6Fz0Sse6HpHcX)
* [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [created new UX](https://www.google.com/url?q=https://semrush.slack.com/archives/C02NHM9GCKG/p1733846810661199&sa=D&source=editors&ust=1768225019956197&usg=AOvVaw3xzEP78xb00865SwkRX81k) for experiments images

* In progress

* New UX for experiment results
* Experimentation development plan
* Fullstack developer interviews
* Investigating VWO integration, GTMs, GA4

* Next week

* Remove redundant docs and communicate changes to analysts
* Experimentation development plan
* Fullstack developer interviews
* Start transition prefect -> DBT

Sync topics:

* BOTO for [analytics-tableau-prod-tf](https://www.google.com/url?q=https://gitlab.semrush.net/analytics-team/dbt/-/tree/master/models/analytics-tableau-prod-tf?ref_type%3Dheads&sa=D&source=editors&ust=1768225019957233&usg=AOvVaw01C_dihMUPJ3HQq3Ma6nig) tables

## Dec 6, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEyMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225019957631&usg=AOvVaw2uvA15Ou8LZ78k21qTxtCc)

Attendees: [Data Platform Unit](mailto:analytics-infrastructure@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com)

Weekly Update:

DQ

* Completed
* In progress

* Knowledge sharing with Pavel
* BU\_Attribution to Stork 4.0 testing
* Daily Report tests exploration & traceability matrix updates

* Next week

* Cac\_contacts to Stork 4.0 testing
* Daily Report tests updates (MRR cumulative increase/decrease & weekly expansion visualizations)
* Cost monitoring test for Daily Report
* (optional: if any help from other functions needed)

DE

* Completed

* Upgraded several airflow virtual machines

* In progress

* Potential bot users table
* Collecting historical data from GSC

* Next week
* (optional: if any help from other functions needed)

DG

* Completed

* Metadata Architecture
* Workshops on BOTO

* In progress

* CI Job & Codeowners Logic Update
* Alerts Fix

* Next week

* BOTO for datamart & other projects

WA

* Completed

* Check monitoring requests
* HR Facebook APIs definition of requirements → Task for DE [AAI-2519](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2519&sa=D&source=editors&ust=1768225019960490&usg=AOvVaw3QH8J1kr7K3XFKC9Ewma9X) (implement API)

* In progress

* Setup GA4, GSC, OLAF, CookieHub, BigQuery for new assets → Just Missing Simon task → [AAI-2509](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2509&sa=D&source=editors&ust=1768225019960824&usg=AOvVaw3HY5Ij2WdtFLUHPoKchjnU)
* Clarify CookieHub implementation for US
* Rockerbox Implementation prep → White team and Coffee team working on pushing hashed email on missing user flows.

* Next week

* Mismatch OWOX and G.Ads registrations

* (optional: if any help from other functions needed)

* [AAI-2519](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2519&sa=D&source=editors&ust=1768225019961554&usg=AOvVaw0MFliHiIsbgD67OyKimFpK) Pending to define DE
* [AAI-2509](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2509&sa=D&source=editors&ust=1768225019961710&usg=AOvVaw1J3wpr5Y11pMH6A7XQCTr3) Simon working on this

BI

* Completed
* In progress
* Next week
* (optional: if any help from other functions needed)

EX

* Completed

* Change the wait period 7 days -> 1 day
* [UX improvement](https://www.google.com/url?q=https://semrush.slack.com/archives/C02NHM9GCKG&sa=D&source=editors&ust=1768225019962408&usg=AOvVaw17ASWlCpKUsoYrqjpCpH3S) in trebuchet
* Fix the Docker build container for trebuchet
* [Interviews](https://www.google.com/url?q=https://docs.google.com/document/d/1qJW3km5_AcD5rPh-9f7G17tSuOjlJKb85h50n8lATh4/edit?tab%3Dt.0%23heading%3Dh.nyj9392apoph&sa=D&source=editors&ust=1768225019962638&usg=AOvVaw3nqNgBUreGjKY1Ryhm6C8W) of  trebuchet customers (POs, UI/UX, TOs)

* In progress

* Experimentation development plan
* Fullstack developer interviews

* Next week

* VWO integration with trebuchet investigation
* Further UX improvements of trebuchet
* Start transition prefect -> DBT

* (optional: if any help from other functions needed)

* create a new dataset trebuchet-prod-tf.analyst\_metrics.
* create a pipeline to copy data from the 'experiments\_experiment' table in the internal Trebuchet PostgreSQL database to trebuchet-prod-tf.analyst\_metrics.trebuchet\_experiments.
* grant [@anatolii.pokhylko](https://www.google.com/url?q=https://semrush.slack.com/team/U07B65S045V&sa=D&source=editors&ust=1768225019963922&usg=AOvVaw3830n3dzYeh5-yTJChZp-d) access rights to the DBT GitLab.
* configure DBT to create and schedule models in trebuchet-prod-tf.analyst\_metrics.

Notes



Action items



## Nov 29, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEwMThUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225019964597&usg=AOvVaw14ksa3l-1IKXODuTvbMpsp)

Attendees:  [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com)  [Mike Trifonov](mailto:mike.trifonov@semrush.com)  [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com)[Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com) 

DQ

* Completed

* Automated test for OWOX traffic definition
* Holding MRR dashboard testing
* GCM historical data verification

* In progress

* Knowledge sharing with Pavel
* Stork 4.0 testing

* Next week

* Stork 4.0 testing
* SRE Reliability Dashboard testing

DE

* Completed

* BigQuery backup pipeline
* R&D EL-tool
* Hypers pipelines fail
* Document the data flows to SalesForce from Analytics
* Dropped the last eu replicas
* Fixed bug in data unit\_overview\_crs\_overview (for Kostya)

* In progress

* GCM data restoration
* Bug: duplication of data in adwords

* Next week

* Pass GCM to a new etl pipeline

DG

* Completed

* Alerts on BOTO
* Metadata Strategy

* In progress

* Metadata Architecture
* Workshops on BOTO in dbt

* Next week

* BOTO CI Check Job

BI

* Completed

* Holding MRR dashboard
* Owl table technical debt fix

* In progress

* Reliability dashboard for SRE reporting [testing stage]
* GTM monitoring dashboard leveling up
* Adding yes / no agency to semrush wide reports

* Next week

* CookieHub report alerting set up

WA

* Completed

* Update CookieHub version
* Local Unit test Frontend events

* In progress

* HR Facebook APIs definition of requirements
* Setup GA4, GSC, OLAF, CookieHub, BigQuery for new assets
* RockerBox implementation

* Next week

* Check Monitoring requests

EX

* Completed

* [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com)Fixed backend bug with images
* [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com)Fixed devops bug with Helm
* Marketo integration on pause

* In progress

* Interviews for Fullstack
* Interviewing POs about the experiments

* Next week

* Start to dig into adding new metrics
* Collect info into Trebuchet about the past experiments

Sync topics:



## 

## Nov 22, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEwMThUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225019969810&usg=AOvVaw3ZT7Tz5NAjezD1USgXo6T6)

Attendees:  [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com)  [Mike Trifonov](mailto:mike.trifonov@semrush.com)  [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com)[Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com) 

QA DQ

* Completed

* Сreate “DQ Service Catalog” in KB
* Develop on-boarding plan for newcomer

* In progress

* Holding MRR dashboard testing

* Next week

* Create a test for OWOX traffic definition

BI

* Completed

* Local Unit Funnel report visual refactoring
* Change filters in Local Marketing dashboard
* Documentation for Holding MRR
* Test Holding MRR dash to align with the data source, and metrics are being computed properly and conduct UAT alpha.
* Create a checklist for UAT of dashboards.

* In progress

* Visual refactoring PMF Local dashboard
* Refactoring of new pages for Units Overview dashboard
* Holding MRR dashboard: conduct UAT beta  for stakeholders.
* Viz Refactoring Local PMF Dash
* The Reliability Dashboard is back to development. Added traffic source and other visualizations to support SRE teams with reporting.

* Next week

* GTM monitoring leveling up and documentation

DG

* Completed

* Data Catalog Features:

* Storage and Partitions Information

* Completed Owners List for DP20
* Made Announcement on Metadata/BOTO Collection in DBT

* In progress

* Metadata Strategy
* Workshops on Metadata/BOTO Collection in DBT

* Next week

* Slack alerting on new BOTO

DE

* Completed

* Usage of eu-replicas has been stopped

* In progress

* Historical data for Google Campaign Manager
* Documentazing el-tool
* Ad-words duplication bug
* Hyper crs\_overview bug
* Implement is\_bot function for ga4 streaming

* Next week

* Internal knowledge sharing (to prepare for the new year's eve) (SP)
* Deletion of the remaining eu-replicas

WA

* Completed

* Research missing sign\_up and login events and the reason behind it
* Clean Up DM tags / triggers

* In progress

* Rockerbox Implementation
* Setup GA4, GSC, OLAF, CookieHub, BigQuery for new assets → Will require DE to connect GA to BigQuery.

* DE support will be needed

* Investigate reasons why GTM / GA4 attributes were downgraded

* Next week

* Implement CookieHub version 2.8.3
* Local Unit, test frontend events

EX

* Completed

* Collecting the knowledge about the trebuchet and documenting along the way
* Implemented key metric
* Started to research the Prefect

* In progress

* Found the queries and integration Trebuchet <-> Marketo
* Interviewing POs about the experiments

* Next week

* Marketo - digging deeper into the trench
* Interviewing POs about the experiments

Sync topics:

* [Paul] Demo on Metadata & BOTO Collection in DBT
* [Mike] We’re slowly opening DWH 2.0 project
* [Mike] We’re opening a +1 position of Data Engineer

## Nov 15, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEwMThUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225019976037&usg=AOvVaw0KaUk1p9STrsmMCt7HSxYD)

Attendees:  [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com)  [Mike Trifonov](mailto:mike.trifonov@semrush.com)  [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com)[Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com) 

QA

* Completed

* Fix auto tests for marketing

* In progress

* Сreate “DQ Service Catalog” in KB
* Create a test for OWOX traffic definition

* Next week

* Develop on-boarding plan for newcomer
* Create a test for OWOX traffic definition

DE

* Completed

* Fixed gitlab runners issue that was causing merge requests to get stuck.
* Fixed Bing bug (credentials upd)

* In progress

* Collect historical data for backlinko.com domain from google search console.
* Historical data for Google Campaign Manager
* Remaining tasks for migration to US

* Next week

* Collect historical data from google search console for other domains.
* Remaining tasks for migration to US

BI

* Completed

* Create Hyper for new DS Units overview and replace it + additional tasks
* Local Unit Funnel Report (in BI testing)
* Migrated MRR dash to new company size & industry dimensions
* Switched Churn Penguin from extract to hyper to enhance performance and address failures
* Updated the visualization in Churn Penguin to display time frames for the reasons

* In progress

* Viz Refactoring Local PMF Dash
* The Reliability Dashboard is back to development. Added traffic source and other visualizations to support SRE teams with reporting.

* Next week

* GTM monitoring leveling up and documentation

DG

* Completed

* Data Catalog Features:

* Airflow links
* Compiled SQL code
* DC update execution logging

* In progress

* BOTO Framework Soft Rollout

* Next week

* Agree on BOTO for all DP20 tables w/ TLs
* Next features for DC: storage stats, and estimated time to load a new batch of data

WA

* Completed

* Prepare a draft function to identify bots, and requirements to create a table with users with high probability of being bots → send to DE to improve Function & create table.
* Research missing sign\_up and login events and the reason behind it

* In progress

* Rockerbox Implementation prep
* Check the data source for Local Funnels calculations to verify the reason behind the recent spikes in data.

* Next week

* GTM monitoring template fixes and improvements
* Research touchpoints from direct traffic
* New acquired assets setup

* DE Help needed: AAI-2487 and AAI-2488

EX

* Completed

* Fixed CI pipeline bug in Trebuchet
* Fixed bug in tests in Trebuchet
* [Violetta Lomako](mailto:violetta.lomako@semrush.com)helped to start to understand VWO integration to trebuchet

* In progress

* Interviewing analytics about the experiments

* Next week

* WTF is Marketo and how is it integrated into our pipelines?
* WTF is VWO and how is it integrated into our pipelines?
* Marat and Anatolii are learning backend development
* Anatolii dig into the next backend feature/bug
* Interviews, slack messages

Sync topics:

* [Mike] We’re renaming QA function to Data Quality

* Goal is just to reflect better what we do
* We do not plan to reduce QA activities
* Katya is already has a new title
* Newcomer – “Another-Pavel” will join us in 10 days

* [Mike] Next Weekly Sync – we will start with Introduction to the 6 newcomers :)

## 

## Nov 8, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEwMThUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225019982532&usg=AOvVaw3vFp_gy_FavLaRlXfVgE4Q)

Attendees:  [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com)  [Mike Trifonov](mailto:mike.trifonov@semrush.com)  [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com)[Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com) 

QA

* Completed

* Testing of billing\_payment\_details migration
* Add auto tests for new billing\_payment\_addons table

* In progress

* Create a test for OWOX traffic definition

* Next week

* Create a test for OWOX traffic definition

DE

* Completed

* PRS deployment process was fixed
* Data rotation at table data-paradise-20.finance.salvage\_offer\_events was fixed

* In progress

* Extraction for historical data of Google cloud manager table

* Next week

BI

* Completed

* Add column into Custom Users List
* Salvage offers switched to a new data source
* add new page for Units Overview dash

* In progress

* Churn Penguin data source change in order to fix the bug in the server when calcs are performed
* Small fixes in Holding MRR due to changes in the data source
* Local Unit Funnel Report
* Viz Refactoring Local PMF Dash

* Next week

* Refactor and certify GTM Performance dash

DG

* Completed

* Metadata Collection

* DBT Metadata Collection now in Prod
* Metadata Collection in dbt [Guideline](https://www.google.com/url?q=https://kb.semrush.net/display/ATI/Metadata%2BCollection%2Bin%2BDBT&sa=D&source=editors&ust=1768225019985437&usg=AOvVaw3He_ZK0A9PperOmv0AV2Lf)

* Data Catalog

* Added Upstream and Downstream sources to Data Catalog
* Added DBT docs link and updated Datamart Docs as requested by [Nikita Kudriavtsev](mailto:nikita.kudriavtsev@semrush.com)

* In progress

* Agree on BOTO for all DP20 tables w/ TLs
* New features for DC: SQL code

* Next week

* New features for DC: storage stats, tests in Downstreams, etc

WA

* Completed

* Research recent spikes in new users and strange user activity
* Add bot detection variable.
* Research tech traffic
* Research UA / GA4 / OWOX pageviews discrepancies. → 2 articles were created based on research.

* In progress

* Create BigQuery functions to identify bots, and create table with users with high probability of being bots → send to DE to improve Function & create table.
* Rockerbox Implementation prep

* Next week

* GTM, GSC, BQ, GA, setup for new assets acquired
* Research missing hits in streamin

EX

* Completed

* [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com)fixed his first bug in Backend of trebuchet!

* In progress

* Interviewing analytics about the experiments

* Next week

* WTF is Marketo and how is it integrated into our pipelines?
* Marat and Anatolii are learning backend development
* Anatolii dig into the next backend feature/bug
* Interviews, slack messages

## Oct 31, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEwMThUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225019988115&usg=AOvVaw06j0oKJFadPbRRmn_YkJGV)

Attendees:  [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)  [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com)[Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com) 

QA

* Completed

* App\_center migration testing

* In progress

* Testing of billing\_payment\_details migration
* Add auto tests for new billing\_payment\_addons table

* Next week

* Create a test for OWOX traffic definition

BI

* Completed

* Leveling up Coins / Credits Dashboard [test]

* In progress

* Churn Penguin data source split and addition of reasons using window size [test by stakeholders] and frozen mrr discrepancies research
* Viz Refactoring Local PMF Dash

* Next week

DG

* Completed

* Added “is deleted?” flag to autodoc
* Added BOTO metadata to autodoc (requires dbt restructure in prod to be seen)

* In progress

* dbt restructure ready  - waiting for [MR](https://www.google.com/url?q=https://gitlab.semrush.net/analytics-team/dbt/-/merge_requests/3351&sa=D&source=editors&ust=1768225019990584&usg=AOvVaw3FnRq3ueNRl-kh_s4OLQ1v) to be merged
* BOTO guideline updated - waiting for [Mike Trifonov](mailto:mike.trifonov@semrush.com) to take a look
* Datamart Docs update as requested by [Nikita Kudriavtsev](mailto:nikita.kudriavtsev@semrush.com)

* Next week

* Agree on BOTO for all DP20 tables w/ TLs

EX

* Completed

* First Fullstack hiring interview
* Jira tasks are in order now
* Plan for next month
* Created KB page

* In progress

* Marat and Anatoliy are learning backend development. First bug is in progress.

* Next week

* Marat and Anatoliy are learning backend development
* Interviews with insights about experiments and problems
* Review and fix experiments kb

DE

* Completed

* Billing\_payment\_detail table migration
* Enrichment of adwords table with cm\_campaign\_id and cm\_placement\_id fields.
* .

* In progress

* Loading data with new limits from core team for Andrey.
* Fixing PRS deployment process (trends, trends\_model)

* Next week

* Enrich table 'acquisition.yahoo\_costs' with data from field 'Tracking URL'
* Violetta’s task [ps://jira.semrush.net/browse/AAI-2455](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2455&sa=D&source=editors&ust=1768225019992765&usg=AOvVaw0Ykpd19WvN-Xu4pgIW1hIt) [[c]](#cmnt3)  – it blocks the archivation of old tables, no blocks for business, we just want to complete it

WA

* Completed

* Sensor GTM container was archived

* In progress

* DCM traffic discrepancies research (UA / OWOX / GA4)
* PV discrepancies research (UA / OWOX / GA4)
* Research missing users / events in streaming

* Next week

* Add Bot Variable Template to Flag Bots at Entry Level

Notes

* [Mike] Unit Org Structure after [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com)’s departure:

* DataGov will move to Data Platform Engineering team
* BI & Data Gov team to become BI & WA team
* We’ve opened a new position for “BI Team Lead”

## 

## Oct 18, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEwMThUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225019994575&usg=AOvVaw0Q8S0DJTVH7LwB0HlAgZ9H)

Attendees: [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)  [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com)

QA

* Completed

* Add test for pending mrr (1 sub per user)

* In progress

* App\_center migration testing
* Create a test for OWOX traffic definition

* Next week

* App\_center migration testing
* Create a test for OWOX traffic definition

DE

* Completed

* Migration app\_center tables to the new api

* In progress

* Migration billing\_payment\_detail table to the new one from Paysol team.
* Add column to Google\_Campaign\_Manager
* Fix PRS CICD process

* Next week

* Add column to Google\_Campaign\_Manager
* Fix PRS CICD process

BI

* Completed

* YoY% chart in ATL dash
* Bunch of requests to add filters to Additional ptments dash
* Dashboard pack for Unit
* Pending MRR adding fields to the source and filters to the dashboard

* In progress

* Holding MRR dashboards
* Transitioning dashes from Nastenka
* Local Funnel dash
* Leveling up Coins / Credits Dashboard [test]
* Churn Penguin data source split and addition of reasons using window size
* API semrush2 dashboard [stage data preparation]

* Next week

* Review MRR dimensions in the dash

DG

* Completed

* Added source usage stats to Docs

* In progress

* Ready to test dbt restructure in prod
* Defining BO for whole DP20

* Next week

* Roll out dbt restructure update for DP20 project

WA

* Completed
* In progress

* Send API events to OWOX [part of sm2 API dashboard]
* Research and fix unwanted referral traffic
* Research and find the reason for traffic discrepancies in UA / GA4 / OWOX

* Next week

EX

* Completed

* “Burning Issues” fixed
* Backlog Groomed & Sprint 2 & 3 planned

* In progress / Next week

* Executing only Front-end focused tasks from backlog (30% of them)

## 

## Oct 11, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDEwMTFUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225019999631&usg=AOvVaw1CvK2aOmtW83FlaKergZtc)

Attendees: [r.rinchinov@semrush.com](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [grigorii.timofeev@semrush.com](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com) [Simon Putnikov](mailto:simon.putnikov@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com)

QA

* Completed

* Create tests for other reports like stoppers for Daily reports

(8 tests have been added)

* In progress

* MRR extraordinary expansion test
* Add test for pending mrr (1 sub per user)

* Next week

* Create cost monitoring test for daily report

DE

* Completed

* Fix of linkedin export pipeline

* In progress

* Migration app\_center tables to the new api.
* Adwords enhancement
* Restore of data after pubsub migration

* Next week

* Migration paysol payment detail table to the new one.

BI

* Completed

* Pending mrr old source was switched to new one and archived
* Fixed BI Alert dashboard
* Visual requests for NUMRR Impact Dash

* In progress

* MRR Holding dashboard, [Ekaterina Esina](mailto:ekaterina.esina@semrush.com)testing will be needed next week
* Coins dashboard refactoring and labeling
* Salvage offers dashboard [blocked]
* Pending MRR adding fields to the source and filters to the dashboard
* Churn Penguin data source split and addition of reasons using window size
* Local funnel dash
* Tasks from PaySol team for additional Payments dash

* Next week

DG

* Completed

* DBT Restructure Proposal

* In progress

* Prototyping DBT project in new structure
* Default BOTO for datasets & BOTO teams discussion
* BOTO Assignment Guideline - awaits approval

* Next week

WA

* Completed

* Research Trafic Affiliate Traffic GA4 / UA
* TikTok pixel implementation
* UA & GA4 traffic discrepancies → task for Katia
* Data preparation for EADA to send conversions to GA4

* In progress

* Rockerbox
* CookieHub CCPS & CPRA Documentation
* Research tech traffic
* UA & GA4 traffic discrepancies → was solved, but extra research

* Next week

EX

* Completed

* Preps for Grisha 2.0 hiring

* In progress

* Troubleshooting with Experiments
* Grisha 2.0 hiring

* Next week

* Troubleshooting with Experiments

Notes

* [Mike] As of next week: Anya is on PTO, Simon is on DE Duty!
* [Mike] Thanks for participation in Performance Review – we are the first team!
* [Mike] Retrospective – proposed to be changed to the Team-level Retroes: every team can run their Retro in a more flexible way.

Action items



## Oct 4, 2024 | [Meet Alla + Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA5MjdUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020006794&usg=AOvVaw1pqdp6MkRlufcCbPWUZNyN)

Attendees: [r.rinchinov@semrush.com](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com)

Notes

QA

* Completed

* New Pending MRR tests review + new tests added
* Fixes for automated tests (OLAF and Marketing tests)

* In progress

* Traceability matrix update
* Define owner and priority for Kochanov Ev tests (trials and promo, registrations and others)

* Next week

* Create tests for other reports like stoppers for Daily reports
* MRR extraordinary expansion test

DE

* Completed:

* Upd of gitlab expiring tokens
* Adding new fields Unused\_Period\_Discount\_\_c, Total\_Price\_Without\_Unused\_Period\_\_c to sf Opportunity table (under Sasha D.’s request)
* Transferred specified red-team data from us-eas4 location to us (under Vadim’s request)

* In progress

* Enrich table 'acquisition.adwords'
* LinkedIn pipeline

* Next week

* I have to finish work related to restoring data after the migration of pubsub.

BI

* Completed



* In progress

* Dashboards pack for units
* Local Init Funnel Dash
* Holding MRR dashboard
* Pending Dashboard refactoring and old source deprecation [testing stage]
* Salvage Offer dashboard source was moved to dbt [done, but blocked by bug with incremental model]

* Next week

* Need help from DE to check migration from Tableau tables to BQ
* Need help from DE to check why there is no data [https://jira.semrush.net/browse/AAI-2455](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2455&sa=D&source=editors&ust=1768225020011763&usg=AOvVaw26DD3N1gFU_pLC078Usgyy) [[d]](#cmnt4)

DG

* Completed

* Developed Auto-Doc in new Template: Script in Prod
* Created Guideline for New Docs Template

* In progress

* DBT project restructure proposal
* BOTO Assignment Guideline

* Next week

* DBT project restructure
* Add data usage to Auto-Doc
* New Rules to Define BOTO

WA

* Completed

* Acquired Asset setup → exploding Topics.
* Research Affiliate Traffic GA4 / UA
* UA & GA4 traffic discrepancies

* In progress

* CookieHub CCPA & CPRA Documentation
* TikTok pixel setup → frontend checking whats the prob

* Next week

* CookieHub Improvements
* GTM monitoring dash
* Streaming tests

Notes

* [Mike] Team Updates

## Sep 27, 2024 | [Meet Alla + Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA5MjdUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020015312&usg=AOvVaw00AZGN3sjaixuDhN0UG45w)

Attendees: [r.rinchinov@semrush.com](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com)

Notes

QA

* Completed

* OSM testing INSIGHT-2572
* ZoomInfo Location Enrich testing INSIGHT-2419

* In progress

* New Pending MRR tests review
* Traceability matrix update

* Next week

* QA traceability matrix for critical metrics + test cases review

DE

* Completed
* In progress
* Next week

BI

* Completed

* Active Users Dashboard for IH

* In progress

* Holding MRR dashboard
* Pending MRR dashboard (already in testing)
* Salvage offers dashboard data source replacement
* Design Dashboards pack for unit
* Local Unit Funnel DS

* Next week

DG

* Completed

* Channel, sub channel, short url, user stage, marketing stage, target dimensions description
* 3 Project Docs migrated to New Template

* In progress

* Device, traffic source dimensions (last piece)
* Update Auodoc script to new template: updating datamart and BQ description

* Next week

* Presentations of the new docs template
* Start project on dbt metadata

WA

* Completed

* VWO mark up experiment pages → avoid double page\_view count

* In progress

* CookieHub CCPA & CPRA Documentation
* Research Affiliate Traffic GA4 / UA
* [blocked]Archive sensor GTM
* [blocked]Acquired asset setup Exploding Topics

* [Anna Obyskalova](mailto:anna.obyskalova@semrush.com) please provide support to WA for ExplodingTopics.com – [Violetta Lomako](mailto:violetta.lomako@semrush.com) will reach Anya Out

* [blocked]TikTok Pixel & LDU function

* Next week

* UA & GA4 traffic discrepancies

Notes

* [Pavel] New Docs Template
* [Mike] Big thanks from [Vitalii Obishchenko](mailto:v.obishchenko@semrush.com) for the SRE dashboard! – to [Violetta Lomako](mailto:violetta.lomako@semrush.com), [Natalia Karpova](mailto:natalia.karpova@semrush.com) and [Anna Obyskalova](mailto:anna.obyskalova@semrush.com)
* [Mike] Next Monday, Sept 30, a new DE is joining us – Semyon / Ru-speaker / Spain
* [Mike] As of Oct 1, the Experimentation team is joining us (Marat to lead)

## Sep 20, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA5MjBUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020022403&usg=AOvVaw3fMgOMa3yex2fhK5YaPL69)

Attendees: [r.rinchinov@semrush.com](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com)

Notes

QA

* Completed

* Preparation and finalization of the interview questions list.
* Refactoring of some tests in dbt.

* In progress

* OSM testing INSIGHT-2572
* ZoomInfo Location Enrich testing INSIGHT-2419
* New Pending MRR tests review and traceability matrix update

* Next week

* ZoomInfo Location Enrich testing INSIGHT-2419
* QA traceability matrix for critical metrics + test cases review

DE

* Completed
* In progress
* Next week

BI

* Completed

* Added additional fields to user rebill dash for CS specialists
* Small modifications of Email statistics dash (date filter and new style guide)
* LTV prediction dashboard switched to the new data source
* Added department from hr table to internal dashes

* In progress

* SRE dashboard, hourly data charts
* Penduing dashboard refactoring
* Active Users dashboard for IH
* Funnel dashboard for Local Unit datasource

* Next week

DG

* Completed

* Finalized Assigned Team dimension
* Autodoc for Datamart tables
* New Autodoc template

* In progress

* Prototyping autodoc on new template
* Awaiting DE to archive DP20 tables
* Awaiting feedback on Bus&Tech Ownership of top50
* Marketing dimensions: channel, sub channel, campaign, short url

* Next week

* Develop and test new autodoc

WA

* Completed

* App Center events table to sent through MP in GA4
* Listed all of service providers that are set up in GTM, with description and cookies their set (WA + Compliance documentation)
* New acquired asset tracking setup (OLAF, GA4, OWOX, CookieHub)
* Include Ads Launch Assistant in GTM tags, trial & payment

* In progress

* Drafted CookieHub CCPA & CPRA Documentation to align current setup with
* Tik Tik Pixel + LDU Function research and setup

* Next week

* Research UA & GA4 traffic discrepancies, fix and explain

Action items

* [Pavel/Mike] [DataGov Roadmap](https://www.google.com/url?q=https://miro.com/app/board/uXjVLdQnoVg%3D/&sa=D&source=editors&ust=1768225020027431&usg=AOvVaw20-hI-r7P2QKRXphKEnAz5)
* [Mike] Spain holiday – upcoming Tuesday, Sept 24
* [Mike] [BOTO project – please check it out / read the docs](https://www.google.com/url?q=https://docs.google.com/presentation/d/1zLTOLjtSVl9jpFU1lL1LnIFsbPMBsxsf7s5A9IepxZQ/edit%23slide%3Did.ga9fd6372a3_2_0&sa=D&source=editors&ust=1768225020027754&usg=AOvVaw1T9VQazj4dOAIUS2OcrA9R) :)

## Sep 13, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA5MTNUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020028038&usg=AOvVaw0u7Y_lSJpf0ZYWLW794Fbh)

Attendees: [r.rinchinov@semrush.com](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Anatolii Pokhylko](mailto:anatolii.pokhylko@semrush.com)

QA

* Completed

* QA knowledge transfer process
* QA team kb page creation

* In progress

* OSM testing INSIGHT-2572
* ZoomInfo Location Enrich testing INSIGHT-2419

* Next week

* QA Data Quality interview preparation ADQA-57
* OSM testing INSIGHT-2572
* ZoomInfo Location Enrich testing INSIGHT-2419

* Deferred



BI

* Completed

* Marketing dashboard refactor for Local Unit
* Small visual fixed in MRR dash

* In progress

* Active Users dashboard fro IH
* Funnel dashboard for Local Unit
* SRE dashboard
* Pending MRR dashboard refactor
* Rebills dashboard additional fields

DG

* Completed

* Corp User & sub-user dimension

* In progress

* Assigned Team dimensions, Marketing dimensions like channel, sub-channel, campaign, short url
* Helicopter view DG Strategy&Roadmap
* Table Docs Template & Datamart Auto-Doc
* Awaiting feedback on Bus&Tech Ownership
* Awaiting approval on list of tables to archive

WA

* Completed

* GA4 Main KPI Events Mapping → find ways to trigger events on .Trends
* Add event and parameter definitions to Google Analytics

* In progress

* VWO redirection fix
* Mismatch between UA streaming and GA4 streaming in source coming from affiliate
* Service providers setup through GTM documentation
* Set up ads launch assistant tracking events
* Delete Sensor GTM container → waiting to include main container code in /sensor
* Acquired asset [ExplodingTopics.com](https://www.google.com/url?q=http://explodingtopics.com/&sa=D&source=editors&ust=1768225020034743&usg=AOvVaw0T5cUERryTdkGC2MQt3D4w) setup.

* Next week

* VWO

DE

* Completed

* SRE table for Violetta (by  Natasha)
* New fields to Account table (for Vadim and Anya I)
* Exporting Google ads assistant related table from deep purple team (for Roma B)
* Restored emails related data that were affected during incident with pubsub

* In progress  
        -        Fixing remaining tables that need to be restored

* Exporting userMonetizationTypes table from Lava Team (for Roma B)

Notes

* [Mike] Performance Evaluation Launch

* What you need to know:

* In one sentence – Semrush is moving all the HR processes into Workday and now it’s time to TRY how Performance Evaluation will work
* The first iteration is starting on Sept 23
* They call the first interaction a “pilot” as it has some simplifications vs the further recurring process (like there were no “expectations” set)

* Action Points:

* Please find in your mailboxes the mail as of Spet 5th, titled “Performance Evaluation Launch” from Lisandro
* Please read it
* Please study the[learning resources](https://www.google.com/url?q=https://www.figma.com/proto/lAKDDPiKcBSRMm54gJec3m/Performance-Development-Playbook?page-id%3D194%253A916%26node-id%3D194-917%26viewport%3D759%252C831%252C0.3%26t%3D7vybaxDaJAbcXHnf-1%26scaling%3Dcontain%26content-scaling%3Dfixed%26starting-point-node-id%3D194%253A917&sa=D&source=editors&ust=1768225020039019&usg=AOvVaw0wq2fkjf4MwvJBOu6zMSvQ) by September 23 – it seems, it could take a couple of hours, so pls plan it in advance
* Please try to participate in the Webinar on the Performance Evaluation scheduled for all of us on Sept 20
* Please expect further steps, initiated by HR

* [Mike] Survival Mode for QA and DE

* DE Plan

* Our [Natalia Karpova](mailto:natalia.karpova@semrush.com) will be on “RU PTO” till Oct 3rd
* DE Newcomer will join us on Sept 30th
* Lead hiring moves rather slowly, lack of candidates
* [Anna Obyskalova](mailto:anna.obyskalova@semrush.com) will be the only DE for that time
* I know it’s tough, but please try to request only the most important tasks from DE
* Please keep all the lower-priority requests till Oct-Nov

* QA Plan

* [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) is the only QA for some time
* We’ve opened the Data Quality Engineer hiring
* Hiring is weak
* Again, please try to turn to QA (Katya) only with the most important requests, keeping “nice to have” things for the future

* [Mike] Business & Tech Owners Framework

* Next week – will send you an invite to share the update on the project

* [Mike] Retro today

* Would be great to have it
* Depends if we have enough to discuss

* [Mike / Nastenka] Tableau-Slack integration

Action items



## Sep 6, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA4MzBUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020042189&usg=AOvVaw1LEfIRepeAJrp74bwix4VG)

Attendees:  [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com)

QA

* Completed

* QA team kb pages update
* Traceability matrix draft version created

* In progress

* OSM testing INSIGHT-2572
* QA knowledge transfer process

* Next week

* QA knowledge transfer process till 11 sept
* QA team kb page creation
* OSM testing INSIGHT-2572
* ZoomInfo Location Enrich testing INSIGHT-2419

* Deferred

* All QA tasks till 12 sept

* BI

* Completed

* Change Live MRR to Frozen in Unit Overview and Advanced version of MRRhawk

* In progress

* Moved to BI testing Local Unit Marketing Dash and Active Users Dashboard for SMM
* Group Sanctioned countries in Dashboards
* SRE dashboard in progress -> added page\_path to product mapping table based on sm2
* Add department to internal dashes

* Next week

* DG

* Completed

* Interviews w/ Analysts

* In progress

* Helicopter view DG strategy
* Table Docs Template
* Awaiting feedback on Bus&Tech Ownership
* Awaiting approval on list of tables to archive

* Next week

* Collect feedback on list of tables to archive
* Add usage statistics to KB autodoc
* Present 1st iteration of DG Strategy

* WA

* Completed

* Guidelines for [Event tracking design](https://www.google.com/url?q=https://kb.semrush.net/display/AST/Recommendation%2Bfor%2BEvent%2BTracking%2BDesign%2Bin%2BGA4&sa=D&source=editors&ust=1768225020047024&usg=AOvVaw1RItk4r55_qIJZWpDBpH2m) in GA4 and OWOX
* GTM Server Side planning
* CookieHub Error installation → Pavel deleted useless CookieHub codes
* Create document for compliance to Check Bing and Google Ads remarketing tags
* Duplicate User Properties as Event Properties → to simplify querying in Bigquery

* In progress

* GA4 Main KPI Events Mapping → find ways to trigger events on .Trends

* Next week

* VWO
* Mismatch between UA streaming and GA4 streaming in source coming from affiliate

Notes



Action items

## 

## Aug 30, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA4MzBUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020050155&usg=AOvVaw2sl927GK17pK-a0Vq2CAUA)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com)

QA

* Completed

* [QA strategy](https://www.google.com/url?q=https://miro.com/app/board/uXjVKodqyfM%3D/?share_link_id%3D273638793018&sa=D&source=editors&ust=1768225020051370&usg=AOvVaw2GNVm5P_-QdhQkvwpm3uYM) preparation: shared with the team
* Marketing dashboard automated tests task: all tests are added
* Churn historical data testing
* QA JIRA [project](https://www.google.com/url?q=https://jira.semrush.net/secure/RapidBoard.jspa?rapidView%3D1105%26view%3Dplanning.nodetail%26selectedIssue%3DADQA-24%26epics%3Dvisible%26issueLimit%3D100%26selectedEpic%3DADQA-7&sa=D&source=editors&ust=1768225020052077&usg=AOvVaw39UmBn-NGSoi5yc6xxkWgV) created and backlog is organized

* In progress

* OSM testing INSIGHT-2572
* Marketing dashboard automated tests creation(cta32, frozen stork)

* Next week

* QA knowledge transfer process till 11 sept
* QA team kb page creation
* OSM testing INSIGHT-2572
* ZoomInfo Location Enrich testing INSIGHT-2419

* Deferred

* All QA tasks till 12 sept

* BI

* Completed

* Change Live MRR to Frozen in Unit Overview and Advanced version of MRRhawk

* In progress

* Moved to BI testing Local Unit Marketing Dash
* Group Sanctioned countries in Dashboards
* Active Users Dashboard for SMM
* SRE dashboard in progress

* Next week

* DG

* Completed

* Company size & Industry dimension unification
* Analyzed usage stats for tables in analytics-tableau-prod-tf , analytics-datamart-prod-tf and data-paradise-20. Prepared a list of tables for deprecation
* Finished interviewing Analysts

* In progress

* Helicopter view DG strategy
* Awaiting feedback on Bus&Tech Ownership

* Next week

* Archive tables Monday
* Add data usage to auto-documentation in KB

* WA

* Completed

* Product Localization report
* CookieHub marketing category bug

* In progress

* CookieHub Error installation → waiting for Pavel to delete unnecessary domain codes.
* Check Bing and Google Ads remarketing tags → [https://jira.semrush.net/browse/BI-317](https://www.google.com/url?q=https://jira.semrush.net/browse/BI-317&sa=D&source=editors&ust=1768225020056264&usg=AOvVaw2uZ3FoIn6_UK9myTbL3T1b)
* GA4 Main KPI Events Mapping → find ways to trigger events on .Trends
* Duplicate User Properties as Event Properties → to simplify querying in Bigquery

* Next week

Notes



Action items



---

## Aug 23, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA4MzBUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020057042&usg=AOvVaw05gDgr9A34Cs8qaAArI0fJ)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com)

* DE

* Completed

* Post migrations activity: hot fixing
* Troubleshooted cu short 2 days gap
* Billing additional details migration

* In progress

* Roma’s KTS
* Research how to move all analytics-team subscriptions to pythons script

* Next week

* Create detailed plan for deprecation of EU region
* Roma’s departure and last handover checks

* QA

* Completed

* QA strategy preparation: 1st version visualization
* Marketing dashboard automated tests review (tiktok and tread)

* In progress

* Churn historical data testing
* OSM testing INSIGHT-2572
* Marketing dashboard automated tests creation(cta32, frozen stork)

* Next week

* QA strategy preparation: 1st version presentation
* QA team kb page creation
* OSM testing INSIGHT-2572
* ZoomInfo Location Enrich testing INSIGHT-2419

* Deferred

* Start ga4 forecast table testing: less priority, no time
* Complete payments table description in kb (focus for Dimensions Unification project): less priority, no time
* New channels testing
* Subscriptions automated tests creation
* Marketo delayed queue of emails testing(planned, till Nastya is back from vacation, requested by Fedor) INSIGHT-2209

* BI

* Completed

* Added filter "if first payment" for Semrush, Unit, Limit and App into [Additional Limits Payments](https://www.google.com/url?q=https://tableau.semrush.net/%23/workbooks/2663&sa=D&source=editors&ust=1768225020060047&usg=AOvVaw2fEiRCWs12i9XvMzXRV1QD) & Leveled up from Bronze to Silver Additional Limits Payments dash
* Adjusted Stork Costs tab visual -> found problems with costs table, marketing team will fix

* In progress

* Active Users Dashboard’s for IH  datasource in progress
* Refactor Marketing Dash for Local Unit
* Sanctioned countries grouping in dashes (Violetta many thanks for function creation!!)[[e]](#cmnt5)
* SRE Dashboard 2d iteration → Create a source will all the traffic on the products and match with SRE data.
* User Rebills → Final step: make improvements in the dashboard, data is ready
* Churn Old Source Deprecation → archive all unused tables connected to the old source, update dashboards data

* Next week
* Start Funnel Dashboard for Local Unit
* Level up bronze -> silver Custom User Lists

* Help from DE

* SRE data source

* DG

* Completed

* Owners set up researched. Process for Metadata filling in dbt awaits approval.
* Knowledge from Roma taken (on owners, dbt & ci/cd)

* In progress

* CustDev Interviews
* DP20 bo&to for top50 tables acceptance
* DG Projects Roadmap (ongoing process)
* Company Size dimension documentation

* Next week

* Approve Owners&metadata set up process with Nastya&Mike
* Approve new DG projects with Nastya&Mike
* One-time clean up of sources

* Web Analytics

* Completed

* Events double check for App Center. → Find a missing event and create a trigger to fire the payment event.
* GA4 / GSC connect and sub-property creation. → Finish Looker Studio dashboard for /agencies directory for external SEO agency

* In progress

* GA4 Product Localization report → waiting for response from Elena
* CookieHub Error installation → Pavel Aleksandrov is discussing a few things with CookieHub support, waiting for him.
* CookieHub Marketing Category Bug → Waiting also to have a response from CookieHub Support, error seems to be on their side.
* Create table GA4 AppCenter events to sent with MP →  To send all the conversions to G4 and import them to GAds, events would be sent by EADA
* GTM Server-Side →  roadmap to create a list of tasks and make time estimations for their execution

* Next week

* GA4 Main KPI Events Mapping → understand events being fired and discuss with marketing team necessities
* Duplicate User Properties as Event Properties → to simplify querying in Bigquery

Notes

* [Paul] Architectural Overview Intro and Feedback Collection

Action items



---

## Aug 16, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA4MTZUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020064943&usg=AOvVaw19BbJX2a-pu_3J4BXzAgk5)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com)

Notes

* DE

* Completed:

* [AAI-2371](https://www.google.com/url?q=https://jira.semrush.net/browse/AAI-2371&sa=D&source=editors&ust=1768225020065687&usg=AOvVaw0UnmijqxT7Wdz4ZcKZtCvD) New field was added to fb tables (for deduplication)

* In progress:

* Migration to new billing invoice additional table from PaySol
* Investigation users table in scope of change cu\_short time interval task from Kostya (it looks like we have 2 days lag in users table)
* Roma prepares knowledge sharing sessions.
* Final preparations and checks for migration to the US region.
* Fixing some issues in churn historical data

* Next week plan:

* Perform several tasks from analysts

* QA ([Nastya Dotsina](mailto:anastasia.dotsina@semrush.com))

* Completed

* Marketing dashboard automated tests creation(CMO, NUMRR)
* Billing\_invoice\_additional\_addons\_scd testing

* In progress

* Churn historical data testing
* QA strategy preparation: 1st version
* Marketing dashboard automated tests creation(tiktok, tread, cta32)

* Next week plan

* QA strategy preparation: 1st version visualization and presentation
* QA team kb page creation
* ZoomInfo Location Enrich testing INSIGHT-2419
* OSM testing INSIGHT-2572

* Deferred

* Start ga4 forecast table testing: less priority, no time
* Complete payments table description in kb (focus for Dimensions Unification project): less priority, no time
* New channels testing
* Subscriptions automated tests creation
* Marketo delayed queue of emails testing(planned, till Nastya is back from vacation, requested by Fedor) INSIGHT-2209

* BI ([Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com))

* Completed

* Tableau server was updated. It required some additional testing for our side. This Saturday it will be restarted again to apply oAuth
* Updated Figma prototyping toolkit

* In progress

* SRE dashboard visual was finalized for the first part.
* REviewing high load extracts and dashboard to optimize server performance.
* User rebills dashboard updates
* Stork dashboard updates (costs tab)
* Additional payments dashboard
* Active Users dashboard for IH

* Deferred

* Corp user bug (Kostya is fixing a table for corp users data)

* Data Governance ([Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com))

* Completed

* Payment System dimension documentation

* In progress

* Old Churn table deprecation
* Old Users table depreciation (restricted users table usage in MR)
* CustDev to define DG pain points
* Owners set up and modifications research

* Web Analytics ([Violetta Lomako](mailto:violetta.lomako@semrush.com))

* Completed

* Discussed and Agreed on GTM scripts governance with GRC team

* In progress

* GA4 Product Localization Report
* GA4 / GSC connect and sub-property creation: can’t create sub-property, instead a Looker dash was made, on review
* Send App Center event with Measurement Protocol to GA4

Notes

* [Mike] DE – testing “Weekly Duty” for Analytics Requests: every week 1 person is Duty
* [Mike] Hiring Update – DE / BI we’ve chosen the final candidate. For DE – no Team Meering, for BI?

## Aug 9, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA4MDlUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020070901&usg=AOvVaw1UrqBNMkao7Kfh6wbBRNlo)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com)

* DE

* Completed:

* Churn historical data bug fix
* Recursion pipeline bug fix
* Downloaded a new geo Google Ads report for Maria
* Loaded pistachio business category predict
* Brought mart\_workday table from data team to our dwh

* In progress:

* Migration to new billing invoice additional table from PaySol
* Test owox location change
* Fb pixel deduplication

* Next week plan:

* De-integration of user-segments from UDH

* QA ([Nastya Dotsina](mailto:anastasia.dotsina@semrush.com))

* Completed

* Updating CTA32 tests for marketing
* Creating the first version of QA kanban board

* In progress

* Marketing dashboard automated tests creation
* Churn historical data testing

* Next week plan

* Subscriptions automated tests creation
* QA strategy preparation: 1st version
* Billing\_invoice\_additional\_addons\_scd testing
* New channels testing

* Deferred

* Start ga4 forecast table testing: less priority, no time
* Complete payments table description in kb (focus for Dimensions Unification project): less priority, no time
* ZoomInfo Location Enrich testing(planned, till Nastya is back from vacation, requested by Fedor) INSIGHT-2419
* Marketo delayed queue of emails testing(planned, till Nastya is back from vacation, requested by Fedor) INSIGHT-2209

* BI ([Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com))

* Completed

* Traffic source filter to Stork dashboards

* In progress

* SRE dashboard for platform stability (for cl-level). Many thanks to DE for pulling needed data for the dash!
* User rebills dashboards. In progress of rewriting code and adding limits so units can track users' rebill rate.
* High load extract review – have server performance issues

* Next week plan

* Migration to new churn table
* Fix figma prototyping process

This Saturday – Tableau server update.

* Data Governance ([Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com))

* Completed

* Classification of tables in data paradise by complexity matrix to define owners (37/50 of top-50 are simple.basic so can be owners by us)

* In progress

* Grouping of sanctioned countries in the dashes
* Payment system dimension documentation
* Tech audit of our data platform, [preliminary result](https://www.google.com/url?q=https://kb.semrush.net/display/ATI/Architecture%2Bof%2BData%2BServices&sa=D&source=editors&ust=1768225020076977&usg=AOvVaw3Xy4l4eXums8mGK4PubVwT)
* CustDev audit of our DG pain points

* Next week plan

* Take DG knowledge from Roman
* Owners research

* Web-Analytics ([Violetta Lomako](mailto:violetta.lomako@semrush.com))

* Completed

* Helped Agency to set up GA accesses for external agency
* Server Side GTM research finished and presented
* High Value Events added to the validation list along with is\_user\_activity for future PO dash

* In progress

* GA4 product localization report
* Events double check for App Center
* CookieHub Error Installation
* FB Conversion API setup

* Next week

Help from DE, QA:

* DE: SRE team data
* DE: Help with iso\_codes dictionary double check

Notes

* [Mike] Spain / Cyprus Holidays – Aug 15 (next Thursday) – the majority of the team will be out

* Please don’t release something important on Aug 14th

* [Mike] Roma’s departure

* We plan to clarify his last day on next week – it is between Sept 1 and Sept 30
* As of Aug 12 we’ll be focusing on Roma’s knowledge sharing
* Proposed a meeting on next Wednesday – at the time of Daily
* 2 topics from Team

* [Violetta Lomako](mailto:violetta.lomako@semrush.com) OLAF documentation / tables / logic – where is the knowledge?
* [Violetta Lomako](mailto:violetta.lomako@semrush.com) How to set up Streaming for GA4 properties
* [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) Tableau things: automations, hypers, extracts, subs
* [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) Facebook Conversion API ownership and documentation

* [Mike] Experimentation Team

* Folks will join Data Platform Unit in the nearest time (Timing – TBD)
* We’ll be three teams in our Unit

* [Mike] Retro meeting time

* Sam set a new meeting on the same time as Retro
* Propose to make Retro 1 hour earlier (14:30 CET instead of 15:30 CET)
* is everyone ok?

* [Mike] Engagement Survey

* Sam shared her plan for how we can “work with Engagement Survey results”
* Sam also would like our teams to work on some action points, that teams to propose
* We’ve [drafted 7 ideas](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1SFyhm-gOvt_TqGzgqFWRh3pZCpcH-8-i8w-gSM7XYcw/edit?gid%3D500463132%23gid%3D500463132&sa=D&source=editors&ust=1768225020080713&usg=AOvVaw3NUujdsVDXSjsf82gFNxUM)
* [Our plan](https://www.google.com/url?q=https://semrush.slack.com/archives/C04F2NEUB61/p1721993220881789?thread_ts%3D1721980491.657989%26cid%3DC04F2NEUB61&sa=D&source=editors&ust=1768225020080888&usg=AOvVaw3x7Hs96yfbrylRfLvrMGfN)
* Let’s meet next week to finalize “our part”

* [Mike] New DE candidate – Semyon

* Pls raise your hand if you’d like to conduct a “Team Meeting” with Syoma

* [Mike] “Team Meeting” (aka “Teambuilding” aka “Offsite”) in Belgrade

* Danil is working on it
* Planned for 28-31 October or 4-7th November
* we‘re waiting for further updates

* [Nastenka + Violetta] Facebook Conversion API ownership and documentation

Action items



---

## Aug 2, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA4MDJUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020081892&usg=AOvVaw0F1uhmjStfeTJjOwiGmEZe)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* DE ([Natalia Karpova](mailto:natalia.karpova@semrush.com))

* Completed:

* Loaded brand24 data for enterprise MRR

* In progress:

Downloading a new Google Ads report

Bringing one of mart\_workday tables from data team to analytics dwh

* Next week plan:

        Switch app\_payments on new billing invoice additional table from PaySol

* QA ([Ekaterina Esina](mailto:ekaterina.esina@semrush.com))

* Completed

* MRR dashboard testing (data issues and front-end fixes)
* Unit Overview dashboard testing: added App type

* In progress

* Marketing dashboard automated tests creation

* Next week plan

* Marketing dashboard automated tests creation

* Deferred

* Start ga4 forecast table testing: less priority, no time
* Complete payments table description in kb (focus for Dimensions Unification project): less priority, no time
* Churn historical data testing (bugs to be fixed): till Nastya is back from vacation (till 5th of August)
* New channels testing: till Nastya is back from vacation (till 5th of August)
* ZoomInfo Location Enrich testing(planned, till Nastya is back from vacation, requested by Fedor) INSIGHT-2419
* Marketo delayed queue of emails testing(planned, till Nastya is back from vacation, requested by Fedor) INSIGHT-2209

* BI ([Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com))

* Completed

* Unit Overview with Apps and MRRdashbord  in prod, many thanks to Katya!! <3

* In progress

* Active Users dashboard for IH
* SRE dashboard in progress

* Deferred

* Marketo tables transition, EADA have problems with setting semrush\_user\_id
* Corp users bug, need research from Kostya and Agatha

* Help from DE/QA team

* Nothing specific but maybe we’ll have a plan of removing Live Monthly MRR and some testing might be needed

* Data Governance ([Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com))

* Completed:

* Pending MRR in prod! Next steps: dashboard refactor and downstream migration to new table.
* Usage analysis of tables to define critical data sources for Ownership project

* In progress

* Company size, Industry dimension description, waiting for changes of table location

* Help from DE/QA team



* Web Analytics ([Violetta Lomako](mailto:violetta.lomako@semrush.com))

* Completed:

* Added a new event\_id to streaming and all Facebook conversions to handle duplicate pixels and conversions.
* Completed research, castdev with developers, and a web performance audit to decide on the server-side GTM solution.
* Handled the incident with Cookiehub that led to reduced new visitors' traffic for countries without explicit consent, such as the US.

* In progress:

* Adding a list of new events for activity criteria to the validator and preparing an announcement on how it will work.
* GA4 product localization report is ready for stakeholder review

* Help from DE/QA team

* Update FB tables with event\_id

* Topics to discuss
* [Nastenka] holidays in Spain?

* 15th of August is Spain & Cyprus holiday
* Diego on Vacation 12th - 18th

* [Nastenka] to Katya about testing experience of web-analytical tools (discussed with Violetta)

* [Violetta Lomako](mailto:violetta.lomako@semrush.com) and [Ekaterina Esina](mailto:ekaterina.esina@semrush.com)will discuss it together, maybe  we can add additional QA testing to web-analytics activites

Action items



## 

## Jul 26, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA3MjZUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020088473&usg=AOvVaw2fc9b4aVFGi4a2b0xrOlV9)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com) [Pavel Kuchin](mailto:pavel.kuchin@semrush.com)

Notes

* Weekly Update
* DE ([Roman Rinchinov](mailto:r.rinchinov@semrush.com))

* Completed:



* In progress:

* EU -> US migration – final preparations
* Deploying Voyantis pipeline

* Next week plan:

* Go to vacation 😀

* QA ([Ekaterina Esina](mailto:ekaterina.esina@semrush.com))

* Completed

* Regression testing of Unit type in Unit Overview dashboard

* In progress

* MRR dashboard bugs testing (data issues and front-end fixes)
* Unit Overview dashboard testing: added App type

* Next week plan

* Marketing dashboard automated tests creation
* MRR dashboard testing(bugs to be fixed)

* Deferred  
  - Start ga4 forecast table testing: less priority, no time  
  - Complete payments table description in kb (focus for Dimensions Unification project): less priority, no time

- Churn historical data testing (bugs to be fixed): till Nastya is back from vacation (till 5th of August)  
- New channels testing: till Nastya is back from vacation (till 5th of August)

- ZoomInfo Location Enrich testing(planned, till Nastya is back from vacation, requested by Fedor) INSIGHT-2419

- Marketo delayed queue of emails testing(planned, till Nastya is back from vacation, requested by Fedor) INSIGHT-2209

* BI ([Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com))

* Completed

* Added possibility to choose between attribution types in Stork dashes

* In progress

* Unit Overview fixes after testing
* MRR dash fixes after testing
* Active users dashboard for IH
* Adding First payments to additional payments limits
* SRE stability dashboard

* Help from DE/QA team

* Marketo?

* Data Governance ([Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com))

* Completed:

* Survey Segment Dimension documentation and data sources description

* In progress

* DWH structure documentation and description

* Help from DE/QA team

* DE: how to get usage statistics for tables and data sources. Will come with this question :)

* Web Analytics ([Violetta Lomako](mailto:violetta.lomako@semrush.com))

* Completed:

* Audit GTM container
* Updated cookie hub

* In progress:

* GA4 product localization report
* Link agency subfolder in GSC to GA4
* Research the best way to grant access only to a specific subset of data in GA4 as sub-properties are not available for us.

* Help from DE/QA team

* None, thank you

* Topics to discuss
* Alyona will be on vacation best two weeks
* [Nastenka] Marketo tables
* [Nastenka] data-platform channel, what about transferring tableau questions there?
* [Mike] We now run Engagement Survey Brainstorm during this meeting – do you believe we have anything for today’s Retro?

Action items



26th of July(Nastya filled her part, Katya to add her part)

## 

## Jul 19, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA2MjhUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020094241&usg=AOvVaw0UBHsW9ullYCf_bcz9XYgv)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com)

DE

* Completed:

- Updated R env to newer versions.

- New jupyterlab images were created.

- Voyantis pipeline

- GitLab runners switcher to admins (for stability)

* In progress:

* EU -> US migration
* Gitrunners: add deletion of docker-images
* Churn table - bug review

* Next week plan:

QA

* Completed

- Сhurn automated tests creation for prod table (no historical data)

* In progress

- Churn historical data testing (bugs to be fixed)  
- New channels testing

- MRR dashboard testing

* Next week plan  
  - MRR dashboard testing(bugs to be fixed)

- Marketing dashboard automated tests creation  
- Unit Overview testing: app is added

* Deferred  
  - Start ga4 forecast table testing: less priority, no time  
  - Complete payments table description in kb (focus for Dimensions Unification project): less priority, no time

- Churn historical data testing (bugs to be fixed): till Nastya is back from vacation  
- New channels testing: till Nastya is back from vacation (till 5th of August)

BI

* Completed

* none :(

* In progress

* MRR types to Paid Users within MRR dash (working with Nastya testing)
* Adding App to Unit Overview (testing will be required)
* SRE dashboard (DE help is required) [[f]](#cmnt6)
* Active Users dash for IH
* Pending MRR data source optimization

* Help from DE/QA team

* Bring SRE data to out external project (DE)
* QA testing for Unit Overview and MRR dash

Web Analytics

* Completed:

* OWOX streaming events problems  
  Then some magic happened and it apparently did fix itself.

Although I suspect that perhaps the provider did something, but hasn't notified me yet.

I think that we could hardly influence it from our side - it's a fine-tuning of the client.

But if you get feedback from the provider (if they even share a technical solution), please share it with us as well

Bug is not reproducible, none of us know why and how

* In progress:

* Audit and optimize GTM container
* Spotlight Conf Marketing Analytics
* CookieHub update

* Help from DE/QA team

* OWOX events remove duplicates (DE will start next week)

Notes

* [Nastenka] MR duty for merging

* BI can merge but approval is still required

* [Nastenka + Violetta] what’s happening with mergers (tests, script failures)

* Known issue, fixable



---

## Jul 12, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA2MjhUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020099614&usg=AOvVaw3589SbFEX0bLFao6Kyvana)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com)

### 

DE

* Completed:

* Prepared and deployed all R code and dbt for US migration
* Research how to move all analytics-team subscriptions to pythons script (a mechanism has been prepared)
* Exported data from Display & Video 360 API
* Updated app relations dictionary (applications.r\_app\_limits.sql)

* In progress:

* Research how to move all analytics-team subscriptions to pythons script (set up particular subscriptions)
* Preparation for migration to US

* Next week plan:

* Final checks of environment for migration to US
* Owox raw data deduplication
* Natalia’s vacation

QA

* Completed

- Unit Overview dashboard testing

* In progress

- Churn historical data testing (bugs to be fixed)  
- Сhurn automated tests creation for prod table(no historical data)  
- New channels testing

* Next week plan  
  - MRR dashboard testing  
  - Сhurn automated tests creation for prod table(no historical data)  
  - New channels testing
* Deferred  
  - Start ga4 forecast table testing(Less priority, no time)  
  - Complete payments table description in kb (focus for Dimensions Unification project)(Less priority, no time)

BI

* Completed

* Adding Full/Full ACA/Partial Churn split to [Churn Penguin](https://www.google.com/url?q=https://tableau.semrush.net/%23/workbooks/3139&sa=D&source=editors&ust=1768225020102200&usg=AOvVaw3AQ1fXPEfVoBWjfYh4AUZJ). This would allows units with Apps better to track full churn they can influence.
* Visual fixes of  [Churn Prediction](https://www.google.com/url?q=https://tableau.semrush.net/%23/redirect_to_view/36484&sa=D&source=editors&ust=1768225020102447&usg=AOvVaw2jYRP2FYJHArbrvJyyRVX9) LTV tab
* Finished research on how to add alerts to dashbors, First iteration is ready to use in [Units Overview](https://www.google.com/url?q=https://tableau.semrush.net/%23/workbooks/4934&sa=D&source=editors&ust=1768225020102657&usg=AOvVaw2qKOjZSOzQJAHjlrk1GYkc). In case of the next incident, we’ll be ready to try it out there.
* Applied all fixes after QA testing in [Units Overview](https://www.google.com/url?q=https://tableau.semrush.net/%23/workbooks/4934&sa=D&source=editors&ust=1768225020102887&usg=AOvVaw22AoCbERWZDqzzpauZKhgh)
* Added New+Returned Paid Users chart to [Units Overview](https://www.google.com/url?q=https://tableau.semrush.net/%23/workbooks/4934&sa=D&source=editors&ust=1768225020103074&usg=AOvVaw3tvdcyoXMbcBO7TIG_iTBv), this allows units to track not only new but their net increase in new and returned users
* Bug Fix Internal Dashes after data bugs

* In progress

* Churn table fixes after testing
* MRR types to paid users in [MRRhawk 2.0](https://www.google.com/url?q=https://tableau.semrush.net/%23/workbooks/4773&sa=D&source=editors&ust=1768225020103506&usg=AOvVaw3QsVW6cXctNeogvGTq61Em). need to finish naming and colors for a couple of charts, hope to move to testing next week
* Active users dashboard for IH
* Investigation on how to make "is first payment" filter for Additional limits Dash
* Testing Tableau server for updates, CH set up in progress

* Help from DE/QA team

* Gonna need help with dashboard testing from QA

Web Analytics

* Completed:

* Answered Agency Unit questions about GA4
* Semrush Conference events set up

* In progress:

* Debugging with Owox our current setup to identify the reason for duplicates

* Help from DE/QA team

* DE help with OWOX duplicates -> later QA testing of that

Notes

* [Roma] Roma’s Update
* [Mike] Hiring Update

## 

## Jul 5, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA2MjhUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020105026&usg=AOvVaw0-AmcNLg9jlq4XsN0BvSDD)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com)

### 

DE

* Completed:

* Migration of airflow VMs to the US region
* Preparation of all Python code and dbt for US migration
* Created slack notification if dbt test is failed (dashboard view is sent to the chat if test is failed, like alerting)
* Stopped relying on rows with zeros in billing\_subs\_addon table from paysol team

* In progress:

* Preparation of all R code and dbt for US migration
* Researching the possibility of unifying all Tableau email subscriptions in one place (slack and email)

* Next week plan:

* Check code readiness to migrate to us and decide what to do with R
* De-integrate user segments API from UDH
* Add clean up for images at gitlab runners in CI
* Complete everything in progress??

QA

* Completed:  
  - Main part of Churn transformations testing (prod table)
* In progress:  
  - Churn historical data testing (bugs to be fixed)

- Unit Overview dashboard testing

* Next week plan:  
  - Start new channels transformations testing

- MRR dashboard testing (dependent on BI)

- Complete payments table description in kb (focus for Dimensions Unification project)  
- Start ga4 forecast table testing

* No additional assistance from BI team required

BI

* Completed

* Host name task canceled after research. Stork fixes are needed.

* In progress

* Unit overview fixed after testing
* Local Unit dashes refactor, requirements gathering calls are in progress
* Helping IH with dashes (educational sessions)
* MRR types addition to MRRhawk dashboards. Most likely testing will be needed after prod.
* Churn Penguin visual fixes and adding more dimensions to the dashboards
* Created a plan on how to level-up dashboards quality labeling

* Next week plan

* Continue what’s in progress.
* MRR dash testing will be needed.

Web Analytics

* Completed:

* We successfully debugged the duplicates in the OWOX streaming table.
* We finished the setup for tracking on our new domain spotlightconf.com

* In progress:

* The onboarding process for Diego is going fine.
* Helping Agency Unit with GA4 questions

* Next week plan:

* Continue Diego's onboarding process to WA
* Prepare weekly Q&A session for CI designers about GA4 reports
* GTM Server Side Research pros and cons

Notes

* [Violetta] q about SurroundSound costs

Actions

* Create dash with dbt and non-dbt queries costs and give it to analysts so they’ll try to optimize it or archive
* Tag person in the slack if his query spends more than 100$ threshold

## Jun 28, 2024 | [Weekly Unit Sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DNmRrcWh0aTdhOGtjcjMzYzNrdDM0ZmdwMzNfMjAyNDA2MjhUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020109990&usg=AOvVaw0YGWVTwP5A54cLxgYm-l83)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Diego Paz](mailto:diego.paz@semrush.com)

Notes

* [All] Welcome Diego!
* [All] Brainstorm the Agenda / Structure of Weekly Unit Sync
* [Mike] Engagement Survey – Division Meeting next Tuesday, hosted by Sam

* No prep required, Sam will share the key findings + plan

* Absences

* [Nastenka] how to request pto in workday….?
* [Mike] Roma wants PTO for the next week? I just miss it in analytics-department-hr
* [Mike] Next Firday – CZ Holiday (affects only Mike)

* Will [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) be able to run the meeting please?

* [Mike] Next week there’s a newcomer in insights Damir

* Proposal to meet with 2 newcomers Jelmer + Damir in 2 weeks, on Jul 12

* [Mike] [Platform Stability Metric 1.0](https://www.google.com/url?q=https://semrush.slack.com/archives/C04F2NEUB61/p1719508979701239?thread_ts%3D1718705771.478159%26cid%3DC04F2NEUB61&sa=D&source=editors&ust=1768225020111983&usg=AOvVaw3vAohezStyWa-7ub5yePVn) – ready to release it?
* [Mike] Retro topic for today?

* from Mike – is our prev Retro’s discussion of Analytics Engineer

* [Nastenka] Dashboards Stylegulde was updated!
* [Nastenka] to DE – ”moving Tableau subscriptions to Python” tasks – do you have a vision when it could be completed?

* Plan to start next week, the time-frames to be defined after research

* [Nastenka] How do Business / Tech Owners thing is going?

Agenda of this Weekly Unit Sync ideas:

* Goal – is to give a brief overview of what each of the teams did on the current week and what is planned for next week
* Speakers:

* BI & Data Governance
* Web Analytics
* Data Eng
* QA
* GREGORY :)

* Form:

* Short Written Summary in this doc + Verbal description in roder to answer q’s

* Content:

* Mike proposes try to group activities and focus on high-level status (if it makes sense for a specific activity)

* Proposal from Mike, example of Violetta representing Web Aanlytics:

* Web Analytics
* Finished X and
* In progress Y projects + ad hoc requests, onboarding Diego
* [option] Prelim plan for next week project Y and Z
* [option] If any support of anyone req’d next week

Action items



## 

## Jun 21, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA2MjFUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020115065&usg=AOvVaw1Xqn-CIu0kWQcwC3fpiVV8)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com)

Notes

* [Mike] Both positions for us were approved!

* BI Engineer – to ensure we will well cover Semrush-wide dashboards
* Junior DataEng – to take over routine & standard migration tasks, allowing more senior folks to concentrate on the more hardcore projects

* [Mike] Sam is in Barcelona on 29-31 July

* Would be great if you can be in the office to see her in person

* [Mike] As of next week we’re splitting our “AI Kanban syncs” to 2 teams
* [Mike] Our Q3 Plan

* See our actual [Portfolio 2024-2025](https://www.google.com/url?q=https://miro.com/app/board/uXjVKMXdVVw%3D/&sa=D&source=editors&ust=1768225020116394&usg=AOvVaw3niox9gKx30Vh228vUrHH-)
* Update for Voyantis question – Voyantis will integrate into Google Ads directly, our help is not needed
* Update from Nikita on “MRR Frozen / Activity Criteria” on QA support – Regarding MRR (not only Frozen) we expect to have support with creating auto-tests for pre-MRR stages,[https://semrush.slack.com/archives/C072U3RTU4D/p1716467651668199](https://www.google.com/url?q=https://semrush.slack.com/archives/C072U3RTU4D/p1716467651668199&sa=D&source=editors&ust=1768225020116994&usg=AOvVaw2p9xy2G68_cNOvbLlFtADe). Regarding activity criteria - probably nothing so far.
* Update on “EU -> US” Infra migration – Roma was able to speed up the migration and now we plan to make a one-time “switch” to US in the very beginning of September

* [Mike] #analytics-requests are blessed to be deprecated!
* [Mike] There was an initiative that we’d need to have our own channel for external requests (like #analytics-data-platform-requests)

* Mike will need to collect ideas for what we want to solve there. Will create a doc for async brainstorming

* [Mike] Spain is on holiday next Monday, so Data Platform Eng’g Team – see you on Wed
* [Mike / Nastenka] Stason Offboarding Doc

* [https://docs.google.com/document/d/1uWUoBIm3aVVg1IGuxJ9N3zQPIOjHYGlucnQwcW58zaY/edit](https://www.google.com/url?q=https://docs.google.com/document/d/1uWUoBIm3aVVg1IGuxJ9N3zQPIOjHYGlucnQwcW58zaY/edit&sa=D&source=editors&ust=1768225020118045&usg=AOvVaw1xr3q51tp0VATcn5gR4MwN)
* please contribute into it to ensure Stason won’t forget to hand it over :)

 

Action items

* [Mike Trifonov](mailto:mike.trifonov@semrush.com) to create a discussion aroun “#analytics-data-platform-requests” – as per above

## Jun 21, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA2MjFUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020118647&usg=AOvVaw2hRBrI1xbrVTOozIdpMVn2)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com)

Notes

* [Mike] Ownership of Users – testing right now: on Mike & Nastya (Subs tables should be the next one)
* [Mike] Spain national holiday next Monday
* [Mike] Brainstorming on Q3 priorities – tomorrow
* [Mike] Anya & Natasha – could you pls check you’ll be able to participate in tomorrow’s EU->US Project review?
* [Mike] We’ll have our “Team coffee meeting” with Pavel (DataGov) – pls nominate the“lead interviewer”?
* [Mike] Data Platform Eng’g Team – daily / bi-daily meetings?
* [Nastya] Business / Tech Owners

Action items



---

## Jun 19, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA2MTlUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020120094&usg=AOvVaw0q4R92mA1yakIccQIG-DhC)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com)

Notes

* [Mike] A channel for external requests to our Unit

* Idea – the questions that cannot be covered by Data Buddy or existing dedicated channels (like ga4, gtm, else?), could be raised there
* Possible namings

* data-platform-requests
* analytics-data-platform-requests
* analytics-data-helpdesk
* Analytics-helpdesk

* Types of q’s

* To be discussed

* [Mike] Daily meetings for Data Platform Engineering Team

* pros/cons

Action items



---

## Jun 17, 2024 | [Evgeniy S. + AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA2MTdUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020121531&usg=AOvVaw202WftQRECrWvogUasqpkE)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Evgeniy Sobolev](mailto:e.sobolev@semrush.com)

Notes

* [All] Eugeniy
* [Mike] Release the release
* [Alyona] We need to fill in Workday by Jun 21 – but what to update?
* [Mike] Retro – we agreed to move in one week

Action items

* [Mike Trifonov](mailto:mike.trifonov@semrush.com) to clarify what is required from us re Workday

## Jun 12, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA2MTJUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020123016&usg=AOvVaw0M8ZkJKBEOFyyJqd69i3Hk)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Roma] [Roman Rinchinov](mailto:r.rinchinov@semrush.com) will share Marketo tables with [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com)

Action items



## Jun 10, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA2MTBUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020124690&usg=AOvVaw02oh0HamSfp1FONBhS_pgN)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Ekaterina Esina](mailto:ekaterina.esina@semrush.com)

Notes

* [Mike] Voyantis – [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Natalia Karpova](mailto:natalia.karpova@semrush.com) [Anna Obyskalova](mailto:anna.obyskalova@semrush.com)

* Anya will lead, and Roma will support in case of any issues

* [Natenka] Stork / SaaS reports come rather late

* Could we re-schedule Stork to another time
* SaaS reports version from 8th of June contained MRR issues – yes, there were issues w/ ML projects

* [Roma] Not-Incident on July 8th?

* Every month “LTV forecast” fails every 8th. Stason said he’ll refactor it
* Let’s delete it?
* [Mike Trifonov](mailto:mike.trifonov@semrush.com) to ask [Nikita Kudriavtsev](mailto:nikita.kudriavtsev@semrush.com)

* [Roma] OLAF & bots

* Roma recalls that nobody knew how to distinguish Bots

* [Violetta] OLAF cookie for Analytics Div purposes

* Mike: Stepan forbade usage of OLAF cookie as we wanted
* Right now we do not have any option to do it

* [Anya] [Evgeniy Sobolev](mailto:e.sobolev@semrush.com) maybe joined Analytics Div?

* We’ll know abt it tomorrow on Ringleaders’ meeting

Action items

* [Mike Trifonov](mailto:mike.trifonov@semrush.com) to talk to [Nikita Kudriavtsev](mailto:nikita.kudriavtsev@semrush.com) abt the above

---

## Jun 7, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA2MDdUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020129395&usg=AOvVaw0RFLMwAmOcem_IKhSrC24U)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Katya Esina](mailto:ekaterina.esina@semrush.com)

Notes

* [Mike] Incident
* [Nastenka] - SF tables copying

* [Mike Trifonov](mailto:mike.trifonov@semrush.com) to follow up w/EADA / [Nikolai Grushin](mailto:n.grushin@semrush.com) [Sam Bishop](mailto:lynne.bishop@semrush.com)

* [Mike] Changes of Kanban Syncs
* [Mike] “Russian Club”

* On Mondays

* [Mike] Aliases for DE / QA / WA  in slack.
* [All] Absences

* [Nastya Dotsina](mailto:anastasia.dotsina@semrush.com) and [Mike Trifonov](mailto:mike.trifonov@semrush.com) – absent on Wed-Friday
* [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) – absent on Wed

Action items



---

## Jun 5, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA2MDVUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020132372&usg=AOvVaw0j0_ba1IzpcPzVxVlxtn8_)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com) [Katya Esina](mailto:ekaterina.esina@semrush.com)

Notes

* [All] Welcome [Katya Esina](mailto:ekaterina.esina@semrush.com) and [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com)
* [Mike] Hiring update

Action items



---

## Jun 3, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA2MDNUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020134228&usg=AOvVaw0Q4EfavHrXeZnNJJiv7Bq2)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] Release the release
* [Mike] New Structure
* [Mike] For Violetta & Anya

* Grisha with us on these meetings
* Diego’s first working day is Jun 26
* Btw, for Katya’s first day – mike still not sure, likely in a week (to be clarified)

* [Mike] ChatGPT – changes “licensing”

* Now it’s personal
* Costs $30/month
* please indicate who from our team would need it?

* [Alyona Kotovich](mailto:alena.kotovich@semrush.com) [Anna Obyskalova](mailto:anna.obyskalova@semrush.com) [Nastya Dotsina](mailto:anastasia.dotsina@semrush.com) [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Violetta Lomako](mailto:violetta.lomako@semrush.com) [Natalia Karpova](mailto:natalia.karpova@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com)[Mike Trifonov](mailto:mike.trifonov@semrush.com)

* [Mike] Business Owners + Tech Owners

* Roma made an update: now we have TWO owners in dbt
* We with Roma redefined these roles and would like to check with you
* Mike will write you separately in weissbier-infra channel
* NB! We’d need to think how it will work for Tests

Action items



---

## May 31, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA1MzFUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020138320&usg=AOvVaw35vphMApX1wXqhEafaKMHS)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes



Action items



---

## May 29, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA1MjlUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020139657&usg=AOvVaw2y6ggw3-hgVezgXs5TyBuR)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] Grisha – to “sit with us” not to be alone)
* [Mike] BI alert
* [Mike] Request for Violetta: creation of container

Action items



---

## May 24, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA1MjRUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020141363&usg=AOvVaw1VNtPL6iq7oOzAv2FXulvR)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] today’s Retro is for Team Meeting w/Sam

* I propose to keep the same process as we had during our recent meeting w/Anna, Marat & Sasha
* Please be ready to share a bit abt you)
* I guess we will have too many focus on Sam, so we won’t need to “switch to regular retro”. Bur pls suggest if you want to run meeting w/Sam -> then regular Retro

* [Nastenka & Mike] Tableau Aleting to Weissbeir-infrastructure

* Mike’s idea is to move it to proper dedicated channel

* [Nastenka]

* Idea – maybe we want to run “BI Talks” to share experience b/w diff Analytics Teams
* Idea – maybe we can share w/ them “Infra Talks”?
* Question – are we ready to share our best practices?

Action items



---

## May 20, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA1MjBUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020144025&usg=AOvVaw3Z5vPp-_o1NFIQ8vNIW-VD)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] Release the release
* [Mike] Team Meeting with Diego – [Alyona Kotovich](mailto:alena.kotovich@semrush.com)?
* [Mike] Incident
* [Nastenka] Migration to Tableau 23 (incl tech issues fix, migration to US)

Action items



## May 17, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA1MTdUMDkzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020145031&usg=AOvVaw1LJuwZG0cx1W2V64VxyNUI)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [nastenka] - task to research possbility to add several dashes into one email – will do with sbs unify logic

Action items



## May 15, 2024 | [Meeting w/ Anna, Marat & Sasha + AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA1MTVUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020145867&usg=AOvVaw1bTXw8yxKoYTo7Ct7x88UV)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Anna Khachatryan](mailto:anna.khachatryan@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Alexandra Dumchenko](mailto:a.dumchenko@semrush.com)

Notes

* [All] Meeting w/ [Anna Khachatryan](mailto:anna.khachatryan@semrush.com) [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) [Alexandra Dumchenko](mailto:a.dumchenko@semrush.com)

Action items



---

## May 10, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA1MTBUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020146968&usg=AOvVaw24ZDkRiGm9rul69a_PlddY)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Nastenka] copy to data mart or cl?

Action items



---

## May 6, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA1MDZUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020147741&usg=AOvVaw1L4pcPJ9o8I1lnHZUavC0A)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] to release the release
* [Mike] Reminder on Days Off this week

* CZ – Wednesday
* Nastya – May 9-10 (PTO)
* Natasha – May 9-10 (PTO)
* Nastenka – May 8-9 (Conference)
* Roma – could be morning 7 May

* [Mike] We’ll meet with the newcomers [Anna Khachatryan](mailto:anna.khachatryan@semrush.com) and [Marat Yuldashev](mailto:marat.yuldashev@semrush.com) on our Kanban Sync on May 15

Action items



---

## May 3, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA1MDNUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020149100&usg=AOvVaw0KUVfatgvDc6ksYrMLrNTy)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] New insight analyst in Andrei’s team – she almost does not speak Russian

Action items



---

## Apr 29, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA0MjlUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020149943&usg=AOvVaw3-uvrVmZubCtsToV-bwpp0)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] release the release
* [Mike] Wednesday Kanban Sync – to be cancelled

Action items



---

## Apr 26, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA0MjZUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020150833&usg=AOvVaw39WB7kfqV_0LFVAKVz9Pj5)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] Vova is leaving
* [Mike] Engagement Survey
* [Mike] Jira. Natasha’s task is disappearing, seems due to GitLab – who knows how to fix it?
* [Mike] Retro – did it slide by 1 hour or is it at the same time? Is this time ok for everyone?
* [Roma] App\_payments migration to MRR-data
* [Alyona] Educations in Rubles

* Интерфейсы (полезно троим) [https://bureau.ru/courses/ui-online/](https://www.google.com/url?q=https://bureau.ru/courses/ui-online/&sa=D&source=editors&ust=1768225020151908&usg=AOvVaw0DArXqiu5d_Ax1a5PLI6N9)
* Визуализация (Алёна хотела) [https://bureau.ru/courses/data-online/?utm\_source=bu-c-data-online-260324](https://www.google.com/url?q=https://bureau.ru/courses/data-online/?utm_source%3Dbu-c-data-online-260324&sa=D&source=editors&ust=1768225020152200&usg=AOvVaw1A_0ENS0_TlLybky3oYY6g)
* Верстка (мы с Виолеттой хотели бы) [https://www.igorshtang.ru/course/](https://www.google.com/url?q=https://www.igorshtang.ru/course/&sa=D&source=editors&ust=1768225020152430&usg=AOvVaw1XoD3aXwejN70G79TRqkCD)
* Про тимлида (я бы хотела) [https://tough-dev.school/teamlead](https://www.google.com/url?q=https://tough-dev.school/teamlead&sa=D&source=editors&ust=1768225020152631&usg=AOvVaw2ez-PuQLGsim2bBzaxiwBo)

Action items



---

## Apr 24, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA0MjRUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020153185&usg=AOvVaw3L3bhpmfKcHTj1uHqHiAW9)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] The release was released
* [Mike] Engagement Survey
* [Mike] Incident
* [Mike] Probation Period -> Strategy / Our New Roles
* [Mike] Hiring update
* [Mike] Our assessment cycle
* [Mike] May holidays

* CZ + Nastenka – 1+8 May
* SRB – 1-6 both incl.
* ES – 1 May

* [Mike] Nastya’s PTO?

* 25 – 30 Apr
* 9-10 May

* [Mike] Natasha PTO

* 9-10 May

* [Mike] Anya PTO

* 2-3 May

Action items

* [Mike Trifonov](mailto:mike.trifonov@semrush.com) to set a weekly Incidents discussion

---

## Apr 19, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA0MTlUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020154864&usg=AOvVaw2BeifCLUmQP6Dv-hZ6jtud)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] Absent on Monday – Could [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) help to run the Meeting on Monday?

Action items



---

## Apr 17, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA0MTdUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020155722&usg=AOvVaw3o0YqbkHMc_O69WKsnb_GH)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes



Action items



---

## Apr 15, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA0MTVUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020156400&usg=AOvVaw1Cpe24A1O6ntQnsLPj9MW7)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] Release the Release

Action items



---

## Apr 12, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA0MTJUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020157077&usg=AOvVaw0Jm1MU7Cfm1NFJyBr4Kf5X)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Nastenka] Tableau mailings

* Agreed to start test the approach asked by it\_support:
* they won’t give a new license, but ask us to modify mailing forwarding logic to include the new user (it should help to reduce the number of licenses)
* In ~June we agreed to start refactoring the process of mailing from all the current solutions to Python API

Action items



---

## Apr 10, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA0MTBUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020158346&usg=AOvVaw1u6XoOyCL0BOunyh_gCMUO)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com)

Notes

* [Mike] Final on Hiring:

* BI Developer – Danil shifted to Q3
* QA Engineer – opening hiring now
* Data Governance Engineer – opening hiring now
* Web Analyst – opening hiring now

* [Violetta] Questions from Developers on GA4 enhancements

* Maybe we could have a str parameter to store json to save in BQ?



Action items



---

## Apr 8, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA0MDhUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020159716&usg=AOvVaw2Bmz8yBAPvvf5uwi9jazKa)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com)

Notes

* [All] release the release
* [Mike] New Incident?

Action items



---

## Apr 5, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA0MDVUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020160530&usg=AOvVaw2npeF-FilH0dl57oaBivv8)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] Thank some of you – we’ve send the Job Descriptions for initiation of Hiring process:

* Data Governace, QA, Web Analyst – full throttle
* BI – under investigation

* [All] Let’s make a new channel for External users who contact Infra Team

* Let’s add the bot to route the FAQ

Action items

* [Mike Trifonov](mailto:mike.trifonov@semrush.com) and [Violetta Lomako](mailto:violetta.lomako@semrush.com) – sit together to hand over some responsibilities (granting accesses) to #it\_support ( [Ioannis Karlakis](mailto:i.karlakis@semrush.com))
* [Mike Trifonov](mailto:mike.trifonov@semrush.com)to make a new channel for External users

---

## 3 Apr 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDA0MDNUMDkzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020161979&usg=AOvVaw0pUriWDCpLAMBCn53Adxww)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Nikita Kudriavtsev](mailto:nikita.kudriavtsev@semrush.com)

Notes

* [Nikita] Vova is leaving Semrush ~ May 1

* PRS project goes to Kirill
* Other – to Yulya

* [Nikita] Stason is leaving Semrush between Jun 15 – Jul 15

* ML predictions – we hope the newcomer will take
* MRR – Stas volunteers to be a backup

* [Nikita] Data Party is opening 2 positions:

* Analytics Engineer
* “Data Analyst with Love to ML” – we have a strong candidate

* [Nikita] Other Projects

* Daily Report refactoring – delayed till Q3
* User Segments – Online Predictions – Nikita wants to do this early, but it is likely in Q4

Action items



---

## Mar 27, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAzMjdUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020164565&usg=AOvVaw2rhDiqFdHJPta6wMabzArT)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Violetta] New request on email for taxation?

* It’s received by “old employees” only (Mike doesn’t have it)
* Violetta’s point – it’s not clear what is the process. KB’s link is not enough.

Action items

* [Mike Trifonov](mailto:mike.trifonov@semrush.com) to ask HR to host a live session on Shares – for at least 4 of us.
* [Mike Trifonov](mailto:mike.trifonov@semrush.com) to get ChatGPT for all

## Mar 25, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAzMjBUMTAzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020165796&usg=AOvVaw2FxtNp2zAzGcE-0TlT5ZEG)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

Notes

* [Mike] CZ/ES Holiday on Friday + Next Monday - [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Natalia Karpova](mailto:natalia.karpova@semrush.com) [Violetta Lomako](mailto:violetta.lomako@semrush.com) [Anna Obyskalova](mailto:anna.obyskalova@semrush.com)
* [Mike] Time change! 31 Mar – CZ, ES, SRB
* [Natya + Nastenka] PTO since the beginning of April

## 

## Mar 22, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAzMjBUMTAzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020167246&usg=AOvVaw1-zxCr9BA847m-_h_MociN)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) 

Notes

* [Mike & Nastya] When we plan to go to PTO and write into #analytics-department-hr  – let’s add who will act on our behalf once we are out.

* Do you support it?
* Counter-proposal:

* For absence of ≥5 days: To keep dates + backup in Slack PTO status

* [Mike & Nastya] Process of Testing Bug tracking

* We’d like to start a small pilot in AI team to track testing activities for any testing by QA

* Pilot for 1,5 months: starting from this week till end of April
* For Infra team

* When Nastya tests something and finds any issues – she creates a dedicated task (“bug” type) for the testing requestor and
* You’re asked to change the status once it’s solved
* Are you ok w/it?

* For External requests

* Nastya creates/updates bugs for external stakeholders

* [Nastenka] can we expense education from Russian courses? Like BURO
* [Violetta] PTO back up

* ~April 15–25
* Could be back ups: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Natalia Karpova](mailto:natalia.karpova@semrush.com)
* Urgent Questions:

* BI – BI Team
* GA4

* We want to route all the request to GA4\_channel
* Case 1: Addition of new Values into Validator into lists: Allow\_lists Teams and Products  – [Natalia Karpova](mailto:natalia.karpova@semrush.com)?

* Validate?
* Add
* Merge (which is to write to XXX Team to merge)

* Case 2: For “Event Verification” questions – to send user to data buddy or send to KB – [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com)
* All the rest: waits for Violetta

* GTM approvals

* We want to route all the request to GTM\_channel

Action items

* [Mike Trifonov](mailto:mike.trifonov@semrush.com) to check with HR if we can pay for Russian courses in thru “education budget”
* [Mike Trifonov](mailto:mike.trifonov@semrush.com) to arrange a meeting wth the above persons for [Violetta Lomako](mailto:violetta.lomako@semrush.com)’s PTO

## 

## Mar 20, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAzMjBUMTAzMDAwWiBhbmFzdGFzaXlhLmt1em5ldHNvdmFAc2VtcnVzaC5jb20&sa=D&source=editors&ust=1768225020170855&usg=AOvVaw0EVnRxh8J-DGU7tOUPYYk0)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Gregory Timofeev](mailto:grigorii.timofeev@semrush.com)

Notes

* [All] Welcome Gregory!
* [Mike] Mike is back from Product Courses – thanks [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) for backing up
* [Nastenka] вопрос про открытие документации сторонним аналитикам, Вадим собирает список источников, которыми они пользуются, чтобы оторвать доступ до centering land и давать только до data-paradise
* [Nastenka] как перевезти всех из cl в data paradise
* [Mike] Danil asked Mike to lead the “GA4 migration” project

Action items



## 

## Mar 11, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAzMTFUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020172257&usg=AOvVaw0T57RHb-BdiE7vZpxa_fP5)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] Release the “release”
* [Mike] Just to remind if something – Mike is on PTO on Tuesday
* [Mike] Mike will have to be late to our Kanban Syncs on Wednesday and Friday

* was appointed to a 6-hour Product Course: Wed-Friday
* Will be 30 minutes late on both days
* Could [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com)lead the meeting on Mike’s behalf pls (and not wait for Mike)?

* [Mike] Due to the same reason I modified some of our meetings this week
* [Mike] BTW, received no info from you for your “news” for the last week. I wrote my impressions but still would appreciate it if you’d be able to highlight your achievements to recognize them on a wider level. thanks)
* [Mike] MEMO: here’re all the SLAs we’ve collected on Analytics Team’s services to external teams – [https://kb.semrush.net/pages/viewpage.action?pageId=169639446](https://www.google.com/url?q=https://kb.semrush.net/pages/viewpage.action?pageId%3D169639446&sa=D&source=editors&ust=1768225020173860&usg=AOvVaw0DCCRxASkxplywvFdxLMb-)
* [Mike] Mike’s proposal for Business / Tech Owners:

* Owner could be a particular person or a team
* Let’s set TWO Owners for any table in “data paradise” and "datamarts" projects:
* Business Owner is responsible for:

* Table life-cycle (they decide to create/update/delete the table in this project)
* Define/collect Business Requirements to this table with exact calculation methods (which tables, fields, and calculations should be used)
* Define the Logic on how the table should be composed

* Technical Owner is responsible for:

* Table creation/update/optimization in line with requirements and conventions/policies (incl. naming, code styling, performance, cost)
* Enabling table uptime (incl, tests, monitoring & alerting)
* Be the first to investigate incidents with this table (if the problem in business logic – to address to the Business Owner)

* In our team’s structure, the Business Owners are mainly Insight Birds and Data Party. Technical Ownership could be spread across diff teams, in the end, i’d like to focus infra team to be the Technical Owner for the majority of the tables.

* [Mike] Mike’s proposal for minimal Documentation:

* When anyone asks to add any new table to datamarts project, infra team will kindly ask the requestor to provide the Minimal Documentation in KB catalog as a new page in the below format.
* Any newly created Table cannot be moved to datamarts without Minimal Documentation
* Minimal Documentation proposal

* Table Name (clickable link to BQ)
* Table Description – what this exact table contains: a paragraph of several sentences, which should help to understand what this table is about in principle
* Major Use Cases (if exist) – just to say what key purposes this table serves
* Table Schema
* Key Upstreams (if exist) – to list the key upstream Sources for this table (like Cancellations, Churn, MRR etc.)
* Business Owner – person to contact about this table
* Technical Owner – person to enable table availability & quality

* [Naskenka] Wants to have a transparent “lineage” b/w dashboards-sources-tests

* Why? We want to be able to find easily all the tests associated with the certain dash/source

Action items



---

## Mar 8, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAzMDhUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020177681&usg=AOvVaw1FNCZ803u8s4lMa2XuZ65E)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] Management Reporting – pls contribute today
* [Mike] 24/7 support of API and Truebuchet..

Action items



---

## Mar 6, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAzMDZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020178687&usg=AOvVaw2Y5Y_8rJ5BusMLMbSa-COa)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] Incidents handling – could you pls share what do we have on hands
* [Mike] ask team on naming convention (ci check?)
* [Mike] share abt Labelling Project
* [Mike] share abt EU->US project
* [Mike] team building update
* [Mike] Data Sources in “Data Marts” BQ project documentation req’s

* Pls ask Nikita

Action items



---

## Mar 4, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAzMDRUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020180138&usg=AOvVaw2xhvP7ojlQiL-gAUYet-Ik)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] Release the “release”
* [Mike] just to mention that Mike’s PTO is shifted from Mar 5 to Mar 12
* [Mike] Incident on Airflow

* [Roma] Issues not with Scheduler
* 2 VM went out of memory → Airflow lock → 2 tasks were frozen
* Impact: delay ~12 hours
* Fix:

* Roma to reconfigure VMs
* Roma to add time-outs in the “problematic” DAGs
* Anya is in progress of setting Monitoring of VMs

* [Violetta] Does it impact the clustered Streaming?

* [Roma] seems yes



Action items

* [Roma] To craft the dailt alerting at 9:00am CET if hyper-tables for MRR dashed are not updated  – in weissbier-infrastructure

---

## Mar 1, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAzMDFUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020181919&usg=AOvVaw3pmwO01xlL3a3jlve_BlKH)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] Jim’s visit results:

* EADA has a huge long-list of projects thay would like to do
* EADA does not have a detailed plan for our coop as we hoped to get
* We were able to craft a 2027 plan [Miro](https://www.google.com/url?q=https://miro.com/app/board/uXjVNnUlRY0%3D/&sa=D&source=editors&ust=1768225020182663&usg=AOvVaw2_JLEytV56gwF9zFsnSR1w) which assumes
* Integrations Ownership

* To handover ownership of pipelines TO SFDC in Q1-Q2
* To handover integrations FROM and TO 3rd parties in Q2

* Certifications

* EADA and Analytics team will work on our own sources & dashboards “certification” implementations in 2024
* However, we will sync trying to align on our list of certification criterias
* BTW, our current list for Dash certifications is almost ready – now it’s being discussed with Analytics Ringleaders and Mike plans to get their final support on upcoming Monday

* We’ll work to align on MRR calculations

* Should be a tough cookie
* Mike prepared the highlevel MRR Landscape [Miro](https://www.google.com/url?q=https://miro.com/app/board/uXjVNmzb0zM%3D/&sa=D&source=editors&ust=1768225020183767&usg=AOvVaw1GdOHkEFAH0fnQXZFAMCQU)
* Further joint actions – TBD

* Crafting a common definition of “Customer Account” – there’s a project in IT which has a goal to create a SSOT (sinlge-source of truth) for Customer Account

* Current action items – to investigate the current usage of Cust.Acc. in Analytics – on [Mike Trifonov](mailto:mike.trifonov@semrush.com)
* Mike to ask [Nastya Dotsina](mailto:anastasia.dotsina@semrush.com)

* No other active collab is seen for 2024 (EADA will focus on HR / Finance data in 2024)

* [Mike] We do have our Retro today, where we’ll welcome [Yuliya Batova](mailto:yuliya.batova@semrush.com) today

Action items



---

## Feb 28, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAyMjhUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020185124&usg=AOvVaw2owf9AKCEI5H-MVHZOD6W2)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] PTO March 5th

Action items



---

## Feb 26, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAyMjZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020185962&usg=AOvVaw05gXthYafWtuAxlXcRh3wF)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] to compose a Release
* [Mike] Repeatnig for [Alyona Kotovich](mailto:alena.kotovich@semrush.com)and [Nastya Dotsina](mailto:anastasia.dotsina@semrush.com):

* [Yuliya Batova](mailto:yuliya.batova@semrush.com) invites all of us to participate in the Coaching sessions!

Action items



---

## Feb 23, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAyMjNUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020186967&usg=AOvVaw2S4n6gpTZBfGsYDNZE_1Ce)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Roma] Vacation – next week Monday-Wednesday
* [Mike] Roma’s approved to move to Spain this summer – congrats!
* [Mike] [Yuliya Batova](mailto:yuliya.batova@semrush.com) invites all of us to participate in the Coaching sessions!

* Yulia is now being certified as a Career Coach, she offered us her help
* Def: Coaching is when an individual works with a trained professional in a process of self-discovery and self-awareness. Working together, the coach helps the individual identify strengths and develop goals. Together, the coach and coachee practice and build the skills and behaviors required to make progress toward their goals.
* She can coach any of us for our career/professional development
* It is optional and you can always “skip in” and “skip off”
* Interested? – just pls write to [Yuliya Batova](mailto:yuliya.batova@semrush.com) or [Mike Trifonov](mailto:mike.trifonov@semrush.com)

* [Mike] Next week [Jim Orefice](mailto:jim.orefice@semrush.com) (director of Data Team, Kolya’s boss) will be in Prague

* We’ll be discussing the alignment b/w our teams
* Mike’s calendar is squeezed, so will have to reschedule or cancel some of our 1x1  meetings for the next week (only)

* [Mike] Question from Wire Team

* [https://semrush.slack.com/archives/C0559JL54C8/p1708596708647479](https://www.google.com/url?q=https://semrush.slack.com/archives/C0559JL54C8/p1708596708647479&sa=D&source=editors&ust=1768225020189233&usg=AOvVaw2BOUTGCSCfhsIjoj1043Do)
* К нам в чатик команды пришли с вопросом, что пользователь 6095199 не получает письма tracking-2021-alerts, так как отписан.
* Будет возможность выгрузить аналитику по тому, когда данный пользователь отписался от этих писем?
* Mike would like to hear opinions, why it’s us doing it / how can do it

Action items



---

## Feb 21, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAyMjFUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020190038&usg=AOvVaw2c9U1OOnzAYjFAgPthtERD)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] We’ve created the [“BI project” in Jira](https://www.google.com/url?q=https://jira.semrush.net/secure/RapidBoard.jspa?rapidView%3D1039%26projectKey%3DBI&sa=D&source=editors&ust=1768225020190541&usg=AOvVaw09da1C4RgRP5hP2Gegcgle) and [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) is casting some magic there, testing how it works
* [Mike] [Referrals for Insight Analysts are welcome](https://www.google.com/url?q=https://semrush.slack.com/archives/C04F2NEUB61/p1708432197189929&sa=D&source=editors&ust=1768225020190820&usg=AOvVaw35Ktu71wCfodBvRL2WbnXm)!
* [Mike] We are no more Data Buddy for anything
* [Nastya] Is on PTO this Friday
* [Nastenka] George asks for a new Dash (beneficial for the whole Company)

* But it requires Research – George should do it himself

* [Mike] only to [Violetta Lomako](mailto:violetta.lomako@semrush.com) re:

* Andrey Shapovalov  [12:06 PM]
* Hi Mike! It’s Andrey from the Brand Marketing team, Violetta directed me to you so that I could have her time on this task:
* She previously helped with creating of a custom script for Marketing Landing pages (it connects the headline of the page with the keyword from Paid Search channel). And now I need to update it and change the logic. Will it be possible to have Violetta’s time this week to help us out?

Action items



---

## Feb 19, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAyMTlUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020192241&usg=AOvVaw0qhGKY_ZyleqL50w6W1wI7)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] close the “release” of prev week
* [Mike] pls don’t forget to [fill in the file](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1VQhwJjraveK0fhzRlQvBsIg2jf9UxADpjU4BFaxHoWc/edit?usp%3Dsharing&sa=D&source=editors&ust=1768225020192846&usg=AOvVaw2Z4ChyFOFwjMXPIOI8rL-O) for LLM/GenAI use cases
* [Mike] FYI: As per our invitation, [Yuliya Batova](mailto:yuliya.batova@semrush.com) would like to join us on our Retro (Mar 1st)
* [Mike] 30 mins for AI Infra review set on this Thur, plus we’re collecting your q’s in [slack](https://www.google.com/url?q=https://semrush.slack.com/archives/C04F2NEUB61/p1708338062344649&sa=D&source=editors&ust=1768225020193259&usg=AOvVaw3BuqI06z-BvfpiB1aCwkDT)
* [Mike] UAE is closing Russian bank accounts?
* [Nastenka] it\_support is forgetting to add users to the groups for Tableau

* [Aleksei Gerasimov](mailto:aleksey.gerasimov@semrush.com)

* [Natenka] There was a “plan to make a plan” from Danil’s side / it\_support

* Abt the roadmap of migration to personal accounts in Tableau
* And now they are granting personal + group accounts in mix. We don’t understand the logic and want to see a roadmap

Action items

* [Mike Trifonov](mailto:mike.trifonov@semrush.com) to investigate the issue with it\_support and addition to Tableau groups
* [Mike Trifonov](mailto:mike.trifonov@semrush.com) to get the it\_support / Danil’s roadmap

---

## Feb 16, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAyMTZUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020194518&usg=AOvVaw01b4AphspmTMhhJUGgg0RO)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [ALL] Happy Birth Day, Roma!
* [Mike] Analytics Priorities for Q1

* [Officially declared Priorities](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/19zO1BvuLB29I_i-7_UQi92Pn5OA6tpyScmkSx9ko5KI/edit?pli%3D1%23gid%3D1391485739&sa=D&source=editors&ust=1768225020195231&usg=AOvVaw3nPsL8e9du7kst9wg6Cg09)
* Question to all – To which initiatives do we contribute?

* [Mike] Experiment with Jira “BI” project

* Reason: Jira is not flexible right now and we cannot have more than 3 levels of tasks (Epic/Task/Subtask)
* We want to test a new Jira project “BI” in parallel to “AAI”
* We want to see if it’ll be handy and efficient for “cross-project” task tracking
* Draft structure in “BI” project:

* Epic = Dashboard
* Tags = Units

* [Mike] Usage of GenAI / LLM

* LLMs – are the great performance booster, but using it inside our “public company” could be associated with some risk of data leakage to the outer world (like what you send to ChatGPT is logged inside, so everything you’ve sent there - is already “leaked”)
* Please [fill in the file](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1VQhwJjraveK0fhzRlQvBsIg2jf9UxADpjU4BFaxHoWc/edit?usp%3Dsharing&sa=D&source=editors&ust=1768225020196523&usg=AOvVaw2r3WGLLtgCm4Sp1jGn_IjF) to track or your actual and wished use cases for LLM at work

* [Mike] jfyi: [Yulia Kondratenko](mailto:iuliia.kondratenko@semrush.com) is moving from [Insights] to [dparty]
* [Mike] jfyi: [Nikita Kudriavtsev](mailto:nikita.kudriavtsev@semrush.com) will be on PTO next week
* [Mike] HR updated our [file with “Admin” questions](https://www.google.com/url?q=https://docs.google.com/document/d/1IYkE8ctVIcmpygtZgNVaXhgsjkluCtVwP2V9GPZO-Ik/edit?usp%3Dsharing&sa=D&source=editors&ust=1768225020197047&usg=AOvVaw0rYJCMsf8myht1yHU4Nfr0) – please have a look
* [Violetta] Meeting w/Google

* Users w/o Consent -> we’re proposed to write our cookie to event\_properties
* So this “tech” cookie” gives us a trick to match the user

Action items



---

## Feb 14, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAyMTRUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020197758&usg=AOvVaw0-gsZ0cfy1i9WAS5-B8zTv)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] MEMO: Our [Roles Register](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1MuUvW4DVo0RhMAHOGTWMib2iCm7yotk8uNdrd3BqfpY/edit?usp%3Dsharing&sa=D&source=editors&ust=1768225020198297&usg=AOvVaw21smYl1xQRBHtzYWIoNIPv) is here. Thanks for your contribution!
* [Mike] Do you like to add HR Yulia Batova to our monthly Retroes?
* [Mike] We as Data Buddy?

* Violetta – for External Products, HR Brand
* All – for “IT / Tech” teams
* All – Wire Team

Action items

* [Mike Trifonov](mailto:mike.trifonov@semrush.com) – to add Yulia to our nearest Retro

* [Mike Trifonov](mailto:mike.trifonov@semrush.com) – What is Data Buddy?

---

## Feb 12, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAyMTJUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020199236&usg=AOvVaw0YduYNrLYuYMCxCN5DozUH)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* Decision: [Nastya Dotsina](mailto:anastasia.dotsina@semrush.com) works under Russian holidays calendar
* Decision: [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) works under Czech holidays calendar

Action items

* [Mike Trifonov](mailto:mike.trifonov@semrush.com) subscribe to Vacations Calendar (stas Kolomin in trash)

---

## Feb 9, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAyMDlUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020200356&usg=AOvVaw3misJZ8eZlEBZoGgVgOMz3)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [Mike] MRR pipeline to SFDC fail
* [Mike] Travel to other Russia/Belarus
* [Mike] Travel to other Countries
* [Mike] Insights Team Retro today - do you go?
* [Mike] Add 30 mins meeting after “AI Kanban Sync” for “informal talks”

Action items



---

## Feb 7, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAyMDdUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020201525&usg=AOvVaw2Y8wUi2B0YeZWOtxtykcfM)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Analytics Infrastructure](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com)

Notes

* [All] Holidays

* Spain: Feb 12-13 (short week)
* Serbia: Feb 15-16 (short week)
* [https://calendar.google.com/calendar/embed?src=semrush.com\_oal23nqou2ilvuj520fl7miuqk%40group.calendar.google.com&ctz=Europe%2FPrague](https://www.google.com/url?q=https://calendar.google.com/calendar/embed?src%3Dsemrush.com_oal23nqou2ilvuj520fl7miuqk%2540group.calendar.google.com%26ctz%3DEurope%252FPrague&sa=D&source=editors&ust=1768225020202351&usg=AOvVaw0Re9HM2h8ID01SH10Wuqma)

* [Mike] Infra Diagrams

* [Infra Data Flow](https://www.google.com/url?q=https://miro.com/app/board/uXjVNykQY3Y%3D/?moveToWidget%3D3458764577920853831%26cot%3D14&sa=D&source=editors&ust=1768225020202547&usg=AOvVaw3QBYTWGzPxU-GQOCuzVbWX)
* [Code CI/CD](https://www.google.com/url?q=https://miro.com/app/board/uXjVNykQY3Y%3D/?moveToWidget%3D3458764577921157109%26cot%3D14&sa=D&source=editors&ust=1768225020202682&usg=AOvVaw2NnQ4YYqdsD27ld4C7oG-7)



Action items

* [Mike Trifonov](mailto:mike.trifonov@semrush.com) to arrange 30 mins to review our Architecture (to collect q’s in advance)
* [Mike Trifonov](mailto:mike.trifonov@semrush.com) to clarify what to do if teammate is planning to go to other country - what is the process?

---

## Feb 5, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAyMDVUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020203387&usg=AOvVaw3HuyH6lj063e-qEyqg1VYe)

Attendees: [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [analytics-infrastructure@semrush.com](mailto:analytics-infrastructure@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Kostya Perevozchikov](mailto:k.perevozchikov@semrush.com)

Notes

* [Kostya] Masha Andreikovich is leaving for sabbatical as of Feb 28 for 3 months

* Insight Analytics capacity will be really limited

* [Mike] English’fication

* Let’s keep the channel “wissbeir-infrastructure” in English
* Current meetings – let’s switch to English as of next meeting?
* Mike will try to use English in 1x1 slack

* [Mike] Infra Diagrams

* [Infra Data Flow](https://www.google.com/url?q=https://miro.com/app/board/uXjVNykQY3Y%3D/?moveToWidget%3D3458764577920853831%26cot%3D14&sa=D&source=editors&ust=1768225020204731&usg=AOvVaw3Q_3HORBVAu0rzdbx1KQwH)
* [Code CI/CD](https://www.google.com/url?q=https://miro.com/app/board/uXjVNykQY3Y%3D/?moveToWidget%3D3458764577921157109%26cot%3D14&sa=D&source=editors&ust=1768225020204952&usg=AOvVaw12aVfSlj9tL5t-wBNFQPJ6)

* [Mike] don’t you mind if i’ll rename the “weissbeir-infrastructure” channel into something less-alcohol-related?

 

Action items

* We’d need to discuss the process of collab w/ [Violetta Lomako](mailto:violetta.lomako@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Anna Obyskalova](mailto:anna.obyskalova@semrush.com) – [Mike Trifonov](mailto:mike.trifonov@semrush.com) to arrange a meeting

* Mike to discuss code ownership w/ [Roman Rinchinov](mailto:r.rinchinov@semrush.com) and [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com)
* Mike to gather a meeting to discuss cross-domain topics: olaf, other ([Roman Rinchinov](mailto:r.rinchinov@semrush.com), [Violetta Lomako](mailto:violetta.lomako@semrush.com))
* Mike to take over tasks [from Olya](https://www.google.com/url?q=https://jira.semrush.net/secure/RapidBoard.jspa?rapidView%3D543%26projectKey%3DAAI%26view%3Ddetail%26selectedIssue%3DAAI-1284%26quickFilter%3D4763&sa=D&source=editors&ust=1768225020206571&usg=AOvVaw0m2EAnwDwrbfiZfArEgmLO)
* [Mike Trifonov](mailto:mike.trifonov@semrush.com) Efficiency of M&A vis Cross-domain audience tracking. Mike to investigate our role etc. Mike pls check with Dparty

---

## Feb 2, 2024 | [AI kanban sync](https://www.google.com/url?q=https://www.google.com/calendar/event?eid%3DMXA4NTY5Z2N0OWVlYjBzNGk0aXVydDltdDdfMjAyNDAyMDJUMTAzMDAwWiBtaWtlLnRyaWZvbm92QHNlbXJ1c2guY29t&sa=D&source=editors&ust=1768225020207235&usg=AOvVaw34U4QpvQYcvF8afhOtEoEh)

Attendees: [Alena Kotovich](mailto:alena.kotovich@semrush.com) [analytics-infrastructure@semrush.com](mailto:analytics-infrastructure@semrush.com) [Nastya Dotsina](mailto:anastasia.dotsina@semrush.com) [Nastya Kuznetsova](mailto:anastasiya.kuznetsova@semrush.com) [Anna Obyskalova](mailto:anna.obyskalova@semrush.com) [Mike Trifonov](mailto:mike.trifonov@semrush.com) [Natalia Karpova](mailto:natalia.karpova@semrush.com) [Olga Kosyreva](mailto:o.kosyreva@semrush.com) [Roman Rinchinov](mailto:r.rinchinov@semrush.com) [Violetta Lomako](mailto:violetta.lomako@semrush.com) 

Notes

* [Kostya] Kostya will tell about analytics update
* [Mike] Agenda & Structure for these meetings:

* Start when everyone is on the call, not later than hh:02
* [All] Kanban Review
* [Mike] Any Announcements
* [All] Work-related Sync Topics
* [All] Non-work-related Sync Topics
* [Groups] Dedicated discussions

* [Mike] Results of the Happiness Survey
* [Nastenka] Clickhouse and Nulls (if Null: indexes are working weirdly)

* For any q’s re Clickhouse pls turn to [Azat Khuzhin](mailto:a.khuzhin@semrush.com) – our local Clickhouse developer

* [Nastenka] Webinar for Karpov.pro courses

* [Mike Trifonov](mailto:mike.trifonov@semrush.com) pls see #analytics-internal: [https://semrush.slack.com/archives/G011Q58AZKR/p1701271827442299](https://www.google.com/url?q=https://semrush.slack.com/archives/G011Q58AZKR/p1701271827442299&sa=D&source=editors&ust=1768225020210212&usg=AOvVaw0zQ2C2Ksfu4vOsbhxkyDZc)

Action items



[[a]](#cmnt_ref1)@maksim.degtiarev@semrush.com please move it to Completed if it is recalculated in the morning

[[b]](#cmnt_ref2)👍

[[c]](#cmnt_ref3)@mike.trifonov@semrush.com

[[d]](#cmnt_ref4)@mike.trifonov@semrush.com

[[e]](#cmnt_ref5)On prod -> completed

[[f]](#cmnt_ref6)@violetta.lomako@semrush.com create a task for DE (Roma/Anya)