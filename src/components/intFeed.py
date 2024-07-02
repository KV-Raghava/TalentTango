import streamlit as st
from google.generativeai import GenerativeModel, ChatSession, configure
from dotenv import load_dotenv
import os
 
load_dotenv()
 
# Get the API key from environment variables
API_KEY = os.getenv("GOOGLE_GENAI_API_KEY")
 
# Ensure the API key is set
if not API_KEY:
    raise ValueError("Google Generative AI API key not found in environment variables")
 
# Configure the generative model
try:
    model = GenerativeModel('gemini-pro')
    newChat = model.start_chat()
except Exception as e:
    st.error(f"Failed to initialize the Gemini Pro model. Error: {e}")
    st.stop()
response="""
Areas of Improvement for the Candidate
Specific Metrics and Outcomes: While the candidate provided general success metrics (e.g., exceeding sales targets by 20%), more specific data points and detailed outcomes for other projects could strengthen their responses.
Conflict Resolution Details: The candidate's example of resolving a disagreement between engineering and marketing teams could include more specifics on the negotiation process and the exact steps taken to reach a compromise.
Experience with Fast-Paced Startup Environments: The candidate mentioned experience in a startup environment as a plus but did not provide detailed examples. Specific instances showcasing agility and innovation in a fast-paced startup setting would be beneficial.
Technical Proficiency: While the candidate mentioned a background in Computer Science, there was no discussion about their technical skills or how they have directly influenced product development. More emphasis on technical competencies and how they have used them in previous roles could be helpful.
Further Questions for Next Rounds
Technical Proficiency:
 
Can you provide specific examples of how your technical background has influenced your product decisions?
How do you collaborate with engineering teams to address technical challenges?
Conflict Resolution:
 
Can you describe a time when a conflict with a key stakeholder could not be resolved easily? What steps did you take, and what was the outcome?
How do you handle situations where there is a persistent disagreement on product direction within your team?
Data-Driven Decision Making:
 
How do you use data to drive product decisions? Can you provide an example where data analysis led to a significant change in product strategy?
What tools and metrics do you use to measure product performance?
Adaptability in Fast-Paced Environments:
 
Can you share an experience from a startup or a fast-paced environment where you had to pivot quickly due to market changes or new information?
How do you prioritize tasks and manage time in a rapidly changing environment?
Customer Interaction:
 
Can you provide an example of how customer feedback directly influenced a product feature or a strategic decision?
How do you ensure continuous improvement in product usability and customer satisfaction?
Leadership and Mentorship:
 
Can you give a detailed example of how you’ve mentored a junior team member, including the challenges faced and the results achieved?
How do you foster a culture of continuous learning and development within your team?
Recommendation for Next Round
Based on the screening interview, the candidate demonstrates strong qualifications and relevant experience for the Product Manager role. They have a solid background in leading product development, market analysis, and cross-functional collaboration. Their responses indicate strong leadership skills and a strategic mindset.
 
Recommendation: Yes, proceed to the next round of interviews. The candidate shows potential and alignment with the job requirements. Further interviews should focus on technical proficiency, conflict resolution, and adaptability in fast-paced environments to ensure a comprehensive assessment.
"""
transcript="""Interviewer (HR): Good morning, [Candidate's Name].
Thank you for taking the time to speak with us today about the Product Manager
position at our company. How are you doing?
 
Candidate: Good morning. I'm doing well, thank you. I'm excited to be here and discuss this opportunity.
 
Interviewer (HR): Great to hear! Let's start with a brief introduction. Can you tell me a little bit about your background and experience related to product management?
 
Candidate: Certainly. I have a degree in Computer Science and an MBA. Over the past six years, I've worked in various product management roles, primarily in the software industry. My experience includes leading cross-functional teams to develop and launch products, conducting market research, and defining product strategies. Most recently, I was a Senior Product Manager at [Previous Company], where I successfully led the development and launch of a new SaaS product that exceeded our sales targets by 20%.
 
Interviewer (HR): That sounds impressive. Could you elaborate on a specific project where you had to lead a team to deliver an innovative solution? What was your approach and the outcome?
 
Candidate: Absolutely. At [Previous Company], we identified a market gap for a comprehensive project management tool tailored for small to medium-sized enterprises. I led a team of 10, including engineers, designers, and marketing professionals. We started with extensive market research and user interviews to understand the needs and pain points. Based on the findings, we developed a product roadmap with clear milestones. Throughout the project, I facilitated regular stand-ups and sprint reviews to ensure we stayed on track. The result was a product that not only met market needs but also received positive feedback for its user-friendly interface and robust feature set. It contributed significantly to our revenue growth.
 
Interviewer (HR): Excellent. Can you describe a time when you had to prioritize features based on business value and user feedback? How did you balance these aspects?
 
Candidate: Prioritizing features is always a critical aspect of product management. At [Previous Company], we used a combination of user feedback, market analysis, and business value to prioritize our product features. For instance, we had a list of potential features for an update, but limited resources. I used a prioritization matrix, considering factors like user demand, market trends, and revenue potential. By engaging with key stakeholders and using data-driven insights, we prioritized features that offered the highest business value and user satisfaction. This approach ensured we delivered a product that aligned with both our strategic goals and customer expectations.
 
Interviewer (HR): That's a thorough approach. How do you handle collaboration with cross-functional teams, especially when there are differing opinions or conflicts?
 
Candidate: Collaboration and effective communication are key. I ensure that everyone is aligned with the product vision and goals from the outset. When conflicts arise, I focus on fostering open communication and finding common ground. For example, during a product launch, there was a disagreement between the engineering and marketing teams about the release timeline. I organized a meeting where both sides could voice their concerns and priorities. By facilitating a constructive discussion, we reached a compromise that adjusted the timeline slightly but ensured a successful launch with adequate marketing support. This experience reinforced the importance of empathy, active listening, and being solution-oriented.
 
Interviewer (HR): That's a great example of leadership. Speaking of leadership, how do you mentor and coach junior product managers?
 
Candidate: Mentoring junior product managers is something I'm passionate about. I focus on creating a supportive environment where they can learn and grow. I schedule regular one-on-one meetings to discuss their goals, challenges, and progress. I also encourage them to take ownership of smaller projects to build their confidence. Additionally, I provide constructive feedback and share best practices from my experience. For example, I once mentored a junior PM who was struggling with stakeholder management. We worked together on communication strategies and stakeholder engagement, which helped them improve significantly and succeed in their role.
 
Interviewer (HR): That’s great to hear. Finally, why are you interested in this Product Manager role at our company, and how do you think you can contribute to our team?
 
Candidate: I am particularly impressed by your company’s commitment to innovation and customer-centric approach. The opportunity to lead the development of impactful products in a dynamic environment like yours is very appealing to me. With my experience in product strategy, team leadership, and market analysis, I am confident I can contribute to your product vision and help drive growth. I am also excited about the chance to work in a collaborative and fast-paced environment, which aligns well with my background and career aspirations.
 
Interviewer (HR): Thank you, [Candidate's Name]. This has been a very insightful conversation. We will be in touch soon regarding the next steps in the interview process.
 
Candidate: Thank you for the opportunity. I look forward to hearing from you"""
transcript="""
Interview Transcript for the Role of Salesforce Developer
Interviewer: Jane Smith (JS), Senior Technical Manager
Candidate: John Doe (JD)
JS: Good morning, John. Thank you for joining us today. How are you?

JD: Good morning, Jane. I'm doing well, thank you. How about you?

JS: I'm doing great, thanks. Let's get started. Could you please give us a brief overview of your experience with Salesforce development?

JD: Sure. I have over six years of experience working with Salesforce. My experience includes developing custom solutions using Apex, Visualforce, and Lightning Web Components. I've worked extensively with both Service Cloud and Sales Cloud and have also had some experience with Communities and Manufacturing Cloud.

JS: That sounds impressive. Can you tell me about a recent project where you developed a custom solution on the Salesforce platform?

JD: Certainly. In my last project, I was tasked with creating a custom solution for a sales team that needed a more efficient way to manage their leads and opportunities. I used Lightning Web Components and Apex to develop a new lead management system. The system included custom forms, automated workflows, and real-time data updates using Salesforce's REST API. This solution greatly improved the team's efficiency and reduced the time they spent on administrative tasks.

JS: That's great to hear. How do you approach integrating Salesforce with other applications?

JD: Integration is a critical part of many Salesforce projects I've worked on. I usually start by understanding the business requirements and the systems involved. I then design the integration architecture, often using REST or SOAP APIs for communication. For example, in one project, I integrated Salesforce with an ERP system using REST API calls to exchange data in real-time. This ensured that the data in both systems was always synchronized, which was crucial for business operations.

JS: Integration can be quite complex. How do you handle security and data governance when working on Salesforce integrations?

JD: Security and data governance are always top priorities. I make sure to use Salesforce's security features such as profiles, permission sets, and sharing settings to control access to data. When integrating with other systems, I ensure that data is encrypted both in transit and at rest. I also conduct regular security reviews and audits to identify and mitigate any potential vulnerabilities.

JS: That’s very thorough. Can you describe a situation where you had to troubleshoot and resolve a Salesforce-related issue?

JD: Sure. In one instance, users were experiencing significant delays when accessing a custom Visualforce page. I started by analyzing the performance logs and identified that a SOQL query was not using selective filters, causing a full table scan. I optimized the query by adding appropriate indexes and selective filters, which improved the page load time from over 10 seconds to under 2 seconds. Additionally, I refactored some of the backend logic to be more efficient.

JS: Excellent. How do you ensure that the solutions you build are scalable and performance-oriented?

JD: Scalability and performance are always at the forefront of my design process. I follow Salesforce best practices such as governor limits management, efficient SOQL queries, and bulk processing with Apex. I also leverage asynchronous processing methods like Batch Apex and Queueable Apex for long-running operations. For performance, I use tools like the Salesforce Optimizer and perform regular code reviews to ensure adherence to best practices.

JS: That’s great to hear. Collaboration is key in our projects. How do you work with business stakeholders and other developers to translate business requirements into technical solutions?

JD: Effective collaboration starts with clear communication. I engage with business stakeholders to fully understand their requirements and pain points. I then work with other developers to brainstorm and design technical solutions that align with these requirements. Throughout the development process, I maintain regular check-ins with stakeholders to ensure that the solution is on track and make adjustments as needed. I also encourage peer reviews and knowledge sharing within the development team.

JS: Wonderful. Lastly, could you share an example of a complex business requirement that you translated into a Salesforce solution?

JD: Absolutely. One of our clients needed a custom solution to manage their product warranty process. The requirement was complex due to various conditions and workflows involved. I designed a solution using Flow Builder for creating dynamic workflows and Lightning Web Components for a user-friendly interface. The solution included automated notifications, condition-based approvals, and integration with their existing CRM system. This not only streamlined their warranty process but also improved customer satisfaction.

JS: Thank you, John. Your experience and approach to Salesforce development are impressive. Do you have any questions for us?

JD: Yes, I would like to know more about the team I’ll be working with and the types of projects you typically handle.

JS: Certainly. Our team is composed of experienced Salesforce developers, business analysts, and project managers. We handle a wide range of projects, from custom application development to large-scale integrations and data migrations. Collaboration and continuous learning are core aspects of our team culture.

JD: That sounds like a great environment. Thank you for sharing.

JS: Thank you, John. It was great talking to you. We’ll be in touch soon regarding the next steps.

JD: Thank you, Jane. I look forward to hearing from you.
"""
async def readText(file):
    content=file.read()
    st.session_state.transcript = content.decode('utf-8')
    print(f"content in read text")
