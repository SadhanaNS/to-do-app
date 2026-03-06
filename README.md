# 🔐 To-Do App — GitHub Advanced Security (GHAS) Practice

A intentionally vulnerable Python To-Do application built to **practice and demonstrate GitHub Advanced Security (GHAS)** features — secret scanning, code scanning, and dependency vulnerability detection.

> ⚠️ This repository is intentionally created with security issues for learning purposes. Do NOT use this code in production.

---

## 🎯 Purpose

This repo was created to:
- Practice setting up **GitHub Advanced Security (GHAS)** on a real repository
- Understand how **secret scanning** detects accidentally committed credentials
- Learn how **code scanning** identifies vulnerabilities in Python code
- Explore **Dependabot** alerts for vulnerable dependencies
- Simulate real-world scenarios where developers accidentally expose secrets

---

## 🔍 GHAS Features Practised

| Feature | What it does | Status |
|---|---|---|
| Secret Scanning | Detects hardcoded API keys, passwords, tokens committed to repo | ✅ Configured |
| Code Scanning | Static analysis to find security vulnerabilities in code | ✅ Configured |
| Dependabot Alerts | Flags vulnerable open source dependencies in requirements.txt | ✅ Configured |
| Security Policy | Defines responsible disclosure process | ✅ Added |

---

## 📁 Repository Structure

```
to-do-app/
├── app.py / scanner.py     # Python app with intentional vulnerabilities
├── requirements.txt        # Dependencies (includes outdated packages for scanning)
├── secrets.txt             # ⚠️ Demo file — simulates accidentally committed secrets
├── tasks.txt               # Sample to-do data
├── SECURITY.md             # Security policy and responsible disclosure
└── README.md               # This file
```

---

## 🧪 What Was Tested

**1. Secret Scanning**
- Committed a `secrets.txt` file containing fake credentials
- GHAS secret scanning successfully detected and alerted on exposed secrets
- Practiced the remediation workflow — removing secrets, rotating credentials

**2. Code Scanning (CodeQL)**
- Enabled CodeQL analysis on Python codebase
- Identified common vulnerabilities — SQL injection patterns, insecure imports
- Reviewed and triaged alerts in the Security tab

**3. Dependabot**
- Used outdated package versions in `requirements.txt`
- Dependabot raised alerts for known CVEs
- Practiced reviewing and dismissing alerts with justification

---

## 📚 Key Learnings

- How GHAS secret scanning works and what patterns it detects
- Difference between **secret scanning** (credentials) vs **code scanning** (vulnerabilities)
- How to enable and configure GHAS on a public/private repository
- How to triage, dismiss, and resolve security alerts
- Importance of `.gitignore` and pre-commit hooks to prevent secret leaks
- How Dependabot automates dependency vulnerability management

---

## 🔗 Related Project

This repo is part of a broader DevSecOps learning journey.  
The production-grade CI/CD pipeline project with full Azure DevOps, AKS, and Trivy integration is here → *(link to new repo once created)*

---

## 👩‍💻 Author

**Sadhana Singh** — Senior DevOps Engineer  
[LinkedIn](https://linkedin.com/in/sadhana-singh226) · [GitHub](https://github.com/SadhanaNS)  
Azure DevOps Expert (AZ-400) | Azure Administrator (AZ-104)
