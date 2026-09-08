# Course 3: Identify and Protect Against Threats - Lab Overview

## 📚 Course Objectives
Develop practical skills in threat detection, network protection, and implementing security controls to defend against cyberattacks. Learn to configure firewalls, DDoS protection, and threat monitoring.

---

## 🔬 Lab 1: VPC Firewall Rules & Network Traffic Control

### Objective
Implement firewall rules to control network traffic and enforce security policies.

### Key Tasks Completed
- ✅ Created ingress firewall rules to allow necessary traffic
- ✅ Created egress firewall rules to restrict outbound traffic
- ✅ Configured firewall rules by service and port
- ✅ Tested firewall rules for effectiveness
- ✅ Implemented firewall logging for monitoring
- ✅ Created allow-lists and deny-lists for IP addresses

### Security Concepts Demonstrated
- **Defense in Depth**: Layered network security controls
- **Least Privilege Access**: Only allow necessary traffic
- **Network Segmentation**: Isolating resources by security zone
- **Traffic Monitoring**: Logging all network connections
- **Zero Trust**: Deny-by-default approach to network access

### Firewall Rule Configuration
```
INGRESS RULES (Inbound Traffic):

1. Allow SSH Admin Access
   Priority: 1000
   Direction: INGRESS
   Protocol: TCP
   Port: 22
   Source IPs: [Admin IP Range]
   Target: admin-vms
   Action: ALLOW

2. Allow HTTP Web Traffic
   Priority: 1010
   Direction: INGRESS
   Protocol: TCP
   Port: 80
   Source: 0.0.0.0/0 (with Cloud Armor DDoS protection)
   Target: web-servers
   Action: ALLOW

3. Allow HTTPS Web Traffic
   Priority: 1020
   Direction: INGRESS
   Protocol: TCP
   Port: 443
   Source: 0.0.0.0/0 (with Cloud Armor DDoS protection)
   Target: web-servers
   Action: ALLOW

4. Allow Database Access (Internal Only)
   Priority: 1030
   Direction: INGRESS
   Protocol: TCP
   Port: 3306
   Source: app-servers (tag-based)
   Target: database-servers
   Action: ALLOW

5. Deny All Other Traffic
   Priority: 65534
   Direction: INGRESS
   Source: 0.0.0.0/0
   Target: all
   Action: DENY

EGRESS RULES (Outbound Traffic):

1. Allow Internal Communication
   Priority: 1000
   Direction: EGRESS
   Destination: 10.0.0.0/8 (internal VPC)
   Action: ALLOW

2. Allow DNS Queries
   Priority: 1010
   Direction: EGRESS
   Protocol: UDP
   Port: 53
   Destination: 8.8.8.8, 8.8.4.4 (Google DNS)
   Action: ALLOW

3. Allow HTTPS to Google APIs
   Priority: 1020
   Direction: EGRESS
   Protocol: TCP
   Port: 443
   Destination: restricted.googleapis.com
   Action: ALLOW

4. Deny All Other Outbound Traffic
   Priority: 65534
   Direction: EGRESS
   Destination: 0.0.0.0/0
   Action: DENY
```

### Screenshots Referenced
- `Firewall_Rules_Console.png` - Creating ingress/egress rules
- `Firewall_Rules_Summary.png` - Complete rule configuration overview
- `Traffic_Flow_Diagram.png` - Visual representation of allowed traffic
- `Firewall_Logs_Analysis.png` - Monitoring allowed and denied traffic
- `Rule_Testing_Results.png` - Verification of firewall effectiveness

---

## 🔬 Lab 2: Cloud Armor DDoS Protection & Cloud Load Balancing

### Objective
Implement DDoS protection and load balancing to defend against attacks and ensure availability.

### Key Tasks Completed
- ✅ Configured Cloud Load Balancer (HTTP(S) Load Balancer)
- ✅ Enabled Cloud Armor security policies
- ✅ Created rate limiting rules
- ✅ Configured geographic restrictions
- ✅ Set up bot and abuse detection
- ✅ Tested DDoS protection effectiveness

### Security Concepts Demonstrated
- **DDoS Mitigation**: Protection against distributed denial-of-service attacks
- **Rate Limiting**: Controlling traffic volume from single sources
- **Geographic Filtering**: Restricting access by country/region
- **Bot Detection**: Identifying and blocking automated attacks
- **Availability Protection**: Ensuring service continuity during attacks

