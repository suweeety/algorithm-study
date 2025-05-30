import os

README_PATH= "README.md"
SOLUTION_DIR = "solution"

header = """# Algorithm Study

| 플랫폼 | 문제 번호 | 제목        | 난이도 | 풀이 링크 |
|--------|-----------|-------------|--------|------------|
"""

rows = []

# solutions 디렉토리에 있는 파일들 반복
for file in sorted(os.listdir(SOLUTION_DIR)):
    if file.endswith(".md"):
        # 파일 이름에서 문제 번호와 제목 추출
        parts = file.replace(".md", "").split('_', 1)
        problem_no = parts[0]
        title = parts[1].replace('-', ' ').title() # 파일명에서 제목 추출
        rows.append(f"| baekjoon | {problem_no} | {title} | | [링크]({SOLUTION_DIR}/{file}) |")

# README 내용 생성
with open(README_PATH, "w") as f:
    f.write(header)
    for row in rows;
        f.write(row + "\n")