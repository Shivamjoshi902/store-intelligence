# Store Intelligence System

An AI-powered Store Intelligence Platform that transforms raw CCTV footage into actionable business insights using Computer Vision, Real-Time Analytics, Event Processing, and Monitoring Dashboards.

## Problem Statement

Retail stores generate massive amounts of CCTV footage every day, but most of this data remains unused.

The goal of this project is to convert CCTV video streams into meaningful operational insights such as:

- Customer Footfall
- Real-Time Occupancy
- Average Visit Duration
- Peak Store Hours
- Queue Detection
- Crowd Detection
- Dwell Time Analytics
- Operational Alerts

## Solution Overview

The system processes CCTV footage through a multi-stage pipeline:

1. Person Detection using YOLOv8
2. Multi-Object Tracking using ByteTrack
3. Event Generation (Entry/Exit)
4. Data Storage
5. Analytics Engine
6. FastAPI Backend
7. Real-Time Dashboard

## System Architecture

```text
CCTV Video
      |
      v
YOLOv8 Detection
      |
      v
ByteTrack Tracking
      |
      v
Event Processing
      |
      +-------> Database
      |
      +-------> Alert Engine
      |
      +-------> Analytics Engine
                     |
                     v
                FastAPI
                     |
                     v
               Dashboard