---
layout: post
title: "Job Recommendation Engine"
author: "Ganesan Santhanam"
date: "2024-05-01"
---

## Overview

As part of my role at Maxil Technology Solutions, I led the design and development of a job recommendation engine. The primary goal was to increase job application conversions by providing highly relevant job suggestions to users.

### My Role

I was responsible for the end-to-end development of this feature, from initial design to deployment. This involved architecting the service, selecting the right technologies, and implementing the core logic.

### Tech Stack

- **Backend:** Python, AWS EC2
- **NLP:** spaCy
- **Database:** PostgreSQL with the `pgvector` extension
- **Deployment:** AWS

### Problem & Solution

**Problem:** The existing job board showed generic listings, leading to low user engagement and application rates.

**Solution:** I engineered a service that analyzes a user's profile and skills and compares them to job descriptions.

1.  **Vectorization:** User skills and job requirements were converted into numerical vectors using a spaCy NLP model.
2.  **Storage:** These vectors were stored efficiently in a PostgreSQL database using the `pgvector` extension, which is optimized for vector similarity searches.
3.  **Scoring:** When a user viewed jobs, the engine calculated the Euclidean distance between the user's skill vector and the vectors of available jobs to find the closest matches.
4.  **Deployment:** The entire recommendation service was hosted on an AWS EC2 instance for scalability and reliability.