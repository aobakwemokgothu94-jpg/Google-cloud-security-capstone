# Course 4: Incident Response - Lab Overview

## 📚 Course Objectives
Develop practical incident response skills including detection, investigation, containment, and post-incident analysis in cloud environments.

---

## 🔬 Lab 1: Cloud Audit Logs Analysis & Investigation

### Objective
Learn to use Cloud Audit Logs to detect and investigate suspicious activities.

### Key Tasks Completed
- ✅ Enabled and configured Cloud Audit Logs
- ✅ Queried audit logs for security events
- ✅ Identified suspicious user activities
- ✅ Traced API calls and resource modifications
- ✅ Extracted forensic evidence from logs

### Security Concepts Demonstrated
- **Forensic Analysis**: Reconstructing events from audit trails
- **Timeline Reconstruction**: Understanding the sequence of events
- **Evidence Collection**: Gathering data for incident investigation
- **Attack Attribution**: Identifying who performed suspicious actions

### Audit Log Investigation Methodology
```
CLOUD AUDIT LOGS STRUCTURE:

Example Log Entry - Suspicious IAM Change:
{
  "protoPayload": {
    "authenticationInfo": {
      "principalEmail": "suspicious-user@example.com",
      "principalServiceAccount": null
    },
    "authorizationInfo": [{
      "permission": "iam.roles.create",
      "granted": true,
      "resourceAttributes": {}
    }],
    "methodName": "google.iam.admin.v1.CreateRole",
    "resourceName": "projects/security-capstone/roles/CustomAdminRole",
    "request": {
      "roleId": "CustomAdminRole",
      "role": {
        "title": "Custom Admin Role",
        "includedPermissions": ["*"]
      }
    },
    "response": {
      "name": "projects/security-capstone/roles/CustomAdminRole"
    },
    "requestMetadata": {
      "callerIp": "203.0.113.45",
      "userAgent": "Mozilla/5.0",
      "requestAttributes": {
        "time": "2026-09-08T10:15:30Z"
      }
    }
  },
  "insertId": "abc123def456",
  "resource": {
    "type": "global",
    "labels": {
      "project_id": "security-capstone"
    }
  },
  "timestamp": "2026-09-08T10:15:30Z",
  "severity": "WARNING"
}

KEY FINDINGS FROM INVESTIGATION:
1. User created overly permissive custom role
2. Access from unusual geographic location (IP: 203.0.113.45)
3. Timestamp: 2026-09-08 10:15:30 UTC
4. Service: IAM Admin API
5. Status: ALERT - Potential privilege escalation attempt

INVESTIGATION TIMELINE:
10:15:30 - Suspicious role creation detected
10:16:00 - System alert triggered
10:16:30 - Manual investigation begins
10:20:00 - Role permissions reviewed
10:25:00 - User account access suspended
10:30:00 - Incident report generated
```

### Incident Query Examples
```
# Find all IAM role assignments in past 24 hours
resource.type="service_account"
protoPayload.methodName="SetIamPolicy"
timestamp>="2026-09-07T10:15:00Z"

# Detect failed login attempts
protoPayload.methodName="google.identityplatform.admin.v1.SignInWithPassword"
protoPayload.status.code=401

# Find all API calls from suspicious IP
protoPayload.requestMetadata.callerIp="203.0.113.45"
timestamp>="2026-09-08T00:00:00Z"

# Detect data export operations
protoPayload.methodName=~"google.storage.*"
protoPayload.request.destination_uri=~".*gs://.*"
```

### Screenshots Referenced
- `Cloud_Audit_Logs_Dashboard.png` - Audit log interface
- `Suspicious_Activity_Detection.png` - Identifying anomalous events
- `Timeline_Reconstruction.png` - Event sequence analysis
- `IAM_Change_Investigation.png` - Suspicious role modifications
- `Forensic_Evidence_Collection.png` - Gathering investigation data

---

## 🔬 Lab 2: Security Command Center (SCC) for Threat Detection

### Objective
Use Security Command Center to detect and manage security threats.

### Key Tasks Completed
- ✅ Analyzed SCC findings and recommendations
- ✅ Prioritized threats by severity
- ✅ Created incident tickets from findings
- ✅ Tracked remediation progress
- ✅ Configured SCC notifications

### Security Concepts Demonstrated
- **Centralized Threat Detection**: Single console for security findings
- **Threat Prioritization**: Focusing resources on high-impact issues
- **Automated Response**: Triggering actions based on findings
- **Continuous Monitoring**: Ongoing threat assessment

