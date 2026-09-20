# The Heap Book of Questions — Heap Inc. (2022)

*Hypotheses About Your Product and Experiments For Improving It.* Extracted from `the-heap-book-of-questions.pdf`; `<!-- page N -->` markers match the PDF's own page numbering.

<!-- page 1 -->

The Heap Book of Questions
Hypotheses About Your Product and Experiments For Improving It

<!-- page 2 -->

Table of Contents
Introduction
Improving Your Product: A Scientific Approach 4
A Note on Metrics Correlation and Causation

Section 1

Product Features and General Usage 

10

Why Use Quantitive Data?

Questions on Product Features And General Usage

Section 2:
Conversion, Retention, and Customer Health 18
Conversion Rate Optimization Retention Three Stages of Retention

Section 3
Product Launches
30 Days After Launch

29

<!-- page 3 -->

Section 3 - con’t
Active Usage Analysis 6 Months After Launch /1 Year After Launch
Section 4:
Behavioral Segmentation
Recommended Behavioral Segments Touchpoints Outside The Product
Section 5
Marketing
Questions To Ask About Marketing Efforts Your Website
Closing
Worksheets
Hypothesis Brief After-Action Report

36
41 26 47 50

<!-- page 4 -->

Introduction

As a Product Manager, your job isn’t just to build your product—it’s to keep on working to provide value to your users and drive your company’s larger objectives. What’s the best way to do this?
At Heap, we believe the answer is to ask questions.

Welcome to The Heap Book of Questions. In it, we’ll describe a great number of questions, hypotheses, and experiments you can run in your product. We’ll walk through product use cases, behavioral segmentation, conversion, and more. Together, these questions are meant to help you gain a deeper, more impactful understanding of how your product works: what features customers like, where your moments of friction are, how marketing spend can be improved, how you can better measure feature launches, and much more.
Why questions and hypotheses? Simple: If your goal is to improve the product, the best way to do that is to learn about it. Learn everything: how people use it, what problems they have, where they come from, and how the improvements you make impact larger business goals. And the best way to do that is to ask creative questions, then probe the information you have to figure out how to answer them.

Question Experiment
Conclusion

Observation Hypothesis Analytics

<!-- page 5 -->

## Introduction

If this process sounds familiar, it should: it’s the basic model of scientific exploration. Indeed, at Heap we believe that Product Management is most effective (most productive, most focused, most efficient) when it’s performed in a scientific manner. This doesn’t necessarily mean putting on a lab coat every day (though you’re more than welcome to). Rather, it means two things: being rigorous and intentional when generating knowledge and making decisions, and being exploratory with the information you have. Experiment! Try ideas out! Search for unexpected correlations, and see what turns up!
Indeed, while this book offers many questions and helps guide you towards answering them, our ultimate goal is less for you to ask these specific questions than for you to adopt the mindset implied here—to come up with questions that lead you to discover things you’re not currently looking at, but which can return huge dividends when found.
Along the way, we provide many examples of easy-to-find but counter-intuitive insights our customers and partners have encountered, and show how these insights allowed our customers and partners to improve retention, conversion, adoption, loyalty, and revenue.
A note on audience: what follows should be relevant to anyone whose job involves thinking about their company’s product. Product Managers will be the primary readers, but the information in it should also be useful to CPOs/VPs of Product, Designers, Marketers, CEOs, and anyone else interested in building a great product.
Read on to improve your product or feature!


<!-- page 6 -->

## Introduction

Improving Your Product: A Scientific Approach
At Heap, we believe that improving your product is a goal best reached when teams can be both creative and rigorous. This means two things: on one hand, teams need the freedom to ask creative questions, and on the other, that creativity is best served when ideas are tested and verified through organized experimentation.
What does this mean in practice? See the steps below.
The basic steps here form a scientific approach for improving your product, and give you a way to organize your practice. The creativity comes from figuring out what questions you should be asking, and then figuring out how to answer them.

Figure out question

Determine the proper metrics for answering it

Figure out what actions in the
product can give you those metrics

Track those actions and see what data
they give you

Correlation vs. causation: can you disprove your hypothesis?

<!-- page 7 -->

## Introduction

A Note on Metrics
Determining which metrics to gather to answer any given question can be more difficult than it seems. For example: when asking about retention, one might be tempted to simply measure how often users visit your site. (This is what Google Analytics does.) The problem is that raw visit numbers don’t necessarily tell you what users are doing while in your product. For lots of digital products, visiting the site is not at all the same as getting value from your site.
For retention, a more useful metric is one that tells you something like “what is the behavior that signifies getting value in my product, and how often are users taking that action?” Honing in on this metric can take some work, and often some discussion.
In some of the questions that follow, we recom-mend metrics you may want to use. These are offered more as suggestions. Our ultimate goal is for you to spend time thinking about the metrics that will return the most information about your product, or the relevant component of your product.

<!-- page 8 -->

## Introduction

Correlation and Causation
When trying to answer the questions in this book, the information you find will often return you a correlation rather than a causal relationship. We’ll assume you’re cognizant of the difference, it’s worth paying attention to.
For example: learning that people who visit your blog tend to convert more often than people who don’t can be a very useful piece of information. But that observation doesn’t tell you that going to the blog is causing more people to convert.
If going to the blog is only correlated with conversion, but doesn’t increase it, you don’t need to work to push people there.

Indicator?

<!-- page 9 -->

## Introduction

