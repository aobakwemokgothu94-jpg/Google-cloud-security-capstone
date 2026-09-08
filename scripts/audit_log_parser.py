#!/usr/bin/env python3
"""
Cloud Audit Logs Parser
Analyzes Cloud Audit Logs for security anomalies and threats.
"""

import json
import re
from datetime import datetime, timedelta
from typing import List, Dict, Tuple

class AuditLogParser:
    """Parse and analyze Cloud Audit Logs for security threats."""
    
    # Suspicious patterns to detect
    SUSPICIOUS_PATTERNS = {
        "privilege_escalation": r"iam\.(roles\.create|setIamPolicy)",
        "key_creation": r"CreateServiceAccountKey",
        "role_modification": r"UpdateRole|ModifyRole",
        "network_change": r"compute\.(firewalls|networks)\.(insert|update|delete)",
        "storage_access": r"storage\.buckets\.(get|list|update)",
        "unauthorized_access": r".*403|.*401"
    }
    
    def __init__(self):
        """Initialize the log parser."""
        self.logs = []
        self.threats = []
        self.audit_trail = []
    
    def parse_log_entry(self, entry: Dict) -> Dict:
        """
        Parse individual audit log entry.
        
        Args:
            entry: Raw audit log entry from Cloud Logging
            
        Returns:
            Parsed and enriched log entry
        """
        parsed = {
            "timestamp": entry.get("timestamp"),
            "principal_email": entry.get("protoPayload", {}).get("authenticationInfo", {}).get("principalEmail"),
            "method": entry.get("protoPayload", {}).get("methodName"),
            "resource": entry.get("protoPayload", {}).get("resourceName"),
            "status": entry.get("protoPayload", {}).get("status", {}).get("code"),
            "caller_ip": entry.get("protoPayload", {}).get("requestMetadata", {}).get("callerIp"),
            "user_agent": entry.get("protoPayload", {}).get("requestMetadata", {}).get("userAgent"),
            "severity": entry.get("severity", "UNKNOWN")
        }
        
        return parsed
    
    def detect_threats(self, entry: Dict) -> List[Dict]:
        """
        Detect potential threats in log entry.
        
        Args:
            entry: Parsed audit log entry
            
        Returns:
            List of detected threats
        """
        detected_threats = []
        method = entry.get("method", "")
        
        # Check for privilege escalation
        if re.search(self.SUSPICIOUS_PATTERNS["privilege_escalation"], method):
            detected_threats.append({
                "threat_type": "PRIVILEGE_ESCALATION",
                "severity": "HIGH",
                "description": f"Potential privilege escalation: {method}",
                "timestamp": entry["timestamp"],
                "principal": entry["principal_email"]
            })
        
        # Check for service account key creation
        if re.search(self.SUSPICIOUS_PATTERNS["key_creation"], method):
            detected_threats.append({
                "threat_type": "KEY_CREATION",
                "severity": "MEDIUM",
                "description": "Service account key created",
                "timestamp": entry["timestamp"],
                "principal": entry["principal_email"]
            })
        
        # Check for network changes
        if re.search(self.SUSPICIOUS_PATTERNS["network_change"], method):
            detected_threats.append({
                "threat_type": "NETWORK_CHANGE",
                "severity": "MEDIUM",
                "description": f"Network configuration changed: {method}",
                "timestamp": entry["timestamp"],
                "principal": entry["principal_email"]
            })
        
        # Check for failed access attempts
        if entry.get("status") in ["401", "403"]:
            detected_threats.append({
                "threat_type": "FAILED_ACCESS",
                "severity": "LOW",
                "description": "Unauthorized access attempt",
                "timestamp": entry["timestamp"],
                "principal": entry["principal_email"],
                "status": entry["status"]
            })
        
        return detected_threats
    
    def analyze_patterns(self, entries: List[Dict]) -> Dict:
        """
        Analyze patterns in multiple log entries.
        
        Args:
            entries: List of parsed log entries
            
        Returns:
            Analysis of patterns
        """
        analysis = {
            "total_entries": len(entries),
            "unique_principals": set(),
            "unique_resources": set(),
            "unique_methods": set(),
            "threat_timeline": [],
            "high_risk_users": []
        }
        
        principal_threat_count = {}
        
        for entry in entries:
            analysis["unique_principals"].add(entry.get("principal_email"))
            analysis["unique_resources"].add(entry.get("resource"))
            analysis["unique_methods"].add(entry.get("method"))
            
            threats = self.detect_threats(entry)
            if threats:
                analysis["threat_timeline"].extend(threats)
                principal = entry.get("principal_email")
                principal_threat_count[principal] = principal_threat_count.get(principal, 0) + len(threats)
        
        # Identify high-risk users (>5 suspicious activities)
        analysis["high_risk_users"] = [
            {"principal": p, "threat_count": c}
            for p, c in principal_threat_count.items()
            if c > 5
        ]
        
        return analysis
    
    def generate_report(self, analysis: Dict) -> str:
        """
        Generate human-readable security report.
        
        Args:
            analysis: Analysis results
            
        Returns:
            Formatted report string
        """
        report = []
        report.append("=" * 80)
        report.append("CLOUD AUDIT LOG ANALYSIS REPORT")
        report.append("=" * 80)
        report.append(f"\nAnalyzed Entries: {analysis['total_entries']}")
        report.append(f"Unique Principals: {len(analysis['unique_principals'])}")
        report.append(f"Unique Resources: {len(analysis['unique_resources'])}")
        report.append(f"Unique Methods: {len(analysis['unique_methods'])}")
        
        if analysis["threat_timeline"]:
            report.append("\n[DETECTED THREATS]")
            report.append("-" * 80)
            for threat in analysis["threat_timeline"]:
                report.append(f"Type: {threat['threat_type']} | Severity: {threat['severity']}")
                report.append(f"Description: {threat['description']}")
                report.append(f"Principal: {threat['principal']} | Time: {threat['timestamp']}\n")
        
        if analysis["high_risk_users"]:
            report.append("\n[HIGH-RISK USERS]")
            report.append("-" * 80)
            for user in analysis["high_risk_users"]:
                report.append(f"Principal: {user['principal']} | Suspicious Activities: {user['threat_count']}")
        
        report.append("\n" + "=" * 80)
        return "\n".join(report)


# Example usage with sample log entry
sample_log = {
    "timestamp": datetime.now().isoformat(),
    "protoPayload": {
        "authenticationInfo": {
            "principalEmail": "suspicious-user@example.com"
        },
        "methodName": "google.iam.admin.v1.CreateRole",
        "resourceName": "projects/security-capstone/roles/CustomAdminRole",
        "status": {"code": 200},
        "requestMetadata": {
            "callerIp": "203.0.113.45",
            "userAgent": "Mozilla/5.0"
        }
    },
    "severity": "WARNING"
}

if __name__ == "__main__":
    parser = AuditLogParser()
    parsed = parser.parse_log_entry(sample_log)
    threats = parser.detect_threats(parsed)
    analysis = parser.analyze_patterns([parsed])
    report = parser.generate_report(analysis)
    print(report)
