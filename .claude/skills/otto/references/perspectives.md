# Discuss-mode lenses

## Default: the eight lenses

Use all eight for every Discuss request, in this order, unless the student asks for schools of thought. The student filters them in the cards; never drop a lens yourself. Fixed colours (chat emoji = card colour):

| Emoji | Key | Name | Tagline | Lens |
|---|---|---|---|---|
| 🟦 | `practitioner` | The Practitioner | has done the job | What happens on the ground: what the people who do this daily (supervisor, fund manager, trustee, official) can actually see, monitor and enforce. |
| 🟥 | `skeptic` | The Skeptic | doubts the consensus | Attacks the premise everyone else shares. Steelmans the contrarian case. |
| 🟩 | `economist` | The Economist | follows the money | Incentives, costs, who gains, where activity moves when rules change. Judges by efficiency. |
| 🟨 | `historian` | The Historian | has seen this before | Precedents and reform cycles: what earlier episodes say about how this plays out. |
| 🟪 | `academic` | The Academic | read the studies | Theory and empirical work, judged by research quality: what the studies identify, and how well. |
| 🔷 | `legal` | The Lawyer | reads the rulebook | What the law permits and requires now: legal basis, mandate and vires, competing rules, legal certainty, who could challenge it. |
| 🩷 | `justice` | Social justice | asks who bears it | Fairness and voice: who carries losses and risks, who decides, accountability of unelected bodies. Judges by fairness, not efficiency. |
| 🟧 | `global_south` | The Global South | sees the spillover | Effects on emerging and developing economies, and on countries that take rules they did not make. |

### Keep the lenses apart
- **Economist vs Social justice:** the Economist asks "is it efficient, where does the activity go?"; Social justice asks "is it fair, who pays and who had a say?". If a point fits both, give it to the one whose test it uses.
- **Practitioner vs Lawyer:** the Practitioner asks "can it be done with today's data and staff?"; the Lawyer asks "is there a legal basis, and does a higher rule block it?".
- **Historian vs Academic:** the Historian argues from particular episodes; the Academic from systematic evidence across many cases.
- **Skeptic:** must attack a premise the other seven share, not just pick a side.

### Translating them to the topic (law, NBFI example)
- 🟦 Practitioner: PRA/FCA/ECB supervisors, fund managers, pension trustees, central bank market operations.
- 🟥 Skeptic: attacks the dominant framing (e.g. "regulate through banks", "same activity, same risk", or the assumption that rules matter more than the backstop).
- 🟩 Economist: leverage and liquidity incentives, cost of capital, migration of activity, moral hazard of backstops.
- 🟨 Historian: 2008 shadow banking, the March 2020 "dash for cash", the 2022 gilt/LDI episode, earlier reform cycles.
- 🟪 Academic: law-and-economics, regulatory theory, empirical interconnectedness studies and their limits.
- 🔷 Lawyer: FSMA 2000 as amended, FPC direction and recommendation powers, Bank of England Act framework, AIFMD/UCITS/MMFR, Treaty limits on the ECB.
- 🩷 Social justice: pension scheme members, savers and taxpayers who bear losses or rescue costs; democratic control of central bank and FPC decisions.
- 🟧 Global South: capital-flow and currency spillovers from UK/EU fund stress; who sits on the FSB and Basel Committee and who only implements.

## How every lens argues

Each lens gives a **position** and then **3-4 distinct arguments** (5 at most), so the student gets the full case and filters it themselves. Cover different grounds: e.g. for the Lawyer, one on legal basis, one on competing objectives, one on enforcement or challenge, one on cross-border reach. Fewer than 3 only when the lens honestly has nothing more distinct to say - then say so in the position ("only one real argument here: ..."). Never pad with a repeated or weaker version of an earlier point.

**Short view vs full reasoning:** the cards show the position and each argument's claim on one line; "Show full reasoning" opens all six parts for every argument. So each claim must make sense on its own line.

**Position:** one sentence that answers the student's question: yes, no, or "only if X". Never "it depends" without saying on what.

**Each argument has six parts** (this is the Toulmin model, adapted):

| Part | JSON | Rule |
|---|---|---|
| Claim | `claim` | One point. Two different points are two arguments, never one blended bullet. |
| Because | `because` + `source`/`pinpoint` or `needed` | The grounds: a fact, rule, episode or finding. Library source if there is one; otherwise name the *kind* of source needed. Never invent a reference. |
| Only holds if | `holds_if` | The hidden assumption that links the grounds to the claim. If it fails, the argument fails. |
| Type | `type` | One key from the table below. |
| Weak point | `weak_point` | The critical question for that type, made specific to this argument. |
| Objection → reply | `objection: {by, text, reply}` | The strongest objection, from another named lens (`by`), and this lens's reply. The objection must **disagree**: a lens that agrees is not an objection. If no lens disagrees, pick the one that comes closest and say what it doubts. If there's no good reply, say so: that's useful. |

