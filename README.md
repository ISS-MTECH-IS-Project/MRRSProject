## IRS-PM-2022-01-29-IS04-GRP8-OhMyFish


------------


## SECTION 1: PROJECT TITLE
### OHMYFISH - Your Friendly Pet Fish Veterinarian


------------


## SECTION 2: EXECUTIVE SUMMARY
#### Preface
The Group Project is one of the key learning outcomes of the Intelligent Reasoning System (IRS) Graduate Certification and in this report, details the extensive but extremely rewarding learning journey we (Group 8) have undertaken to alleviate the impacts brought about by Covid-19 on the pet fish veterinary services in relation to pet fishkeeping hobbyists. This report details the problem statement and our investigative research journey for a solution through the analysis performed, approaches evaluated through trail-and-error, knowledge and insights formed, and observations made.

#### Problem
Covid-19 in Singapore has had a profound impact on our daily lives, completely upheaving the physical and social interactions that many have relied on all their lives for companionship. This resulting cataclysm has caused many to seek companionship through pet ownership with fishkeeping being highly popular due to the lack of licensing regulations as well as being an affordable hobby when entry-level pet fishes are concerned. Despite all the reasons making pet fishkeeping a popular hobby, the unravelling of limited availability of professional veterinary services during the pandemic coupled with limited published knowledge of pet fish care and limited of self-service options have left many hobbyists frustrated when their beloved pet fishes fall sick and eventually succumb to diseases. 

#### Opportunity
With the pet fish imports and exports in Singapore valued at USD$40M in 2020, the growing fraternity of pet fish hobbyist amidst the highly limited professional veterinary services lies a lucrative business opportunity that can be tapped into with an intelligent reasoning system built to offer self-diagnostic veterinary capabilities. The system built based on knowledge and various techniques acquired throughout the learning journey of the Intelligent Reasoning Systems (IRS) Graduate Certificate, will be able to solve the underlying problems brought about by the impacts of Covid-19 namely availability of veterinary services, accessibility of knowledge of pet fish diseases and symptoms and on-demand self-service diagnostic inquiry to enable hobbyists to triangulate on the most possible disease suffered by their pet fishes. 

#### Solution
The proposed solution in response to the business opportunity is an intelligent reasoning veterinary ChatBot entitled OhMyFish that is built upon a knowledge base of pet fish diseases, enabling hobbyists to perform diagnostic inquires for their pet fishes suspected to be suffering from diseases through an iterative set of textual inputs describing the symptoms observed, acknowledging recommended symptoms or a combination of both until OhMyFish is able to triangulate on the most probable diseases with the highest confidence scores accumulated during the inquiry process. OhMyFish will offer two approaches to inquiry, namely Guided and Unguided. Guided approach is meant for novice hobbyists with OhMyFish taking charge of the inquiry from symptom recommendations to disease triangulation while Unguided approach is meant for expert hobbyists to discover the symptoms leaving only the disease triangulation to OhMyFish.

#### Design and Techniques
OhMyFish is based on an Object-Oriented design built on a Three-Tier Architecture to ensure future development can easily extend the system design and to scale for future growth. Using a combination of Natural Language Processing, Natural Language Understanding, Deductive Reasoning, Logic-Based Inference and Reinforced Learning, the underlying design of OhMyFish involves a Four-Stage Process consisting of Text Pre-Processing (Input Processing), Topic Modelling (Input Understanding), Knowledge Base Inquiry (Response Selection) and Decisioning (Action Plan Generation and Response) [1].
Given OhMyFish is a chatbot that primarily processes textual data where such data in its native form is both sparse and unstructured which will require “connecting the dots” [2], a Graph Database has been determined to be the most suited data model to identify relationships between diseases, symptoms, treatments as well as similarity or dissimilarity [2].
A hybrid exploratory method of Investigative Research and Trial-And-Error forms the guiding principle behind an iterative process backed by a data-driven approach was adopted to determine the various techniques in consideration and select the most optimum technique to form the core reasoning intelligence of OhMyFish. To that end, a total of four techniques were comprehensively evaluated and with spaCy with Text Pre-Processing augmented with Custom Stopwords being selected as one of the core techniques underpinning the first two stages of the four-stage process. The final two stages of the four-stage process are then underpinned by Custom Heuristic Model that adopts a weighted approach whereby diseases with higher confidence are accorded higher weightages through having more associated symptoms that are unconfirmed returned for confirmation during the diagnostic inquiry.

