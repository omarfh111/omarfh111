#!/usr/bin/env python3
"""Render a self-hosted, rate-limit-free GitHub activity card."""
import json
import os
import urllib.request
from datetime import datetime, timezone

LOGIN = os.getenv("PROFILE_LOGIN", "omarfh111")
TOKEN = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
OUT = os.getenv("ACTIVITY_OUT", "assets/activity.svg")
QUERY = """query($login:String!){user(login:$login){contributionsCollection{
totalCommitContributions totalPullRequestContributions totalRepositoryContributions
contributionCalendar{totalContributions weeks{contributionDays{date contributionCount weekday}}}
}}}"""


def fetch():
    if not TOKEN:
        raise SystemExit("GH_TOKEN is required")
    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
        headers={
            "Authorization": f"bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": f"{LOGIN}-profile",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    if payload.get("errors"):
        raise SystemExit(json.dumps(payload["errors"]))
    return payload["data"]["user"]["contributionsCollection"]


def render(data):
    calendar = data["contributionCalendar"]
    weeks = calendar["weeks"]
    days = sorted(
        (day for week in weeks for day in week["contributionDays"]),
        key=lambda day: day["date"],
    )
    active = sum(day["contributionCount"] > 0 for day in days)
    peak = max((day["contributionCount"] for day in days), default=0)
    longest = run = 0
    for day in days:
        run = run + 1 if day["contributionCount"] else 0
        longest = max(longest, run)
    weekly = [
        sum(day["contributionCount"] for day in week["contributionDays"])
        for week in weeks
    ]
    busiest_week = max(weekly, default=0)

    colors = ["#0B1526", "#103552", "#12648F", "#1E93C9", "#38BDF8"]

    def color(value):
        if not value:
            return colors[0]
        ratio = value / max(peak, 1)
        return colors[1 if ratio <= .20 else 2 if ratio <= .45 else 3 if ratio <= .70 else 4]

    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" '
        'width="1200" height="520" role="img" aria-label="Public GitHub activity">',
        '<defs><linearGradient id="accent"><stop stop-color="#38BDF8"/>'
        '<stop offset="1" stop-color="#8B5CF6"/></linearGradient>'
        '<linearGradient id="area" x1="0" y1="0" x2="0" y2="1">'
        '<stop stop-color="#38BDF8" stop-opacity=".25"/>'
        '<stop offset="1" stop-color="#38BDF8" stop-opacity="0"/></linearGradient></defs>',
        '<rect width="1200" height="520" rx="16" fill="#060B16"/>',
        '<rect width="1200" height="3" fill="url(#accent)"/>',
        '<g font-family="Segoe UI,Arial,sans-serif">',
        '<text x="28" y="40" fill="#64748B" font-size="12" font-weight="700" '
        'letter-spacing="2">PUBLIC CONTRIBUTION ACTIVITY · LAST 12 MONTHS</text>',
        f'<text x="28" y="82" fill="#F8FAFC" font-size="30" font-weight="700">'
        f'{calendar["totalContributions"]}<tspan fill="#64748B" font-size="14" '
        'font-weight="400"> contributions</tspan></text>',
        '<text x="1172" y="40" text-anchor="end" fill="#334155" font-size="10">'
        'self-hosted · rebuilt daily by GitHub Actions</text>',
    ]

    cell, gap, x0, y0 = 13, 4, 70, 118
    month_seen = set()
    for week_index, week in enumerate(weeks):
        for day in week["contributionDays"]:
            x = x0 + week_index * (cell + gap)
            y = y0 + day["weekday"] * (cell + gap)
            month = day["date"][5:7]
            if day["date"][8:] <= "07" and month not in month_seen:
                label = datetime.strptime(month, "%m").strftime("%b")
                parts.append(
                    f'<text x="{x}" y="108" fill="#475569" font-size="10">{label}</text>'
                )
                month_seen.add(month)
            parts.append(
                f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" '
                f'fill="{color(day["contributionCount"])}"><title>{day["date"]}: '
                f'{day["contributionCount"]} contributions</title></rect>'
            )

    stats = [
        ("COMMITS", data["totalCommitContributions"]),
        ("ACTIVE DAYS", active),
        ("LONGEST STREAK", f"{longest} days"),
        ("BUSIEST DAY", peak),
        ("BUSIEST WEEK", busiest_week),
        ("REPOS CREATED", data["totalRepositoryContributions"]),
    ]
    for index, (name, value) in enumerate(stats):
        x = 28 + index * 192
        parts.append(
            f'<rect x="{x}" y="260" width="180" height="74" rx="10" '
            'fill="#0D1B30" stroke="#1E334B"/>'
            f'<text x="{x + 14}" y="286" fill="#64748B" font-size="10" '
            f'font-weight="700" letter-spacing="1.3">{name}</text>'
            f'<text x="{x + 14}" y="318" fill="#E2E8F0" font-size="22" '
            f'font-weight="700">{value}</text>'
        )

    graph_x, graph_y, graph_w, graph_h = 28, 365, 1144, 105
    max_week = max(weekly, default=1) or 1
    points = []
    for index, value in enumerate(weekly):
        x = graph_x + index * graph_w / max(len(weekly) - 1, 1)
        y = graph_y + graph_h - value * graph_h / max_week
        points.append((x, y))
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    area = f"{graph_x},{graph_y + graph_h} {line} {graph_x + graph_w},{graph_y + graph_h}"
    parts.extend([
        f'<polygon points="{area}" fill="url(#area)"/>',
        f'<polyline points="{line}" fill="none" stroke="#38BDF8" '
        'stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>',
        f'<text x="{graph_x}" y="492" fill="#334155" font-size="10">'
        f'weekly contribution volume · peak {busiest_week} in one week</text>',
    ])
    stamp = datetime.now(timezone.utc).strftime("%d %b %Y")
    parts.append(
        f'<text x="1172" y="492" text-anchor="end" fill="#334155" font-size="10">'
        f'updated {stamp}</text></g></svg>'
    )
    return "".join(parts)


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as output:
        output.write(render(fetch()))