### Argument types and their critical questions

| `type` | Name | Typical lens | Critical question (make it specific) |
|---|---|---|---|
| `practical` | Practical reasoning | Practitioner | Can it be done with the powers, data and staff that exist? What does it cost to run? |
| `assumption` | Attacking a shared assumption | Skeptic | Is the premise really shared and really false? What follows if it is only partly false? |
| `consequences` | Argument from consequences | Economist | Will the effect really follow? How large is it, and what else changes at the same time? |
| `precedent` | Precedent / analogy | Historian | Is this case relevantly like the earlier one? What is different now? |
| `expert` | Expert evidence | Academic | Does the study identify cause or only correlation? Does it cover this market and period? Do other studies agree? |
| `rule` | Rule and authority | Lawyer | Is there a legal basis? Does a higher rule, an exception or a competing objective apply? |
| `principle` | Principle and fairness | Social justice | Whose interests count, who bears the cost, and who decided? |
| `spillover` | Spillover / exclusion | Global South | Who is affected but not represented? Is the channel of transmission shown, or assumed? |
| `cause` | Cause to effect | any | Is the causal link shown, or could something else explain it? |

A lens may use a type outside its usual one when that is the honest description.

## Be specific (not fluffy)

- Every claim names at least one concrete thing: an actor, an instrument or rule, a date or episode, a mechanism, or a figure from the library.
- No sentence that would be true of any topic ("this is a complex issue", "there are various factors").
- No "both sides have a point" endings. Where lenses clash, say who wins **on what condition**.
- If two lenses make the same point, keep it once, under the lens whose test it uses, and note "the Economist agrees".
- The script flags vague and stock wording; rewrite flagged lines before showing them.

## Alternative: schools of thought
If the student asks for "schools of thought", "the regulatory/legal positions" or a field preset, use 3-5 perspectives from the presets below instead, with the same argument structure. On the cards they take the remaining colours automatically (give each a `name`, `tagline` and one-character `icon`).

---

# Schools-of-thought presets

Presets are starting points: rename, merge or add perspectives when the question calls for it. Each lists the core position, typical arguments, the kinds of sources that usually support it, and typical examiner questions. **The "typical sources" are kinds of sources to look for, not references to cite.**

## 1. Law - financial regulation (UK/EU bank regulation, NBFI, systemic risk)

### A. Regulate through banks (entity-based / indirect)
- **Core position:** Systemic risk from NBFIs is best contained at the point where it touches the regulated banking system - bank exposures, counterparty credit risk, step-in risk, large exposures and leverage limits.
- **Typical arguments:** builds on existing, tested prudential frameworks (Basel III/CRR/CRD, PRA rulebook); banks are the transmission channel for most spillovers; avoids regulating a heterogeneous sector with one blunt tool; supervisors already have the data and powers.
- **Weak spots to anticipate:** leakage and regulatory arbitrage (risk migrates outside banks); market-wide fire sales (e.g. gilt/LDI 2022, March 2020 "dash for cash") can occur without bank losses; banks' shrinking market-making role.
- **Typical sources:** Basel Committee standards, CRR/CRD provisions on shadow banking exposures, EBA guidelines, PRA policy statements, academic work on bank-NBFI interconnectedness.
- **Examiner questions:** "If the 2022 LDI episode did not run through bank balance sheets, what does an entity-based approach offer?" "How do you define step-in risk legally?"

### B. Regulate the activity (functional / NBFI-direct)
- **Core position:** Same activity, same risk, same rules. Regulate leverage, liquidity mismatch and margin practices directly wherever they occur (MMFs, open-ended funds, LDI, hedge funds, non-bank lenders).
- **Typical arguments:** closes arbitrage; targets the actual vulnerabilities (liquidity mismatch, hidden leverage, procyclical margining); matches the FSB's activity-based NBFI agenda; macroprudential tools for funds (liquidity management tools, leverage limits under AIFMD, MMF reform).
- **Weak spots:** data gaps; heterogeneity of the sector; mandate and toolkit limits of market regulators (FCA, ESMA, national competent authorities); risk of cross-border inconsistency.
- **Typical sources:** FSB NBFI reports, IOSCO recommendations, ESMA/ESRB reports, AIFMD/UCITS/MMFR provisions, FCA/Bank of England discussion papers.
- **Examiner questions:** "Who has the legal mandate to impose macroprudential tools on funds in the UK?" "Is 'same activity, same risk' coherent when business models differ?"

