# Job Search Python Client

A lightweight Python client for the [Lattice Job Search API](https://rapidapi.com/lattice-data-lattice-data-default/api/job-search4/).

## Contents

  - [Setup](#Setup)
    - [Installation](#Installation)
    - [API Authentication](#API-Authentication)
    - [Dependencies](#Dependencies)
  - [Usage](#Usage)
    - [Function: lawjobs](#function-lawjobs)
    - [Function: indeed](#function-indeed)
    - [Function: simplehired](#function-simplehired)
    - [Function: craigslist](#function-craigslist)
    - [Function: craigslist_regions](#function-craigslist_regions)
    - [Function: careerjet](#function-careerjet)
    - [Function: dice](#function-dice)
    - [Function: xing](#function-xing)
    - [Function: stackoverflow](#function-stackoverflow)
    - [Function: monster](#function-monster)
    - [Function: linkedin](#function-linkedin)
  - [License](#license)

## Setup

### Installation
The easiest way to install this package is using pip:
```bash
pip install job-search
```
### API Authentication
To successfully use this library you will need an API key for the [Lattice Job Search API](https://rapidapi.com/lattice-data-lattice-data-default/api/job-search4/) that powers it. Navigate to [RapidAPI](https://rapidapi.com/lattice-data-lattice-data-default/api/job-search4/) to sign up for a free API key and then save it to an environment variable called `JOB_SEARCH_X_RAPID_API_KEY` in your environment. The library will automatically load that environment variable and use it to authenticate API calls made under the hood.

### Dependencies
This library relies on the following Python libraries:
 - numpy
 - python-dotenv
 - lxml
 - xmltodict
 - pytest
 - requests
 - cachetools
 - pymongo
 - pandas

These are listed in the `requirements.txt` file. Install them using pip:

```bash
pip install -r requirements.txt
```

## Usage

### Function: `lawjobs`

Conducts a comprehensive search of jobs posted on Lawjobs.com based on a free text search query.
```bash
lawjobs(query,page)
```
#### Arguments:

Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`
`page` | `int` | Page Number | `True` | `1` 

#### Return value:

Returns the list of jobs available in json format.

#### Example:

```bash
>>> from jobsearch import lawjobs
>>> from pprint import pprint
>>> pprint(lawjobs("attorney"))
{
    'date': '2021-10-02T10:15:29.114525',
    'jobs': [
        {
            'city': 'New York',
            'company_name': None,
            'country': 'United States',
            'date_posted': '2021-09-21T00:00:00',
            'description': "Cozen O'Connor Strategic Risk & Complex Litigation Practice Group",
            'detail_url': 'https://lawjobs.com/job/insurance-defense-trial-attorney-new-york-new-york-186133',
            'location': 'New York, New York',
            'source': 'lawjobs.com',
            'state': 'New York',
            'title': 'Insurance Defense - Trial Attorney',
        },
        {
            'city': 'Trenton',
            'company_name': None,
            'country': 'United States',
            'date_posted': '2021-09-27T00:00:00',
            'description': '(Court Executive 2A)The New Jersey Judiciary seeks an experienced professional with excellent leadership, managerial and communication skills to serve as the Assistant Chief, Special Civil Part in...',
            'detail_url': 'https://lawjobs.com/job/assistant-chief-special-civil-part-trenton-new-jersey-186170',
            'location': 'Trenton, New Jersey',
            'source': 'lawjobs.com',
            'state': 'New Jersey',
            'title': 'Assistant Chief, Special Civil Part',
        },
        ...
    ]
}
```

### Function: `indeed`

Conducts a comprehensive search of jobs posted on Indeed.com based on a free text query.
```bash
indeed(query,page)
```

#### Arguments:

Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`
`page` | `int` | Page Number | `True` | `1` 


#### Return value:

Returns the list of jobs available in json format.

#### Example:
```bash
>>> from jobsearch import indeed 
>>> from pprint import pprint
>>> pprint(indeed("Software Engineer"))
{   
    'date': '2021-10-02T10:18:28.627304',
    'jobs': [
        {
            'city': None,
            'company_name': None,
            'country': 'United States',
            'date_posted': '2021-10-02T10:18:25.729601',
            'description': '5+ years of professional software engineering experience.Work closely with the rest of the product team on user-facing features that delight parents and their… ...',
            'detail_url': 'https://www.indeed.com/rc/clk?jk=462c73f0539f47dc&fccid=29ce24cf04b05f6f&vjs=3',
            'location': None,
            'source': 'indeed.com',
            'state': None,
            'title': 'Software Engineer, Backend',
        },
        {
            'city': None,
            'company_name': 'Pearson',
            'country': 'United States',
            'date_posted': '2021-09-30T09:28:53',
            'description': 'We have proprietary technology to generate millions of personalized animated videos, each one customized to the individual viewer, in up to 15 different… ...',
            'detail_url': 'https://www.indeed.com/rc/clk?jk=42746b60a478521b&fccid=915b1c0ee87e5e8a&vjs=3',
            'location': None,
            'source': 'indeed.com',
            'state': None,
            'title': 'Associate Software Engineer (entry-level)',
        },
        ...
    ]
}
```

### Function: `simplehired`

Conducts a comprehensive search of jobs posted on SimplyHired.com based on a free text query.
```bash
simplehired(query,page)
```

#### Arguments:

Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`
`page` | `int` | Page Number | `True` | `1` 

#### Return value:

Returns the list of jobs available in json format.

#### Example:
```bash
>>> from jobsearch import simplehired
>>> from pprint import pprint
>>> pprint(simplehired("consultant"))
{   
    'date': '2021-10-02T10:21:04.083304',
    'jobs': [
        {
            'city': None,
            'company_name': 'Roessel Joy',
            'country': 'United States',
            'date_posted': '2021-09-17T00:00:00',
            'description': 'As a consultant you will be part of a joint client and consultant team, working to identify the highest value-at-stake issues facing the client company,…',
            'detail_url': 'https://www.simplyhired.com/job/r3yAvBFFpPuPWfkKZmo__o5uacZLZ5yDxrcS3IvGl29PVoiKLtj2fg?q=consultant',
            'location': 'Remote',
            'source': 'simplyhired.com',
            'state': None,
            'title': 'Management Consultant',
        },
        {
            'city': None,
            'company_name': 'Chandler Learning Center',
            'country': 'United States',
            'date_posted': '2021-08-16T00:00:00',
            'description': 'Qualifying full-time employees are afforded flexible scheduling and are eligible to participate in 401k and health benefits. Job Types: Full-time, Part-time.',
            'detail_url': 'https://www.simplyhired.com/job/7SuouAoaeFNaiSGf21NvTQFugVPzL-vcl71Kw9v438GyMAoBm3tkDw?q=consultant',
            'location': 'Remote',
            'source': 'simplyhired.com',
            'state': None,
            'title': 'College Admissions Consultant',
        },
        ...
    ]
}
```

### Function: `craigslist`

Conducts a comprehensive search of jobs posted on Craigslist based on a free text query.
```bash
craigslist(query,region_id)
```

#### Arguments:

Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`
`region_id` | `str` | Job Location | `False`
`page` | `int` | Page Number | `True` | `1` 

#### Return value:

Returns the list of jobs available in json format.

#### Example:
```bash
>>> from jobsearch import craigslist     
>>> from pprint import pprint
>>> pprint(craigslist("researcher","newyork"))
{   
    'date': '2021-10-02T10:25:51.278095',
    'jobs': [
        {
            'city': 'fairfield county',
            'company_name': None,
            'country': 'United States',
            'date_posted': '2021-09-22T11:41:00',
            'description': 'QR Code Link to This Post\n\n\nDo you want to help companies navigate the complexities of acquiring government approvals? Does the thought of working on issues involving legal and operational compliance make you happy?\n\nWe are an entrepreneurial federal administrative law firm that is on track for aggressive growth and we need an experienced Legal Administrative Assistant to join our team and be a total superstar – working directly with the owner to support the team and help our clients.\n\nWe want to be known for helping our clients capture a new business opportunity or overcome a hurdle with a government agency, and come away feeling as though they are a better company, in a better position, and that they had a team behind them that really cared and fought for them. We are growing fast and we need a Legal Administrative Assistant who can hit the ground running.\n\nIf these statements appeal to you, then you may be our Superstar:\n\n- You are an amazing researcher with a sickening degree of attention to detail.\n\n- You know how to follow instructions\n\n- You always double (or triple) check your work before handing it in to your supervisor\n\n- When are unsure about how to do something you can propose a potential solution(s) to complete it\n\n- You are not afraid to ask questions\n\n- You think in terms of outlines, chronologies, and spreadsheets.\n\n- You see an opportunity for organization where other people see a mess.\n\n- You understand that sometimes it’s OK to leave a message, but sometimes you’ve got to keep trying until you speak to a person.\n\n- You smile when you answer the phone.\n\n- You are very good with calendars, e-mail, spreadsheets, word processing, software programs, and the internet.\n\n- Your middle name is “No Drama.”\n\n- You are an awesome juggler of tasks and can change gears quickly.\n\n- You do not think scanning and copying are “beneath you.”\n\n- You have excellent MS Office skills, are comfortable with online applications and technology in general.\n\n- You know how to follow processes and have strong self-organizational and time management skills\n\nWe love to help people learn and grow. We need a Legal Administrative Assistant with experience in a professional setting. The ideal candidate will be able to take initiative on work that needs to be done and complete tasks with minimal hand-holding. They will also have a love of international affairs.\n\nThis is a 20 hr/wk part-time contract job. Salary is $15 to $18/hr (DOE).\n\nIf this exciting opportunity appeals to you, please follow the instructions listed below. APPLICATIONS THAT DO NOT FOLLOW INSTRUCTIONS WILL NOT BE CONSIDERED.\n\nPrepare a cover letter with no more than TWO paragraphs and a closing sentence. In the first paragraph explain what you believe are the 3 most important qualities needed in someone who works with companies seeking government approvals and meeting legal compliance requirements and why you believe they are the most important qualities. In the second paragraph, explain why you applied to this particular ad. As a closing sentence please write, “I have read the instructions contained in the job posting and have followed the instructions.”\n\nDo not send your resume through this website. Email your resume and cover letter in PDF format to the ‘contact’ email at the bottom of the home page of our website at www.clarkespositolaw.com. The subject line of the email should have your last name (all caps), followed by the position you are applying for in lower case, followed by one word that you would use to describe yourself in all caps. [For example: SMITH Legal Administrative Assistant AWESOME]\n\nWe look forward to reviewing your application. We are equal opportunity employer. Applicants from diverse backgrounds are encouraged.',
            'detail_url': 'https://newyork.craigslist.org/fct/lgl/d/new-york-hiring-superstar-part-time/7383905000.html',
            'location': 'fairfield county / New York Fairfield Co, Ct ',
            'source': 'craigslist.com',
            'state': 'Connecticut',
            'title': 'Hiring a Superstar Part-Time Legal Administrative Assistant - REMOTE',
        },
        {
            'city': 'fairfield county',
            'company_name': None,
            'country': 'United States',
            'date_posted': '2021-09-27T15:35:00',
            'description': "QR Code Link to This Post\n\n\nPAY FOR SUCCESS, REMOTE, PART-TIME CONTRACT OPPORTUNITY\n\nAbout RWS\nRWS is the world leader in intellectual property (IP) search services. With the AOP Connect™ platform and our global community of researchers, RWS has revolutionized the way patents are searched by uniquely leveraging a crowdsourcing model.  RWS broadcasts its studies to the world’s largest patent research community, over 42,000 highly-educated and qualified researchers, distributing millions in 
rewards to researchers for their work.  RWS specializes in identifying non-textual and non-patent literature, finding prior art references and Evidence of Use that others simply do not have the resources to find. RWS is a partner to 17 Fortune 100 companies, 74 Forbes Global 2000 and 7 of the top 10 US patent filers.\n\nIn the past few months, we've 
seen a great response from clients bringing in more studies, resulting in a total current pool of $37,000 USD available for open studies and we’ve paid out $432,155 USD in rewards in the last 12 months.  Click here to see the complete list of open studies: https://app.articleonepartners.com/ip-research/studies/active.  It's worth mentioning that we recently achieved a tremendous milestone - $10,000,000 USD in total rewards paid!!! We're expecting this growth to continue, which means more studies, more technologies, and more earnings opportunities for you.\nOur community is a diverse global group of students, professionals, freelance technology experts and other individuals who are generally interested in research and technology. Your unique background and experience will allow you to be a vital member of the RWS community. \n\nOpportunity \nRWS is seeking Technical Literature Researchers to support our growing inventory of technical and research studies. \n•\tPay for Success – the best researchers get rewarded based on the quality of their 
research. Earn compensation for finding key technical literature related to selected patents and technology areas. \n•\tWork at your convenience. Choose your projects, and conduct your research at your own time. \n•\tUse your expertise, and explore new technology areas. Join a global community of researchers who enjoy the challenge and reward of using their investigatory and analytical skills to increase patent quality and resolve litigation activities. \n•\tSpecifically, if your background is in Physics, Imaging, Computer Engineering, Electronics, Telecommunications, Cybersecurity, Information Services, Software Engineering, Machinery, Mechanical Engineering, Robotics, Technology and/or Industrial & Product Design, we’ve got some public studies available right now!\n\nWhat is Technical Literature Research? \nTechnical literature research involves searching for and analyzing documents that provide information related to a particular subject area, technology, product, etc. Technical literature includes everything from issued patents to white papers to product manuals and can come from all parts of the world; we may even request physical products themselves.  Your goal as a Technical Literature Researcher is to use industry / market knowledge, literature and technical information, web searching capabilities, and/or technical experience to help uncover literature that is related to a specific Study that is posted on RWS’s AOP Connect™ platform. \n\nWho Should Register? \nWe encourage anyone who has an interest in technical literature research, or even the hunt 
of simply “finding things”, to join our community. This opportunity is a perfect fit for: \n• Those looking to leverage their education and/or work experience to earn additional money; \n• Those interested in putting their technical or research skills to use on their own schedule; \n• Those with a high level of intellectual curiosity and a desire to 
solve technical challenges; \n\nBeneficial Skills \n•\tStrong research skills (Boolean searching, advanced Google searchers, access to technical information)\n•\tStrong attention to detail \n•\tAnalytical mindset with excellent problem-solving skills \n•\tAbility to prioritize and follow a detailed list of search requirements \n•\tHigh level of initiative \n•\tReceptive to feedback and guidance from study organizers \n•\tTenacious and determined; you will be contributing alongside many talented researchers \n\nWant to take a look at how it all works?  CLICK THIS LINK OR PASTE DIRECTLY INTO YOUR BROWSER to view our Quick Start Guide:  https://app.articleonepartners.com/resources/quick-start-guide.pdf?v=12.7.1\n\nStill unsure as to how to find Technical Literature? Don't worry, we will provide access to training which will help establish key Researcher skills and get you started with this exciting opportunity.   \n\nWhat Now?  You must register to participate.  To register as a Researcher, CLICK THIS LINK OR PASTE DIRECTLY INTO YOUR BROWSER: 
 https://www.rws.com/intellectual-property-services/research/become-a-researcher/\n\nTo obtain more information about RWS, CLICK THIS LINK:  https://www.rws.com/intellectual-property-services/research/",
            'detail_url': 'https://newyork.craigslist.org/jsy/sci/d/new-york-technical-literature-researcher/7386338593.html',
            'location': 'fairfield county / 90 Broad Street New Jersey ',
            'source': 'craigslist.com',
            'state': 'Connecticut',
            'title': 'Technical Literature Researcher',
        },
        ...
    ]
}
```

### Function: `craigslist_regions`

Returns the list of all available Craiglist region IDs.
```bash
craigslist_regions()
```

#### Arguments:

None

#### Return value:

Returns the list of jobs available in json format.

#### Example:

```bash
>>> from jobsearch import craigslist_regions
>>> from pprint import pprint
>>> pprint(craigslist_regions())
{
  'date': '2021-10-02T10:28:15.391094',
  'status': 'success',
  'regions': [
        {
            'city': 'Salem',
            'country': 'United States',
            'region_id': 'salem',
            'state': 'Oregon',
        },
        {
            'city': 'Tuscarawas Co',
            'country': 'United States',
            'region_id': 'tuscarawas',
            'state': 'Ohio',
        },
        {
            'city': 'Youngstown',
            'country': 'United States',
            'region_id': 'youngstown',
            'state': 'Ohio',
        },
        ...
  ]
}
```
### Function: `careerjet`

Conducts a comprehensive search of jobs posted on Careerjet.com based on a free text search query.
```bash
careerjet(query,page)
```
#### Arguments:

Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`
`page` | `int` | Page Number | `True` | `1` 

#### Return value:

Returns the list of jobs available in json format.

#### Example:

```bash
>>> from jobsearch import careerjet
>>> from pprint import pprint
>>> pprint(careerjet("penetration tester"))
{
    'date': '2021-10-02T10:39:15.114510',
    'jobs': [
        {
            'city': 'Morrisville',
            'company_name': 'Lenovo',
            'country': 'USA',
            'date_posted': '2021-10-01T09:24:56',
            'description': "Sr Penetration Tester  General Information  Req #  WD00013047  Career area:  Cloud Computing  Country/Region:  United States of America  State:  North Carolina  City:  Morrisville  Date:  Wednesday, September 29, 2021  Working time:  Full-time  Why Work at Lenovo  Here at Lenovo, we believe in smarter technology for all, so we spend our time building a society that's brighter and more inclusive. And we go big. No, not big-huge.  We're a US$60 billion revenue Fortune Global 500 company serving customers in 180 markets around the world. Focused on a bold vision to deliver smarter technology for all, we are developing world-changing technologies that power (through devices and infrastructure) and empower (through solutions, services and software) millions of customers every day and together create a more inclusive, trustworthy and sustainable 
digital society for everyone, everywhere.  The one thing that's missing? Well… you...  Description and Requirements  What You'll Do:  This position is for a penetration testing Lead in the Security Center of Excellence for the Global PC and Smart Device Business Unit (PCSD). This is an exciting role that will give you the opportunity to work with Product teams around the globe to perform penetration test on PCSD's many products. You will be working alongside the best security teams in the industry. This roll will be responsible to lead pen testing for PCSD Products sold around the world. This will include scoping and planning pen tests with the development teams and then leading execution of those pen tests. You'll report findings, produce reports and work with the development and security teams to resolve the issues you and your team members find. Other members of the security team will work with you to assess the overall security and privacy risk of the products you are testing. You'll stay up to date with the industry's latest techniques and tools. This role will be testing a variety of products and will be well versed in cloud, client, IoT and hardware penetration testing.  As a lead member of the team, you'll be mentoring and coaching other team members on your immediate team. You will be researching new penetration tools and techniques. This position will be keeping metrics and KPIs to track the team's performance over time ensuring that growth, improvements, and gaps are accurately communicated to management. You'll work with development teams to coordinate penetration tests and ensure that products are tested within an appropriate time frame. As a team leader you will be assisting in communicating the priority and risk of 
both your and other team member's security findings to development teams. You will have excellent organizational and communication skills ensuring that development teams, other security team members and management are well informed of the penetration testing team's activities. You will ensure the team is using documented, standard and appropriate penetration testing mythologies.  In Summary you will:  · Perform penetration tests on PCSD's Cloud, Client, IoT and hardware products  · Work with development and security teams 
to find and explain security issues, suggest mitigations, and ensure they are mitigated.  · Stay up to date on the latest testing tools and techniques ensure both yourself and 
the teams are using the most effective methods.  · Coach and mentor other members of the penetration teams.  · Ensure proper KPIs and metrics are being recorded  · Schedule penetration tests for product development teams.  Position Requirements  Basic Qualifications:  · Bachelor's degree in a relevant field or equivalent relevant experience  · 5+ years of cybersecurity experience  · 3+ years of experience of penetration testing  · 2+ years of acting in a team lead capacity  · 2+ years of mentoring and coaching others in technical roles.  · Strong written and verbal communications and interpersonal skills  · Ability to work independently as well as function as an integral part of a team, take initiative and ownership in a fast-paced environment  · Ability to successfully work across regions and functions to solve problems and get things done  Preferred Qualifications: 
 · Master's Degree or equivalent experience in a relevant field  · Experience with penetration testing and diagnostic tools such Burp Suite, Kali Linux, tcpdump, wireshark, nmap, fuzzing tools, code analyst tools, DAST tools, Metasploit, etc.  · Knowledge of Agile processes  · Experience working in a development environment.  · Experience building Red / Purple teams.  · SANS certifications such as GIAC Cloud Penetration Tester (GCPN), GIAC Certified Forensic Examiner (GCFE), GIAC Certified Incident Handler (GCIH), GIAC Penetration Tester (GPEN), GIAC Web Application Penetration Tester (GWAPT), GIAC Reverse Engineering Malware (GREM), and GIAC Exploit Researcher and Advanced Penetration Tester (GXPN)  · EC-Council certifications such as Certified Ethical Hacker (ANSI or Practical)  · Offensive Security certiciations such as Offensive Security Certified Professional (OSCP), Offensive Security Experienced Penetration Tester (OSEP), Offensive Security Web Expert (OSWE), Offensive Security Exploit Developer (OSED), and Offensive Security Exploitation Expert (OSEE  · Industry security certifications such as CISSP, Security+, etc.  We are an Equal Opportunity Employer and do not discriminate against any employee or applicant for employment because of race, color, sex, age, religion, sexual orientation, gender identity, status as a veteran, and basis of disability or any federal, state, or local protected class.\n  \n  \n  \n    \n    \n\n        Lenovo",
            'detail_url': 'https://www.careerjet.com/jobad/usb24a0370c0c7fc40cb459a13e77b002d',
            'location': 'Morrisville, NC',
            'source': 'careerjet.com',
            'state': 'North Carolina',
            'title': 'Sr Penetration Tester',
        },
        {
            'city': 'USA',
            'company_name': 'KPMG',
            'country': 'USA',
            'date_posted': '2021-09-30T09:46:53',
            'description': "Historically, the travel requirement for this position has ranged from 80-100%. The safety and well-being of our people continues to be the top priority, and our decisions around travel are informed by government COVID-19 response directives, recommendations from leading health authorities, and guidance from a number of infectious disease experts. For now, all KPMG business travel, international and domestic, is currently restricted to client-essential sales/delivery activity only. At some point in the future and with the safety of people as the critical factor, the travel requirement will likely increase, possibly to previous levels, but KPMG is committed to balancing client requirements with new delivery capabilities.  The KPMG Advisory practice is currently our fastest growing practice. We are seeing tremendous client demand, and looking forward we don't anticipate that slowing down. In this ever-changing market environment, our professionals must be adaptable and thrive in a collaborative, team-driven culture. At KPMG, our people are our number one priority. With a wealth of learning and career development opportunities, a world-class training facility and leading market tools, we 
make sure our people continue to grow both professionally and personally. If you're looking for a firm with a strong team connection where you can be your whole self, have an impact, advance your skills, deepen your experiences, and have the flexibility and access to constantly find new areas of inspiration and expand your capabilities, then consider a career in Advisory.  KPMG is currently seeking a Senior Specialist to join our practice.  Responsibilities:  Formulate and define the strategic direction for Managed Detection & Response as a managed service to grow pipeline of the solution, by working closely with internal and external channels Perform manual penetration tests of websites, APIs, 
web services, infrastructure, networks, IoT Devices and mobile applications to discover and exploit vulnerabilities; Provide technical leadership and advice to team members on 
attack and penetration test engagements Converse with non-technical audiences and articulate both scoping/pricing conversations as well as report read-outs Guide technical audiences on remediation options and assist them in weighing those options Partner with the Cyber Defense teams to develop new testing techniques, automation for testing and marketing collateral to support the practice and mentor junior and offshore team members on tools and techniques in performing test  Qualifications:  Minimum three years of recent experience working with using penetration tools to perform security tests: NetsSparker/Acunetix, ZAP, Veracode, Kali Linux, BurpSuite, Nikto or equivalent Bachelor抯 Degree from 
an accredited college/university Major ethical hacking certifications preferred; CEH, GPEN, CREST Demonstrated at least 3 years of working with Enterprise technical and non-technical audiences in reporting results and lead remediation conversations Knowledge of using orchestration and automation solutions in managing campaign and results Previous experience in Web Application testing, Mobile Application testing and Infrastructure testing and would lead engagement teams and scope engagements Ability to travel as necessary Applicants must be currently authorized to work in the United States without the need for visa sponsorship now or in the future   Colorado Salary Statement:  The salary range displayed is specifically for those potential hires who will work or reside in the state of Colorado if selected for the role. Any offered salary is determined based on internal 
equity, internal salary ranges, market data/ranges, applicant's skills and prior relevant experience, certain degrees and certifications (e.g. JD/technology), for example.  Colorado Salary Range: Low: $58700 - High: $128300  KPMG LLP (the U.S. member firm of KPMG International) offers a comprehensive compensation and benefits package. KPMG is an affirmative action-equal opportunity employer. KPMG complies with all applicable federal, state and local laws regarding recruitment and hiring. All qualified applicants are considered for employment without regard to race, color, religion, age, sex, sexual orientation, gender identity, national origin, disability, protected veteran status, or any other 
category protected by applicable federal, state or local laws. The contains further information regarding the firm's compliance with federal, state and local recruitment and hiring laws. No phone calls or agencies please.  Our Benefits  Health  KPMG offers a range of medical insurance options to meet your needs as well as prescription drug coverage, 
health care flexible spending accounts, and dependent day care flexible spending accounts.  Personal Time Off (PTO)  Up to 25 PTO Days per year (depending on job classification/level/years of service).  Financial  401(k) and Pension Plans Dependent Care Flexible Spending Account Health Care Flexible Spending Account Mortgage Assistance Program HomeBenefits@Work Program Hyatt Legal Plan \n\n\n        KPMG",
            'detail_url': 'https://www.careerjet.com/jobad/usd84655a7c1388af6cb46b2ac8057a0e4',
            'location': 'USA',
            'source': 'careerjet.com',
            'state': None,
            'title': 'Senior Specialist, Application Penetration Tester I',
        },
        ...
    ]
}
```

### Function: `dice`

Conducts a comprehensive search of jobs posted on Dice.com based on a free text search query.
```bash
dice(query,page)
```

#### Arguments:

Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`
`page` | `int` | Page Number | `True` | `1` 

#### Return value:

Returns the list of jobs available in json format.

#### Example:

```bash
>>> from jobsearch import dice
>>> from pprint import pprint
>>> pprint(dice("penetration tester"))
{   
    'date': '2021-10-02T10:40:38.477352',
    'jobs': [
        {
            'city': 'Ashburn',
            'company_name': 'Leidos',    
            'country': 'US',
            'date_posted': '2021-06-30T22:45:12Z',
            'description': "Leidos\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLeidos\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\tSecurity, Tester, LAN, WAN, Java, XML, Perl, HTML, IT, Python, JavaScript, Web, Application, Applications, Manager, System, CISSP\n\t\t\t\n\n\n\n\n\n\n\n\nFull Time\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nJob Description\n\nDescription Job Description:10K sign on bonus!!Exciting opening for an experienced Cyber Security Penetration Tester!This person will work on a team of cyber SMEs providing support to the DHS SOC Support Services Program/CBP.Department of Homeland Security (DHS), Customs and Border Protection (CBP) Security Operations Center (SOC) is a US Government program responsible to prevent, identify, contain and eradicate cyber threats to CBP networks through monitoring, intrusion detection and protective security services to CBP information systems including local area networks/wide area networks (LAN/WAN), commercial Internet connection, public facing websites, wireless, mobile/cellular, cloud, security devices, servers and workstations. The CBP SOC is responsible for the overall security of CBP Enterprise-wide information systems, and collects, investigates and reports any suspected and confirmed security violations.The CBP SOC Program has a critical need for a Penetration 
Tester to join our team working in Ashburn, VAPrimary ResponsibilitiesPerform internal and external pentest against systems to determine vulnerabilities and offer mitigation strategies.Perform web app pentestsPerform vulnerability risk assessmentPerform physical pentests and social engineeringPerform cyber incident response as needed for programsQualificationsA minimum of an active Secret clearance (and be able to obtain a DHS CBP BI clearance to support this program.)BS degree and 8 years of prior relevant experienceAdditional years of experience and cyber certifications may be considered in lieu of a degree.Experience in web development and programming languages - such as Java, XML, Perl and HTMLExtensive experience performing IT security risk assessmentsExperience with programming/scripting in Python, Powershell, Ruby, C, JavaScript, etcExperienced with the following Web Application tools; Burp Suite, Web Inspect, AppdetectiveExperienced with KaliExperienced with IPS/IDS solutionsUnderstanding for the Cyber Kill Chain methodologyPrefer one of the following certifications:GIAC Web Applications Penetration Tester (GWAPT)GIAC Penetration Tester (GPEN)Certified Ethical Hacker (CEH)Certified Information Security Manager (CISM)Certified Web Application Defender (GWEB)Certified Information System Security Professional (CISSP)External Referral Bonus:EligibleExternal Referral Bonus $:5000Potential for Telework:NoClearance Level Required:NoneTravel:NoScheduled Weekly Hours:40Shift:DayRequisition Category:ProfessionalJob Family:Cyber OperationsPay Range:\n\n\n\n\n\n\nSave\n\n\n\n\n\n\n\n\n\n\n\n\n\nCreate Alert\n\t\t\n\n\nSave\n\n\n\nToggle\n\t\t\t\t\tDropdown\n\n\n\n\n \n \n\n\n \n\n\n\n\n\n\n\n\n Create Alert\n\t\t\n\n\nSave\n\n\n\n Toggle\n\t\t\t\t\tDropdown\n\n\n\n\n \n \n\n\n \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCompany Information\n\n\t\t\t\t\t\t\tLeidos is a Fortune 500® information technology, engineering, and science solutions and services leader working to solve the world's toughest challenges in the defense, intelligence, homeland security, civil, and health markets. The company's 31,000 employees support vital missions for government and commercial customers. Headquartered in Reston, Virginia, Leidos reported annual revenues of approximately $10.17 billion for the fiscal year ended December 29, 2017. (NYSE: LDOS) All qualified applicants will receive consideration for employment without regard to race, color, religion, 
sex, sexual orientation, gender identity, national origin, disability or veteran status.\n\t\t\t\t\t\t\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDice Id : SCNCAPI2 \n\n\nPosition Id : R-00060041\n\n\nOriginally Posted : 3 months ago\n\n\n\n\n\nSimilar Positions at Leidos\n\nRed Team/Penetration Tester Engineer\n\nReston, VA\n1 day ago\n\n\n\n\nRed Team/Penetration Tester Engineer\n\nReston, VA\n1 day ago\n\n\n\n\nRed Team/Penetration Tester Engineer\n\nGaithersburg, MD\n1 day ago\n\n\n\n\nRed Team/Penetration Tester Engineer\n\nGaithersburg, MD\n1 day ago\n\n\n\n\nPenetration Tester\n\nWashington, DC\n1 day ago\n\n\n\n\nTier 1 Penetration Tester\n\nWashington, DC\n1 day ago\n\n\n\n\nTier 2 VAT Analyst\n\nAshburn, VA\n1 day ago\n\n\n\n\nThreat Hunter\n\nAshburn, VA\n1 day ago\n\n\n\n\nCyber Security Engineer\n\nAshburn, VA\n1 day ago\n\n\n\n\nTier 2 Security Monitoring Analyst\n\nBluemont, VA\n1 day ago",
            'detail_url': 'https://www.dice.com/jobs/detail/604ad279a3c87b0108231b01b4e168a4?searchlink=search%2F%3Fq%3Dpenetration%2520tester%26countryCode%3DUS%26radius%3D30%26radiusUnit%3Dmi%26page%3D1%26pageSize%3D20%26filters.postedDate%3DSEVEN%26language%3Den%26eid%3DS2Q_%2C6Q_0&searchId=94e30b33-057d-40b5-b135-723ba2587173',
            'location': 'Ashburn, VA',
            'source': 'dice.com',
            'state': 'VA',
            'title': 'Penetration Tester',
        },
        {
            'city': 'Charlotte',
            'company_name': 'Apex Systems',
            'country': 'US',
            'date_posted': '2021-09-25T22:06:25Z',
            'description': "Apex Systems\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nApex Systems\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\tTester, Security, Systems, Windows, Linux, Middleware, Applications, Database, Management, Testing, API\n\t\t\t\n\n\n\n\n\n\n\n\nFull Time\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nJob Description\n\nPosition: Penetration Tester  Location: 100% Remote  Contract Length: 6 months + Top Requirements:   5+ year of experience in performing penetration tests Some experience in scripting and/or programming as it related to pen testing Must have strong communication skills, personality and be a team player Plus: Knowledge and/or experience with DevOps or automation tools  Day to Day Responsibilities/project specifics:  Principle Duties and Responsibilities:  Work closely with Scrum Teams as a security consultant and educator. Through hands-on testing, verify security controls are in place for recently deployed applications and solutions. Automate repeatable security checks through scripting or other techniques. Assess and recommend methods for consistently implementing security controls through DevOps workflow. 
Create reports both summarizing and detailing findings for Devops, Scrum, and Security Teams. Coordinate with Information Security and Scrum teams to ensure work is prioritized based on risk to the organization.  Basic Qualifications:  Bachelor's degree in Information Systems or related field or equivalent work experience. 5+ years of experience performing penetration tests. Knowledge of managing the entire lifecycle of vulnerabilities from discovery, triage, advising, remediation, and validation. Scripting and / or programming experience. Excellent organization, communication, collaboration, and interpersonal skills. Ability to communicate and present complex issues and ideas with precision and clarity, adjusting appropriately for the audience; ability to communicate effectively at all levels of the organization. Experience working within a large, complex corporate environment providing consulting services on large initiatives. Experience managing and prioritizing multiple tasks in an effective manner. Knowledge and understanding of network and security fundamentals, protocols, and technologies. Strong understanding of mitigating security controls (i.e., anti-virus, IPS/IDS, email filtering, web site blocking, patching) and how they work in an overall defense in depth risk assessment methodology. Understanding of Technology Platforms (Windows, Linux, Open Source, Middleware Applications, Database Applications, Firewalls). Experience developing and providing effective and professional presentations to all levels (including Senior Management). Knowledge of cloud computing technology (e.g. Azure, Google Cloud, AWS, etc.).  Preferred Qualifications:  Industry-recognized security, network, or other professional certifications. Experience in conducting training and mentoring of less experienced security professionals. Strong subject matter expertise in penetration testing and vulnerability remediation. Strong understanding of Information Security industry standards/best practices such as NIST. Strong understanding of Information Security related laws and regulations including HIPAA and PCI. Experience with engineering and/or architecture of technologies such as network firewalls, intrusion detection sensors, antimalware technologies, vulnerability scanning technologies, and APT prevention technologies. Working knowledge of MITRE ATT&CK Framework, Penetration Testing Framework (PTF), and OWASP. Knowledge of API security best practices.  EEO EmployerApex Systems is an equal opportunity employer. We do not discriminate or allow discrimination on the basis of race, color, religion, creed, sex (including pregnancy, childbirth, breastfeeding, or related medical conditions), age, sexual orientation, gender identity, national origin, ancestry, citizenship, genetic information, registered domestic partner status, marital status, disability, status as a crime victim, protected veteran status, political affiliation, union membership, or any other characteristic protected by law. Apex will consider qualified applicants with criminal histories in a manner consistent with the requirements of applicable law. If you have visited our website in search of information on employment opportunities or to apply for a position, and you require an accommodation in using our website for a search or application, please contact our Employee Services Department at employeeservices@apexsystemsinc.com or 844-463-6178.\n\t\t\n\n\n\n\n\nSave\n\n\n\n\n\n\n\n\n\n\n\n\n\nCreate Alert\n\t\t\n\n\nSave\n\n\n\nToggle\n\t\t\t\t\tDropdown\n\n\n\n\n \n \n\n\n \n\n\n\n\n\n\n\n\n Create Alert\n\t\t\n\n\nSave\n\n\n\n Toggle\n\t\t\t\t\tDropdown\n\n\n\n\n \n \n\n\n \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCompany Information\n\nApex Systems is a world class technology services business that incorporates industry insights and experience to deliver solutions that fulfill our clients’ digital visions. We provide a continuum of service from workforce mobilization and modern enterprise solutions to digital innovation to drive better results and bring more value to our clients. Apex transforms our customers with modern enterprise solutions tailored to the industries we serve. Apex has a presence in over 70 markets across US, Canada and Mexico. Apex is a segment of ASGN Inc. (NYSE: ASGN).\n\t\t\t\t\t\t\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDice Id : apexsan \n\n\nPosition Id : BHJOB2374_1188693\n\n\nOriginally Posted : 7 days ago\n\n\n\n\n\nSimilar Positions at Apex Systems\n\nPerformance Tester\n\nCharlotte, NC\n1 day ago\n\n\n\n\nAPI Integration Architect\n\nCharlotte, NC\n1 day ago\n\n\n\n\nCyber Security Manager\n\nSalisbury, NC\n1 day ago\n\n\n\n\nSalesForce Developer\n\nCharlotte, NC\n1 day ago\n\n\n\n\nSoftware Engineer- Terraform, Azure, Google Cloud\n\nCharlotte, NC\n1 day ago\n\n\n\n\nInfo Security Engineer\n\nCharlotte, NC\n1 day ago\n\n\n\n\nMobile Solutions Architect\n\nCharlotte, NC\n1 day ago\n\n\n\n\nAutomation Tester\n\nAtlanta, GA\n1 day ago\n\n\n\n\nAutomated Tester\n\nAtlanta, GA\n1 day ago\n\n\n\n\nApplication Support Engineer\n\nCharlotte, NC\n1 day ago",   
            'detail_url': 'https://www.dice.com/jobs/detail/8e7326153ef2f75224ed2503e95db45f?searchlink=search%2F%3Fq%3Dpenetration%2520tester%26countryCode%3DUS%26radius%3D30%26radiusUnit%3Dmi%26page%3D1%26pageSize%3D20%26filters.postedDate%3DSEVEN%26language%3Den%26eid%3DS2Q_%2C6Q_0&searchId=94e30b33-057d-40b5-b135-723ba2587173',
            'location': 'Charlotte, NC',
            'source': 'dice.com',
            'state': 'NC',
            'title': 'Penetration Tester',
        },
        ...
    ]
}
```

### Function: `glassdoor`

Conducts a comprehensive search of jobs posted on Glassdoor.com based on a free text search query.
```bash
glassdoor(query,page)
```

#### Arguments:

Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`
`page` | `int` | Page Number | `True` | `1` 


#### Return value:

Returns the list of jobs available in json format.

#### Example:
```bash
>>> from jobsearch import glassdoor
>>> from pprint import pprint
>>> pprint(glassdoor("penetration tester"))
{   
    'date': '2021-10-02T10:40:38.477352',
    'jobs': [
      {
            'city': None,
            'company_name': 'TestPros3.1â\x98\x85',
            'country': None,
            'date_posted': '2021-09-25T00:00:00',
            'description': 'Company OverviewTestPros is a successful and growing business, established in 1988 to provide Information Technology (IT) technical support services to a wide range of Commercial and U.S. Federal, State, and Local Government customers. Our capabilities include Program Management, Program Oversight, Process Audit, Intelligence Analysis, Cyber Security, NIST SP 800-171 Assessment and Compliance, Computer Forensics, Software Assurance, Software Testing, Test Automation, Section 508 and WCAG Accessibility Assessment, Localization Testing, Independent Verification and Validation (IV&V), Quality Assurance (QA), Compliance, and Research and Development (R&D) services. TestPros is an Equal Opportunity Employer.TestPros delivers innovative independent IT assessment solutions to critical challenges facing the nation and the world. We support the U.S. Federal Government and Commercial clients within the continental USA. TestPros is dedicated to making lives better, safer, and more secure.Job SummaryTestPros is seeking a Penetration Tester 4 located in the Washington, DC area, for a federal contract. The ideal candidate takes initiative and uses a structured, analytical approach to problem-solving, and looks for process improvement opportunities.Position:  Full-timeCitizenship:  U.S. CitizenshipLocation:  Washington, DC areaClearance:  Secret clearance or higherRequired ExperienceA minimum of five (5) years of experience in penetration testing and/or offensive cyber operations.Demonstrated experience utilizing penetration tools.Hands on demonstrated experience in mimicking threat behavior. (c) At least four (4) in this labor category must be eligible for TOP SECRET/SCI Security clearance and accesses (SI/TK/G/HCS-P). (See Mandatory Requirements C.3).Required Degree/CertificationMinimum certification as 541 (or similar as required by the Technical Instruction) at the Intermediate level per DoDD 8140.01, or successor.Offensive Security Certified Professional (OSCP) or Offensive Security Certified Expert (OSCE) or Offensive Security Exploitation Expert (OSEE) or 
Offensive Security Wireless Professional (OSWP) certification required.All persons performing as Privileged Users are required to have and maintain a final adjudicated Tier 5 security investigation with an IT level-1 designation in Joint Personnel Adjudication System (JPAS) and/or Defense Information System for Security (DISS).BenefitsTestPros offers a competitive salary, medical/dental/vision insurance, life insurance, paid time off, paid holidays, 401(k) retirement plan with company match, opportunities for professional 
growth, cell phone discounts, and much more! All benefits are per TestPros current policies and are subject to change without notice. Benefits are available to full-time employees.TestPros, Inc. is an Equal Opportunity Employer.EEO StatementAll qualified applicants will receive consideration for employment without regard to race, color, religion, gender, sexual orientation, gender identity, marital status, age, national origin, or protected veteransâ\x80\x99 status.kMzHWbmuyCJob Type: Full-timeWork Location: Multiple Locations',
            'detail_url': 'https://glassdoor.com/partner/jobListing.htm?pos=124&ao=1136043&s=58&guid=0000017c3df2163d80e14c4c3a4f781f&src=GD_JOB_AD&t=SR&vt=w&cs=1_8b2bf5a4&cb=1633126848672&jobListingId=1007324420383&jrtk=3-0-1fguv45pnu4tr801-1fguv45qnu3ib800-4712161283befc7e-',
            'location': 'Washington, DC',
            'source': 'glassdoor.com',
            'state': None,
            'title': 'Penetration Tester 4',
        },
        {
            'city': None,
            'company_name': 'MindPoint Group, LLC4.8★',
            'country': None,
            'date_posted': '2021-09-25',
            'description': '',
            'detail_url': 'https://glassdoor.com/partner/jobListing.htm?pos=101&ao=1110586&s=58&guid=0000017c3df2163d80e14c4c3a4f781f&src=GD_JOB_AD&t=SR&vt=w&cs=1_006b650f&cb=1633126848664&jobListingId=1007324738077&cpc=ABD31432EBADCA3A&jrtk=3-0-1fguv45pnu4tr801-1fguv45qnu3ib800-fd820759fa21f851&jvt=aHR0cHM6Ly93d3cuaW5kZWVkLmNvbS9yYy9nZC9wbmc%2FYT05ajJEdzFTanhOTzgzVlZhUU1ReFRKV0NUUmdJOElBUTlQVUR6RlctbEpMaTlKYjJ6dDdablFQbkI3cGRHX1QxdU9IRGhfVHllU0Q4cFJOYjZFWU5lME5yYlI4ZnYtZ3lFak82TDN6MXcyOTZXTElzU0Fjci1zSWRDNi1WRm1scHBxUFFtczNBdkZBTDNPMjI1NFc3SWpvQlBRYXhGcm9YZEx5YWRGSGdsQXlKamM4eXZyN0hXNkZXT1hhUEhpbjRYZ0lXa2NSOG43U2dVN2N4T28xUnkyMnUtbFNKNmhvRHJjMTA0TXYxVnN2eWhCNk9Nd3hLbXNiVmZlRkpMeWpuMkVNd0NRWVRNa2NtVkVubWEwV1FuNFBvSkVCNmgxYU91dE1HR2hlb09RdFQ0NkdESUN2OE9IWlFjcWxDVWZWdXdIMmFvSnRfemRncFY0VU9VZVFvYkozY0VLVkJVbjEtMHI3UmpsWUJfRUNrNTRBUm5BcktyTkZVdEkzai1Wc2M3anY4OG5qT1hJR2dHUEdmdUFiMTVmenFzaGczbW1aRzNpTWNNc3hWUlliQ2NsWWgxenBacENYRGFLdC1lVngwTllWQWo5SDJDUWZlRXBVSXlFZkU2eGdWVFZQSWZhWGMweUxneXp0cXV4ZGNsdnk3d3ZfRVpqdF8tcFhuOW9WbXFCNTNkR3M4TmZmMmdfQmlvbjdadThsU0JaUnZfYTcxV1RrRlNENW5ncEEwNEtUUTNlNFByZGN1TDBWSk9vN3cwelEtY0ZYUXNRT0N4YmI2bGxPWTUyVVVHTS0tR3AzTUl5Z2VkX1ZOQ3Y3LVNlaUJDTlVTTWtHY0FWR2pBT2RpQVE2YWZZaE1YaGNrUlpHVTcwckdFbmo0TmxEQzJfN19NRktKNEp1SVRaS1NyRmxYNUlaTU9xcEJOUzRtb1o1MEVUY3RXbENpaVNrMnlhUFI1Uk5GMml0cFV3RW9tRmZUbHNMb0pDWXpkSDVWb05iNkVkb3ZCVWdhVWNyMzdDajRLaDl2SGFXc2xQdHBKSFJvNG5oVGJjM2tHSk9HdnRXSFNkWjNnbU10WmlXVmt3LXZYSHp2Y0E',
            'location': 'Washington, DC',
            'source': 'glassdoor.com',
            'state': None,
            'title': 'Penetration Tester',
        },
        ...
    ]
}
```

### Function: `xing`

Conducts a comprehensive search of jobs posted on Xing.com based on a free text search query.
```bash
xing(query,page)
```

#### Arguments:

Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`
`page` | `int` | Page Number | `True` | `1` 


#### Return value:

Returns the list of jobs available in json format.

#### Example:
```bash
>>> from jobsearch import xing
>>> from pprint import pprint
>>> pprint(xing("penetration tester"))
{   
    'date': '2021-10-02T10:51:36.396075',      
    'jobs': [
        {
            'city': 'Köln',
            'company_name': 'Stolzberger GmbH',
            'country': 'DE',
            'date_posted': '2021-10-01T11:38:45Z',
            'description': '',
            'detail_url': 'https://www.xing.com/jobs/koeln-it-security-spezialist-koeln-76105443?paging_context=search&search_query%5Bkeywords%5D=penetration%20tester&search_query%5Blimit%5D=20&search_query%5Blocation%5D=&search_query%5Boffset%5D=0&search_query%5Bsort%5D=date&ijt=jb_18',
            'location': 'Köln',
            'source': 'xing.com',
            'state': None,
            'title': 'IT-Security Spezialist (m/w/d) in Köln',
        },
        {
            'city': 'Düsseldorf',
            'company_name': 'Stolzberger GmbH',
            'country': 'DE',
            'date_posted': '2021-10-01T11:37:02Z',
            'description': '',
            'detail_url': 'https://www.xing.com/jobs/duesseldorf-it-security-spezialist-duesseldorf-76105431?paging_context=search&search_query%5Bkeywords%5D=penetration%20tester&search_query%5Blimit%5D=20&search_query%5Blocation%5D=&search_query%5Boffset%5D=0&search_query%5Bsort%5D=date&ijt=jb_18',
            'location': 'Düsseldorf',
            'source': 'xing.com',
            'state': None,
            'title': 'IT-Security Spezialist (m/w/d) in Düsseldorf',
        },
        ...
    ]
}
```

### Function: `stackoverflow`

Conducts a comprehensive search of jobs posted on StackOverflow.com based on a free text search query.
```bash
stackoverflow(query,page)
```

#### Arguments:

Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`
`page` | `int` | Page Number | `True` | `1` 


#### Return value:

Returns the list of jobs available in json format.

#### Example:
```bash
>>> from jobsearch import stackoverflow
>>> from pprint import pprint
>>> pprint(stackoverflow("penetration tester"))
{   
    'date': '2021-10-02T10:52:54.784537',
    'jobs': [
        {
            'city': 'Berlin',
            'company_name': 'STRATO AG',
            'country': 'DE',
            'date_posted': '2021-10-02',
            'description': 'Posted 2 hours ago\n\n\nAbout this job\n\n\n\nJob type: \nFull-time\n\n\nExperience level: \nMid-Level, Senior\n\n\nRole: \nDevOps, System Administrator\n\n\n\n\nIndustry: \nCloud Services, Information Technology, Web Hosting\n\n\nCompany size: \n201-500 people\n\n\nCompany type: \nPrivate\n\n\n\n\n\nTechnologies\n\ngopythonansiblekubernetesopenstack\n\n\n\nJob description\n\nDie STRATO AG sucht am Standort Berlin für den Bereich Backend Development zum frühestmöglichen Eintrittstermin eine/n\nSite Reliability Engineer (m/w/d) für Managed Kubernetes\nWas Dich bei uns erwarten wird:\nUnser Team entwickelt, testet und betreibt ein Managed Kubernetes-Angebot. Kunden erhalten Kubernetes-Cluster, und wir sorgen für Updates, Security, Betriebssicherheit und Monitoring. Wir entwickeln Infrastruktur-Automatisierung (vor allem in Ansible) sowie unsere REST APIs, Patches, Treiber und Features für Kubernetes und Cloud Native Projekte in Go, und CI/CD-Tests und -Prozesse in Python.Für unser Team suchen wir einen weiteren DevOps Mitarbeiter, der uns hilft die von uns betreuten Systeme sicher und produktiv zu halten, und dabei immer einen Blick auf Automatisierung und Verbesserungen hat.\nFür Dich als baldigen Teamkollegen ergeben sich daraus im Wesentlichen die folgenden Haupt-Aufgabenbereiche:\n\nSicherstellung des zuverlässigen Betriebs der Infrastruktur\nAutomatisierung von Infrastrukturaufgaben\nEntwicklung von Test-Pipelines die gleichzeitig schnell und trotzdem gründlich sind\nRelease Management und Rollouts\n\nWas Du dafür mitbringen solltest:\n\nDu bringst Erfahrung aus dem Infrastruktur- oder Backendbereich mit. Am besten natürlich Erfahrung mit Kubernetes, aber gern auch andere - zum Beispiel OpenStack oder AWS.\nDu bist es bereits gewohnt, bei Deiner Arbeit selbstständig und eigenverantwortlich zu handeln, "enge Führung" und das Zerschneiden von Aufgaben benötigst du nicht.\nDu bringst solide Englischkenntnisse mit. Unser Team arbeitet im Schriftverkehr und bei Bedarf auch in Meetings in Englisch.\n\nWir haben gute Erfahrungen mit Berufseinsteigern. 
Natürlich ist die Lernkurve dann entsprechend höher. Du bist bei uns richtig...\n... wenn Zuverlässigkeit für Dich der wichtigste Aspekt jeder Infrastruktur ist.... wenn Go oder Python deine Leidenschaft sind, JavaScript und Frontend-Enticklung eher nicht.... wenn Du gern mit modernen Technologien arbeitest.... wenn Du Dich im Backend wohl fühlst und auch ohne GUIs und Selenium-Tests auskommst.... wenn Du lieber einmal mehr (richtig) automatisierst, als Dinge zweimal zu tun.... wenn Du zusammen mit Deinen Kollegen lieber selbstständig und eigenverantwortlich arbeiten willst, als strikt nach Vorgaben. \n\n\n\n\n\n\r\nApply',
            'detail_url': 'https://stackoverflow.com/jobs/497364/site-reliability-engineer-m-w-d-managed-strato-ag',
            'location': 'Berlin, Deutschland',
            'source': 'stackoverflow.com',
            'state': '-',
            'title': 'Site Reliability Engineer (m/w/d) Managed Kubernetes',
        },
        {
            'city': 'München',
            'company_name': 'Apply',
            'country': 'DE',
            'date_posted': '2021-10-02',
            'description': "Posted < 1 hour ago\n\n\nAbout this job\n\n\n\nJob type: \nFull-time\n\n\nExperience level: \nMid-Level\n\n\nRole: \nMobile Developer\n\n\n\n\n\nRemote details\n\n\nEmployer's note:\nOption des Home Office wird angeboten\n\n\n\n\nTechnologies\n\nandroidjavamobilekotlin\n\n\n\nJob description\n\nFor all our german locations we are looking for a (Senior) Android Developer at BurdaForward (Focus Online and other brands) (m/f/x).\nYou are a clean coder (gender doesn’t matter!) and you love clean code? You know why not even Chuck Norris holds a reference to any Context?So, become a part of the development team around the Focus Online news app and help us create the best news experience for our users!\nWhat you can expect from us ...\n\nDevelopment of the Android app of Focus Online – one of the best news apps in Germany\nWorking on a product and not on projects\nDesign and engineering of software components in close collaboration with UX, Design, Product Management and of course your co-developers\nTouchpoints with Firebase, backend development and everything in and around apps\nBeing part of every step of the development! This includes concepts, design, engineering, implementation and testing\nCollaboration und communication with colleagues from Chip, TV Spielfilm, The Weather Channel, Finanzen100, Netmoms, Bunte, etc.\n\nWhat we can offer you ...\n\nPermanent employment in a future-proof environment\nWe respond individually to your life situation. This includes flexible working time models, sabbaticals and support with childcare\nOur trust-based workplace offer includes the option of working from home or using our individual flexdesk solution in the company office\nSupport and assistance in learning new techniques and technologies – including attending professional conferences and training sessions or simply chatting with colleagues\nYou have a new business idea and want to found a start-up within the company? Convince us and we will support you structurally and financially\nYou will receive a smartphone and a laptop for professional and private use at the start. Apple or Windows? Your choice!\nFun and humor during and outside of work (we regularly play games like Among Us)\nContribute to a product that is responsible for a large part of our traffic and sales – one of our mottos is: User first!\nExciting tasks and freedom to create independently, to give impulses and to actively contribute to our further development in an ambitious working environment\n\nWhat we would expect from you ...\n\nExperience in developing Android apps in Kotlin (and Java)\nExpertise in the field of informatics and computer science\nHigh willingness to learn in every aspect\nPassion and drive to deliver quality work for the best user experience\nHigh enthusiasm for 
new technologies and tools\nPersonal responsibility and accountability\nGood English language skills\n\nWould you like to get a first impression of BurdaForward in advance? Then you should watch our videos on YouTube.\nSign-up to our Tech Newsletter to receive BurdaForward tech an product news as well as invitations to our tech events and the latest 
job postings.\nWe respect diversity and we therefore welcome all applications – independently of gender, nationality, ethnic and social origin, religion and ideology, disability, age as well as sexual orientation and identity.\nApply Now!\nContactLisa TrogusRecruiting Centerbewerbung@burda.comwww.burda.com \n\n\n\n\n\n\r\nApply",
            'detail_url': 'https://stackoverflow.com/jobs/547854/senior-android-developer-burdaforward-focus-burdaforward',
            'location': 'München, Deutschland',
            'source': 'stackoverflow.com',
            'state': '-',
            'title': 'BurdaForward',
        },
      ...
    ]
}
```

### Function: `monster`

Conducts a comprehensive search of jobs posted on Monster.com based on a free text search query.
```bash
monster(query,state)
```

#### Arguments:

Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`
`state` | `str` | Job location | `True` | `CA (California)` 
`page` | `int` | Page Number | `True` | `1` 


#### Return value:

Returns the list of jobs available in json format.

#### Example:
```bash
>>> from jobsearch import monster
>>> from pprint import pprint
>>> pprint(monster("penetration tester"))
{
    'date': '2021-10-02T10:54:35.228911',
    'jobs': [
        {
            'city': 'Chesterfield',
            'company_name': 'Mastech',
            'country': 'US',
            'date_posted': '2021-10-01T05:24:24.173Z',
            'description': 'Job Description:Mastech Digital provides digital and mainstream technology staff as well as Digital Transformation Services for all American Corporations. We are currently seeking a Vulnerability/Penetration Tester for our client in the Telecom domain. We value our professionals, providing comprehensive benefits and the opportunity for growth. This is a Contract position and the client is looking for someone to start immediately.Duration: 12 Months ContractLocation: Chesterfield, VA (100% Remote)Role: Vulnerability/Penetration TesterPrimary Skills: Penetration Testing, Vulnerability, Vulnerability Assessments, Vulnerabilities, Security TestingRole Description: The Vulnerability/Penetration Tester must have at least 5+ years of experience. As the Penetration Testing professional, you should be proficient in vulnerability assessments, penetration testing, and professionally relaying technical vulnerabilities and their impact to technical and non-technical customers.Required Experience:In this role, you would perform various penetration testing assessments for enterprise customers as an individual contributor or as part of a team delivering the assessment. The assessments that would be delivered would either be remote or onsite at a customer location.For the remote assessments, you would telecommute from your home office connecting into attack lab to perform assessments, or for internal assessments travel to the designated customer locations.\xa0You should be comfortable identifying vulnerabilities, exploiting vulnerabilities, performing post-exploitation activities, and explaining the path to compromise to external and internal stakeholders. You should have experience performing these activities manually 
and also leveraging automated tools.Education: Bachelorâ€™s degree in Computer Science, Electrical/Electronic Engineering, Information Technology or another related field or EquivalentExperience: Minimum 5+ yearsRelocation: This position will not cover relocation expensesTravel: NoLocal Preferred: YesNote: Must be able to work on a W2 basis\xa0Recruiter Name: Sachin KumarRecruiter Phone: T: (412) 226-0751 Ext: 2074/C: (412) 968-6186Equal Employment OpportunityMinimum Education Required: Bachelor\n\nYears of Experience Required: More than 5 years\n\nExpected Travel Time: None',
            'detail_url': 'http://jobview.monster.com/Vulnerability-Penetration-Tester-Job-Chesterfield-VA-US-231840905.aspx',
            'location': 'Chesterfield',
            'source': 'monster.com',
            'state': 'VA',
            'title': 'Vulnerability/Penetration Tester',
        },
      ...
    ]
}
```

### Function: `linkedin`

Conducts a comprehensive search of jobs posted on LinkedIn based on a free text search query.
```bash
linkedin(query,page)
```

#### Arguments:

Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`
`page` | `int` | Page Number | `True` | `1` 


#### Return value:

Returns the list of jobs available in json format.

#### Example:

```bash
>>> from jobsearch import linkedin
>>> from pprint import pprint
>>> pprint(linkedin("penetration tester"))
{   
    'date': '2021-10-02T10:57:12.809599',
    'jobs': [
        {
            'city': 'Palm Bay',
            'company_name': 'L3Harris Technologies',
            'country': 'US',
            'date_posted': '2021-10-02T10:45:42.000Z',
            'description': 'Cybersecurity analytical skills to include:Security control selection & assessmentEvaluating network and software design approaches against security control implementationParticipation in subcontractor meetings to ensure they meet cyber guidelinesReview Coverity scan results and ensure SW developers understand resolutionCybersecurity and IT architecture requirements developmentAbility to identify and address / mitigate cyber vulnerabilitiesAbility to engineer cybersecurity solutionsExperience with Linux and Windows based systemsExperience in cross-domain system security and authorizationProvide technical execution support of information security activities associated 
with the authorization and accreditation (A&A) of information systems and data using NIST Risk Management Framework (RMF) (and derivative) processes (SP 800-37, DOD 8510, JSIG, ICD503)Work with B&P teams to develop proposal packages as part of a larger B&P process teamAssist program security in the development of policies and procedures for emerging 
security technologiesSupport vulnerability assessment activities as requiredSupport the evaluation, qualification, testing and delivery of security architecture improvement, obsolescence replacement and vulnerability response projectsExperience in writing and managing RMF body of evidence documents (e.g., System Security Plan (SSP), Security Compliance Traceability Matrix (SCTM), Risk Assessment Report (RAR), Continuous Monitoring (ConMon) Plan, and Security Assessment Plans and Procedures (SAPP)), to include submission and maintenance of documentation in tools such as eMASS and XACTA.Experience with application of Secure Template Implementation Guides (STIGs) on operating systems and applicationsExperience in configuration and use of cyber defense and vulnerability assessment tools such as ACAS and SCCLeadership skills, either directly within the discipline or the ability to lead Integrated Project Teams as the SME/LeadTravel up to 10% domesticallySecurity control selection & assessmentEvaluating network and software design approaches against security control implementationParticipation in subcontractor meetings to ensure they meet cyber guidelinesReview Coverity scan results and ensure SW developers understand 
resolutionCybersecurity and IT architecture requirements developmentAbility to identify and address / mitigate cyber vulnerabilitiesAbility to engineer cybersecurity solutionsExperience with Linux and Windows based systemsExperience in cross-domain system security and authorizationProvide technical execution support of information security activities associated with the authorization and accreditation (A&A) of information systems and data using NIST Risk Management Framework (RMF) (and derivative) processes (SP 800-37, DOD 8510, JSIG, ICD503)Work with B&P teams to develop proposal packages as part of a larger B&P process teamAssist program security in the development of policies and procedures for emerging security technologiesSupport vulnerability assessment activities as requiredSupport the evaluation, qualification, testing and delivery of security architecture improvement, obsolescence replacement and vulnerability response projectsExperience in writing and managing RMF body of evidence documents (e.g., System Security Plan (SSP), Security Compliance Traceability Matrix (SCTM), Risk Assessment Report (RAR), Continuous Monitoring (ConMon) Plan, and Security Assessment Plans and Procedures (SAPP)), to include submission and maintenance of documentation in tools such as eMASS and XACTA.Experience with application of Secure Template Implementation Guides (STIGs) on operating systems and applicationsExperience in configuration and use of cyber defense and vulnerability assessment tools such as ACAS and SCCLeadership skills, either directly within the discipline or the ability to lead Integrated Project Teams as the SME/LeadTravel up to 10% domesticallyEducation:Bachelor’s Degree and minimum 9 years of prior relevant experience, or 
Graduate Degree and a minimum of 7 years of prior related experienceSECRET clearance required to start (must be clearable to Top Secret/SCI)DOD 8570.01M IASAE 2 certification required (CISSP, GIAC, etc.)Bachelor’s Degree and minimum 9 years of prior relevant experience, or Graduate Degree and a minimum of 7 years of prior related experienceSECRET clearance required to start (must be clearable to Top Secret/SCI)DOD 8570.01M IASAE 2 certification required (CISSP, GIAC, etc.)Experience with DoD Special Access ProgramsExperience in Model-Based Systems Engineering (MBSE)DOD 8570.01M IASAE 3 certification is desiredExperience with NSA Type-1 Encryption engineering/certification is highly desiredTop Secret and Top Secret/SCI candidates are extremely competitive',
            'detail_url': 'https://www.linkedin.com/jobs/view/information-security-systems-engineer-at-l3harris-technologies-2684657278?refId=fCYjFJIfqR8IOfME5OrcQQ%3D%3D&trackingId=hLhjDyUWWiWb5VSPOGBu5g%3D%3D&position=4&pageNum=0&trk=public_jobs_jserp-result_search-card',
            'location': 'Palm Bay, FL',
            'source': 'linkedin.com',
            'state': 'FL',
            'title': 'Information Security Systems Engineer',
        },
        {
            'city': 'Fort Belvoir',
            'company_name': 'Aveshka, Inc',
            'country': 'US',
            'date_posted': '2021-10-02T10:54:29.000Z',
            'description': 'The contractor team shall support the Government in identifying vulnerabilities affecting defense critical assets, task critical assets, and critical infrastructure that support defense critical missions. The assessment team works with installation and mission personnel to identify risks that may lead to mission loss or degradation and provide recommendations for risk reduction based on DoD Mission Assurance Assessment benchmarks.  The contractor team shall provide a balanced look at the mission survivability of key DoD facilities and provide specific recommendations with supporting rationale to leadership. These assessments identify vulnerabilities within United States and Allied critical mission systems. The assessment team provides continuing support to infrastructure leadership to enable them to carry out a long-term investment strategy for risk management.  The contractor team shall identify weaknesses that can be exploited. The contractor team shall perform assessments from an adversarial viewpoint and use 
the full spectrum of identified adversarial capabilities, limited only by restrictions mandated by the customer and legal, safety, and security constraints, to test and evaluate protection strategies and demonstrate exploitation of identified vulnerabilities.Not RequiredMinimum of 7 years experience conducting vulnerability assessments on communications using computer networks, industrial control systems, radio, wireless, and other communication systems.  Certification(s) required for this position are as follows: IAT Level II certification as defined and described in Joint Publication 3-13 Information Operations and 3-12 Cyberspace Operations, DoDI 8500.1and DoD 8570.01 and 8570.01-M, and as amended.IAT Level II certification as defined and described in Joint Publication 3-13 Information Operations and 3-12 Cyberspace Operations, DoDI 8500.1and DoD 8570.01 and 8570.01-M, and as amended.TS/SCIExperience with DTRA and/or DODExtensive training programs  Gym membership reimbursement  Education reimbursement  Technology benefits  Commuter benefits  Generous paid time off and much more!',
            'detail_url': 'https://www.linkedin.com/jobs/view/cyber-space-operator-at-aveshka-inc-2417246256?refId=fCYjFJIfqR8IOfME5OrcQQ%3D%3D&trackingId=d3%2FrfqQbBp6Nf4QrpkPACw%3D%3D&position=1&pageNum=0&trk=public_jobs_jserp-result_search-card',
            'location': 'Fort Belvoir, VA',
            'source': 'linkedin.com',
            'state': 'VA',
            'title': 'Cyber Space Operator',
        },
      ...
    ]
}

```

## License

`job-search` is licensed under the
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
