#!/usr/bin/env python3
"""Render a self-hosted SVG from GitHub's contribution calendar."""
import json, os, urllib.request
from datetime import datetime, timezone

LOGIN = os.getenv("PROFILE_LOGIN", "omarfh111")
TOKEN = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
OUT = os.getenv("ACTIVITY_OUT", "assets/activity.svg")
QUERY = """query($login:String!){user(login:$login){contributionsCollection{totalCommitContributions totalPullRequestContributions totalRepositoryContributions contributionCalendar{totalContributions weeks{contributionDays{date contributionCount weekday}}}}}}"""

def fetch():
    if not TOKEN: raise SystemExit("GH_TOKEN is required")
    req = urllib.request.Request("https://api.github.com/graphql", data=json.dumps({"query":QUERY,"variables":{"login":LOGIN}}).encode(), headers={"Authorization":f"bearer {TOKEN}","Content-Type":"application/json","User-Agent":f"{LOGIN}-profile"})
    with urllib.request.urlopen(req, timeout=30) as response: payload=json.load(response)
    if payload.get("errors"): raise SystemExit(json.dumps(payload["errors"]))
    return payload["data"]["user"]["contributionsCollection"]

def render(data):
    weeks=data["contributionCalendar"]["weeks"]
    days=sorted((d for w in weeks for d in w["contributionDays"]), key=lambda d:d["date"])
    active=sum(d["contributionCount"]>0 for d in days); peak=max((d["contributionCount"] for d in days),default=0)
    longest=run=0
    for d in days:
        run=run+1 if d["contributionCount"] else 0; longest=max(longest,run)
    colors=["#0D1726","#103552","#12648F","#1E93C9","#38BDF8"]
    def color(n):
        if not n:return colors[0]
        q=n/max(peak,1); return colors[1 if q<=.2 else 2 if q<=.45 else 3 if q<=.7 else 4]
    p=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 390" width="1200" height="390" role="img" aria-label="Public GitHub activity">','<defs><linearGradient id="acc"><stop stop-color="#38BDF8"/><stop offset="1" stop-color="#8B5CF6"/></linearGradient></defs><rect width="1200" height="390" rx="14" fill="#060B16"/><rect width="1200" height="3" fill="url(#acc)"/>','<g font-family="Segoe UI,Arial,sans-serif"><text x="28" y="40" fill="#64748B" font-size="12" font-weight="700" letter-spacing="2">PUBLIC CONTRIBUTION ACTIVITY · LAST 12 MONTHS</text>']
    p.append(f'<text x="28" y="80" fill="#F8FAFC" font-size="30" font-weight="700">{data["contributionCalendar"]["totalContributions"]}<tspan fill="#64748B" font-size="14" font-weight="400"> contributions</tspan></text>')
    cell,gap,x0,y0=14,4,62,108
    by_date={d["date"]:d for d in days}
    for wi,w in enumerate(weeks):
        for d in w["contributionDays"]:
            x=x0+wi*(cell+gap); y=y0+d["weekday"]*(cell+gap)
            p.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="{color(d["contributionCount"])}"><title>{d["date"]}: {d["contributionCount"]}</title></rect>')
    stats=[("COMMITS",data["totalCommitContributions"]),("ACTIVE DAYS",active),("LONGEST STREAK",f"{longest} days"),("BUSIEST DAY",peak),("PULL REQUESTS",data["totalPullRequestContributions"]),("REPOS CREATED",data["totalRepositoryContributions"])]
    for i,(name,value) in enumerate(stats):
        x=28+i*192
        p.append(f'<rect x="{x}" y="270" width="180" height="76" rx="10" fill="#0D1B30" stroke="#1E334B"/><text x="{x+14}" y="296" fill="#64748B" font-size="10" font-weight="700" letter-spacing="1.3">{name}</text><text x="{x+14}" y="329" fill="#E2E8F0" font-size="23" font-weight="700">{value}</text>')
    stamp=datetime.now(timezone.utc).strftime("%d %b %Y")
    p.append(f'<text x="1172" y="374" text-anchor="end" fill="#334155" font-size="10">updated {stamp} · self-hosted</text></g></svg>')
    return "".join(p)

if __name__=="__main__":
    os.makedirs(os.path.dirname(OUT),exist_ok=True)
    with open(OUT,"w",encoding="utf-8") as f:f.write(render(fetch()))