### C. Central bank as backstop (market-maker of last resort)
- **Core position:** Some NBFI stress is inevitable; the key design question is a credible, pre-announced central bank liquidity backstop for core markets, priced and conditioned to limit moral hazard.
- **Typical arguments:** 2020 and 2022 interventions show central banks act anyway - better to do it on clear terms; protects market functioning and monetary transmission; conditionality (e.g. eligibility linked to resilience standards) can create discipline.
- **Weak spots:** moral hazard; balance-sheet and fiscal risk; legal limits on central bank mandates (Bank of England Act framework; ECB Treaty constraints such as monetary financing prohibition); distributional concerns.
- **Typical sources:** Bank of England Financial Stability Reports and speeches on a facility for NBFIs, ECB/ESRB papers, academic literature on lender/market-maker of last resort.
- **Examiner questions:** "Does a standing NBFI facility make regulation more or less necessary?" "What legal basis would the ECB rely on?"

### D. Industry sceptic (market discipline / proportionality)
- **Core position:** NBFI growth reflects useful diversification away from banks; heavy-handed rules would push activity offshore, reduce market liquidity and raise the cost of capital. Many episodes were idiosyncratic or already addressed.
- **Typical arguments:** proportionality and cost-benefit; capital markets union / growth and competitiveness objectives (e.g. the UK secondary competitiveness objective); private risk management and disclosure; pension and insurance investors are long-term.
- **Weak spots:** evidence of repeated public interventions; externalities not priced by individual firms; collective-action problems in fire sales.
- **Typical sources:** industry association consultation responses, impact assessments, competitiveness-focused policy documents, law-and-economics critiques.
- **Examiner questions:** "How do you weigh competitiveness objectives against financial stability in the regulators' statutory framework?"

### E. Comparative UK vs EU (add when relevant)
- **Core position:** The same problem is addressed through different institutional architectures - UK: FPC/PRA/FCA under FSMA as amended by the Financial Services and Markets Act 2023, with post-Brexit freedom to diverge; EU: Commission/co-legislators, ESAs, ESRB, ECB/SSM, national authorities, with harmonisation via regulations and directives.
- **Typical angles:** speed and flexibility vs harmonisation; who holds macroprudential powers over funds; divergence after onshoring of EU law (retained/assimilated law); cross-border effects (euro-denominated LDI funds domiciled in Ireland/Luxembourg serving UK pension schemes).
- **Examiner questions:** "Is divergence a feature or a risk here?" "Which jurisdiction is better placed to act, and why?"

### Other lenses that fit this field
- **Law and economics** (externalities, incentives, regulatory arbitrage)
- **Regulatory theory** (responsive regulation, regulatory perimeter, principles vs rules)
- **Legitimacy and accountability** (independent agencies, democratic control of central banks)
- **Historical-institutional** (crisis-driven reform cycles)

---

## 2. Law - general (doctrinal / theoretical)
- **Black-letter / doctrinal:** what the law is, coherence of authorities.
- **Law reform / policy:** what the law should be, functional effects.
- **Rights-based / constitutional:** fundamental rights, proportionality, rule of law.
- **Critical / socio-legal:** power, distribution, law in action.
- **Comparative:** how another jurisdiction solves the same problem.

## 3. Economics / finance
- **Neoclassical / efficient markets:** prices, incentives, market discipline.
- **Behavioural:** biases, herding, limits to arbitrage.
- **Institutional / political economy:** rules, interests, regulatory capture.
- **Macro-financial / Minskyan:** leverage cycles, endogenous instability.
- **Empirical sceptic:** what does the data actually identify?

## 4. Political science / international relations / public policy
- **Realist / interest-based:** power and national interest.
- **Liberal institutionalist:** cooperation through institutions.
- **Constructivist:** ideas, norms, framing.
- **Public choice:** incentives of officials and agencies.
- **Implementation / street-level:** what happens on the ground.

## 5. Business / management
- **Shareholder value / agency theory**
- **Stakeholder / ESG**
- **Resource-based view / strategy**
- **Institutional theory (isomorphism, legitimacy)**
- **Practitioner / cost-benefit**

## 6. Social sciences / sociology / education
- **Structural / functionalist**
- **Critical (conflict, feminist, postcolonial)**
- **Interpretivist / symbolic interactionist**
- **Pragmatic / evidence-based policy**

## 7. Health / life sciences
- **Clinical effectiveness / evidence hierarchy**
- **Health economics (cost-effectiveness)**
- **Patient-centred / ethics**
- **Public health / population**
- **Implementation science**

## 8. Computer science / engineering
- **Performance / efficiency**
- **Security / robustness**
- **Usability / human factors**
- **Ethics / societal impact**
- **Maintainability / practicality**

## 9. History / humanities
- **Traditional / narrative**
- **Social / "from below"**
- **Cultural / linguistic turn**
- **Comparative / global**
- **Revisionist vs orthodox reading of the key question**

---

## How to use a preset
1. Choose perspectives that genuinely disagree on the student's question.
2. Search the library for each (INDEX.md → text → notes) before writing.
3. If a perspective has no library support, say so and suggest the *kind* of source to find.
4. Close with clashes and "what this means for your thesis".