### Cloud Armor Configuration
```
SECURITY POLICY: prod-security-policy

RULE 1: Allow Trusted Geographic Regions
  Priority: 100
  Match: trafficDirectionMatch = INBOUND
  Origin Region: US, EU, CA
  Action: ALLOW
  Logging: Enabled

RULE 2: Rate Limiting - Prevent DDoS Floods
  Priority: 200
  Match: All HTTP(S) traffic
  Rate Limit: 1000 requests per minute per IP
  Enforce on Path: /api/*
  Action: Rate based throttle
  Ban Duration: 10 minutes
  Logging: Enabled

RULE 3: Bot Detection
  Priority: 300
  Match: Suspicious user agents, automated requests
  Action: CHALLENGE (CAPTCHA)
  Logging: Enabled

RULE 4: Geo-Blocking - Block High-Risk Regions
  Priority: 400
  Origin Region: North Korea, Iran, Syria
  Action: DENY
  Logging: Enabled

RULE 5: Adaptive Protections
  Priority: 500
  Type: Automatic DDoS detection
  Action: Adaptive throttling
  Logging: Enabled

DEFAULT RULE:
  Priority: 65535
  Action: ALLOW
  Logging: Enabled

BACKEND HEALTH CHECKS:
  Protocol: HTTP
  Path: /health
  Port: 80
  Interval: 10 seconds
  Timeout: 5 seconds
  Healthy Threshold: 2
  Unhealthy Threshold: 3
```

### Screenshots Referenced
- `Cloud_Load_Balancer_Setup.png` - Configuring load balancer
- `Cloud_Armor_Policy_Configuration.png` - Security policy creation
- `Rate_Limiting_Rules.png` - Configuring rate limits
- `DDoS_Attack_Simulation.png` - Testing attack mitigation
- `DDoS_Protection_Dashboard.png` - Monitoring attack prevention
- `Geographic_Filtering_Map.png` - Viewing geographic restrictions

---

## 🔬 Lab 3: VPC Flow Logs & Network Threat Detection

### Objective
Implement comprehensive network monitoring to detect suspicious activity and potential threats.

### Key Tasks Completed
- ✅ Enabled VPC Flow Logs on all subnets
- ✅ Configured log aggregation and analysis
- ✅ Set up alerting for suspicious patterns
- ✅ Analyzed network traffic for threats
- ✅ Created dashboards for visualization
- ✅ Identified and investigated anomalies

### Security Concepts Demonstrated
- **Network Visibility**: Complete view of traffic flows
- **Anomaly Detection**: Identifying unusual traffic patterns
- **Threat Investigation**: Finding potential security incidents
- **Compliance Monitoring**: Tracking network activity for audit
- **Incident Response**: Rapid response to detected threats

### VPC Flow Logs Configuration
```
VPC FLOW LOGS SETUP:

Subnet Monitoring:
  - prod-subnet: Enabled (all traffic)
  - dev-subnet: Enabled (all traffic)
  - management-subnet: Enabled (all traffic)

Log Aggregation:
  Destination: Cloud Logging
  Log Name: vpc-flows
  Include Options:
    ✓ Source and destination IPs
    ✓ Port numbers
    ✓ Protocol
    ✓ Bytes/packets sent
    ✓ Start and end time
    ✓ Status (accepted/rejected)

SAMPLE VPC FLOW LOG ENTRY:
{
  "version": "1",
  "start_time": "1609459200",
  "end_time": "1609459260",
  "src_ip": "10.1.1.100",
  "dest_ip": "10.1.2.50",
  "src_port": "54321",
  "dest_port": "443",
  "protocol": "6",  // TCP
  "bytes_sent": "2048",
  "bytes_received": "1024",
  "packets_sent": "15",
  "packets_received": "12",
  "action": "ACCEPT",
  "tcp_flags": "SYN,ACK,FIN",
  "rtt_msec": "5"
}

ANALYSIS METRICS:
  Total Flow Records: ~10,000+ per day
  Suspicious Flows Detected: 5-10 per week
  Blocked Connections: Tracked in deny logs
  Protocol Distribution: TCP 70%, UDP 25%, ICMP 5%
  Top Talkers: Analyzing high-volume source/dest pairs
```

### Screenshots Referenced
- `VPC_Flow_Logs_Enable.png` - Enabling flow logs on subnets
- `Flow_Logs_Dashboard.png` - Visualizing network traffic
- `Suspicious_Traffic_Analysis.png` - Identifying anomalies
- `Connection_Pattern_Analysis.png` - Finding unusual behavior
- `Threat_Alert_Configuration.png` - Setting up alerts
- `Network_Incident_Investigation.png` - Investigating detected threats

---

## 🔬 Lab 4: Cloud Security Command Center (SCC) Integration

### Objective
Use Security Command Center for centralized threat detection and security posture management.

### Key Tasks Completed
- ✅ Enabled Security Command Center
- ✅ Configured security findings
- ✅ Set up automated scanning
- ✅ Created custom rules for threat detection
- ✅ Configured notifications and alerts
- ✅ Integrated with incident response workflows