So how can you isolate the difference? We suggest the following: disprove your hypothesis. (Knowing you’ll be trying to disprove it can also sharpen your hypothesis from the beginning.)
For example, If your hypothesis is that going to the blog causes people to convert (instead of arguing that people going to the blog were already more likely to convert, in which case going to the blog would simply be a leading indicator for conversion, not necessarily a cause of it), you will want to also figure out if people who were going to buy anyway tend to go to the blog. There are a number of ways you could do this. You could run an A/B test where some users saw the blog and others didn’t, then track the difference in conversion. You could exclude from your analysis people who viewed the blog after converting (since purchase might be driving traffic to the blog). Or many other options - be as creative as you can!
BAD PM:
“People who convert tend to look at the blog, so let’s push people to the blog.”
GOOD PM:
“Let’s see if people who weren’t going to convert changed their minds by going to the blog.”
Sales
Indicator?
Blog Visits

Cause?

<!-- page 10 -->

## Section One

Product Features and General Usage
This first set of questions includes the basic investigations any PM should be doing. If you’re just starting out with product analytics, these are the questions you should start with, since they give you information on what is working and what isn’t.

<!-- page 11 -->

## Section One: Product Features And General Usage

Why Use Quantitive Data?
PMs may wonder about the value of using quantitative data. After all, customer interviews are a powerful tool PMs have long wielded to find out what users like and what gives them trouble.
One answer is that customers interviews are very useful, but behavioral data can often get you answers much quicker, and can give you much more detail. Customers often say they’re doing something in your product, but product analytics tell you what they’re actually doing. How much time do they spend on certain features? Where do users drop off in the user flow? How do different groups of people use a given feature? Quantitative data can answer these questions immediately.
For best results, we recommend blending quantitative and qualitative processes.
For example, quantitative data can tell you what happens in your product, but can’t always tell you why. This is where customer interviews can be enormously useful. (“I noticed that people with your title tend to use these features in this way. Why is that, do you think?”)
In the other direction, customer interviews can help generate ideas that you can implement as hypotheses. (“5 customers have said they wish there was X feature. Let’s add an improvement, roll it out to half of our customers, and measure the results.”)

Product

Feature

<!-- page 12 -->

## Section One: Product Features And General Usage

Questions on Product Features and General Usage

If you’re at all interested in following a more data-driven approach to product, it’s crucial that you establish baseline metrics, all across your product.
Doing this serves multiple goals:
01  It gives you initial measurements to use
02  It lets you connect your efforts to higher, business-level KPIs. By establishing - and tracking - metrics throughout your product, you’ll be able to see how the changes you make improve the business. If CAC or LTV matter most to your business, your job is to figure out which product changes impact those the most.
03  It helps you prioritize. Establishing baseline metrics is a great way to see which parts of your product are underperforming. It also lets you know what kinds of experiments are more likely to help the business.
Over the next few pages, we try to offer some base-level measurements you’ll want to take in your product, and give you a brief idea of how you can measure these things in Heap.
For some products, a “feature” will be a high-level activity. For others, it will be a small collection of low-level events. The difference is not so important; what is important is that you’re measuring them!
For more information about how to answer these questions in Heap, feel free to visit the Heap Docs.

Note on “How to measure in Heap”:
For these questions alone, we give a brief suggestion of how to use Heap to gather the information you’re looking for. These suggestions are not meant to be exhaustive. There are plenty of other ways you may want to analyze your data, and many further questions you may want to ask after getting these initial measurements.

<!-- page 13 -->

## Section One: Product Features And General Usage

Which features are being used most often?
How to measure in Heap: Count of Features
— Define key events for the features you’re interested in
— Analyze your events
— What is the aggregate feature usage over time? How to measure: Count of events from step #1 (series per event/feature)
— For users of a given feature, how often do they return to use it? How to measure: Retention – Use Interval
— What portion of monthly active users have done event X? How to measure: Ratio of
— “Number of users” vs. “Users who have done [the event you’re interested in] in the past 30 days” (or whatever segment of time is useful for you)
— “Number of users” vs. “In Segment” and “Monthly Active Users”
— Frequency

Are they being used by the people you designed them for?
How to measure in Heap:
Define the Segment of users you designed feature for, then graph the size of segment and Group by “has done [the event you’re interested in].” Bonus: also group by “has not done [event]” to compare adoption rates.
Which features aren’t being used?
How to measure in Heap:
Count of [event you’re interested in]. See which events occupy the bottom of the list.

<!-- page 14 -->

## Section One: Product Features And General Usage

Which groups of customers are using your features?
How to measure in Heap
Count of [event you’re interested in], grouped by different user properties.
Is there a drop-off in my conversion funnel? If so, where is it?
How to measure in Heap
Build a funnel of your conversion steps. Then: — To make exploratory measurements: Query Paths into [event you’re interested in] to discover specific paths that may be interesting or unexpected — To analyze the specific funnel: Funnel , based on Paths
How often are users returning to my product?
How to measure in Heap:
— Retention : Session-Session — Size of segments: DAU, WAU, MAU
What are my baseline metrics for:
How to measure in Heap:
— User activation rate — Time to activation — Retention rate — DAU/MAU

<!-- page 15 -->

## Section One: Product Features And General Usage

Some Scenarios and Hypotheses on Product Features and General Usage:
Now that you have baseline measurements, you’ll be able to dig through your data to see if the numbers you’re pulling up match your expectations. If not, it’s time to figure out why.

SCENARIO 1
Fewer people are using the feature than we would like.
Hypothesis
The feature is too complicated to use. If we make it easier to use, more people will get value from it.
EXPERIMENTS 01. Brainstorm ways to make it easier to use; implement them; test again. 02. A/B test different user flows to see which is adopted more frequently or quicker. — For both options, you’ll want to measure activation and retention for the options you choose, then make decisions based on the results.
Hypothesis
The feature is too hard to find. If we make it easier to locate, more peoplewill start using it.
EXPERIMENTS 01. Put the feature in a different place in your product flow. 02. Add guides to your product, directing users to your feature.

