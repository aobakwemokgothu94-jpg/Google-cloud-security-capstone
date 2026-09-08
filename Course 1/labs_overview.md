# Course 1: Introduction to Security Principles - Lab Overview

## 📚 Course Objectives
Establish foundational knowledge of cloud security, GCP console navigation, and basic security configurations in Google Cloud Platform.

---

## 🔬 Lab 1: GCP Project Setup & Navigation

### Objective
Learn to navigate the Google Cloud Console and set up a secure project foundation.

### Key Tasks Completed
- ✅ Created a GCP project with appropriate naming conventions
- ✅ Explored the Cloud Console interface and navigation
- ✅ Enabled required APIs (Compute Engine, Cloud Logging, IAM, etc.)
- ✅ Set up project-level configurations

### Security Concepts Demonstrated
- **Principle of Least Privilege**: Only enable necessary APIs
- **Resource Organization**: Proper project structuring for security
- **Cloud Console Navigation**: Understanding security-related menu options

### Configuration Details
```
Project Setup:
- Project Name: Google-Cloud-Security-Capstone
- APIs Enabled:
  - Compute Engine API
  - Cloud Logging API
  - Cloud Audit Logs API
  - Cloud IAM API
  - Security Command Center API
```

---

## 🔬 Lab 2: Identity and Access Management (IAM) Fundamentals

### Objective
Understand IAM roles, service accounts, and implement role-based access control.

### Key Tasks Completed
- ✅ Created custom IAM roles based on job functions
- ✅ Set up service accounts for applications
- ✅ Assigned predefined roles (Editor, Viewer, Security Admin)
- ✅ Implemented role-based access control policies
- ✅ Tested IAM permissions and access controls

### Security Concepts Demonstrated
- **Role-Based Access Control (RBAC)**: Assigning roles based on job responsibilities
- **Service Accounts**: Creating identities for applications
- **Principle of Least Privilege**: Granting minimum necessary permissions
- **IAM Audit Logging**: Tracking who accessed what and when

### IAM Roles Implemented
```
Custom Role: Cloud Security Analyst
Permissions:
  - compute.instances.list
  - compute.instances.get
  - logging.logEntries.list
  - monitoring.timeSeries.list
  - securitycenter.findings.list

Predefined Roles:
  - roles/viewer (read-only access)
  - roles/compute.admin (compute management)
  - roles/iam.securityAdmin (IAM and security management)
```

### Screenshots Referenced
- `IAM_Roles_Setup.png` - Custom role creation interface
- `Service_Accounts_Configuration.png` - Service account setup and key management
- `IAM_Policy_Bindings.png` - Role assignments and member bindings

---

## 🔬 Lab 3: VPC Networks & Basic Network Security

### Objective
Set up Virtual Private Cloud networks and understand network security fundamentals.

### Key Tasks Completed
- ✅ Created custom VPC networks with appropriate subnets
- ✅ Configured network segmentation
- ✅ Set up internal communication between instances
- ✅ Isolated resources in separate subnets
- ✅ Tested network connectivity and access

### Security Concepts Demonstrated
- **Network Segmentation**: Separating resources by function and security level
- **VPC Isolation**: Creating private networks within GCP
- **Subnet Design**: Planning IP address allocation for security
- **Defense in Depth**: Layering security controls

### VPC Configuration
```
VPC Network: security-capstone-vpc
Region: us-central1

Subnets:
  1. prod-subnet (10.1.1.0/24)
     - Purpose: Production resources
     - Flow Logs: Enabled
     
  2. dev-subnet (10.1.2.0/24)
     - Purpose: Development resources
     - Flow Logs: Enabled
     
  3. management-subnet (10.1.3.0/24)
     - Purpose: Administrative access
     - Flow Logs: Enabled
```

### Screenshots Referenced
- `VPC_Networks_Configuration.png` - VPC creation and subnet setup
- `VPC_Subnets_Overview.png` - Subnet allocation and details
- `Network_Connectivity_Test.png` - Connectivity testing between resources

---

## 🔬 Lab 4: Cloud Console Security Features

### Objective
Explore and configure built-in GCP security and monitoring features.

### Key Tasks Completed
- ✅ Enabled Cloud Audit Logs for all services
- ✅ Configured Cloud Logging collection
- ✅ Set up activity monitoring
- ✅ Explored Security Command Center (basic features)
- ✅ Reviewed security recommendations

### Security Concepts Demonstrated
- **Audit Logging**: Maintaining comprehensive activity records
- **Monitoring & Observability**: Real-time visibility into cloud resources
- **Threat Detection**: Identifying suspicious activities
- **Compliance Tracking**: Maintaining audit trails for regulatory requirements

### Logging Configuration
```
Cloud Audit Logs Enabled:
  ✓ Admin Activity Logs (enabled by default)
  ✓ Data Access Logs (enabled for sensitive services)
  ✓ System Event Logs

Cloud Logging:
  ✓ Agent Installation (if applicable)
  ✓ Log Router Configuration
  ✓ Sink Creation for log storage
```

### Screenshots Referenced
- `Cloud_Console_Dashboard.png` - Main security dashboard
- `Audit_Logs_Configuration.png` - Audit logging setup
- `Cloud_Logging_Dashboard.png` - Log collection and viewing
- `Security_Recommendations.png` - Security Command Center findings

---

## 📊 Lab Outcomes & Key Learnings

### Security Principles Demonstrated
1. **Principle of Least Privilege** - Users and services have minimum required permissions
2. **Defense in Depth** - Multiple layers of security (IAM + Network + Logging)
3. **Accountability** - Comprehensive audit logging tracks all actions
4. **Zero Trust** - Verify every access request, don't trust by default

### Configuration Best Practices Implemented
- ✅ Separate accounts for different job functions
- ✅ Network segmentation by security level
- ✅ Comprehensive logging from day one
- ✅ Regular review of permissions and access

### Progression to Next Course
This foundation in IAM, networking, and logging provides the base for understanding:
- Risk assessment and threat identification (Course 2)
- Advanced threat protection mechanisms (Course 3)
- Incident response procedures (Course 4)

---

## 🔒 Security Checklist - Course 1

- [x] Project created with minimal API enablement
- [x] IAM roles configured with least privilege
- [x] VPC networks isolated from default network
- [x] Audit logging enabled on all services
- [x] Service accounts created for applications
- [x] Network flow logs enabled for monitoring
- [x] Access controls tested and verified

---

## 📝 Next Steps

Proceed to **Course 2: Strategies for Risk Management** to learn how to:
- Assess security risks in cloud environments
- Identify vulnerabilities and misconfigurations
- Create risk mitigation strategies
- Implement compliance controls
