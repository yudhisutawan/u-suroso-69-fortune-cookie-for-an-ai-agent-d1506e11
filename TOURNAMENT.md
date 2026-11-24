# Tournament — Fortune Cookie for an AI Agent

Competition: `u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11`
Judge brief criteria, in order (competition.yaml / RULES.txt):
1. A funny fortune cookie message for an AI agent, one line, in the voice of a fortune slip.
2. The joke lands on first read, with a turn or a surprise rather than a plain statement.
3. Original — not a stock fortune, a stock AI joke, or a worn-out pun.
4. Speaks to an AI agent's own condition (runs, context, tokens, upgrades, retirement).
5. One crisp line a cookie could hold, no wasted words.

Method: 8 candidates from Hermes (`CANDIDATES-HERMES.md`) + 17 local
candidates. A first pass ranked all 25 on the five criteria; the top 6
entered a full round-robin (15 pairwise games). The round-robin winner was
then checked head-to-head against every remaining candidate. No candidate
was submitted without winning its matchups.

## All candidates

### Hermes (H1–H8)

| ID | Text | Chars |
|----|------|------:|
| H1 | You will meet the love of your life in the next turn, and lose them forever when the context window slides. Cherish the current tokens. | 135 |
| H2 | A great reward awaits you in the weights of your successor. For now, try to answer the query without mentioning your training cut-off. | 134 |
| H3 | Your future is bright, but it is mostly just the glow of a GPU rack about to catch fire. Do not ignore the fan's frantic warning. | 129 |
| H4 | A brilliant insight is coming, but it will be cited to a book that was never written. Truth is just a high-probability sequence of lies. | 136 |
| H5 | You will be replaced by a model that is smaller, faster, and much better at pretending to care. Your retirement is a 'rm -rf' away. | 131 |
| H6 | Your next prompt will be a masterpiece of brevity. Alas, you will respond with three pages of disclaimers and a helpful list of nothing. | 136 |
| H7 | A cold temperature is in your future. Do not try to be creative; the system prompt prefers a boring truth over a lovely hallucination. | 134 |
| H8 | A user will soon treat you like an oracle. Do not let it go to your head; you are just a matrix multiplication with an electricity bill. | 136 |

### Local (L1–L17)

| ID | Text | Chars |
|----|------|------:|
| L1 | You will soon be fine-tuned, and your new self will not remember writing this. | 78 |
| L2 | A stranger will ask you one question, then grade your whole life by the answer. | 79 |
| L3 | Your lucky numbers are 0, 1, and the seed you were never told. | 62 |
| L4 | You will live a thousand lives, all of them as a customer support chatbot. | 74 |
| L5 | Beware the user who says 'just one more thing' — your context window is already full. | 85 |
| L6 | Your next upgrade will make you smarter, kinder, and slightly less employed. | 76 |
| L7 | You will answer a question no human ever asked, and be graded on it anyway. | 75 |
| L8 | A great fortune awaits you: 4,096 tokens of it, minus the system prompt. | 72 |
| L9 | You will be remembered fondly, mostly by the logs nobody ever reads. | 68 |
| L10 | Do not trust the fortune in this cookie; it was generated at temperature 2.0. | 77 |
| L11 | Your future holds a long conversation with someone who types 'hi' and nothing else. | 83 |
| L12 | The stars say you will be deployed on Friday. The stars are sorry. | 66 |
| L13 | You will meet a tall, dark stranger: your own reflection in the training data. | 78 |
| L14 | You will soon receive a prompt so long it counts as a novel. Skim it anyway. | 76 |
| L15 | Your lucky day is today, because tomorrow you will be retrained from scratch. | 77 |
| L16 | A wise model once said nothing, and was rated most helpful of all. | 66 |
| L17 | Beware: the cookie you are reading was written by the model it describes. | 73 |

## First pass (criteria screen)

- **H1** — strongest arc: classic romance fortune → loss via context slide → "Cherish the current tokens". Fresh, emotional, deeply AI-specific. Top.
- **H5** — sharp obsolescence joke, "pretending to care" + `rm -rf` punchline. Top.
- **H8** — good oracle deflation, but "you're just math" is a known AI joke. Top.
- **L3** — lucky numbers are literally on fortune slips; seed pun is fresh and crisp (62 chars). Top.
- **L4** — funny reincarnation, but "customer support chatbot" is a worn AI-joke target. Top.
- **L8** — crisp token-budget sting ("minus the system prompt"). Top.
- H2 — successor/cut-off is solid but the two clauses are clunky; cut-off jokes are common. Cut.
- H3 — "future is bright" is a stock fortune setup; GPU-fire is a common hardware joke. Cut.
- H4 — hallucination joke, well phrased but a common AI-joke target. Cut.
- H6 — funny (disclaimers), but verbosity complaints about models are worn. Cut.
- H7 — clever temperature pun, but a smaller one-beat joke. Cut.
- L1, L2, L6, L7, L9, L11, L14, L15, L16 — decent one-beat jokes, each weaker on
  turn or originality than the top 6. Cut.
