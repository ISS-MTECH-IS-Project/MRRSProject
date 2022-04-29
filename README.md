## OHMYFISH - Your Friendly Pet Fish Veterinarian

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


------------


1. X. Lu, S. Leslie, L. Kay and J. C. L. Chow, “Chatbot for Health Care and Oncology Applications Using Artificial Intelligence and Machine Learning: Systematic Review,” National Library of Medicine, 29 November 2021. [Online]. Available: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8669585/
2. D. A. Negro and D. V. Kus, “Bring Order to Chaos: A Graph-Based Journey from Textual Data to Wisdom,” neo4j, 19 September 2018. [Online]. Available: https://neo4j.com/blog/bring-order-to-chaos-graph-based-journey-textual-data-to-wisdom/

## CREDITS / PROJECT CONTRIBUTION
|  Full Name |  Student ID | Work Item Contribution  | Email  |
| ------------ | ------------ | ------------ | ------------ |
| Lim Eng Hwee Jason  | A0180557Y  | 1. Team Leader<br/>2. Designing the data preparation module<br/>3. Ideation<br/>4. Architecture and System Design<br/>4. Neomodel layer abstraction and data access layer<br/>5. Filling up data fields related to disease treatments and causes<br/>6. Cleaning up CSV and labelling of diseases and symptoms<br/>7. Front-end UI enhancements and revamp of desired cosmetic (user) behaviours<br/>8. Testing of front and backend integration<br/>9. Test cases write up and test evaluation<br/>| e0284043@u.nus.edu |
| Tan Sio Poh | SXXXX916J  |   | siopoh@gmail.com |
| Teo Wei Ming  |  A0249278M | 1. Contributed to the initial ideation and selection of the idea<br/>2. Established the project proposal<br/>3. Defined the problem statement, business opportunity, solution with the value proposition<br/>4. Project managed the scope and delivery schedule<br/>5. Participated and contributed to the system architecture and module designs<br/>Researched on the pet fishkeeping and market value in Singapore<br/>7. Established the executive summary and conclusion<br/>8. Amalgamated the project report<br/>9. Developed the Conversational Control Module (CCM) | weimingteo@u.nus.edu |
| Teoh Jeng Wei  | A0093899B  | 1. Ideation<br/>2. System architecture and application logic flow designs<br/>3. Data Acquisition and Knowledge Discovery<br/>4. Web scrapping to extract and structure information<br/>5. Data ingestion into neo4j Graph DB<br/>6. Marketing and System Architecture videos<br/>7. Storyboarding, animation, scripting, AI audio creation and video-audio synchronization. | e0938628@u.nus.edu |
| Wang Song  | A0026411X  | 1. Ideation<br/>2. Architecture and System Design<br/>3. Designs and coding the Knowledge Base Decisioning Model<br/>4. Design and code the backend APIs and frontend logic to integrate with the backend APIs.<br/>5. Integration of all components<br/>6. Installation guide, class diagram and knowledge base model. | wangsong@u.nus.edu |

## VIDEO SHOWCASE


## INSTALLATION & USER GUIDE

#### Installation for Windows OS
[Click here to go to the Windows Installation Section](https://github.com/TeamEightIS04/MRRSProject/tree/main/EnvironmentSetup/Windows "Click here to go to the Windows Installation Section")

#### Installation for Linux OS
[Click here to go to the Linux Installation Section](https://github.com/TeamEightIS04/MRRSProject/tree/main/EnvironmentSetup/Linux "Click here to go to the Linux Installation Section")

#### User Guide
[Click here to see the User guide](https://github.com/TeamEightIS04/MRRSProject/blob/main/Documentation/User%20Guide.docx "Click here to see the User guide")
