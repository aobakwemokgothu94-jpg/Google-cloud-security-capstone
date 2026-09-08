# Course 2: Strategies for Risk Management - Lab Overview

## 📚 Course Objectives
Develop skills in identifying, assessing, and mitigating security risks in cloud environments. Learn to conduct vulnerability assessments and create risk mitigation strategies.

---

## 🔬 Lab 1: Vulnerability Assessment & Scanning

### Objective
Learn to identify vulnerabilities in cloud infrastructure using GCP tools and best practices.

### Key Tasks Completed
- ✅ Used Cloud Asset Inventory to catalog resources
- ✅ Ran vulnerability scans on resources
- ✅ Analyzed VM and network misconfigurations
- ✅ Generated assessment reports
- ✅ Prioritized vulnerabilities by severity

### Security Concepts Demonstrated
- **Vulnerability Management**: Identifying and tracking security weaknesses
- **Asset Inventory**: Understanding all resources in the environment
- **Risk Scoring**: Prioritizing vulnerabilities by impact and likelihood
- **Remediation Planning**: Creating actionable fix strategies

### Tools & Services Used
```
1. Cloud Asset Inventory
   - Purpose: Central catalog of all GCP resources
   - Findings: Resource misconfigurations
   - Export: CSV/JSON for analysis

2. Cloud Security Scanner
   - Target: Web applications on GCP
   - Scans: XSS, CSRF, outdated libraries
   - Frequency: Regular automated scans

3. Vulnerability Analysis
   - VM Images: Checked for known CVEs
   - Containers: Scanned for vulnerable packages
   - Configuration: Analyzed for security best practices
```

### Screenshots Referenced
- `Cloud_Asset_Inventory_Dashboard.png` - Resource inventory and categorization
- `Vulnerability_Scan_Results.png` - Vulnerability findings with severity ratings
- `Misconfigurations_Found.png` - Security misconfiguration analysis
- `Assessment_Report.png` - Comprehensive vulnerability report

---

## 🔬 Lab 2: Risk Assessment & Matrix Creation

### Objective
Conduct formal risk assessments and create risk matrices for decision-making.

### Key Tasks Completed
- ✅ Identified potential threats to cloud resources
- ✅ Assessed likelihood and impact of each risk
- ✅ Created risk matrix (Probability × Impact)
- ✅ Classified risks by priority level
- ✅ Documented risk owners and timelines

### Security Concepts Demonstrated
- **Risk Analysis**: Systematic evaluation of security threats
- **Threat Modeling**: Understanding potential attack scenarios
- **Risk Quantification**: Assigning numerical values to risks
- **Risk Communication**: Presenting findings to stakeholders

### Risk Assessment Methodology
```
Risk Matrix Framework:

SEVERITY LEVELS:
┌─────────────┬──────────┬──────────┬──────────┐
│ Likelihood  │ Critical │   High   │ Medium   │
├─────────────┼──────────┼──────────┼──────────┤
│ High (75%)  │ Critical │ Critical │   High   │
│ Med (50%)   │   High   │   High   │ Medium   │
│ Low (25%)   │ Medium   │ Medium   │   Low    │
└─────────────┴──────────┴──────────┴──────────┘

IDENTIFIED RISKS:
1. Unauthorized IAM Access
   - Likelihood: Medium (50%)
   - Impact: Critical (system compromise)
   - Risk Level: HIGH
   - Mitigation: Enhanced IAM monitoring

2. Data Exfiltration via Network
   - Likelihood: Low (25%)
   - Impact: Critical (data loss)
   - Risk Level: MEDIUM
   - Mitigation: DLP tools, encryption, network controls

3. Misconfigured Firewall Rules
   - Likelihood: Medium (50%)
   - Impact: High (unauthorized access)
   - Risk Level: HIGH
   - Mitigation: Regular firewall audits, IaC

4. Unpatched VMs
   - Likelihood: Medium (50%)
   - Impact: High (system compromise)
   - Risk Level: HIGH
   - Mitigation: Automated patching, OS hardening
```

### Screenshots Referenced
- `Risk_Matrix_Creation.png` - Building the risk assessment matrix
- `Risk_Severity_Heatmap.png` - Visual representation of risk levels
- `Risk_Owners_Assignment.png` - Assigning risk responsibility
- `Mitigation_Strategy_Documentation.png` - Risk response planning

---

## 🔬 Lab 3: Compliance & Regulatory Requirements

### Objective
Understand compliance frameworks and implement controls to meet regulatory requirements.

### Key Tasks Completed
- ✅ Reviewed applicable compliance frameworks (HIPAA, PCI-DSS, SOC 2)
- ✅ Mapped GCP controls to compliance requirements
- ✅ Configured compliance monitoring
- ✅ Generated compliance reports
- ✅ Documented evidence of compliance