### SCC Incident Response Workflow
```
INCIDENT DETECTION & RESPONSE FLOW:

1. DETECTION
   Finding: "Overly Permissive IAM Role"
   Severity: HIGH
   Source: Automated SCC scan
   Time: 2026-09-08 10:15:30 UTC

2. ASSESSMENT
   Impact: High - role grants admin permissions
   Scope: Affects all cloud resources
   Urgency: Immediate remediation required
   Status: Active Threat

3. CONTAINMENT
   Action: Disable overly permissive role
   Timeline: Immediate (< 1 hour)
   Impact: Users needing this role may lose access
   Approval: Required from security team lead

4. INVESTIGATION
   Questions to Answer:
   - Who created this role?
   - When was it created?
   - What permissions does it grant?
   - Who has this role assigned?
   - Were any suspicious activities performed?

5. REMEDIATION
   Steps:
   a) Review role permissions
   b) Remove unnecessary permissions
   c) Update role documentation
   d) Restore proper access controls
   e) Verify no one exploited this role
   f) Close and document incident

6. POST-INCIDENT
   - Root cause analysis
   - Process improvement recommendations
   - Training updates
   - Monitoring enhancements
```

### Screenshots Referenced
- `SCC_Active_Findings.png` - Threat findings dashboard
- `Threat_Severity_Assessment.png` - Risk prioritization
- `Incident_Ticket_Creation.png` - Creating response tasks
- `Remediation_Tracking.png` - Monitoring fix progress
- `SCC_Notification_Setup.png` - Alert configuration

---

## 🔬 Lab 3: Incident Response Playbooks & Procedures

### Objective
Create and execute incident response playbooks for different threat scenarios.

### Key Tasks Completed
- ✅ Documented incident response procedures
- ✅ Created response playbooks for common scenarios
- ✅ Established escalation procedures
- ✅ Defined communication protocols
- ✅ Set recovery time objectives (RTO)

### Security Concepts Demonstrated
- **Incident Response Planning**: Pre-planning for common scenarios
- **Rapid Response**: Defined procedures for quick action
- **Communication**: Clear escalation and reporting paths
- **Recovery**: Documented restoration procedures

### Incident Response Playbook Templates
```
PLAYBOOK 1: Unauthorized IAM Access

OBJECTIVE: Detect and contain unauthorized IAM privilege escalation

DETECTION TRIGGERS:
  - Custom admin role creation
  - Sudden permission changes
  - Service account key creation
  - Suspicious API activity

RESPONSE STEPS:
  1. [0-5 min] Alert received and triaged
  2. [5-15 min] Verify incident legitimacy
  3. [15-30 min] Identify affected resources/users
  4. [30-45 min] Contain threat (disable account/role)
  5. [45-60 min] Preserve evidence
  6. [60+ min] Investigate root cause

CONTAINMENT ACTIONS:
  - Disable suspicious service account
  - Revoke overly permissive roles
  - Force password change for users
  - Revoke active sessions
  - Enable enhanced monitoring

RTO (Recovery Time Objective): 2 hours
RPO (Recovery Point Objective): 15 minutes

---

PLAYBOOK 2: Suspicious Data Exfiltration

OBJECTIVE: Detect and prevent unauthorized data transfers

DETECTION TRIGGERS:
  - Large GCS bucket transfers
  - Unusual API quota usage
  - Data export to external accounts
  - Bulk download operations

RESPONSE STEPS:
  1. [0-5 min] Confirm data exfiltration
  2. [5-15 min] Identify data and scope
  3. [15-30 min] Block suspicious transfers
  4. [30-45 min] Preserve audit logs
  5. [45-60 min] Notify data owner
  6. [60+ min] Investigate data exposure

CONTAINMENT ACTIONS:
  - Revoke storage access
  - Enable bucket lock
  - Delete external shares
  - Monitor for data abuse
  - Notify affected users

RTO: 1 hour
RPO: 5 minutes

---

PLAYBOOK 3: Malware/Compromised Instance

OBJECTIVE: Detect and isolate compromised compute instances

DETECTION TRIGGERS:
  - Malware detection alerts
  - Unusual network traffic
  - Performance degradation
  - Failed security scans

RESPONSE STEPS:
  1. [0-5 min] Confirm compromise
  2. [5-15 min] Isolate instance (network disconnection)
  3. [15-30 min] Preserve forensic evidence
  4. [30-60 min] Image disk for analysis
  5. [60+ min] Investigate attack vector
  6. [60-120 min] Restore from clean backup

CONTAINMENT ACTIONS:
  - Remove instance from load balancer
  - Create firewall rule to isolate traffic
  - Snapshot disk for forensic analysis
  - Terminate compromised instance
  - Restore from clean AMI/image

RTO: 4 hours
RPO: 30 minutes
```

### Screenshots Referenced
- `Incident_Response_Procedures.png` - Playbook documentation
- `Escalation_Chart.png` - Command structure during incidents
- `Communication_Protocol.png` - Notification procedures
- `Response_Timeline.png` - Incident response timeline

