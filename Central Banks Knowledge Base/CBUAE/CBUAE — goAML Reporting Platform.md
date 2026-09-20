# goAML Reporting Platform

Concept node on the reporting channel used to notify UAE authorities of suspicious activity and of sanctions matches and freezing actions. It sits at the intersection of STR/SAR filing to the FIU and TFS reporting on listed persons and measures taken, and applies to LFIs and registered hawala providers. Useful for confirming who must report, what is reported and to which authority, rather than platform mechanics.

**Regimes:** AML/CTF, sanctions/TFS

## Sources

- `corpus/markdown/CBUAE_EN_498_VER1.md`
- `corpus/markdown/CBUAE_EN_6725_VER1.md`

## Connections

### [[CBUAE — Suspicious Transaction Report (STR)|Suspicious Transaction Report (STR)]] — `references` [EXTRACTED]
- **What this link tells you:** The reporting obligation is channel-specific: a suspicion must be submitted through the designated FIU reporting platform using the correct report type, so an institution that has not completed registration on that platform is not in a position to discharge its duty at all. The guidance distinguishes first-instance reports from supplementary filings, meaning the choice of report type is itself a compliance decision rather than an administrative formality. Practically, registration should be treated as a precondition to commencing regulated activity, and follow-up information on an existing suspicion should be filed as a supplementary report rather than as a new one.
- **Grounding — this node** (CBUAE_EN_498_VER1 · Page 23): "4.3 Reporting Suspicious Transactions and registration to GoAML RHP must monitor transactions that they carry out to identify those that may be suspicious and where a Suspicious Transaction Report (“STR”), or suspicious activity report ("SAR") or other report types may need to be"
- **Grounding — related node** (CBUAE_EN_418_VER2 · Page 15): "The STR and SAR are the primary (or first instance) reports which must be used to report a new suspicion, whereas Additional Information File without Transactions (“AIF”) and Additional Information File with Transactions (“AIFT”) report types are supplementary reports which can b"

### [[CBUAE — Targeted Financial Sanctions Obligations|Targeted Financial Sanctions Obligations]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_498_VER1 · Page 12): "Report any listed persons and the actions the RHP has taken to the appropriate authorities With regards to LFIs obligation for TFS reporting, the CBUAE in coordination with the Executive Office, has established a unified mechanism to report TFS obligations utilizing the UAE Finan"
- **Grounding — related node** (CBUAE_EN_498_VER1 · Page 10): "Part II: Guidance for RHP 1 Sanctions Obligations and Freezing Without Delay Targeted Financial Sanctions (TFS) are legal restrictions on financial activity imposed by the United Nations Security Council (UNSC) or the UAE."

### [[CBUAE — Transaction Monitoring and STRSAR|Transaction Monitoring and STR/SAR]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_498_VER1 · Page 13): "Registration on SACM is a prerequisite for goAML registration;  Register in the relevant SACM and subsequently to the CBUAE’s Remittance Reporting System (RRS) for the daily reporting and Integrated Regulatory Reporting System (IRR) for the quarterly reporting (see Part II secti"
- **Grounding — related node** (CBUAE_EN_6725_VER1 · Page 35): "Transaction Monitoring Under Article 16 of the AML-CFT Decision, LFIs must monitor activity by all customers to identify behaviour that is potentially suspicious and that may need to be the subject of an STR or SAR."

## Lookup terms

`goAML`, `FIU reporting`, `STR filing`, `SAR`, `TFS reporting`, `freeze notification`, `suspicious transaction report`

#graphify/enriched #source/cbuae #community/insurance-ombudsman-&-hawala