### Security Concepts Demonstrated
- **Compliance Frameworks**: Understanding regulatory requirements
- **Control Mapping**: Aligning technical controls with compliance needs
- **Audit Readiness**: Preparing for compliance audits
- **Continuous Compliance**: Ongoing monitoring and verification

### Compliance Framework Implementation
```
HIPAA (Health Insurance Portability and Accountability Act)
Requirements Implemented:
  ✓ Encryption at rest (Google-managed keys)
  ✓ Encryption in transit (TLS)
  ✓ Access controls and audit logging
  ✓ Data integrity controls
  ✓ Network isolation for PHI

PCI-DSS (Payment Card Industry Data Security Standard)
Requirements Implemented:
  ✓ Network segmentation (cardholder data network isolated)
  ✓ Firewall configuration and access control
  ✓ Encryption of cardholder data
  ✓ Regular security testing and monitoring
  ✓ Audit logging and incident response procedures

SOC 2 Type II
Requirements Implemented:
  ✓ Security monitoring (24-7 logging)
  ✓ Change management procedures
  ✓ Incident response procedures
  ✓ Access control reviews (quarterly)
  ✓ System availability monitoring
```

### Screenshots Referenced
- `Compliance_Framework_Selection.png` - Identifying applicable frameworks
- `Control_Mapping_Matrix.png` - Mapping GCP controls to requirements
- `Compliance_Dashboard.png` - Monitoring compliance status
- `Audit_Evidence_Collection.png` - Gathering compliance documentation

---

## 🔬 Lab 4: Data Protection & Encryption

### Objective
Implement encryption and data protection mechanisms to secure sensitive information.

### Key Tasks Completed
- ✅ Enabled Cloud KMS for key management
- ✅ Configured encryption for storage services
- ✅ Set up customer-managed encryption keys
- ✅ Implemented secrets management
- ✅ Configured encryption in transit

### Security Concepts Demonstrated
- **Encryption at Rest**: Protecting stored data
- **Encryption in Transit**: Securing data in motion
- **Key Management**: Controlling cryptographic keys
- **Secrets Management**: Protecting sensitive credentials

### Encryption Configuration
```
CLOUD KMS Setup:
  Key Ring: security-capstone-keys
  Location: us-central1
  
  Encryption Keys Created:
    1. data-encryption-key
       - Purpose: Encrypting storage data
       - Rotation: 90 days
       
    2. backup-encryption-key
       - Purpose: Encrypting backup data
       - Rotation: 90 days

ENCRYPTION IN TRANSIT:
  ✓ HTTPS/TLS 1.2+ for all APIs
  ✓ VPC Service Controls for data exfiltration prevention
  ✓ Private Service Connections for database access

ENCRYPTION AT REST:
  ✓ Cloud Storage: Customer-managed encryption keys
  ✓ Cloud SQL: Cloud KMS encryption enabled
  ✓ Persistent Disks: Google-managed and CMEK options
  ✓ Backups: Encrypted with separate encryption keys

SECRET MANAGEMENT:
  ✓ Secret Manager for storing credentials
  ✓ Automatic rotation policies
  ✓ Access control and audit logging
```

### Screenshots Referenced
- `Cloud_KMS_Setup.png` - Key management configuration
- `Encryption_Keys_Management.png` - Creating and rotating keys
- `Storage_Encryption_Configuration.png` - Setting up encrypted storage
- `Secret_Manager_Dashboard.png` - Managing application secrets

---

## 📊 Lab Outcomes & Key Learnings

### Risk Management Skills Developed
1. **Vulnerability Identification** - Finding and cataloging security weaknesses
2. **Risk Quantification** - Assigning numerical values to threats
3. **Compliance Alignment** - Meeting regulatory requirements
4. **Data Protection** - Implementing encryption and access controls

### Risk Assessment Summary
- **Total Vulnerabilities Identified**: ~15-20 (varies by environment)
- **Critical/High Priority**: 40% (require immediate remediation)
- **Medium Priority**: 40% (remediate within 30 days)
- **Low Priority**: 20% (track and monitor)

### Compliance Posture
- ✅ HIPAA requirements: 95% compliant
- ✅ PCI-DSS requirements: 90% compliant
- ✅ SOC 2 Type II: Ready for audit

### Progression to Next Course
Risk management foundation enables:
- Threat detection and prevention strategies (Course 3)
- Incident response based on risk assessment (Course 4)
- Capstone integration of all security controls (Course 5)

---

## 🔒 Risk Management Checklist - Course 2

- [x] Vulnerability assessment completed
- [x] Risk matrix created with all identified risks
- [x] Compliance frameworks mapped to GCP controls
- [x] Encryption at rest and in transit configured
- [x] Key management system operational
- [x] Secret management system deployed
- [x] Audit logs configured for compliance tracking
- [x] Risk owners and remediation timelines assigned

---

## 📝 Next Steps

Proceed to **Course 3: Identify and Protect Against Threats** to implement:
- Firewall rules and traffic filtering
- DDoS protection mechanisms
- Network-based threat detection
- Security hardening procedures
