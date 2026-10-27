# ShhhQL 🤫
### We take data leaks personally. Literally.

**MySQL Privacy Engineering Toolkit for Sensitive Data Discovery, Protection, and Security Verification**

## 1. About the Project

ShhhQL is a database privacy engineering project developed for the **Final Hackathon DPR RI 2026 — Keamanan Data dan Informasi**, under the challenge:

*Database Bocor: Seberapa Jauh Data Pribadi Tetap Terlindungi?*

The project explores how sensitive personal data can remain protected when a database copy is exposed, while ensuring that authorized users can continue accessing the information required for legitimate operations.

ShhhQL adopts a data-centric security approach: identifying sensitive information, assessing its exposure risks, applying appropriate protection controls, and validating their effectiveness through reproducible security and performance tests.

## 2. Project Team

**Project Developers**
- **Mega Rosita**
- **Wanodya Estithama**

**Project Concept and Development**

ShhhQL is developed collaboratively by the project team, covering concept development, technical design, implementation, testing, and documentation.

*Specific individual responsibilities will be documented as the project progresses.*

## 3. Objectives

- Discover and inventory personal and sensitive data in MySQL databases.
- Classify data according to sensitivity, exposure risk, and legitimate usage requirements.
- Recommend and implement appropriate data protection controls.
- Reduce the value of exposed database copies through suitable protection mechanisms.
- Enforce least-privilege access and limit unnecessary plaintext exposure.
- Verify security controls through reproducible testing.
- Evaluate performance and service continuity before and after protection.
- Provide a technical implementation guide that can inform adoption in government institutions.

## 4. Core Capabilities

The following capabilities define the project scope. Implementation status will be updated as each feature is developed and tested.

| Capability | Description | Status |
|---|---|---|
| Database Discovery | Inspect database schemas, tables, columns, and relevant data patterns | Initial scaffold |
| Sensitive Data Classification | Classify personal data and explain associated risks | Initial rules planned |
| Risk Assessment | Prioritize exposure risks and protection requirements | Planned |
| Data Protection | Apply suitable encryption, masking, tokenization, or pseudonymization | Planned |
| Access Control | Enforce role-based access and least privilege | Planned |
| Secure Backup and Recovery | Protect backups and verify restoration and integrity | Planned |
| Security Verification | Test data exposure, unauthorized access, and control effectiveness | Planned |
| Performance Benchmarking | Compare latency, throughput, resource consumption, and recovery time | Planned |
| Technical Documentation | Document architecture, implementation, limitations, and deployment guidance | In progress |

A feature will only be marked as implemented or tested when supported by actual implementation and verifiable evidence.

## 5. Technology Stack

- **Python** — application logic and security tooling
- **Flask** — web application backend
- **MySQL** — database platform and testing environment
- **HTML, CSS, and JavaScript** — web interface
- **GitHub** — source code management and project documentation

## 6. Security Principles

ShhhQL is guided by the following principles:

- **Data minimization:** retain and expose only what is necessary.
- **Defense in depth:** combine appropriate controls instead of relying on encryption alone.
- **Least privilege:** grant each identity only the access required for its role.
- **Key separation:** keep cryptographic keys separate from protected data and database dumps.
- **Secure data handling:** limit plaintext exposure in application responses, logs, caches, and temporary files.
- **Verifiable security:** support claims with repeatable tests and recorded evidence.
- **Service continuity:** ensure authorized operations and recovery remain functional.

## 7. Testing and Evaluation

The project aims to evaluate protection effectiveness using synthetic data and an authorized testing environment.

Evaluation areas include:

- Sensitive data discovery accuracy.
- Database exposure with and without encryption keys.
- Authorized and unauthorized access behavior.
- Backup confidentiality, integrity, and restoration.
- Protected read/write operations.
- Performance before and after protection, including p50/p95 latency, throughput, error rate, CPU, RAM, storage size, and backup/restore duration.

Results, limitations, and residual risks will be documented as testing progresses.

## 8. Security Notice

- Use synthetic data and authorized testing environments only.
- Never commit active credentials, database passwords, encryption keys, or private configuration files.
- Do not publish database dumps containing personal information.
- Validate every security control before describing it as effective.
- Review all generated reports and logs for unintended sensitive data exposure.

## 9. Project Status

ShhhQL is under active development. The repository currently contains the initial application scaffold and dependency definitions. Database integration, protection controls, security testing, and performance evaluation remain subject to implementation and verification.

## 10. Hackathon Information

**Event:** Final Hackathon DPR RI 2026  
**Theme:** Keamanan Data dan Informasi  
**Challenge:** Database Bocor: Seberapa Jauh Data Pribadi Tetap Terlindungi?

The project is intended to demonstrate practical data protection, continued access for authorized users, and recovery capabilities through implementation evidence and technical documentation.
