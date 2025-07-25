# cintel-05-cintel
## Action 1: Review Key Terms and Concepts
Review these key terms. Once you've heard of them, you can use your favorite AI or other resources to learn more. 

Data at Rest vs. Data in Motion: Data at rest is stationary, stored data, unchanged until it is accessed or modified. In contrast, data in motion is actively transferring, such as streaming data from IoT devices. Data in motion requires different management, processing, and insight derivation approaches.

Traditional Methods vs. Live Data: Traditional data analysis often relies on batch processing, suited for data at rest. However, live data's continuous and rapid nature requires real-time processing methods, making traditional batch processing ineffective for timely insights and actions.
Data Streams: These are sequences of data generated continuously by different data sources. Understanding data streams is crucial for real-time analytics and decision-making.

Continuous Intelligence (CI): This is the practice of using real-time analytics to process data in motion. CI enables immediate insights and actions based on live data, contrasting with batch processing used for data at rest.

Deque (Double-Ended Queue): A deque (pronounced "deck") is a data structure that allows insertion and removal of elements from both ends efficiently. In the context of live data, deques are useful for holding recent data points for quick analysis without the overhead of processing the entire stream. For example, a deque makes it easy to do analytics on the last, most recent 20 points. It enables continuously updated machine learning models reflecting the current trend. 

Data Lake: A storage repository that holds a vast amount of raw data in its native format. Data lakes are flexible and can store both structured and unstructured data.

Data Warehouse: A system used for reporting and data analysis, storing structured, filtered data that has already been processed for a specific purpose.

Data Pipeline: A set of data processing elements connected in series, where the output of one element is the input of the next. Data pipelines are essential for moving and transforming data in motion.

Data Lakehouse: A newer concept that combines elements of data lakes and data warehouses, offering the scalability and flexibility of lakes with the governance and performance of warehouses.

## Action 2: Review Available Tools
At work, there are many popular tools that you might encounter that work well with live data and data streams. You should recognize these names and understand where and when they are useful. 

Apache Kafka: An open-source stream-processing software platform designed for handling real-time data feeds. Kafka is widely used for building real-time streaming data pipelines and applications. Example users include LinkedIn and Netflix. 

Apache Flink: An open-source framework and distributed processing engine for stateful computations over data streams. Flink is designed for high throughput and low latency. Example users include Uber,  energy companies, and Alibaba (particularly during their annual Singles' Day (11/11) global shopping festival, processing billions of events in real-time).

Spark Streaming: Part of Apache Spark, this tool enables scalable, high-throughput, fault-tolerant stream processing of live data streams. Example users include Netflix recommendations, Pinterest, eBay, and Amazon analytics. 

RabbitMQ: An open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). RabbitMQ facilitates the efficient handling of messages in a distributed system, making it ideal for scenarios where high-throughput and reliable message delivery are required for data streams. Example users include Instagram and Reddit. 
Python Libraries for Streaming: Libraries like Streamz, Faust, and Pulsar help work with streaming data in Python environments, integrating with common tools.

Streamz is a simple option that works with Pandas

Faust, built on Kafka, is scaleable and enables complex analysis

Pulsar is a distributed system for high-throughput publish/subscribe systems that includes distributed storage and is used by Splunk, Yahoo, and Overstock. 

Python Data Structure for Streaming:  We will use Python's collections.deque class to understand how you can manage recent data efficiently. We'll use the deque class in our project. 

## Create and verify your project repo has all 4 files:

README.md
.gitignore
requirements.txt
app.py (OR dashboard/app.py if working locally and deploying to GitHub pages - see more below).
If you decide to try the local development, you'll be able to deploy your live date site using GitHub Pages. To make it easy to build our app from a folder and export the app into the docs folder (for Pages), please move your app.py file into a folder. I named my folder "dashboard", so I have a dashboard/app.py file and no app.py in the root folder. This is a more common organization for Python projects. For help adding a folder in VS Code, ask your favorite AI, do a web search, or try this link: https://github.com/orgs/community/discussions/22534Links to an external site.

