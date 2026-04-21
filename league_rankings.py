import sys
from collections import defaultdict

def parse_line(line):
    home, away = line.strip().split(", ", 1)
    home_team, home_score = home.rsplit(" ", 1)
    away_team, away_score = away.rsplit(" ", 1)
    return home_team, int(home_score), away_team, int(away_score)

def main():
    if len(sys.argv) > 1:
        lines = open(sys.argv[1]).readlines()
    else:
        lines = sys.stdin.readlines()

    points = defaultdict(int)

    for line in lines:
        if not line.strip():
            continue
        ht, hs, at, as_ = parse_line(line)
        # make sure 0-point teams still show up
        points.setdefault(ht, 0)
        points.setdefault(at, 0)
        if hs > as_:
            points[ht] += 3
        elif as_ > hs:
            points[at] += 3
        else:
            points[ht] += 1
            points[at] += 1

    ranked = sorted(points.items(), key=lambda x: (-x[1], x[0]))

    rank = 1
    for i, (team, pts) in enumerate(ranked):
        if i > 0 and pts < ranked[i-1][1]:
            rank = i + 1
        suffix = "pt" if pts == 1 else "pts"
        print(f"{rank}. {team}, {pts} {suffix}")

if __name__ == "__main__":
    main()