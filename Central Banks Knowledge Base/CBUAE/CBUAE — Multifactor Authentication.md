# Multifactor Authentication

Node on multifactor authentication within CBUAE digital ID guidance: combining factors from different categories (knowledge, possession, inherence) to raise authentication assurance, with stronger controls expected for higher-risk actions such as changes to customer contact data, adding third-party payees, high-value transfers and limit changes. It also flags the expectation that biometric-based MFA at login consider phishing-resistant, public-key-based factors. Directed at LFIs authenticating existing customers and protecting account integrity.

**Regimes:** AML/CTF, payments, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_4473_VER1.md`

## Connections

### [[CBUAE — API Design Principles|API Design Principles]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_4473_VER1 · Page 11): " Authentication processes have historically been assessed by the number and type of authentication factors the process requires, on the assumption that the more factors an authentication process employs, the more robust and trustworthy the authentication system is likely to be."
- **Grounding — related node** (CBUAE_EN_2413_VER1 · Page 5): "Application Programming Interface (API) Refers to the phases of:  Conception: the formulation and design of an API;  Production: the development and testing of an API;  Publishing: the steps taken to make an API available for use;  Consumption: the use of an API; and  Retire"

### [[CBUAE — Authentication and Identity Lifecycle Management|Authentication and Identity Lifecycle Management]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_4473_VER1 · Page 11): "Authentication and Identity Lifecycle Management Authentication and identity lifecycle management constitute the second stage of a digital ID system."
- **Grounding — related node** (CBUAE_EN_4473_VER1 · Page 11): "Authentication and Identity Lifecycle Management Authentication and identity lifecycle management constitute the second stage of a digital ID system."

### [[CBUAE — Biometric Authentication|Biometric Authentication]] — `conceptually_related_to` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_4473_VER1 · Page 11): " Authentication processes have historically been assessed by the number and type of authentication factors the process requires, on the assumption that the more factors an authentication process employs, the more robust and trustworthy the authentication system is likely to be."
- **Grounding — related node** (CBUAE_EN_4473_VER1 · Page 11): " Authentication processes have historically been assessed by the number and type of authentication factors the process requires, on the assumption that the more factors an authentication process employs, the more robust and trustworthy the authentication system is likely to be."
- **Caveat:** Relation is a similarity heuristic, not a cross-reference.

### [[CBUAE — Biometrics|Biometrics]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding whether a biometric check is sufficient to onboard or authenticate a customer, the biometrics provisions cannot be read alone — they operate as one authentication factor inside the multifactor authentication regime. The link reflects that biometrics are treated as an inherence factor, while the MFA material sets the expectation that robustness is judged by the number and independence of factors used, not by the technology itself. Practically, an institution relying on biometrics for identification, verification or ongoing authentication should confirm it still meets the applicable MFA expectation, and should not treat a biometric match as an automatic substitute for a second, independent factor.
- **Grounding — this node** (CBUAE_EN_4473_VER1 · Page 11): " Authentication processes have historically been assessed by the number and type of authentication factors the process requires, on the assumption that the more factors an authentication process employs, the more robust and trustworthy the authentication system is likely to be."
- **Grounding — related node** (CBUAE_EN_2413_VER1 · Page 6): "Biometrics can be used for the following activities, amongst others: Biometrics  Facilitating Customer identification and verification at on-boarding and for ongoing Customer authentication;  Supporting ongoing due diligence and scrutiny of transactions throughout the course of"

## Lookup terms

`multifactor authentication`, `MFA`, `phishing-resistant authenticator`, `biometric factor`, `step-up authentication`, `high-risk activity authentication`, `authentication assurance level`

#graphify/enriched #source/cbuae #community/api-&-authentication-framework