Hypothesis
Not enough people understand the value this new feature brings.
EXPERIMENTS 01. Do more outreach to customers, explaining how useful the feature is. 02. Work with marketing to launch an educational campaign on this new feature.
Hypothesis
This feature isn’t useful. We should sunset the feature.
EXPERIMENTS 01. Eliminate the feature and measure the impact. 02. A/B test: eliminate the feature for some users and assess the impact.

<!-- page 16 -->

## Section One: Product Features And General Usage

SCENARIO 2
Different groups of people are using the product differently.
Hypothesis
We actually have 3 different use cases. If we separate them and optimize each, we’ll do better as a business.
EXPERIMENTS 01. Launch a specialized marketing campaign for each feature. 02. Consider spinning off a sub-product. 03. Decide which use case makes the most money for your company, and commit to it above the others.

SCENARIO 3
People aren’t using a combination of features in the way we designed.
Hypothesis
We should educate people more so that they start using the features in the ways they’re supposed to be.
Hypothesis
We should adjust what our product is supposed to do. Maybe we should shift our business towards the way people actually use the product.
Hypothesis
Only parts of our product are valuable. We should sunset the other parts and focus on the parts that people use.

Even if they only apply to single features in your product, these queries can be quite profound. Getting a strong signal that your product isn’t doing what you hoped it would do is often an indication that you should change something about your business.

<!-- page 17 -->

Client Story
Esurance noticed a big drop-off in their funnel. After digging into their behavioral data, they started to wonder if the problem lay in their forms. (As an insurance company, they needed forms. Lots of forms.) To gather more information, the team instrumented error tracking. (See our docs to learn how!) This let them see what errors customers saw at different places in the funnel. After having done this, they quickly learned that the problem was errors in the forms. This discovery prompted a discussion about what form fields truly needed to be in their online applications. The team realized that they could remove about half of their fields without losing any important information from customers. Once they did this, the drop-off disappeared. The moral of the story? Sometimes the fix is easy. The hard part is figuring out what that problem is. Luckily, all it takes is hypothesis and investigation.

<!-- page 18 -->

## Section Two

Conversion, Retention, and Customer Health

Most companies don’t view customer health as a data-driven process. While good companies use frequent check-ins from customers as a way to gather useful feedback, very few use behavioral data as a tool for improving customer satisfaction.

We think they’re missing a valuable opportunity.

The reason is this: when it comes to satisfaction, interviews are a lagging indicator. Churn even more so. Customers maybe noticing problems months before you receive their feedback. All churn tells you is that you weren’t able to fix problems in time.

If you’re concerned with retention, data can show you which actions predict retention and which predict churn. Tracking these actions give you lead time to intervene before customers get frustrated enough to offer feedback, or simply to leave.

PMs, however, have special insight into these issues. This is because they can see how users behave while in the product. If customers aren’t converting, data can show you where. If users are blocked from reaching your “aha” moments, analytics can show you how. If the right customers aren’t using the right features, data can help you better organize your product.

As a PM, you’re on the front lines when it comes to conversion, retention, and customer satisfaction. Behavioral data is how you get there.

<!-- page 19 -->

## Section Two: Conversion, Retention, And Customer Health

Conversion Rate Optimization
For plenty of businesses, conversion is the event that decides whether you’ll be profitable or not. For eCommerce businesses especially, conversion is what your entire product is geared around (your entire business, often). For SaaS companies, large-scale conversion is often a one-time experience. But many SaaS products offer many instances of micro-conversions: steps that have to be completed for the product to produce actual value.
It’s for these reasons that Conversion Rate Optimization (CRO) is often the product experience that receives the most attention from product teams. Luckily, it’s also a product experience that Heap is particularly well-designed to optimize.

Sign up

NAME@EMAIL.

<!-- page 20 -->

## Section Two: Conversion, Retention, And Customer Health

How To Measure CRO
Before figuring out how to improve CRO, you want to make sure you define conversion in the way that matters to your product. This may involve a discussion with your team. If you’re managing an e-commerce site, conversion generally means “purchase.” For a B2B Saas product, conversion usually means signing up for your service. For FinTech companies, conversion ordinarily means completing an application.
All products are unique, and we heartily recommend working to figure out what exactly “conversion” means in yours.
The next step is to define your conversion funnel. Specify all the steps a customer has to complete before reaching your main conversion event. Everything from “lands on our home page” through “adds item to cart” to “presses ‘buy.’” For a Saas product, the funnel may be more idiosyncratic. Either way, you need to identify every potential drop-off point to identify every potential drop-off point.
Finally, you want to get a baseline measurement of conversion health. The most basic measurement here will be the number of people who convert divided by the total number of people who visit your site. However, you may want to get more specific and calculate a percentage of people who perform an action that is a little more focused than simply “visit your site.” This may be the total number of people who add an item to their cart. This may be the total number of people who log in. This may be the total number of people who start an application.
This may take some calibration. The key is that you want to know what percentage of people, after having engaged with your product in a way that indicates the potential for conversion, actually convert. (As we’ll explain soon, you may also want to establish conversion rates for different cohorts of users.)
Do that and you’re ready to optimize.

<!-- page 21 -->

## Section Two: Conversion, Retention, And Customer Health

Improving Conversion
Now that you’ve established your baseline numbers, it’s time to start improving conversion rates. Here’s where Heap comes in handy.
The first step to improving conversion is to identify drop-off points in your conversion flow. Dig in and see where people leave the funnel. Once you’ve done that, you can start to figure out why.
Questions on the conversion funnel:
— What action counts as “conversion”? — What’s the typical path to conversion?
— Is this the path you want users to take? — Can any steps be eliminated?
Experiment: Create a separate conversion path and A/B test it to see the effects. — Where do most people who don’t convert leave the product? — Are there different entry points into your conversion funnel? If so, which produce the most conversions? — Where do most people drop out of the conversion funnel? — Are there any surprising places where people drop out?

