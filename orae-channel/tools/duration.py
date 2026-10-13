"""TTS 원고 길이 계산.

사용법:
  python3 tools/duration.py episodes/001_커피/03_TTS원고.txt
  python3 tools/duration.py 원고.txt --rate 5.0        # 1초당 음절 수 (기본 4.5 = TTS 0.9배속 기준)

빈 줄로 나뉜 문단을 구간으로 보고, 구간별 시작 시각과 길이, 전체 길이를 출력합니다.
숫자는 한 덩어리당 2음절로 어림합니다. 문장 끝마다 0.5초 쉼을 더합니다.
"""
import re
import sys


def seconds(text, rate):
    syllables = len(re.findall(r"[가-힣]", text)) + 2 * len(re.findall(r"[0-9]+", text))
    pauses = len(re.findall(r"[.?!]\s", text + " ")) * 0.5
    return syllables / rate + pauses, syllables


def fmt(t):
    return f"{int(t) // 60}:{int(t) % 60:02d}"


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return
    rate = float(argv[argv.index("--rate") + 1]) if "--rate" in argv else 4.5
    text = open(argv[1], encoding="utf-8").read()
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    t = total_syl = 0
    for i, b in enumerate(blocks, 1):
        d, syl = seconds(b, rate)
        first = b.splitlines()[0][:40]
        print(f"{fmt(t):>6}  {d:5.0f}초  [{i:02d}] {first}")
        t += d
        total_syl += syl
    print(f"\n전체 약 {fmt(t)} ({total_syl}음절, 1초당 {rate}음절 기준)")


if __name__ == "__main__":
    main(sys.argv)