### Security Concepts Demonstrated
- **Centralized Security**: Single pane of glass for threat monitoring
- **Automated Detection**: Continuous scanning for vulnerabilities
- **Threat Prioritization**: Focusing on high-impact findings
- **Security Posture**: Measuring overall security health
- **Remediation Tracking**: Managing fix status and SLAs

### Security Command Center Configuration
```
SECURITY COMMAND CENTER SETUP:

ACTIVE FINDINGS (Example):

1. Open Firewall Rules
   Severity: HIGH
   Resource: security-capstone-vpc/default
   Issue: Firewall rule allows 0.0.0.0/0 on port 22
   Recommendation: Restrict SSH to specific IPs
   Status: OPEN (30 days)

2. Service Account Key Exposure
   Severity: CRITICAL
   Resource: service-account@project.iam.gserviceaccount.com
   Issue: Service account key not rotated in 90+ days
   Recommendation: Rotate keys immediately
   Status: OPEN (5 days)

3. Default Compute Service Account Used
   Severity: MEDIUM
   Resource: vm-instance-1
   Issue: VM uses default service account with excessive permissions
   Recommendation: Create custom service account
   Status: OPEN (15 days)

4. Unencrypted Cloud Storage Bucket
   Severity: HIGH
   Resource: gs://data-bucket-001
   Issue: Bucket not using CMEK encryption
   Recommendation: Enable customer-managed encryption
   Status: OPEN (20 days)

5. Public Cloud SQL Instance
   Severity: CRITICAL
   Resource: production-database
   Issue: Cloud SQL instance publicly accessible
   Recommendation: Enable private IP only
   Status: OPEN (7 days)

AUTOMATED SCANS:
  Frequency: Daily
  Scan Types:
    - Configuration Analysis
    - Container Image Scanning
    - Cloud Asset Inventory Analysis
    - Binary Authorization Policy Check

CUSTOM DETECTION RULES:
  Rule 1: Monitor IAM Changes
    Trigger: Any role assignment changes
    Response: Create finding + Notify team
    
  Rule 2: Detect Large Data Exports
    Trigger: GCS transfers > 100GB
    Response: Create finding + Require approval
    
  Rule 3: Unauthorized API Usage
    Trigger: Unusual API calls from service accounts
    Response: Create finding + Disable service account
```

### Screenshots Referenced
- `SCC_Dashboard_Overview.png` - Main Security Command Center view
- `Findings_Summary.png` - Overview of security findings
- `Active_Threats.png` - Critical and high-severity threats
- `Automated_Scanning_Status.png` - Scan schedules and results
- `Custom_Rules_Configuration.png` - Creating detection rules
- `Notification_Setup.png` - Alert configuration

---

## 📊 Lab Outcomes & Key Learnings

### Threat Protection Skills Developed
1. **Firewall Management** - Implementing effective network access controls
2. **DDoS Protection** - Defending against volumetric attacks
3. **Network Monitoring** - Detecting suspicious traffic patterns
4. **Threat Detection** - Using automated tools to find security issues
5. **Incident Response** - Responding to detected threats

### Protection Metrics
- **Firewall Rules Implemented**: 5+ ingress, 4+ egress per environment
- **Cloud Armor Rules**: 5+ security policies protecting public endpoints
- **VPC Flow Logs**: 10,000+ records/day providing visibility
- **Security Findings**: 10-15 active findings, 40-50 total identified
- **DDoS Attack Scenarios**: 3+ tested and successfully mitigated

### Security Posture Improvements
- ✅ Network access controlled with firewall rules
- ✅ Public endpoints protected with DDoS mitigation
- ✅ All traffic monitored via flow logs
- ✅ Automated threat detection active
- ✅ Centralized security visibility achieved

### Progression to Next Course
Threat protection implementation enables:
- Incident detection and investigation (Course 4)
- Automated incident response (Course 4)
- Integration of all security controls (Course 5)

---

## 🔒 Threat Protection Checklist - Course 3

- [x] Firewall rules configured for all environments
- [x] Ingress/egress traffic policies documented
- [x] Cloud Armor DDoS protection deployed
- [x] Rate limiting configured for APIs
- [x] Geographic restrictions implemented
- [x] VPC Flow Logs enabled on all subnets
- [x] Cloud Security Command Center deployed
- [x] Automated threat scanning configured
- [x] Alert and notification system operational
- [x] Network monitoring dashboards created
- [x] Threat detection playbooks documented

---

## 📝 Next Steps

Proceed to **Course 4: Incident Response** to implement:
- Incident detection and investigation procedures
- Log analysis and forensic techniques
- Automated incident response workflows
- Post-incident analysis and improvement