<!-- page 22 -->

Client Story
Crowdtilt (since acquired by AirBnB) was a platform that allowed groups and communities to collect money and fundraise online. One of the company’s main conversion funnels had users create a “Tilt”: a campaign to collect funds from a group, fundraise for a cause, or sell something.
When investigating why people left the funnel, Crowdtilt’s product team noticed that a large number of people would leave the Tilt creation process to visit the “How it Works” page, or other educational pages on the site. The problem was that once people left the conversion funnel to visit one of these other pages, they rarely returned.
The easy solution? Take educational information from the separate “How it Works” page and add it to the Tilt creation funnel, with pop-up modals and in-line descriptions. No longer would customers have to leave the funnel to gather more information. These simple changes resulted in a 25% increase in overall conversion rate.
Were Crowdtilt measuring only sessions or page views, they’d have no idea how to diagnose the drop-off. By exploring the data, they could uncover a problem they would have never seen otherwise. The lesson? Never stop exploring!

<!-- page 23 -->

## Section Two: Conversion, Retention, And Customer Health

Using Segmentation To Improve Conversion
Isolating the moments where people drop out of the funnel can be enormously instructive. Equally useful can be breaking users up into different kinds of segments. Doing this allows you to compare conversion rates across groups, and to target either your marketing efforts or your in-product experience to different users.
There are three basic axes on which you’ll want to evaluate your users: demographics, behaviors, and attribution. It’s key to run through all of these! Your goal should be to locate groups that either convert at a particularly high rate (in which you can put effort into bringing more of these users in), or that convert at a particularly low rate (in which case you can better deploy your internal resources).

<!-- page 24 -->

## Section Two: Conversion, Retention, And Customer Health

Demographic inputs to conversion
Compare conversion rates by segmenting users by:
— Job title — Geography — Company size — Industry — Gender — Age — Education
And more. The specifics will of course be unique to your product, but the more ways you can slice up the data, the more likely you are to stumble onto an underserved segment.
Behavioral inputs to conversion
Compare conversion rates by segmenting users according to whether or not they:
— Read your docs — Visit a specific page,
or set of pages (TEST ALL OF YOUR PAGES!) — Read your blog — Spent time browsing on your site — Click “learn more” — Go to your FAQ page — Recieve your emails — Share something from your site — Use coupons — Subscribe to updates — Use your in-app chat
There are many more. The only limit is how many ideas wyou can come up with.

Conversion rates by channel
Segmenting conversion rates by channel can be extraordinarily useful for directing marketing spend. Too many marketers measure site traffic, when they should be measuring conversion. Simply driving eyeballs to your site is valuable, but it becomes more valuable when those eyeballs are more likely to convert.
For all your marketing channels, you’ll want to measure conversion. These may include:
— Social media — Search engines — Referring sites — Partner sites — Traditional media — Paid ads
Often you’ll be running multiple campaigns on a single one of these channels. Using Heap, you can measure conversion rates for each campaign.
Combination segments
These are just the most basic questions. You can also combine any of these segments to get a more granular view.
— Is the conversion funnel different for different use cases?
— Do engineers who come from your partner sites convert more often than engineers who arrive from other sites?
— Do people who come to your site via LinkedIn and then visit your FAQ page convert more often?
— Do people who read your FAQ page drop off more often?

<!-- page 25 -->

## Section Two: Conversion, Retention, And Customer Health

Retention
It’s true what they say: retention is the best measure of productmarket fit. Conversion is important for getting users in the door, but if you can’t keep them around, you won’t have a successful business. Poor retention rates put far too much pressure on your marketing and sales teams, who have to work twice as hard to get new people in.
Indeed, for Product Managers, there will rarely be a time when you’re not thinking about retention. Which is why you should be doing what too few product organizations do: measure and track retention rates, then experiment with them.

<!-- page 26 -->

## Section Two: Conversion, Retention, And Customer Health

Three Stages of Retention
Let’s dig in a little further. When thinking about retention, it’s important to recognize the three different stages that indicate different types of retention. These are illustrated in the graph at right.
The first stage represents an initial dropoff of users. This kind of churn is to be expected, as far more people will likely try your product once than will visit it regularly. The second stage represents slower, longerterm churn. (Here we’re measuring retention over the course of a year. The actual time frame may change depending on what your product does.) Finally, there’s a significant fall at the end, when the majority of users in your product drop off entirely.

Retention Rate

Stage 1

Stage 2

Stage 3

70% 60% 50% 40% 30% 20% 10%
0%

Same month After 2 months After 4 months After 6 months After 8 months After 10 months After 12 months

<!-- page 27 -->

## Section Two: Conversion, Retention, And Customer Health

How to measure retention
Your first goal should be to define retention. As stated earlier, this can be harder to do than it may seem. Google Analytics, for example, measures retention by “page visits.” But simple page visits don’t tell you if people on your page are actually getting value from your product. (For example: Maybe your CRM product is the CRM their company has purchased. In this case users have to log in every day, but may not be getting value. In the ecommerce world, many sites incentivize customers to return to the site often. But it’s not clear that these return visits produce big purchases.)
Given this, it’s worth spending time figuring out which action in your product most signifies getting value.
Next you’ll want to make your baseline retention graph, which should resemble the graph on the previous page. (In Heap, creating this graph takes less than a minute.) Keeping track of this graph over time can help you figure out which stage of retention most deserves your attention.
Finally, you can start asking the questions that follow. Experiment and see what happens!

