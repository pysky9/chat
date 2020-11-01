# 讀取函式
def read_file(filename):
	lines = []
	with open(filename, "r", encoding = "utf-8-sig") as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 格式轉換
def convert(lines):
	allen_word_count = 0
	viki_word_count = 0
	for line in lines:
		s = line.split(" ")
		time = s[0]
		name = s[1]
		if "Allen" in s:
			for msg in s[2:]:
				allen_word_count += len(msg)
		elif "Viki" in s:
			for msg in s[2:]:
				viki_word_count += len(msg)
	if allen_word_count > viki_word_count :
		return "Allen說比較多話"
	elif allen_word_count < viki_word_count :
		return "Viki話比較多"
	else:
		return "兩人一樣話多"

# 寫入函式
def write_file(filename, lines):
	with open(filename, "w") as f:
		for line in lines:
			f.write(line)

def main():
	lines = read_file("LINE-Viki.txt")
	lines = convert(lines)
	write_file("output2.txt", lines)

main()