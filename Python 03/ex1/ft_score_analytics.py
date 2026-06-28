import sys

lenght: int = len(sys.argv)
values = []
invalid_values = []

print("=== Player Score Analytics ===")
if lenght <= 1:
    print("No scores provided."
          "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
    args = sys.argv[1:]
    for arg in args:
        try:
            values.append(int(arg))
        except Exception:
            invalid_values.append(arg)
    if (len(invalid_values) > 0):
        for value in invalid_values:
            print(f"Invalid parameter: '{value}'")
    if (len(values) > 0):
        print(f"Scores processed: {values}")
        print(f"Total players: {len(values)}")
        print(f"Total score: {sum(values)}")
        print(f"Average score: {(sum(values) / len(values)):.1f}")
        print(f"High score: {max(values)}")
        print(f"Low score: {min(values)}")
        print(f"Range score: {max(values) - min(values)}")
    else:
        print("No scores provided."
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