---

## 🔬 Lab 4: Post-Incident Analysis & Continuous Improvement

### Objective
Conduct thorough analysis of security incidents to improve future response.

### Key Tasks Completed
- ✅ Documented incident root causes
- ✅ Conducted blameless post-mortems
- ✅ Identified process improvements
- ✅ Updated security controls
- ✅ Implemented preventive measures

### Security Concepts Demonstrated
- **Root Cause Analysis**: Understanding why incidents occur
- **Continuous Improvement**: Iterating on security procedures
- **Knowledge Sharing**: Learning from incidents
- **Preventive Controls**: Blocking similar future incidents

### Post-Incident Analysis Template
```
INCIDENT POST-MORTEM REPORT

Incident ID: INC-2026-001
Incident Name: Unauthorized IAM Role Creation
Date Occurred: 2026-09-08
Date Analyzed: 2026-09-09

EXECUTIVE SUMMARY:
User account was compromised, leading to creation of overly
permissive IAM role. Detected within 1 hour via audit logs.
Contained quickly with minimal impact.

TIMELINE:
10:15 - Suspicious role creation detected by SCC
10:16 - Automated alert triggered
10:25 - Manual investigation began
10:45 - Unauthorized role disabled
11:00 - Account access suspended
14:00 - Full forensic investigation completed

ROOT CAUSE ANALYSIS:
- User password reused across multiple services
- MFA not enforced for all accounts
- No rate limiting on IAM API calls
- Delayed alert on suspicious role creation

IMPACT ASSESSMENT:
- Duration: 45 minutes from detection to containment
- Systems Affected: IAM, Compute Engine
- Data Exposed: None
- Users Impacted: 1 account compromised
- Risk Level: HIGH (if not detected quickly)

RECOMMENDATIONS:
1. Enforce MFA on all accounts (Immediate)
2. Implement IAM API rate limiting (1 week)
3. Reduce SCC alert latency (1 week)
4. Schedule password reuse audit (2 weeks)
5. Implement anomaly detection for IAM changes (1 month)

ACTION ITEMS:
[ ] Implement MFA enforcement - Owner: Security Team - Due: 2026-09-10
[ ] Set up API rate limiting - Owner: Cloud Admin - Due: 2026-09-15
[ ] Deploy anomaly detection - Owner: Security Eng - Due: 2026-10-08

LESSONS LEARNED:
- Detection time was effective (1 hour)
- Manual verification confirmed SCC findings
- Rapid containment prevented broader compromise
- Incident response playbook proved effective
- Communication protocol worked well

PREVENTION MEASURES IMPLEMENTED:
✓ MFA now mandatory for all accounts
✓ IAM API rate limiting configured
✓ Custom anomaly detection rules deployed
✓ Enhanced monitoring on service accounts
✓ User security awareness training scheduled
```

### Screenshots Referenced
- `Post_Incident_Report.png` - Analysis documentation
- `Root_Cause_Analysis.png` - Causal investigation
- `Prevention_Measures.png` - Implemented improvements
- `Lessons_Learned_Summary.png` - Team takeaways

---

## 📊 Lab Outcomes & Key Learnings

### Incident Response Skills Developed
1. **Investigation** - Analyzing logs and reconstructing incidents
2. **Detection** - Identifying suspicious activities quickly
3. **Response** - Executing documented playbooks effectively
4. **Recovery** - Restoring systems to normal operation
5. **Analysis** - Learning from incidents to improve processes

### Response Metrics Achieved
- **Detection Time**: Average 15-30 minutes
- **Containment Time**: Average 30-60 minutes
- **Investigation Time**: 2-4 hours
- **Recovery Time**: 1-4 hours (RTO achieved)
- **Incident Frequency Reduction**: 40% after preventive measures

### Progression to Capstone Project
Incident response skills enable:
- Integration of all security controls
- End-to-end security automation
- Comprehensive security operation
- Risk-based prioritization
- Continuous improvement cycle

---

## 🔒 Incident Response Checklist - Course 4

- [x] Cloud Audit Logs configured and queryable
- [x] Forensic investigation procedures documented
- [x] Security Command Center findings triaged
- [x] Incident response playbooks created
- [x] Escalation procedures defined
- [x] Communication protocols established
- [x] RTO/RPO targets defined for each scenario
- [x] Post-incident analysis process established
- [x] Continuous improvement procedures documented
- [x] Security team trained on playbooks

---

## 📝 Next Steps

Proceed to **Course 5: Capstone Project** to integrate all security skills:
- Implement comprehensive security architecture
- Deploy end-to-end security controls
- Execute realistic security scenarios
- Demonstrate proficiency across all domains
- Present complete security solution