#### Closing Thoughts
Through the union of design and techniques adopted to implement this Minimum Viable Product (MVP) version built upon a limited dataset, OhMyFish has been evaluated to have meet its intended purpose of being an intelligent reasoning veterinary chatbot to enable hobbyists to perform diagnostic inquires on their pet fishes with reasonable accuracy. Further, OhMyFish solves the three problems of limited availability, limited published knowledge, limited of self-service with being always available, published knowledge base and unlimited self-service to all hobbyists.
And while there is good value in this MVP version, there are obvious limitations that inhibits a tremendous amount of untapped potential amidst a lucrative business opportunity in Singapore that can be unlocked with future development on OhMyFish to unlock further capabilities. These future development opportunities include Speech Recognition (Speech-to-Text and Text-to-Speech) for a genuine conversational capability, Computer Vision to enable the usage of images and videos of pet fishes, Sentiment Analysis to evaluate the usefulness of the diagnostic inquiry to the hobbyist, 3rd Party Integrations to applications like Telegram and Whatsapp, Plugins to External Knowledge Bases such as Quora and KPI Measurements to measure performances. There remains in OhMyFish and this domain, much room for further research and future development to improve, and limitless untapped potential.

1. X. Lu, S. Leslie, L. Kay and J. C. L. Chow, “Chatbot for Health Care and Oncology Applications Using Artificial Intelligence and Machine Learning: Systematic Review,” National Library of Medicine, 29 November 2021. [Online]. Available: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8669585/
2. D. A. Negro and D. V. Kus, “Bring Order to Chaos: A Graph-Based Journey from Textual Data to Wisdom,” neo4j, 19 September 2018. [Online]. Available: https://neo4j.com/blog/bring-order-to-chaos-graph-based-journey-textual-data-to-wisdom/


------------


## SECTION 3: CREDITS / PROJECT CONTRIBUTION
|  Full Name |  Student ID | Work Item Contribution  | Email  |
| ------------ | ------------ | ------------ | ------------ |
| Lim Eng Hwee Jason  | A0180557Y  | 1. Team Leader<br/>2. Designing the data preparation module<br/>3. Ideation<br/>4. Architecture and System Design<br/>4. Neomodel layer abstraction and data access layer<br/>5. Filling up data fields related to disease treatments and causes<br/>6. Cleaning up CSV and labelling of diseases and symptoms<br/>7. Front-end UI enhancements and revamp of desired cosmetic (user) behaviours<br/>8. Testing of front and backend integration<br/>9. Test cases write up and test evaluation<br/>| e0284043@u.nus.edu |
| Tan Sio Poh | SXXXX916J  |   | siopoh@gmail.com |
| Teo Wei Ming  |  A0249278M | 1. Contributed to the initial ideation and selection of the idea<br/>2. Established the project proposal<br/>3. Defined the problem statement, business opportunity, solution with the value proposition<br/>4. Project managed the scope and delivery schedule<br/>5. Participated and contributed to the system architecture and module designs<br/>Researched on the pet fishkeeping and market value in Singapore<br/>7. Established the executive summary and conclusion<br/>8. Amalgamated the project report<br/>9. Developed the Conversational Control Module (CCM) | weimingteo@u.nus.edu |
| Teoh Jeng Wei  | A0093899B  | 1. Ideation<br/>2. System architecture and application logic flow designs<br/>3. Data Acquisition and Knowledge Discovery<br/>4. Web scrapping to extract and structure information<br/>5. Data ingestion into neo4j Graph DB<br/>6. Marketing and System Architecture videos<br/>7. Storyboarding, animation, scripting, AI audio creation and video-audio synchronization. | e0938628@u.nus.edu |
| Wang Song  | A0026411X  | 1. Ideation<br/>2. Architecture and System Design<br/>3. Designs and coding the Knowledge Base Decisioning Model<br/>4. Design and code the backend APIs and frontend logic to integrate with the backend APIs.<br/>5. Integration of all components<br/>6. Installation guide, class diagram and knowledge base model. | wangsong@u.nus.edu |


