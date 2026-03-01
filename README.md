# SysAdmin Python Automation

This project contains automation scripts I am building as part of improving my System Administrator and DevOps skills.

Current Environment
- Ubuntu Server (CLI / TTY environment)
- Python
- psutil library

Project Goal
Build automation tools that help system administrators monitor and manage servers efficiently.

Script 1: Server Health Check
This script checks:
- CPU usage
- Memory usage
- Disk usage
- System uptime

It also logs the results to a file for monitoring.

How to Run
python3 health_check.py

Example Output
===== SERVER HEALTH REPORT =====
CPU Usage
Memory Usage
Disk Usage
System Uptime

Why I Built This
System administrators often need quick health checks on servers. This script automates that process and can later be expanded to include alerts and monitoring.

Next Improvements
- Add alerting system
- Email notifications
- Cron job automation
- Multi-server monitoring
- HTML report dashboard