Three Stages of Retention

1

2

3

<!-- page 28 -->

## Section Two: Conversion, Retention, And Customer Health

The first stage of retention:
— Do you have a trial period? EXPERIMENTS — Make the trial period longer or shorter — Add more features to your trial period
— How long is your on-boarding flow?
— Where do users tend to drop off in your on-boarding flow?
— How long (either in steps or time) does it take users to get to your “aha” moments?
— How are you presenting information in your product? EXPERIMENTS — Restructure the way you present information — Add guides to your product
— What are the steps users have to take to get to key actions? Can you reduce those?
— At what point do ask users to pay? EXPERIMENT — Put this ask in a different place in your product
The second stage of retention:
— How many people are discovering your features? Are these the people you want to be discovering these features?
— What counts as beginner, intermediate, and advanced usage? Are users at each stage properly directed to the features that are most relevant for them?
— Is it clear when users gain value in your product? Is there a way to signal that they’re gaining value?
— Can users know how they’re gaining value in your product relative to your competitors’ products? Is there a way to signal that to them?

— How easy is it for users to perform your key features? Can you make the process simpler?
— Is your product bloated? Are key user flows straightforward?
— Are there ads on your site? Do they get in the way for users?
— Are your features keeping up with trends in the market?
— Are there incentives for continued users to keep coming back?
— Are there incentives for new users to come back?
— Are features in your product named in ways that indicate value?
The third stage of retention:
If you’re experiencing churn at the third stage of retention, you’ve got a potentially major problem. We recommend examining some deeper assumptions.
— How long after using the product do users tend to drop off?
— Are you selling to the right users?
— Are you selling a product that solves a legitimate problem?
— Should you change your pricing model?
— Are customers getting enough support?
— Are you following up with them enough?
— Are you talking to customers?
— Do you have a new competitor that is eating up your business?
— Is your product only useful in the short term? Is the problem that its novelty wears off?
— Have you emphasized your differentiators enough?

<!-- page 29 -->

## Section Three

Product Launches

Many teams get product launches wrong. At the majority of companies, the standard for success is simply “we pushed this feature out.” How do you know the feature did what you wanted it to do? Who cares -it’s released!

The problem? Simply having pushed a feature out tells you very little. Of course you should pat yourselves on the back for having released something. (Good job!) But what you really want to know is whether the feature accomplishes its goals.
How do you assess that? Well, first you have to articulate those goals. Before even developing a new feature, we recommend writing a HYPOTHESIS BRIEF. This brief should spell out what KPIs your feature aims to move, and what will count as success.
It’s important to be specific when articulating this success criteria. Every feature you create should be targeted towards a specific segment of users. It should also target specific behaviors and name the KPIs you hope it will move. An answer like “this feature will lead users to convert more” isn’t specific enough to measure. Better is, “this new feature will lead users to do X, which will change the way they do Y, which will raise retention rates and NPS score.”

After launching, there are a ton of questions you want to ask about your feature. Here are some, organized by time frame.
Feature 1
Feature 2
At the end of this ebook you’ll find a Hypothesis Brief worksheet you can use for this. You can also download a copy from heap.io

<!-- page 30 -->

## Product Launches

30 Days* After Launch
*30 days may not be the right time frame for your product. The goal is simply to choose a period in which enough people will have used your feature to give you a sufficient set of data. 30 days is often a good guideline for B2B Saas products.
Question on Adoption
— Are people engaging with my feature? — How are users discovering the feature? — Are they using this feature alongside
the other features it should be used with? — What are users doing before and after using
this feature? — Is use of this feature correlated with a
drop-off in the use of any other features? — Are people using this feature once or
multiple times?

28 29 30 31 32

<!-- page 31 -->

## Product Launches

