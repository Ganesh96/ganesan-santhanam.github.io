---
layout: post
title: "Candidate Referral System"
author: "Ganesan Santhanam"
date: "2024-04-01"
---

## Overview

At Maxil Technology Solutions, I designed and implemented a novel candidate referral system to incentivize high-quality referrals. The system uses a graph database to model and track the network of referrals.

### My Role

I designed the data model for the graph database, developed the backend service to manage referrals, and deployed it on AWS.

### Tech Stack

- **Backend:** Python
- **Database:** Neo4j Graph Database
- **Deployment:** AWS ECS

### Problem & Solution

**Problem:** The company wanted to encourage employees and external recruiters to refer high-quality candidates, but the existing system was manual and offered little incentive.

**Solution:** I built a system around a "vouched referral" concept.

1.  **Graph Model:** I used a Neo4j Graph Database to model the relationships between referrers, candidates, and jobs. This allowed for complex queries, such as finding the shortest path between a candidate and an open role.
2.  **Incentives:** The system tracks "vouched referrals," where a referrer has a strong connection to the candidate, and offers higher bonuses for these successful placements.
3.  **Deployment:** The service was containerized and deployed on AWS ECS (Elastic Container Service) for easy management and scaling.