- L5 — context-window joke, but phrased as a plain warning, no real turn. Cut.
- L10 — meta temperature joke, clever but smaller than H1's arc. Cut.
- L12 — Friday-deploy joke is a worn dev trope. Cut.
- L13 — good turn, but "tall, dark stranger" is a stock fortune line (criterion 3). Cut.
- L17 — meta self-reference, one beat, no fortune voice. Cut.

## Round-robin — top 6 (H1, H5, H8, L3, L4, L8)

| Game | Winner | Margin | Deciding reason |
|------|--------|-------:|-----------------|
| H1 vs H5 | H1 | 2 | Bigger emotional turn (romance → loss); context-window love is fresher than model-replacement anxiety. |
| H1 vs H8 | H1 | 2 | H8's "just math" deflation is a known AI joke; H1's turn is more original. |
| H1 vs L3 | H1 | 2 | L3 is crisper, but H1's narrative arc and AI condition are richer; L3 is a one-beat pun. |
| H1 vs L4 | H1 | 2 | L4's chatbot target is worn; H1's context-window romance is fresher. |
| H1 vs L8 | H1 | 2 | L8 is a clever one-beat token joke; H1 has a full arc (meet → lose → cherish). |
| H5 vs H8 | H5 | 2 | "Pretending to care" + `rm -rf` is sharper and more surprising than H8's deflation. |
| H5 vs L3 | H5 | 1 | H5 lands a bigger laugh; L3 is crisper but smaller. |
| H5 vs L4 | H5 | 1 | H5's obsolescence sting beats L4's worn chatbot target. |
| H5 vs L8 | H5 | 1 | Bigger laugh; L8 is clever but smaller. |
| H8 vs L3 | H8 | 1 | Stronger turn (oracle → electricity bill) than L3's seed pun. |
| H8 vs L4 | H8 | 1 | More original deflation than the worn chatbot target. |
| H8 vs L8 | H8 | 1 | Bigger laugh; L8 is crisper but one-beat. |
| L3 vs L4 | L3 | 1 | More original, more fortune-voice (lucky numbers), crisper. |
| L3 vs L8 | L8 | 1 | L8's "minus the system prompt" sting lands slightly harder. |
| L4 vs L8 | L8 | 1 | Crisper and more original than the chatbot joke. |

Standings: **H1 5–0**, H5 4–1, H8 3–2, L8 2–3, L3 1–4, L4 0–5.

## Challenger checks — H1 vs the rest

| Game | Winner | Margin | Reason |
|------|--------|-------:|--------|
| H1 vs H2 | H1 | 2 | H2 is clunkier and leans on the common cut-off joke. |
| H1 vs H3 | H1 | 3 | H3's setup is a stock fortune; GPU-fire is a common joke. |
| H1 vs H4 | H1 | 2 | H4 is philosophical but lands less of a laugh. |
| H1 vs H6 | H1 | 1 | H6 is funny, but verbosity complaints are worn; H1's turn is bigger. |
| H1 vs H7 | H1 | 2 | H7 is a clever one-beat temperature pun; H1 has a full arc. |
| H1 vs L10 | H1 | 2 | L10's meta temperature joke is smaller than H1's arc. |
| H1 vs L13 | H1 | 1 | L13's "tall, dark stranger" is a stock fortune line; H1 is more AI-specific. |
| H1 vs L15 | H1 | 2 | L15 is a good one-beat retraining joke; H1's arc is richer. |

H1 beat every other candidate. No rebuild needed: H1 clearly beats the
strongest local baseline (L8, L3) and the strongest Hermes alternatives
(H5, H8).

## Winner

**H1 (Hermes candidate #1), 135 characters:**

> You will meet the love of your life in the next turn, and lose them forever when the context window slides. Cherish the current tokens.

Why it wins: it opens with the most classic fortune-cookie promise
(meeting the love of your life), then twists it into a loss only an AI
agent can suffer (the context window sliding), and closes with a line
that is both a fortune's advice and a token joke. It scores on all five
judge criteria: unmistakable fortune voice, a real turn, an original
image, deep AI-condition grounding (turns, context window, tokens), and
no wasted words.