Active Usage Analysis
After assessing if people are using your feature, you can dig into who is using your feature. We call this approach Active Usage Analysis.
To repeat: when designing a feature, you should have a persona in mind. “All users” is rarely a focused-enough category to design for. Rather, features should be designed for a specific type of user. New users, power users, and resurrected users, are all great categories for this.
Active Usage Analyses can help you determine if the right people are using your feature. Or, if they’re not, who is.
Who is using and not using my feature? Query feature adoption for:
— Core users? — New users? — Resurrected users? — Power users? — Users with specific demographic features? — Users with specific behavioral features?
(Users who have also done X thing in your product — Mobile vs Web users? — Users from different sources?
Active Usage Analyses can help you determine if the right people are using your feature. Or, if they’re not, who is.
— For each user group that is using the feature, how often are they using it?
— Are they using the feature in the way you’d imagined?
— Where in the user flow are they using the feature?

<!-- page 32 -->

## Product Launches

Two caveats for Active Usage Analysis:
01  It’s important to run active usage analysis on all of these groups. Ideally you’ve set out to design a feature for a specific group of users. But if you find out that other groups of users are also using your feature, that gives you critical, potentially actionable information.
In Heap running queries on different groups takes very little time - you can run each in a minute or so. But checking usage for all these groups can surface extremely useful insights. It’s this kind of exploratory work that gains you valuable knowledge about your product, far more than you’ll gain if you only analyse usage among users you ostensibly designed the feature for.
02  Remember, your main goal should be to disprove your initial hypothesis. This is a far more useful approach than just trying to prove it. It’s by trying to disprove your hypothesis that you’re most likely to stumble onto other, unexpected correlations.

Agility in Product
You design a feature specifically for new users. The idea is to make it easier for new users to perform some key actions in your product. After running your queries, however, you notice that core users are also using the feature.
Interesting! The next step should be customer interviews. Call up the core users who are using the feature and ask them why they find it valuable. Maybe they find it valuable because X, or maybe Y.
Whatever the answer, this is information that can help you adjust. Maybe you realize that your feature is actually better understood as a tool for core users, and you decide to optimize appropriately. Maybe you split your new feature into two, spinning off a separate revenue stream. Maybe you keep the feature as is, but market it separately to different user groups.
In all cases, it’s only by running all these queries (which in Heap might take you 10 minutes total) that you’ve discovered this information. Customer interviews may have given you the same information, but much later and less clearly, giving you far less time to pivot.
Lots of businesses talk about “agility.” This is what agility means.

<!-- page 33 -->

## Product Launches

Some Scenarios and Hypotheses on Assessing and Improving your Feature:

SCENARIO 1
Fewer people are using the feature than we would like.
Hypothesis
The feature is too hard to find. If we make it easier to locate, more people will start using it.
EXPERIMENTS 01. Put the feature in a different place in your product flow. 02. Add guides to your product, directing users to your feature.
Hypothesis
People don’t know what the feature is for.
EXPERIMENTS 01. Add in-app guides explaining the feature 02. Increase communication about the feature 03. Change the name of the feature to something more understandable Scenario 2:

People use the feature once or twice, but don’t continue to use it.
Hypothesis
The feature is too difficult to use. EXPERIMENTS
01. Add more guardrails to the features 02. Reduce the number of steps it takes to do the
main action
Hypothesis
The feature doesn’t add enough value. FOLLOW UP
Do customer interviews to see if the feature solves an actual problem
EXPERIMENTS 01. Make the feature optional and see who opts in

<!-- page 34 -->

## Product Launches

6 Months After Launch/ 1 Year After Launch

While the questions above are designed to assess if people were using your feature, which people were doing so, and for how long, the questions to ask six or twelve months after launch are about the impact of your feature on the business.
If you wrote a Product Brief before launch, you will have already targeted KPIs you want your feature to impact. Now is the time to measure them.
At the same time, it’s key to remember that simple increases in KPIs don’t tell you much. As the product owner, your job isn’t just to show that conversion increased (or whatever metric you were ultimately trying to impact). It’s to show that your feature impacted this metric. This is good for two reasons:
— It tells you how your feature is being used
— It helps you justify your efforts to management
So how do you go about showing that your feature impacted metrics? At the risk of repeating ourselves too many times, the crucial strategy for assessing impact to disprove your hypothesis. Let’s play “Good PM, Bad PM” again:

Questions to ask six months and a year after launch:
How did X feature?
— Improve retention? — Increase sales? — Improve engagement? — Reduce customer churn?
BAD PM:
“I hypothesized that adding X feature would increase conversion. So I queried whether conversion increased among people who used X feature. It did! My feature was a success.”
GOOD PM:
“I hypothesized that adding X feature would increase conversion. So I queried whether conversion increased among people who used X feature. Then I queried whether conversion increased among people who didn’t use X feature, and compared the results. Then I queried whether conversion increased across different user groups, and asked how much use of this feature correlated with retention.”

<!-- page 35 -->

Client Story
ThirdLove is a D2C company that sells bras tailored to a huge range of sizes and shapes. They accomplish this in part through their online FitFinder quiz, which helps people find the perfect-sized bra. Because the FitFinder is so important to their business, ThirdLove spends a lot of time trying to optimize it. One experiment proved particularly interesting. After changing the way different products were displayed in the FitFinder, ThirdLove noticed a decrease in clickthrough rates. However, the team was savvy enough to measure the downstream effects of this change. It turned out that while overall click-through rates went down, the percentage of people who purchased after clicking through went up! What seemed like a locally negative change ended up being net positive for the business. The moral? Changes can resonate in all sorts of ways. Be sure to explore them!

<!-- page 36 -->

## Section Four

Behavioral Segmentation

For decades, companies have segmented their customers using demographic data. Though details change, these tend to follow a familiar formula. Urban men under 5’7” who wear platform shoes and drink light beer tend to vote for a certain political candidate. Married women between 25-30 who went to Midwestern colleges and currently have one child prefer their kombucha in a blue bottle.

Certainly, knowing who is likely to buy a certain flavor of toothpaste can help marketing efforts. But in most digital products these demographic data points tend to be less useful. Why? Because demographic data is a poor proxy metric for in-product activity.
The general theory behind demographic segmentation is that knowing which group a user comes from can help predict what they’ll do in your product. In digital products, however—especially B2B SaaS products—demographic data usually ends up telling you scant little about conversion, retention, or feature interaction. This is because demographic data is broad, not granular, and by nature applies heuristics across a wide group of people.

At Heap, we recommend a different approach: Behavioral Segmentation. Behavioral Segmentation turns the demographic model on its head. When you take a behavioral approach, you track what people actually do in your product. You see what behaviors tend to correlate with other behaviors. You can segment user groups with whatever degree of granularity is most effective. You can see what sorts of activities predict future activities. And so on.

<!-- page 37 -->

## Section Four: Behavioral Segmentation

Analyzing users by behavior lets you target customer groups with pinpoint accuracy. Once you’ve located a segment of users that is meaningfully distinct, you can start sending them specialized marketing materials or provide different in-app experiences. Send emails. Add in-app guides. Offer them coupons. Call them. Give them a discount.

Actionable insights from behavioral segmentation:

— You discover that users who buy handbags from your fashion website tend to buy shoes as well. You start sending an email or alert offering a 20% off coupon for shoes to users who recently bought a handbag.
— You discover that visitors who use your free app’s bookmarking functionality tend to upgrade to a paid membership at a higher rate than those who don’t. You can create an in-app guide that encourages new visitors to use bookmarks.
— You discover that users who are inactive for longer than 60 days have a low rate of retention. You can send a special three-stage email marketing campaign to re-engage users who have been inactive for 30, 45, and 60 days.
— You discover that customers with a low NPS score rarely view your documentation. You invite them to a product training session that uses your documentation as a resource.

10:10 Search

M.M. LaFleur

Sales vs. emails

<!-- page 38 -->

## Section Four: Behavioral Segmentation

Recommended Behavioral Segments:
As always, we offer the following only as recommendations. Feel free to explore and see what insights you can turn up.

Step 1 – Identify meaningful groups. For E-commerce sites, for example, your groups might be:
— High-value spenders — Low-value spenders — People who shop often but don’t buy — Return purchasers — Cart abandoned

Step 2 – Pick one of these groups and start exploring! For example, you could ask if people who spend a lot of money in your product also ...
— Use your search function? — Go through more pages on your site? (window
shop?)
— Read reviews on your site? — Leave a review? — Read product descriptions? — Click on similar items? — Come from referring sites? — Receive your newsletter? — Get regular emails? — Use your in-app chat? — Use coupons? — Sign up for updates?
These specific questions may not apply to your product, of course. That’s fine! The point is to get in the habit of checking lots of correlations, since doing this can give you crucial information for targeting different kinds of customers.

<!-- page 39 -->

## Section Four: Behavioral Segmentation

Touchpoints Outside The Product
Measuring behaviors from people who come to your product through different channels can also be a useful source of information.
— How do people who have received emails behave? (Do they make more purchases, use different features, come more often?)
— People who have visited your blog? — People who come through paid ads? — People who arrive through social media? — People who have attended your events?
Again, try as many of these as you can! Any might be correlated with specific purchasing behaviors. Knowing which ones matter can help organize both your product roadmap and your marketing efforts.

<!-- page 40 -->

Client Story
MM Lafleur did a behavior analysis on touchpoints outside the product. They found that when they compared people who received emails with people who didn’t, the people who received emails, even if those emails weren’t opened, make more purchases in their product. As a result, MM Lafleur hypothesized that emails were less important for what they contained and more important for simply showing up—the hypothesis was that the fact that emails showed up every day kept potential purchasers aware enough of the brand to remember to actually make the purchase they’d been considering. The fact that people who received emails make more purchases didn’t necessarily prove causation, of course. It’s possible that people who received emails were already more invested in the product. But these results did allow MM Lafleur to not worry so much about what went into their emails. Simple messages were sufficient. The team could spend its precious time working on other activities.

<!-- page 41 -->

## Section Five

Marketing

One of the most powerful things you can do with behavioral data is measure the impact of your marketing efforts.

In the same way that teams often ignore the downstream effects of features they design, marketers often ignore the downstream effects of their investments.
This is important, because what matters to your product is what people do there! For example: you’ve decided to throw significant marketing spend into a specific source. That source brings 1000 new users to your site. Great! However… you later realize that only two of these users convert. Is that ratio what you’re shooting for?
In this scenario, marketing may be happy. They’ve brought in a ton of new users! But from the business’ perspective, there may be far more efficient ways to allocate that money. How do you know the difference? By measuring user behavior.
The situation with A/B tests is similar. A/B tools are extraordinarily useful. (As proponents of the scientific

method, we highly encourage A/B testing.) The problem is that most A/B tools tell you only how many people chose either option. What you’re interested in is what the people who chose each option did.
Finally, we can’t recommend this enough: MEASURE CHANGES ON YOUR WEBSITE. One very easy way to use Heap is to assess the effects of different headers, copy, organization, user flows, and other web elements. You can run A/B tests on these and see which better predict conversion, activation, and retention.
Marketing is built for data. Jump on in.
Version B
Version A

<!-- page 42 -->

## Section Five: Marketing

Questions To Ask About Marketing Efforts:
If there’s a single question that marketers hate, it’s “how can we measure ROI on your spend?” (Seriously. Ask any marketer.)
To do this, lots of marketing teams come up with some kind of arbitrary system for estimating pipeline. Luckily, you can do better.
Measuring user behavior lets you understand how people from different channels act once they’re in your product. This is powerful information that can dramatically affect the way you plan your marketing spend.

For every channel users come from:

— What percentage convert?
— What’s the average spend of those who do convert?
— Which features are they likely to use?
— Which features are they likely to not use?
— What’s their average retention rate?
— What parts of your site do they tend to visit?
— Which pages and/or blogs do they look at?
— Do they read reviews? — Do they use your FAQ and/or help
pages? — Do they visit your docs?

— What other touchpoints do they interact with? Do they also get emails? Attend events? Use coupons? Talk to salespeople? (Doing this might require you to investigate SFDC)
— How do they segment? Do they tend to be high-spenders or low-spenders? Power users or low-volume users?
— If you’ve already figured out which actions in your product tend to predict activation, retention, or revenue: Do these users tend to take this action? How often?

<!-- page 43 -->

## Section Five: Marketing

Your Website
A very easy way to use Heap is to measure the effects of changes on your website. Many, many companies put money into marketing, but spend very little time evaluating the effectiveness of their homepage, or almost anything they put on their website. Channels, paid ads, events—these all get measured and reported. But the website—the asset that literally every prospect will visit—often receives less scrutiny.
If you’re savvy, you’ll start measuring how likely people who visit certain parts of your site are to convert, or to be retained. This gives you immense predictive power, and can help you optimize your website and/or homepage to generate more revenue. Even more powerful, you can measure different types of content to see which makes the largest impact. (Lots of companies do this with pageviews, but pageviews don’t tell you which viewers are likely to convert. A blog post may get lots of views, but produce little conversion.)
It’s time to change that. Behavioral data can provide a wealth of information on the strengths and weaknesses of your website. Use it.

Questions About Your Website
— Which pages most correlate with conversion?
— Which flows correlate with conversion?
— Do people who convert tend to look at your FAQ page?
— Do they read the blog?
— Do they scroll down the page?
— How much time do they spend on your site?
— Does going to a sub-page correlate with using or purchasing a specific item or feature?
— Do people who go to your Events page show up at your events?
— Which pages are never visited?
— If a page is rarely visited, does it still correlate with purchase or a different behavior? (It’s possible that a page is visited rarely, but is critical to retain a small group of users.)
And so on. The options are endless. You can also ask these same questions with any specific segment of users.
— What pages most correlate with conversion for each segment of users?
— Which flows correlate with conversion for each segment of users?
— Which types of content do different segments of users tend to consume?

<!-- page 44 -->

## Section Five: Marketing

SCENARIO 1
More people read blog posts tagged “insurance,” but people who read blog posts tagged “commerce” convert at a much higher rate.
Hypothesis
We should attract more people who are interested in commerce. If we adjust our content strategy to focus on commerce, more of the customers we want will come to the site
EXPERIMENTS 01. Write more blogs on commerce, then track them against spend in your site. (It’s possible that people who are interested in commerce spend more, but that the number of people interested in commerce is too limited for you to pivot your strategy to accommodate them.)

SCENARIO 2
People who read the FAQ page tend to be high spenders.
Hypothesis
We should add more of the FAQ information to our main pages to reduce friction. High spenders want this information, so we should make it easy for them to get it.
EXPERIMENTS 01. Eliminate the FAQ page and add the content to your main pages
Hypothesis
We should add links to the FAQ page, directing people to our most expensive items. People on the FAQ page are likely to be high spenders, so we should direct them to expensive items.

<!-- page 45 -->

## Section Five: Marketing

A/B Tests
A final and also powerful way to use Heap is to measure the downstream effects of your A/B tests. A/B tools can tell you which option more people choose, but the more valuable information for you is to know what those people did. You can run endless experiments on your website and check to see which changes drive users towards the behaviors you want. (Note: by bringing this data into Heap, you can also see how users behave in parts of your product that are not part of your experiment.)

A few examples, out of many:
Change any of the following and see if it drives more people towards conversion (or your desired behavior):
— Copy on your page — Messaging on any page — Location of buttons — Your hero image(s) — Recommendations — Animations — Product Descriptions — Ratings — Relative size of images — Page length
Or anything else! For web designers, tracking behavioral data can be a critical way to gauge impact.

<!-- page 46 -->

Closing

The key to building a good product: keep asking questions!

While this book provides long lists of potential questions, our real goal is to promote an mindset that’s about persistent exploration. Even the most basic questions, when answered properly, can be enormously revealing. Even answering a child’s “Why is the sky blue?,” for example, requires a profound scientific response.
Indeed, some of the creativity involved product management comes from trying to answer questions that may not be immediately answerable. How do you find answers? By being a good scientist: testing hypotheses, running experiments, exploring your product, and iterating over time.
A B
C B

As you strive to be more scientific, more rigorous, more precise, and more systematic about product development, we hope you exercise these creative muscles and discover ways to generate actionable information about your product.
If you have questions or thoughts about any of the material in this book, or if you simply want to learn more about how Heap’s approach to product management can be useful to you, we encourage you to get in touch at support@heap.io.
We thank you very much, and look forward to working with you to innovate the future of product.

C

<!-- page 47 -->

## Worksheets

Hypothesis Brief
Two-sentence summary
This should take the form of “Right now X. We hypothesize that if we change Y, Z people will do A, and the impact will be B.” Do this part last.

01. Problem Statement
What problem are we trying to solve?

a. Who is having this problem and how do we
know?
Examples from specific customers, from data, or from our backlog.
b. How do people currently solve this problem?
Workarounds? Other tools? Do they not know it’s a problem?

c. How do our competitors solve this problem?
d. What are the jobs to be done that are impacted
by this problem?

<!-- page 48 -->

## Worksheets

02. Solution Hypothesis
What does the solution look like?

a. How do we hypothesize that people will act
differently once this solution is in place?

d. What business goal do we expect this to solve
for our company?

b. Is there a specific user group to which this
changeis targeted?

e. How long do we expect it to take to implement
this change or test this hypothesis?

c. What metrics should we expect to change? How
will we expect them to change?

<!-- page 49 -->

## Worksheets

03. What will count as success?
Be specific. Metrics, actions taken or not taken, percentage of people using the feature, etc. Include time. If metrics are involved, be clear about how we can eliminate other possibilities.

04. Open Questions

05. Additional Resources

<!-- page 50 -->

## Worksheets

After-Action Report
01. What Hypothesis Were We Testing?
Provide the two-sentence explanation from the Hypothesis Brief.

02. What Changes Did We Make?

a. What was the timeline? 03. How did we do relative to the success criteria in the Hypothesis Brief?
(List relevant metrics, customer quotes, feedback, adoption rates, etc.)

<!-- page 51 -->

## Worksheets

04. What else did we see?
Other metrics that may have been moved or not moved, other user feedback, unexpected effects of the change, etc.

05. What were our main learnings?
Key insights we gained from this experiment

06. What new hypotheses does this action suggest?
Potential next steps
07. Conclusion

<!-- page 52 -->

About Heap
Heap’s mission is to power business decisions with truth. We empower product teams to focus on what matters — building the best products — not wrestling with their analytics platform. Heap automatically collects and organizes customer behavioral data, allowing product managers to improve their products with maximum agility.
Visit heap.io to learn more.