async def genSummary():
    print(f"transcript:{st.session_state.transcript}")
    transcript = st.session_state.transcript
    # prompt="""From this interview transcript: {transcript} ,
    #           give me feedback for the the candidate's performance in this structure
    #           1) Header: Strengths of canditate. 
    #              Content: Give me 2 bullet points on skills specific to the role and 2 bullet points on general skills(example :soft skills and leadership)
    #              Also give the excerpts from the above transcript and line from which you are picking these points
    #           2) Header: What didn't meet the expectations
    #              content: Areas of improvement
    #           3)Header: Summary
    #             content: Summary and suggestions for the next interview panel. Give me a paragraph with  around 30-50 words
    #           Don't use any other extra details except provided data, make sure that your not adding extra and invalid details, keep responce crisp and clear. Use only the trnacript provided to you in this prompt
    #           """
    prompt=f"""From this interview transcript: {st.session_state.transcript},
give me evidence-based feedback for the candidate's performance in this structure:
1) Header: Strengths of Candidate
   Content: Give me 2 bullet points on skills specific to the role AND 2 bullet points on general skills (e.g., soft skills and leadership)  

2) Header: What Didn't Meet Expectations
   Content: Areas for improvement based on the transcript.
3) Header: Summary
   Content: Summary and suggestions for the next interview panel based on the transcript (around 30-50 words).
Do not generate skills or qualities not explicitly mentioned in the transcript."""
    response = newChat.send_message(prompt)
    st.session_state.intFeedTokenCount = response.usage_metadata.total_token_count
    st.session_state.intFeed = response.text
async def intFeedMain():
    st.title("Summarize interview calls in a snap")
    st.subheader("Upload Meeting Recording/Transcript")
    uploaded_file = st.file_uploader("", type=None, accept_multiple_files=False, key=None, help=None,
                        args=None, kwargs=None, disabled=False,label_visibility="visible",
                        )
    if uploaded_file:
        await readText(uploaded_file)
        st.subheader("Transcript")
        if st.session_state.transcript:
            st.text_area("",f"{st.session_state.transcript}", height=400)
            await genSummary()
        if st.session_state.intFeed:
            st.write(st.session_state.intFeed)
            st.write(f"Token consumption: {st.session_state.intFeedTokenCount}")
   