Aside: To create a file in a folder in GitHub, just name the file with the relative path - for example in GitHub, new File, name it 

dashboard/app.py
And it should work.  Try not to make changes on your machine and in GitHub at the same time - that can create "merge conflicts" which are best avoided. Only edit the repo from one place  at a time. 

## Start Project
Start here:

https://github.com/denisecase/cintel-05-cintel-basicLinks to an external site.

Then, implement this slightly fancier version:

https://github.com/denisecase/cintel-05-cintel-fancyLinks to an external site.

Then, implement this version with a deque wrapped in a reactive value, showing the associated datagrid and a plotly chart with online machine learning. 

https://github.com/denisecase/cintel-05-cintelLinks to an external site.

Read the comments. Organize the code. When you get your version implemented, save it - use a good commit message to indicate you've recreated the functionality as requested. 

Then, review the app, and:

Propose a modification / enhancement / extension. 
Plan your work. 
Estimate the time it will take. 
Implement your plan. 

### Penguin Colony Wind Monitor 🌬️🐧
#### Your job is to:
Implement the example provided (live data simulation using PyShiny).

Propose and implement an enhancement, extension, or variation on the app.

#### Possible Enhancements:
Changing theme, colors, visuals to be more engaging

Changing layout to better display data (e.g., deque or charts)

Changing the chart to avoid flashing on update

Changing the subject domain (e.g., from Antarctic temperature to another metric)

Integrating live data into a previous app for continuous intelligence

Goal: Understand the possibilities and challenges of working with live data and consider how “data in motion” can enhance analytics projects.

#### What I Implemented
1. Base Implementation
Started from the PyShiny live data example (temperature readings in Antarctica).

Used a reactive.calc() to generate fake live data at regular intervals.

Stored the last 5 readings using a deque.

Displayed:

Current reading in a value box

Historical readings in a data table

A scatter plot with regression line for trends

A histogram of recent values

2. My Enhancement
Changed domain: Simulated wind speed in a penguin colony instead of temperature.

Wind speed range: 5–40 km/h.

Added emojis and Font Awesome icon (wind) for visual appeal.

Added a histogram to show wind speed distribution.

Fixed axis formatting on the trend chart to remove scientific notation (display HH:MM:SS).

Updated titles and labels to match the new theme.

Features
Live updates every 5 seconds (configurable).

Deque storage: Always shows most recent 5 readings.

Regression line: Automatically fits best line to recent trend.

Multiple visualizations:

Trend chart with regression line

Histogram distribution

Data table of recent readings

UI Enhancements:

Sidebar with description and resource links

Value box showing current wind speed

Emojis and iconography for clarity and fun

Code Overview
Key Components
1. reactive_calc_combined()
Generates wind speed and timestamp every 5 seconds.

Appends data to a deque.

Returns:

deque_snapshot (raw deque)

df (pandas DataFrame)

latest_entry (most recent reading)

2. UI Layout
ui.page_opts(): Page title and full-width layout.

ui.sidebar(): Info, links, and theme branding.

ui.layout_columns():

Value box for current wind speed

Card for current timestamp

Additional cards for:

Recent readings table

Wind speed trend with regression line

Wind speed histogram

3. Plotly Enhancements
Scatter plot for trend.

Regression line added using scipy.stats.linregress.

Fixed x-axis to display time properly (no scientific notation).

#### How to Run
Option 1: Online (ShinyLive)
Copy full code into https://shinylive.io/py/

Click Run.

Option 2: Locally in VS Code
bash
Copy
Edit
1. Install PyShiny
pip install shiny shinywidgets pandas plotly scipy faicons

2. Save code as app.py

3. Run app
shiny run --reload --launch-browser app.py
Files
app.py – Main PyShiny application

README.md – Documentation (this file)

Future Improvements
Color-coded value box (green/yellow/red) based on wind speed.

Add penguin-specific data (colony size, temperature, etc.).

Integrate real weather API instead of simulated data.

Combine histogram and trend in one dashboard for cleaner visuals.

#### Create Github Pages for app
Create an index.html for the site