------------


## SECTION 4: ARCHITECTURE DESIGN AND DEMO VIDEO



------------


## SECTION 5: INSTALLATION & USER GUIDE

#### Installation for Windows OS
[Click here to go to the Windows Installation Section](https://github.com/TeamEightIS04/MRRSProject/tree/main/EnvironmentSetup/Windows "Click here to go to the Windows Installation Section")

#### Installation for Linux OS
[Click here to go to the Linux Installation Section](https://github.com/TeamEightIS04/MRRSProject/tree/main/EnvironmentSetup/Linux "Click here to go to the Linux Installation Section")


------------


## SECTION 6: User Guide
[Click here to see the User guide](https://github.com/TeamEightIS04/MRRSProject/blob/main/Documentation/User%20Guide.docx "Click here to see the User guide")


------------


## SECTION 7: PROJECT REPORT (OUTLINE)

#### Please refer to the detailed report found in ProjectReport in Github

1	Executive Summary<br/>
2	Introduction<br/>
2.1.	Problem Statement<br/>
2.2.	Business Opportunity<br/>
2.2.1.	Availability<br/>
2.2.2.	Accessibility<br/>
2.2.3.	Self-Service<br/>
2.3.	Proposed Solution<br/>
3.	Design<br/>
3.1.	Conceptual<br/>
3.2.	Architecture<br/>
3.2.1.	Presentation Tier<br/>
3.2.2.	Application Tier<br/<br/>>
3.2.3.	Data Tier<br/>	
3.3.	Class Diagram<br/>	
3.4.	Data<br/>	
3.4.1.	Data Preparation<br/>	
3.4.2.	Data Ingestion to Neo4j<br/>	
3.4.3.	Neo4j to Internal Python Objects<br/>	
3.4.4.	Saving User Case Diagnosis to Neo4j for Expansion of Knowledge Graph<br/>	
3.5.	Flow Diagram<br/>	
3.6.	Sequence Diagrams<br/<br/>>	
3.6.1.	Guided Approach<br/>	
3.6.2.	Unguided Approach – Expert<br/>	
3.7.	Core Reasoning Intelligence<br/>
3.7.1.	Topic Modelling Module (TMM)<br/>	
3.7.1.1.	Structure of Graph Database for Fish Diseases<br/>	
3.7.1.2.	Finding the Best Technique<br/>	
3.7.1.3.	Verdict<br/>	
3.7.2.	Knowledge Base Decisioning Module (KBDM)<br/>	
3.7.2.1.	Developing a Custom Heuristic Model<br/>
3.7.2.2.	Verdict<br/>
3.7.3.	Summary of Hyperparameters<br/>	
4.	Technology Stack<br/>	
5.	Test Results and Evaluation<br/>	
5.1.	Test Results<br/>	
5.2.	Evaluation<br/>	
6.	Known Limitations and Opportunities for Future Development<br/>	
7.	Conclusion<br/>	
8.	Appendix<br/>
8.1.	References<br/>	
8.2.	Image References<br/>	
8.3.	Project Proposal<br/>	
8.4.	Mapping of System Functionalities and Modular Courses<br/>
8.5.	Installation Guide<br/>
8.5.1.	Linux<br/>	
8.6.1	Windows<br/>	
8.7	User Guide<br/>	
8.8	Team Member Reports<br/>	
8.8.1	Jason Lim Eng Hwee<br/>
8.8.2	Tan Sio Poh<br/>
8.8.3	Teo Wei Ming<br/>
8.8.4	Teoh Jeng Wei<br/>
8.8.5	Wang Song<br/>
